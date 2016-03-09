# bitcoin-linter
For Stanford CS251P -- 21.co Marketplace

POST a html document to the server to lint it. Accepts the html file as a post parameter. The response is a JSON object with format `{"doc": <corrected html document>, "err": <list of formatting errors in document>}.`

Example usage:
```
git clone https://github.com/tleavitt/bitcoin-linter.git
cd bitcoin-linter 
python3 lint.py <path-to-html-file>
```
