// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";


contract SharmiToken is ERC20 {

    string public constant name_ = "Sharmi's Super Token";
    string public constant symbol_ = "SSC";
    uint8 public constant decimals_ = 2;
    uint constant _initial_supply = 100_000;

    constructor() ERC20(name_, symbol_) {
        _mint(msg.sender, _initial_supply);
    }

    function decimals() public view override returns(uint8) {
        return decimals();
    }
}