import os, sys
import time
from subprocess import check_output, CalledProcessError
from tempfile import TemporaryFile

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname + "/../")

visited = set()

rt = len(sys.argv) > 1 and sys.argv[1] == 'rt'
al = len(sys.argv) > 1 and sys.argv[1] == 'all'

if rt:
    print("------- Continous build -------")

if al:
    print('------- Build all -------')


def walker(path):
    s5 = 0
    wdir = os.path.dirname(path)
    with open(path, 'r') as f:
        for line in f.readlines():
            if line.startswith("abstract "): break
            if line.startswith("contract "): break
            if line.startswith("interface "): break
            if line.startswith('import "'):
                iname = line[8:]
                iname = iname[:iname.find('"')]
                iname = os.path.realpath(wdir + "/" + iname)
                # print(path + "->" + iname)
                if not os.path.isfile(iname):
                    print("Warning! " + path + " -> " + iname + " does not exist!")
                    return 0
                s6 = os.stat(iname).st_mtime
                if s6 > s5: s5 = s6
                visited.add(iname)
                s6 = walker(iname)
                if s6 > s5: s5 = s6
    return s5

last = dict()

while True:
    tobuild = []
    for fname in os.listdir("src"):
        if not fname.startswith("D4"): continue
        if not fname.endswith(".sol"): continue
        cname = fname[:-4]
        p1 = "./src/{0}".format(fname)
        p2 = "./out/{0}.abi.json".format(cname)
        p3 = "./out/{0}.tvc".format(cname)
        s1 = os.stat(p1).st_mtime
        s2 = os.stat(p2).st_mtime if os.path.isfile(p2) else 0
        s3 = os.stat(p3).st_mtime if os.path.isfile(p3) else 0
        visited = {os.path.realpath(p1)}
        s4 = walker(os.path.realpath(p1))
        # print("{0}: Contract {1}, ABI {2}, TVC {3}, Deps {4}".format(cname, s1, s2, s3, s4))
        lb = last[fname] if fname in last.keys() else 0
        if ((s1 > s2 or s1 > s3 or s4 > s2 or s4 > s3) and (s1 > lb or s4 > lb)) or al:
            tobuild.append((fname, cname, p1, p2, p3))
        else:
            if not rt:
                print("... {0} not changed".format(cname))

    for pack in tobuild:
        (fname, cname, p1, p2, p3) = pack
        last[fname] = time.time()
        print(">>> Building {0}...".format(cname))
        os.chdir("src")
        with TemporaryFile() as t:
            try:
                check_output(["tondev", "sol", "compile", fname], stderr=t)
                print("+++ Success!")
                t.seek(0)
                print(t.read().decode("utf-8"))
                os.rename("{0}.abi.json".format(cname), "../" + p2)
                os.rename("{0}.tvc".format(cname), "../" + p3)
                os.chdir("../out")
                try:
                    check_output(["tondev", "js", "wrap", "{0}.abi.json".format(cname)])
                except CalledProcessError as e2:
                    print("!!! Wrap failed! Code {0}".format(e2.returncode))
            except CalledProcessError as e:
                print("!!! Build failed! Code {0}".format(e.returncode))
                t.seek(0)
                print(t.read().decode("utf-8"))
        os.chdir("..")

    if rt:
        time.sleep(1)
    else:
        break

