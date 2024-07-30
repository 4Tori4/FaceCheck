# Импорт необходимых для работы с Flask компонент
from flask import Flask, render_template, send_from_directory, url_for, request
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
from FaceCheck import result_f
import time


app = Flask(__name__)
app.config['SECRET_KEY'] = 'asldfkjlj'
app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)


class UploadForm(FlaskForm):
    photo = FileField(
        validators=[
            FileAllowed(photos, 'Допустимы только изображения'),
            FileRequired('Поле изображения не должно быть пустым')
        ]
    )
    submit = SubmitField('Загрузить')

# Функция, помещающая файл в директорию по заданному пути
@app.route('/uploads/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)

# Функция для загрузки изображений в формы
@app.route('/', methods=['GET', 'POST'])
def upload_image():
    form = UploadForm()
    file_url = "\\uploads\\start_image.jpg"
    file_url_1 = "\\uploads\\start_image.jpg"
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        image = request.form.get("image")

        if image == "image_1":
            if request.form.get("g_image_1") != "\\uploads\\start_image.jpg" and request.form.get("g_image") != "\\uploads\\start_image.jpg":
                file_url = "\\uploads\\start_image.jpg"
                file_url_1 = "\\uploads\\start_image.jpg"
            else:
                file_url_1 = request.form.get("g_image_1")
            file_url = url_for('get_file', filename=filename)

        if image == "image_2":
            if request.form.get("g_image_1") != "\\uploads\\start_image.jpg" and request.form.get("g_image") != "\\uploads\\start_image.jpg":
                file_url = "\\uploads\\start_image.jpg"
                file_url_1 = "\\uploads\\start_image.jpg"
            else:
                file_url = request.form.get("g_image")
            file_url_1 = url_for('get_file', filename=filename)

    else:
        file_url = "\\uploads\\start_image.jpg"
        file_url_1 = "\\uploads\\start_image.jpg"

    # Вызов функции из FaceCheck.py для вывода результата сравнения
    result = None

    if file_url != "\\uploads\\start_image.jpg" and file_url_1 != "\\uploads\\start_image.jpg":
        result = result_f(file_url, file_url_1)


    return render_template('index.html', form=form, file_url=file_url, form_1=form, file_url_1=file_url_1, result=result )


if __name__ == '__main__':
    app.run(debug=False)



