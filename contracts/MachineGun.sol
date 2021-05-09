pragma ton-solidity >=0.42.0;
pragma AbiHeader time;
pragma AbiHeader pubkey;
pragma AbiHeader expire;

import "./Interfaces.sol";
import "./Libraries.sol";
import "./Structures.sol";

import "./SmvPack.sol";

contract MachineGun {

    address public _root;
    address public _owner;
    uint32 public _expiry;
    string public _base;
    uint32 public i;
    uint32 public _lim;
    uint32 public _chs;

    constructor(address root, address owner, uint32 expiry, string base, uint32 lim, uint32 chs) public {
        require(tvm.pubkey() != 0, 101);
        require(msg.pubkey() == tvm.pubkey(), 102);
        tvm.accept();
        _root = root;
        _owner = owner;
        _expiry = expiry;
        _base = base;
        _lim = lim;
        _chs = chs;
        // MachineGun(address(this)).tratata();
    }

    function tratata() public {
        require(msg.sender == address(this) || msg.pubkey() == tvm.pubkey(), 102);
        tvm.accept();
        uint32 j = i;
        i = i + _chs;
        ProposalInfo pi;
        DeployCertProposalSpecific sp;
        pi.id = pi.start = pi.end = pi.ts = 0;
        pi.title = "";
        pi.proposalType = ProposalType.DeployCert;
        sp.owner = _owner;
        sp.ts = now + 365 days;
        while (j < i) {
            sp.name = format("{}{}", _base, j);
            TvmBuilder b; b.store(sp); pi.specific = b.toCell();
            j += 1;
        }
        if (i < _lim)
            MachineGun(address(this)).tratata{flag:MsgFlag.IgnoreErrors}();
    }

}