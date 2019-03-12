from flask import Flask, render_template, request
from werkzeug import secure_filename

app = Flask(__name__)


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
        email = request.form['email']
        f.save(secure_filename(f.filename))
        file_name = secure_filename(f.filename)
        return 'file uploaded successfully: {} from {}'.format(file_name, email)


if __name__ == '__main__':
    app.run(debug=True)