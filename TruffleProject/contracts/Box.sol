// contracts/Box.sol
// SPDX-License-Identifier: MIT
pragma solidity >=0.4.0 <0.6.0;

contract Box {
  event ValueChanged (
    uint indexed counter
   );
  uint256 private _value;
  uint256 private _CID;
  uint256 private _eStart;
  uint256 private _eEnd;
  
  function initialize(uint CID, uint eStart) public {
    _CID = CID;
	_eStart = eStart;

  }  

  function store(uint x, uint y) public {
    _value = x;

    emit ValueChanged(y);
  }	// this function is the proof function that used in the paper

  function retrieve() public view returns (uint256) {
        return _value;
    }
	
  function finalize(uint CID, uint eEnd) public {
    _CID = CID;
	_eEnd = eEnd;

  }	
}
