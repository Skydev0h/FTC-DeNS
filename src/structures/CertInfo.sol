pragma ton-solidity >=0.45.0;

struct CertInfo {

    uint32 id;
    uint32 sync;

    string name;
    address parent;

    uint32 registered;
    uint32 auctioned;
    uint32 expires;

    address owner;

}
