# 21.co Bitoin HTML Linter
For Stanford CS251P -- 21.co Marketplace

Implements a bitoin-payable API endpoint that accepts an html document and prettifies it for a small amount of bitcoin. This simple example demonstrates how micropyaments-based-SaaS might look.

In it's present state, the server is little more than a wrapper around the [PyTidyLib](http://countergram.com/open-source/pytidylib/) module. However, you could easily extend the server code to lint a variety of different file types (JavaScript, Ruby, CSS, etc.). As you add support for more file types, the server starts to become a useful, versatile command-line tool for running static code analysis programatically.

## Usage
POST a html document to the server to lint it, at a cost of 100 Satoshis. Accepts the html file and 21 wallet address as post parameters. The response is a JSON object with format `{"doc": <corrected html document>, "err": <list of formatting errors in document>}.`

Note: you must have a working copy of 21.co's `two1` library to use this code

Example usage:
```
# get the repo
git clone https://github.com/tleavitt/bitcoin-linter.git
cd bitcoin-linter 

# install dependencies
pip3 install -r ./requirements.txt

# run the server locally
python3 ./server.py 5001

# POST an html file to your local server (from a new shell)
python3 ./lint.py ./test.html 0.0.0.0:5001
```
