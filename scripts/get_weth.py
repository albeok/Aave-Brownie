from scripts.helpful_scripts import get_account
from brownie import interface, config, network
import time


def get_weth():
    """
    Mints WETH by depositing ETH.
    """
    # ABI
    # Address
    account = get_account()
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_token"])
    tx = weth.deposit({"from": account, "value": 0.1 * 10**18})
    print("Received 0.1 WETH")
    tx.wait(1)
    time.sleep(1)
    return tx


def main():
    get_weth()
