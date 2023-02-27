from brownie import (network, config, FundMe, MockV3Aggregator)
from scripts.helper_script import (
    getAccount, LOCAL_BLOCKCHAIN_ENVIRONMENTS)
from scripts.deploy_mock import deployMock


def deployFundMe():
    current_account = getAccount()
    if (network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS):
        deployMock()
        price_feed_address = MockV3Aggregator[-1].address
    else:
        print(f"network {network.show_active()}")
        price_feed_address = config["networks"][network.show_active()].get(
            "eth_usd_price_feed")
    print(f"price_feed_address {price_feed_address}")
    fundMe = FundMe.deploy(price_feed_address, {
                           "from": current_account}, publish_source=config["networks"][network.show_active()].get("verify"))
    print(f"FundMe deployed to {fundMe.address}")
    return fundMe


def main():
    deployFundMe()


if __name__ == "__main__":
    main()
