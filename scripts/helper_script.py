from brownie import accounts, network, config

LOCAL_BLOCKCHAIN_ENVIRONMENTS = [
    "development", "ganache-local", "ganache-local-1"]
FORK_LOCAL_ENVIRONMENTS = ["mainnet-fork-dev"]


def getAccount():
    if (network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or
            network.show_active() in FORK_LOCAL_ENVIRONMENTS):
        # return accounts.add(config["wallet"].get("local_from_key"))
        return accounts[0]
    else:
        return accounts.add(config["wallet"].get("online_from_key"))


def getDiffAccoutForWithdraw():
    if (network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or
            network.show_active() in FORK_LOCAL_ENVIRONMENTS):
        return accounts[1]
    else:
        return None
