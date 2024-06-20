import os
from flask import Flask, render_template, request, session, redirect, url_for, flash, send_file
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from modules.base_64 import utf8_to_base64, base64_to_utf8, encode_file, decode_file
from modules.URL_encoder import url_encode, url_decode
from modules.JSON_manager import json_minify, json_beautify, minify_file, beautify_file
from modules.URL_shortener import url_shorten
from modules.QR_generator import generate_qr_code

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vjw&2bmQx9LDH3!ZcR8e7$fSbFz+o5n@1*p4J0aKPTquMd?YUVtg!6lAiyhB#wN'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Utilitybase.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['DOWNLOAD_FOLDER'] = 'downloads'


os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['DOWNLOAD_FOLDER'], exist_ok=True)

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(9999), nullable=False)


def insert_new_user(username, password):
    new_user = User(username=username, password=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['username'] = username
            flash('Successfully logged in!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password2 = request.form['password2']

        if password != password2:
            flash('Passwords do not match', 'error')
        elif User.query.filter_by(username=username).first():
            flash('Username already exists', 'error')
        else:
            insert_new_user(username, password)
            flash('Successfully registered!', 'success')
            return redirect(url_for('login'))

    return render_template('register.html')


@app.route("/logout")
def logout():
    session.pop('username', None)
    session.pop('password', None)
    return render_template("index.html")


@app.route('/base64', methods=['GET', 'POST'])
def base64_page():
    if 'username' not in session:
        flash('You must be logged in to access this page', 'error')
        return redirect(url_for('login'))

    output_text = ""
    output_filename = ""
    if request.method == 'POST':
        input_text = request.form.get('input_text')
        action = request.form.get('action')
        file = request.files.get('file')

        if file:
            filename = secure_filename(file.filename)
            file_content = file.read()

            if action == 'Encode':
                try:
                    output_text = encode_file(file_content)
                    output_filename = f"{filename}.b64"
                    with open(os.path.join(app.config['DOWNLOAD_FOLDER'], output_filename), 'w') as f:
                        f.write(output_text)
                except Exception as e:
                    flash(str(e), 'error')
                    return render_template('base64.html', input_text=input_text, output_text="", action=action)
            elif action == 'Decode':
                try:
                    output_text = decode_file(file_content)
                    output_filename = filename.replace('.b64', '') 
                    with open(os.path.join(app.config['DOWNLOAD_FOLDER'], output_filename), 'wb') as f:
                        f.write(output_text) 
                except Exception as e:
                    flash(str(e), 'error')
                    return render_template('base64.html', input_text=input_text, output_text="", action=action)
        else:
            if action == 'Encode':
                try:
                    output_text = utf8_to_base64(input_text)
                except Exception as e:
                    flash(str(e), 'error')
                    return render_template('base64.html', input_text=input_text, output_text="", action=action)
            elif action == 'Decode':
                try:
                    output_text = base64_to_utf8(input_text)
                except Exception as e:
                    flash(str(e), 'error')
                    return render_template('base64.html', input_text=input_text, output_text="", action=action)

            output_filename = "output.txt"
            with open(os.path.join(app.config['DOWNLOAD_FOLDER'], output_filename), 'w') as f:
                f.write(output_text)

        return render_template('base64.html', input_text=input_text, output_text=output_text, action=action,
                               output_filename=output_filename)

    return render_template('base64.html')


@app.route('/json', methods=['GET', 'POST'])
def json_page():
    if 'username' not in session:
        flash('You must be logged in to access this page', 'error')
        return redirect(url_for('login'))

    output_text = ""
    output_filename = ""
    if request.method == 'POST':
        input_text = request.form.get('input_text')
        action = request.form.get('action')
        file = request.files.get('file')

        if file:
            filename = secure_filename(file.filename)
            file_content = file.read().decode('utf-8')
            if action == 'Minify':
                output_text = minify_file(file_content)
                output_filename = f"{filename.split('.')[0]}_minified.json"
            elif action == 'Beautify':
                output_text = beautify_file(file_content)
                output_filename = f"{filename.split('.')[0]}_beautified.json"

            with open(os.path.join(app.config['DOWNLOAD_FOLDER'], output_filename), 'w') as f:
                f.write(output_text)
        else:
            if action == 'Minify':
                output_text = json_minify(input_text)
            elif action == 'Beautify':
                output_text = json_beautify(input_text)
            output_filename = "output.json"
            with open(os.path.join(app.config['DOWNLOAD_FOLDER'], output_filename), 'w') as f:
                f.write(output_text)

        return render_template('json.html', input_text=input_text, output_text=output_text, action=action,
                               output_filename=output_filename)

    return render_template('json.html')


@app.route('/url', methods=['GET', 'POST'])
def url_page():
    if 'username' not in session:
        flash('You must be logged in to access this page', 'error')
        return redirect(url_for('login'))

    if request.method == 'POST':
        input_text = request.form['input_text']
        action = request.form['action']

        if action == 'Encode':
            encoded_text = url_encode(input_text)
            return render_template('url.html', input_text=input_text, output_text=encoded_text, action=action)
        elif action == 'Decode':
            decoded_text = url_decode(input_text)
            return render_template('url.html', input_text=input_text, output_text=decoded_text, action=action)

    return render_template('url.html')


@app.route('/qr', methods=['GET', 'POST'])
def qr_page():
    if 'username' not in session:
        flash('You must be logged in to access this page', 'error')
        return redirect(url_for('login'))

    if request.method == 'POST':
        data = request.form.get('text')
        if not data:
            error_message = 'Text is required'
            return render_template('qr.html', error_message=error_message)

        fill_color = request.form.get('fill', 'black')
        back_color = request.form.get('back_color', 'white')

        qr_image = generate_qr_code(data, fill_color, back_color)

        return render_template('qr.html', qr_image=qr_image)

    return render_template('qr.html')


@app.route('/link_shortener', methods=['GET', 'POST'])
def link_shortener():
    if 'username' not in session:
        flash('You must be logged in to access this page', 'error')
        return redirect(url_for('login'))

    if request.method == 'POST':
        inputed_url = request.form.get('input_url')
        shortened_url = url_shorten(inputed_url)
        return render_template('link_shortener.html', input_url=inputed_url, shortened_url=shortened_url)

    return render_template('link_shortener.html')


@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join(app.config['DOWNLOAD_FOLDER'], filename), as_attachment=True)


@app.route("/about_us")
def about_us():
    return render_template("about_us.html")


if __name__ == '__main__':
    app.run(debug=True)
