from brownie import accounts, SimpleStorage, network
import time
from dotenv import load_dotenv

load_dotenv()


def deploy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    time.sleep(1)
    store_val = simple_storage.addPerson("KC", 123, {"from": account})
    time.sleep(1)
    new_val = simple_storage.SeePeople("KC")
    time.sleep(1)
    print(new_val)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.load("0")


def main():
    deploy_simple_storage()
    time.sleep(1)
