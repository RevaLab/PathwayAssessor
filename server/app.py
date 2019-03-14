import io
import os
import tempfile

from flask import Flask, render_template, request
from flask_mail import Mail, Message
from werkzeug import secure_filename

import pandas as pd

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ.get('FLASK_SMTP_EMAIL_PATHWAY_ASSESSOR')
app.config['MAIL_PASSWORD'] = os.environ.get('FLASK_SMTP_KEY_PATHWAY_ASSESSOR')
print(os.environ.get('FLASK_SMTP_KEY_PATHWAY_ASSESSOR'))
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


@app.route('/')
def landing_page():
    return render_template('index.html')


@app.route('/upload')
def upload_file():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file_2():
    if request.method == 'POST':

        f = request.files['file']
        # email = request.form['email']
        email='anna.pamela@gmail.com'
        msg = Message(
            'PathwayAssessor results',
            sender=os.environ.get('FLASK_SMTP_EMAIL_PATHWAY_ASSESSOR'),
            recipients=[email]
        )

        expression_table = pd.read_csv(f, sep='\t', header=0, index_col=0)

        fp = tempfile.TemporaryFile()

        # expression_table.to_csv(fp)
        # towrite = io.BytesIO()
        # expression_table.to_excel(towrite)
        # towrite.seek(0)

        def export_csv(df):
            with io.StringIO() as buffer:
                df.to_csv(buffer, sep='\t')
                return buffer.getvalue()

        # with app.open_resource(fp) as result_f:
        #     msg.attach('mehh.txt', towrite.read())
        msg.attach(filename='mehh.csv', content_type='text/csv', data=export_csv(expression_table))
        msg.body = "This is the email body"
        mail.send(msg)

        fp.close()

        # print(boop)



        return 'email sent to: {}'.format(email)
        # return 'file uploaded successfully: {} from {}'.format(file_name, email)


if __name__ == '__main__':
    app.run(debug=True)