import tensorflow as tf


def model1():
    input_layer = tf.keras.layers.Input(shape=(512, 1024, 3))
    x = tf.keras.layers.Conv2D(filters=1, kernel_size=(256, 128),
                               activation="relu", strides=(1, 4))(input_layer)
    x = tf.keras.layers.Conv2D(filters=2, kernel_size=(128, 64),
                               activation="relu", strides=(1, 4))(x)
    x = tf.keras.layers.Conv2D(filters=4, kernel_size=(64, 32),
                               activation="relu", strides=(1, 4))(x)
    x = tf.keras.layers.Conv2D(filters=8, kernel_size=(32, 16),
                               activation="relu", strides=(1, 4))(x)
    x = tf.keras.layers.Flatten()(x)
    x = tf.keras.layers.Dense(1024, activation="relu")(x)
    output_layer = tf.keras.layers.Dense(10)(x)

    model = tf.keras.Model(input_layer, output_layer)

    model.compile(optimizer="adam", loss=tf.keras.losses.SparseCategoricalCrossentropy)

    return model


m = model1()