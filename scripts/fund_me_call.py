from brownie import FundMe
from scripts.helper_script import getAccount
import time
from web3 import Web3


def fund():
    current_account = getAccount()
    print(f"current account address {current_account.address}")
    print(f"current account balance {current_account.balance()}")
    fund_me = FundMe[-1]
    entrance_fee = fund_me.getEntranceFee()
    print(f"current entrance fee is {entrance_fee}")
    print("Funding...")
    fund_me.fund({"from": current_account,
                 "value": entrance_fee})
    fund_me.fund({"from": current_account,
                 "value": entrance_fee})
    print(f"current account balance {current_account.balance()}")


def withdraw():
    current_account = getAccount()
    print(f"current account address {current_account.address}")
    fund_me = FundMe[-1]
    fund_me.ownerWithdraw({"from": current_account})
    print(f"current account balance {current_account.balance()}")


def main():
    fund()
    time.sleep(2)
    print("funded...")
    withdraw()


if __name__ == "__main__":
    main()
