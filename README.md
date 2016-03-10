# 21.co Bitoin HTML Linter
For Stanford CS251P -- 21.co Marketplace

Implements a simple, bitoin-payable API endpoint that accepts an html document and prettifies it. In it's present state, the server is little more than a wrapper around the [PyTidyLib](http://countergram.com/open-source/pytidylib/) module. However, you could easily extend it to lint a variety of different file types (JavaScript, Ruby, CSS, etc.), at which point it statrs becoming a more useful command-line tool for static code analysis.

## Usage
POST a html document to the server to lint it. Accepts the html file as a post parameter. The response is a JSON object with format `{"doc": <corrected html document>, "err": <list of formatting errors in document>}.`

Note: you must have a working copy of 21.co's `two1` library to use this 

Example usage:
```
# get the repo
git clone https://github.com/tleavitt/bitcoin-linter.git
cd bitcoin-linter 

# install dependencies
pip3 install -r requirements.txt

# run the server locally
python3 server.py 5001

# POST an html file to your local server (from a new shell)
python3 lint.py test.html 0.0.0.0:5001
```
