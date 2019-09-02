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

#from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.layers import GlobalAveragePooling2D, Dense, Dropout,Activation,Flatten
#from official.vision.image_classification import common
#from official.vision.image_classification import imagenet_preprocessing
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

        crop_list, label_list = pipeline.input_pipeline(files, 1)

        #crop_images = np.array(crop_list)
        label_set = np.array(label_list)
        Y = np.asarray(label_list)
        #Y = np_utils.to_categorical(label_set, num_classes)

        x, y = shuffle(crop_list, Y, random_state=2)
        x_np = np.asarray(x)
        y_np = np.asarray(y)
        x_train, x_test, y_train, y_test = train_test_split(x_np, y_np, test_size=0.2, random_state=2)
        print(x_train.shape)
        print(y_train.shape)
        print(x_test.shape)
        print(y_test.shape)


        #model = tf.keras.Sequential([
        #                                # Adds a densely-connected layer with 64 units to the model:
        #                                layers.Dense(64, activation='relu', input_shape=(32,)),
        #                                # Add another:
        #                                layers.Dense(64, activation='relu'),
        #                                # Add a softmax layer with 10 output units:
        #                                layers.Dense(10, activation='softmax')
        #                            ])

        #lr_schedule =  0.1
        #optimizer = common.get_optimizer(lr_schedule)
        image_input = Input(shape=(224, 224, 3))
        #model = keras.applications.resnet.ResNet50(weights='imagenet')
        model = ResNet50(input_tensor=image_input, include_top=True,weights='imagenet')
        model.summary()
        final_layer = model.get_layer('avg_pool').output
        x = Flatten(name='flatten')(final_layer)
        out = Dense(num_classes, activation='softmax', name='output_layer')(x)
        custom_model = Model(inputs=image_input, outputs=out)
        custom_model.summary()

        for layer in custom_model.layers[:-1]:
            layer.trainable = False

        custom_model.layers[-1].trainable

        #train_model = keras.models.Model(inputs=model_input, outputs=model)

        #model.compile(optimizer=tf.train.AdamOptimizer(0.001),
        #              loss='categorical_crossentropy',
        #              metrics=['accuracy'])

        custom_model.compile(loss='sparse_categorical_crossentropy',
          optimizer='adam', metrics=['accuracy'])

        #custom_model.fit(model_input, norm_label, epochs=5, batch_size=32, 
        #    steps_per_epoch=10, verbose=1)


        t=time.time()
        train_hist = custom_model.fit(x_train, y_train, batch_size=32, epochs=12, 
            verbose=1, validation_data=(x_test, y_test) )
        print('Training time: %s' % (t - time.time()))

        (loss, accuracy) = custom_model.evaluate(x_test, y_test, batch_size=10, verbose=1)
        print("loss={:4f}, accuracy: {:.4f}%".format(loss, accuracy * 100))

        #Add final layer
        #final_layer = base_model.output
        #final_layer = Flatten()(final_layer)
        #predictions = tf.keras.layers.Dense(100, activation='softmax')(final_layer)

        #model = Model(input=base_model.input, output=predictions)

        #model.compile(optimizer=keras.optimizers.SGD(lr=0.01, momentum=0.9, nesterov=True), 
        #                loss=keras.losses.categorical_crossentropy)

        #classifier = tf.estimator.Estimator(model_fn=cnn_model_fn, model_dir=/tmp/resnet_models)

        #tensors_to_log = {"probabilities": "softmax_tensor"}
        #logging_hook = tf.train.LoggingTensorHook(tensors=tensors_to_log, every_n_iter=50)
        #classifier.train(input_fn=lambda: train_input_fn(train_list), steps=10, hooks=[logging_hook])


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