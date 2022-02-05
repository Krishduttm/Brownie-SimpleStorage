from brownie import SimpleStorage, accounts
import time


def test_deploy():
    account = accounts[0]

    time.sleep(1)
    simple_storage = SimpleStorage.deploy({"from": account})
    time.sleep(1)
    simple_storage.addPerson("KC", 123, {"from": account})
    time.sleep(1)
    new_val = simple_storage.SeePeople("KC")
    time.sleep(1)
    assert new_val == 123
