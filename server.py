import os

# import from the 21 Bitcoin Developer Library
from two1.lib.wallet import Wallet
from two1.lib.bitserv.flask import Payment

# import from Flask library
from flask import Flask, request
from flask import send_from_directory
from werkzeug import secure_filename

from tidylib import tidy_document
import json

app = Flask(__name__)

# set up the bitcoin wallet
wallet = Wallet()
payment = Payment(app, wallet)

# configure uploads
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = set(['js', 'html'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# verify filetype
def allowed_file(filename):
    return '.' in filename and \
       filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# upload file handler
@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print("filename = {0}".format(filename))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return 'OK'

# cleanup file handler
def cleanup(file_name):
    os.remove(file_name)
    return None

# linter 
@app.route('/lint', methods=['POST'])
@payment.required(100)
def lint():
    lint_file  = request.args.get('file')
    lint_file = "uploads/" + lint_file
    with open(lint_file) as f:
        document, errors = tidy_document(f.read(), options={'numeric-entities':1})
    print("Output String = {0}".format('document'))
    cleanup(lint_file)
    return json.dumps({
        'doc': document,
        'err': errors
    })

# Serves the app manifest to the 21 crawler.
@app.route('/manifest')
def docs():
    with open('manifest.yaml', 'r') as f:
        manifest_yaml = yaml.load(f)
    return json.dumps(manifest_yaml)

# set up and run the server
if __name__ == '__main__':
        # app.debug = True
        app.run(host='0.0.0.0', port=5001)
