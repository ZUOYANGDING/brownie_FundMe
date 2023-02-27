from brownie import network, MockV3Aggregator
from scripts.helper_script import getAccount
from web3 import Web3

# _decimal
DECIMALS = 18
# _initialAnswer
INITIAL_ANSWER = 2000


def deployMock():
    print(f"Network deploying is {network.show_active()}")
    print("deploying mock...")
    account = getAccount()
    MockV3Aggregator.deploy(DECIMALS, Web3.toWei(
        INITIAL_ANSWER, "ether"), {"from": account})
    print("mock deployed")


def main():
    deployMock()


if __name__ == "__main__":
    main()
