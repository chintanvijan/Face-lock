from keras.models import Sequential
from keras.layers import Conv2D,MaxPooling2D,Flatten,Dense
import h5py

classifier = Sequential()

classifier.add(Conv2D(32,(3,3),input_shape = (64,64,3),activation="relu"))

classifier.add(MaxPooling2D(pool_size=(2,2)))

classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

classifier.add(Flatten())

classifier.add(Dense(output_dim=128,activation="relu"))

classifier.add(Dense(output_dim=1,activation="softmax"))

classifier.compile(optimizer="adam",loss="binary_crossentropy",metrics=['accuracy'])

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale=1./255,shear_range=0.2,zoom_range=0.2,horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory('Dataset/Train',target_size=(64,64),batch_size=32,class_mode='binary')

validation_generator = test_datagen.flow_from_directory('Dataset/Test',target_size=(64, 64),batch_size=32,class_mode='binary')

classifier.fit_generator(train_generator,steps_per_epoch=100,epochs=5,validation_data=validation_generator,validation_steps=2000)

classifier.save("classifier.h5")