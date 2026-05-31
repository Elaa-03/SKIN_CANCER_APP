from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'skin_cancer_secret_key'

UPLOAD_FOLDER = 'static/uploads'
MODEL_PATH = 'model/vgg16_malignant_vs_benign.h5'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

model = tf.keras.models.load_model(MODEL_PATH)

def get_db():
    return mysql.connector.connect(
        host='localhost', user='root', password='', database='skin_cancer_db'
    )

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db(); cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone(); db.close()
        if user:
            session['user'] = username
            return redirect(url_for('dashboard'))
        flash('Identifiants incorrects', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    db = get_db(); cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT COUNT(*) as total FROM patients")
    total = cursor.fetchone()['total']
    cursor.execute("SELECT COUNT(*) as cnt FROM patients WHERE result='Malignant'")
    malignant = cursor.fetchone()['cnt']
    benign = total - malignant
    cursor.execute("SELECT * FROM patients ORDER BY created_at DESC LIMIT 5")
    recent = cursor.fetchall(); db.close()
    return render_template('dashboard.html', total=total, malignant=malignant, benign=benign, recent=recent)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if 'user' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        name = request.form['name']
        age  = request.form['age']
        file = request.files['image']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            img = image.load_img(filepath, target_size=(224, 224))
            img_array = image.img_to_array(img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)
            prediction = model.predict(img_array)[0][0]
            result = 'Malignant' if prediction > 0.5 else 'Benign'
            probability = float(prediction) if prediction > 0.5 else float(1 - prediction)
            db = get_db(); cursor = db.cursor()
            cursor.execute(
                "INSERT INTO patients (name, age, result, probability, image_path) VALUES (%s,%s,%s,%s,%s)",
                (name, age, result, probability, filepath)
            )
            db.commit(); db.close()
            return render_template('result.html', result=result, prob=round(probability*100,2), img=filepath, name=name)
        flash("Format non supporté. Utilisez PNG, JPG ou JPEG.", 'warning')
    return render_template('predict.html')

@app.route('/patients')
def patients():
    if 'user' not in session:
        return redirect(url_for('login'))
    db = get_db(); cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM patients ORDER BY created_at DESC")
    patients_list = cursor.fetchall(); db.close()
    return render_template('patients.html', patients=patients_list)

if __name__ == '__main__':
    app.run(debug=True)
