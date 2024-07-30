import dlib
from skimage import io
from scipy.spatial import distance
import time

# Функция для получения результата в main.py
def result_f(url1, url2):
    sh_pr = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
    f_rec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
    marks_detector = dlib.get_frontal_face_detector()


    # Загрузка фотографии
    photo1 = io.imread('C:\\ДИСК\\Учёба\\Диплом\\FaceCheck' + url1)

    # Поиск лица на фотографии
    detected = marks_detector(photo1, 1)

    # Выделение ключевых точек лица
    for k, d in enumerate(detected):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(k, d.left(), d.top(), d.right(), d.bottom()))
        shape = sh_pr(photo1, d)

    # Извлечение дескриптора
    descriptor1 = f_rec.compute_face_descriptor(photo1, shape)
    print(descriptor1)

    # Загрузка фотографии
    photo2 = io.imread('C:\\ДИСК\\Учёба\\Диплом\\FaceCheck' + url2)

    # Поиск на фотографии лица
    detected = marks_detector(photo2, 1)

    # Выделение ключевых точек лица
    for k, d in enumerate(detected):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(k, d.left(), d.top(), d.right(), d.bottom()))
        shape = sh_pr(photo2, d)

    # Извлечение дескриптора
    descriptor2 = f_rec.compute_face_descriptor(photo2, shape)
    print(descriptor2)


    # Расчет Евклидова расстояния между двумя дексрипторами
    result = distance.euclidean(descriptor1, descriptor2)


    # Перевод результата в проценты
    if result == 0.6:
        result = '50%'
    elif result < 0.6:
        result = f'{(100 - (result * 100 / 1.2)):.2f}%'
    else:
        result = f'{(125 - (result * 100 / 0.8)):.2f}%'

    return result
