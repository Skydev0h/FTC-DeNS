pragma ton-solidity >=0.45.0;

library AFlags {

    uint8 constant deploy    =  0x01;
    uint8 constant reserve   =  0x02;
    uint8 constant chown     =  0x04;
    uint8 constant chexp     =  0x08;

    uint8 constant upuser    =  0x10;
    uint8 constant upcert    =  0x20;
    uint8 constant _40       =  0x40;
    uint8 constant _80       =  0x80;

}