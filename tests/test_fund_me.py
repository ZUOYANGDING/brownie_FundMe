from scripts.helper_script import (
    getAccount, getDiffAccoutForWithdraw, LOCAL_BLOCKCHAIN_ENVIRONMENTS, FORK_LOCAL_ENVIRONMENTS)
from scripts.deploy import deployFundMe
from brownie import network, accounts, exceptions
import pytest


def testFundMe():
    account = getAccount()
    fund_me = deployFundMe()
    entrance_fee = fund_me.getEntranceFee() + 100
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    assert fund_me.getAccountBalanceByAddress(account.address) == entrance_fee
    tx2 = fund_me.ownerWithdraw({"from": account})
    tx2.wait(1)
    assert fund_me.getAccountBalanceByAddress(account.address) == 0


def testOnlyOwnerWithdraw():
    if (network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS and
            network.show_active() not in FORK_LOCAL_ENVIRONMENTS):
        pytest.skip("only for dev testing...")
    fund_account = getAccount()
    fund_me = deployFundMe()
    tx = fund_me.fund(
        {"from": fund_account, "value": fund_me.getEntranceFee()+100})
    tx.wait(1)
    withdraw_acount = getDiffAccoutForWithdraw()
    if (withdraw_acount is not None):
        with pytest.raises(exceptions.VirtualMachineError):
            fund_me.ownerWithdraw({"from": withdraw_acount})
