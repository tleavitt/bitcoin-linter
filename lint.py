import sys

# import from the 21 Bitcoin Developer Library
from two1.commands.config import Config
from two1.lib.wallet import Wallet
from two1.lib.bitrequests import BitTransferRequests

username = Config().username
wallet = Wallet()
requests = BitTransferRequests(wallet, username)

def lint(server, file_name):
    """ Call the lint service hosted on the micropayments server"""
    with open(file_name, 'rb') as f:
        lint_url = 'http://' + server + '/lint?&payout_address={}'
        answer = requests.post(url=lint_url.format(wallet.get_payout_address()), files={'file': f})
    return answer.text    

if __name__ == "__main__":
    fname = sys.argv[1]
    server_ip = sys.argv[2]
    res = lint(server_ip, fname)
    print (res) 

