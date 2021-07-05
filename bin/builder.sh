#!/usr/bin/env bash

cd "$(dirname "$0")" || exit 1
# cd .. || exit 1

python3 builder.py "$1"

#function walker() {
#  local wdir="$(dirname $(realpath "$1"))"
#  grep '^import "' $1 | cut -d'"' -f2 | while read line;
#  do
#    local path=$(realpath "$wdir/$line")
#    if printf '%s\n' "${visited[@]}" | grep -q -P '^$path$'; then
#      true
#    else
#      local s5=$(stat -c %Y "$path")
#      if [ "$s5" -gt "$s4" ]; then
#        s4=$s5
#      fi
#      visited+=("$path")
#      walker "$path"
#    fi
#  done
#}
#
#function build() {
#  contract=$1
#  s1=$(stat -c %Y "src/$contract.sol")
#  s2=$(stat -c %Y "out/$contract.abi.json" 2>/dev/null)
#  s3=$(stat -c %Y "out/$contract.tvc" 2>/dev/null)
#  s4=$s1
#  visited=("$(realpath "src/$contract.sol")")
#  walker "src/$contract.sol"
#  if [[ "$s2" == "" ]]; then s2=0; fi
#  if [[ "$s3" == "" ]]; then s3=0; fi
#  if [[ "$s4" == "" ]]; then s4=0; fi
#  if [ "$s1" -gt "$s2" ] || [ "$s1" -gt "$s3" ] \
#  || [ "$s4" -gt "$s2" ] || [ "$s4" -gt "$s3" ]
#  then
#    echo ">>> Building $contract..."
#    cd src || exit 1
#    tondev sol compile "$contract.sol" >/dev/null
#    ec=$?
#    if [ "$ec" != "0" ]
#    then
#      echo "!!! Build failed!"
#    else
#      echo "+++ Success!"
#      mv "$contract.abi.json" "../out/"
#      mv "$contract.tvc" "../out/"
#      cd ../out || exit 1
#      tondev js wrap "$contract.abi.json" >/dev/null
#    fi
#    cd .. || exit 1
#  else
#    echo "... $contract not changed"
#  fi
#}
#
#for f in src/D4*.sol
#do
#  contract=$(basename "$f" .sol)
#  build "$contract"
#done
