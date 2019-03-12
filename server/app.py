import os

from flask import Flask, render_template, request
from flask_mail import Mail, Message
from werkzeug import secure_filename

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ.get('FLASK_SMTP_EMAIL_PATHWAY_ASSESSOR')
app.config['MAIL_PASSWORD'] = os.environ.get('FLASK_SMTP_KEY_PATHWAY_ASSESSOR')
app.config['MAIL_USE_TLS'] = False
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
        # f = request.files['file']
        email = request.form['email']
        # f.save(secure_filename(f.filename))
        # file_name = secure_filename(f.filename)

        msg = Message(
            'PathwayAssessor results',
            sender=os.environ.get('FLASK_SMTP_EMAIL_PATHWAY_ASSESSOR'),
            recipients=[email]
        )
        msg.body = "This is the email body"
        mail.send(msg)

        return 'email sent to: {}'.format(email)
        # return 'file uploaded successfully: {} from {}'.format(file_name, email)


if __name__ == '__main__':
    app.run(debug=True)