import datetime
import io
import os
import pickle
from random import randint

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from flask_mail import Mail, Message

import pandas as pd
import pathway_assessor as pa


app = Flask(__name__,
            static_folder="../client/dist/assets",
            template_folder="../client/dist")

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
    return render_template('index.html')
#
#
# @app.route('/upload')
# def upload_file():
#     return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
@cross_origin()
def upload():
    if request.method == 'POST':

        f = request.files['file']
        email = request.form['email']
        db = request.form['db']
        # ascending = request.form['sortBy'] == 'asc'
        direction = request.form['sortBy']
        rank_method = request.form['rankMethod']
        mode = request.form['mode']

        expression_table = pd.read_csv(f, sep='\t', header=0, index_col=0)

        random_id = randint(10000, 99999)
        datetime_upload = f"{datetime.datetime.now():%Y%m%d%H%M%S}"
        file_id = '{}_{}'.format(random_id, datetime_upload)

        instance = {
            'expression_table': expression_table,
            'email': email,
            'db': db,
            'direction': direction,
            'rank_method': rank_method,
            'mode': mode,
        }

        pickle.dump(instance, open('./tmp/to_send/{}.pkl'.format(file_id), 'wb'))

        return jsonify({'file_id': file_id})


@app.route('/process/<file_id>', methods=['GET'])
@cross_origin()
def process(file_id):
    start_f = './tmp/to_send/{}.pkl'.format(file_id)
    data = pickle.load(open(start_f, 'rb'))

    expression_table = data['expression_table']
    email = data['email']
    db = data['db']
    direction = data['direction']
    rank_method = data['rank_method']
    mode = data['mode']

    kwargs = {
        'expression_table': expression_table,
        'db': db,
    }

    msg = Message(
        'IPAS results',
        sender=os.environ.get('FLASK_SMTP_EMAIL_PATHWAY_ASSESSOR'),
        recipients=[email]
    )

    if direction == 'difference':
        ascending = run_pa(mode, kwargs, ascending=True, rank_method='max')
        descending = run_pa(mode, kwargs, ascending=False, rank_method='min')
        res = ascending - descending
        # print(res)
        msg.attach(
            filename='ipas_{}_{}_difference.csv'.format(db, mode),
            content_type='text/csv',
            data=export_csv(res)
        )

        msg.attach(
            filename='ipas_{}_{}_ascending.csv'.format(db, mode),
            content_type='text/csv',
            data=export_csv(ascending)
        )

        msg.attach(
            filename='ipas_{}_{}_descending.csv'.format(db, mode),
            content_type='text/csv',
            data=export_csv(descending)
        )
    elif direction == 'asc':
        ascending = run_pa(mode, kwargs, ascending=True, rank_method=rank_method)
        msg.attach(
            filename='ipas_{}_{}_ascending.csv'.format(db, mode),
            content_type='text/csv',
            data=export_csv(ascending)
        )
    else:
        descending = run_pa(mode, kwargs, ascending=False, rank_method=rank_method)
        msg.attach(
            filename='ipas_{}_{}_descending.csv'.format(db, mode),
            content_type='text/csv',
            data=export_csv(descending)
        )

    msg.body = """
        Thanks for using IPAS. Your parameters were as follows:
        
        Pathway database: {}
        Mode: {}
        Direction: {}
        Please see your results attached as a TSV file.
        
    """.format(db, mode, direction)

    mail.send(msg)

    os.remove(start_f)

    return jsonify(success=True)


def run_pa(mode, kwargs, ascending, rank_method):
    if mode == 'harmonic':
        res = pa.harmonic(
            **kwargs,
            ascending=ascending,
            rank_method=rank_method,
        )
    elif mode == 'min_p_val':
        res = pa.min_p_val(
            **kwargs,
            ascending=ascending,
            rank_method=rank_method,
        )
    else:
        res = pa.geometric(
            **kwargs,
            ascending=ascending,
            rank_method=rank_method,
        )
    return res


if __name__ == '__main__':
    app.run(debug=True)
