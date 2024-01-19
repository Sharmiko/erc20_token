import pytest
from brownie import SharmiToken


@pytest.fixture
def sharmi_token(SharmiToken, accounts):
    yield SharmiToken.deploy({"from": accounts[-1]})


def test_sharmi_token_total_supply(sharmi_token):
    assert sharmi_token.totalSupply() == 100_000


def test_sharmi_token_name(sharmi_token):
    assert sharmi_token.name() == "Sharmi's Super Token"


def test_sharmi_token_symbol(sharmi_token):
    assert sharmi_token.symbol() == "SSC"


def test_sharmi_token_balance_of_creator(sharmi_token, accounts):
    sharmi_token.balanceOf(accounts[-1]) == 100_000

