from bloomdata.wallet import Wallet
import pytest

# 'Decorators'

# Pytest Fixtures: Scenarios created, especially for 
# the assert statements in the unit tests.

@pytest.fixture
def empty_wallet():
    return Wallet()


@pytest.fixture
def wallet_20():
    return Wallet(20)

# Unit tests.

def test_empty_wallet(empty_wallet):
    # empty_wallet = Wallet()
    # assert Wallet().balance == 0
    assert empty_wallet.balance == 0


def test_wallet_20(wallet_20):
    assert wallet_20.balance == 20


def test_wallet_20_spend_10(wallet_20):
    wallet_20
    assert wallet_20.spend_cash(10) == 'Remaining balance: $10'
    assert wallet_20.balance == 10


def test_spend_all_cash(wallet_20):
    wallet_20
    assert wallet_20.spend_cash(20) == 'Remaining balance: $0'

