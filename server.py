import os
import sys

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

# linter 
@app.route('/lint', methods=['POST'])
@payment.required(100)
def lint():
    if request.method == 'POST':
        lint_file = request.files['file']
        if lint_file and allowed_file(lint_file.filename):
            filename = secure_filename(lint_file.filename)
            print("filename = {0}".format(filename))
            lint_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            with open(filename) as f:
                print("Uploaded File = {}".format(f.read()))
                f.seek(0)
                document, errors = tidy_document(f.read(), options={'numeric-entities':1})
            print("Linted Document:\n{}".format(document));
            print("Errors:\n{}".format(errors));
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return json.dumps({
                'doc': str(document),
                'err': str(errors)
            })

    return json.dumps({
        'error': 'could not process file'
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
    pt = sys.argv[1] if (len(sys.argv) > 1) else 5001
    app.run(host='0.0.0.0', port=pt)
