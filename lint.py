import sys

# import from the 21 Bitcoin Developer Library
from two1.commands.config import Config
from two1.lib.wallet import Wallet
from two1.lib.bitrequests import BitTransferRequests

SERVER_IP = '10.31.229.209'

username = Config().username
wallet = Wallet()
requests = BitTransferRequests(wallet, username)

def lint(server, file_name):
    """ Call the lint service hosted on the micropayments server"""
    with open(file_name, 'rb') as f:
        upload = requests.post('http://' + server + '/upload', files={'file': f})
    lint_url = 'http://' + server + '/lint?file={0}&payout_address={1}'
    answer = requests.post(url=lint_url.format(file_name, wallet.get_payout_address()))
    return answer.text    

if __name__ == "__main__":
    fname = sys.argv[1]
    res = lint(SERVER_IP, fname)
    print (res) 

