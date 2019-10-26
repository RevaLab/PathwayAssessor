import datetime
import io
import os
import pickle
from random import randint

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mail import Mail, Message

import pandas as pd
import pathway_assessor as pa


app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ.get('FLASK_SMTP_EMAIL_PATHWAY_ASSESSOR')
app.config['MAIL_PASSWORD'] = os.environ.get('FLASK_SMTP_KEY_PATHWAY_ASSESSOR')
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

cors = CORS(app, resources={
    r"/upload*": {"origins": "http://localhost:8080"},
    r"/process/*": {"origins": "http://localhost:8080"},
})


def export_csv(df):
    with io.StringIO() as buffer:
        df.to_csv(buffer, sep='\t')
        return buffer.getvalue()


@app.route('/')
def landing_page():
    return jsonify({'hello': 'landing_page'})
#
#
# @app.route('/upload')
# def upload_file():
#     return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':

        f = request.files['file']
        email = request.form['email']
        db = request.form['db']

        expression_table = pd.read_csv(f, sep='\t', header=0, index_col=0)

        random_id = randint(10000, 99999)
        datetime_upload = f"{datetime.datetime.now():%Y%m%d%H%M%S}"
        file_id = '{}_{}'.format(random_id, datetime_upload)

        instance = {
            'expression_table': expression_table,
            'email': email,
            'db': db,
        }

        pickle.dump(instance, open('./tmp/to_send/{}.pkl'.format(file_id), 'wb'))

        return jsonify({'file_id': file_id})


@app.route('/process/<file_id>', methods=['GET'])
def process(file_id):
    start_f = './tmp/to_send/{}.pkl'.format(file_id)
    end_f = './tmp/sent/{}.pkl'.format(file_id)
    data = pickle.load(open(start_f, 'rb'))

    expression_table = data['expression_table']
    email = data['email']
    db = data['db']

    msg = Message(
        'IPAS results',
        sender=os.environ.get('FLASK_SMTP_EMAIL_PATHWAY_ASSESSOR'),
        recipients=[email]
    )

    geometric = pa.geometric(expression_table=expression_table, db=db)

    #TODO: send as link instead of csv
    msg.attach(
        filename='ipas_{}.csv'.format(db),
        content_type='text/csv',
        data=export_csv(geometric)
    )

    msg.body = "Thanks for using IPAS. " \
               "Please see your results attached as a TSV file."
    mail.send(msg)

    os.rename(start_f, end_f)

    return jsonify(success=True)


if __name__ == '__main__':
    app.run(debug=True)
