from __future__ import absolute_import, division, print_function, unicode_literals
import copy
import os
import time
import numpy as np
from resnet50 import ResNet50
import tensorflow as tf
from tensorflow.keras import layers

import keras
from keras.layers import Input
from keras.models import Model
from keras.utils import np_utils

from keras.preprocessing import image
from keras.layers import GlobalAveragePooling2D, Dense, Dropout,Activation,Flatten
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

from sample_pipeline import SamplePipeline

STEPS_PER_EPOCH = 5500 / 1024


def run_sample_pipeline():
    """Run the sample pipeline
    """

    num_classes = 100;
    pipeline = SamplePipeline()
    files = []
    with tf.Graph().as_default() as g, tf.device('/device:GPU:0'):
        raw_files = os.listdir('./TFRecords')
        for file in raw_files:
            if file.find("tfrecord") != -1:
                files.append('./TFRecords/%s' % file)

        # Create dataset
        crop_list, label_list = pipeline.input_pipeline(files, 1)

        label_set = np.array(label_list)
        Y = np.asarray(label_list)

        x, y = shuffle(crop_list, Y, random_state=2)
        x_np = np.asarray(x)
        y_np = np.asarray(y)
        x_train, x_test, y_train, y_test = train_test_split(x_np, y_np, test_size=0.2, random_state=2)
        print(x_train.shape)
        print(y_train.shape)
        print(x_test.shape)
        print(y_test.shape)


        image_input = Input(shape=(224, 224, 3))
        model = ResNet50(input_tensor=image_input, include_top=True,weights='imagenet')
        model.summary()

        #Add final layer
        final_layer = model.get_layer('avg_pool').output
        x = Flatten(name='flatten')(final_layer)
        out = Dense(num_classes, activation='softmax', name='output_layer')(x)
        custom_model = Model(inputs=image_input, outputs=out)
        custom_model.summary()

        for layer in custom_model.layers[:-1]:
            layer.trainable = False

        custom_model.layers[-1].trainable

        custom_model.compile(loss='sparse_categorical_crossentropy',
          optimizer='adam', metrics=['accuracy'])

        t=time.time()
        train_hist = custom_model.fit(x_train, y_train, batch_size=32, epochs=12, 
            verbose=1, validation_data=(x_test, y_test) )
        print('Training time: %s' % (t - time.time()))

        (loss, accuracy) = custom_model.evaluate(x_test, y_test, batch_size=10, verbose=1)
        print("loss={:4f}, accuracy: {:.4f}%".format(loss, accuracy * 100))


        #ctr = 0
        #init = tf.global_variables_initializer()
        #sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True, log_device_placement=False))
        #sess.run(init)

        # Start the queue runners.
        #coord = tf.train.Coordinator()

        #with sess:
        #    while 1:
        #        try:
        #            cr, nrm = sess.run([crop, norm_label])
        #            print(cr.shape)
        #            print(nrm)
                    #print(xcoords)
                    #print(ycoords)
        #        except KeyboardInterrupt:
        #            coord.request_stop()
        #            break

def main(_):
    run_sample_pipeline()

if __name__ == '__main__':
    tf.app.run()