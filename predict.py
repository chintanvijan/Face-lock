from keras.models import load_model
classifier = load_model("classifier.h5")
import numpy as np
from keras.preprocessing import image
test_image = image.load_img('0124.png', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result= classifier.predict(test_image)
#train_generator.class_indices
#if result[0][0] == 1:
 #   prediction = 'dog'
#else:
 #   prediction = 'cat'
print(result*100)