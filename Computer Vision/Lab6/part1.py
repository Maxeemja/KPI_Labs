
import keras.utils as image
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
import numpy as np
from sklearn.cluster import KMeans
import shutil, glob, os.path

image.LOAD_TRUNCATED_IMAGES = True

model = VGG16(weights='imagenet', include_top=False)


imdir = "dataset1/input_imgs"
targetdir = "dataset1/output_imgs/"

number_clusters = 3

# Список файлів
filelist = glob.glob(os.path.join(imdir, '*.jpg'))
print(filelist)

# Формування списку ознак зображень
featurelist = []
for imagepath in filelist:
    img = image.load_img(imagepath, target_size=(50, 50))
    img_data = image.img_to_array(img)
    img_data = np.expand_dims(img_data, axis=0)
    img_data = preprocess_input(img_data)
    features = np.array(model.predict(img_data))
    featurelist.append(features.flatten())

# Кластеризація
kmeans = KMeans(n_clusters=number_clusters, init='k-means++', n_init=10, random_state=0).fit(np.array(featurelist))

# Створення каталогу якщо каталог відсутній
try:
    os.makedirs(targetdir)

except OSError: pass

# Збереження зображень за кластером
print("\n")
for i, m in enumerate(kmeans.labels_):
    print("	Copy: %s / %s" %(i, len(kmeans.labels_)), end="\r")
    shutil.copy(filelist[i], targetdir + str(m) + "_" + str(i) + ".jpg")

