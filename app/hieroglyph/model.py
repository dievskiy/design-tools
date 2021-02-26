import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import uuid


class HieroglyphModel:
    def __init__(self):
        self.N_Z = 50
        self.DIMS = (64, 64, 1)
        generator = [
            tf.keras.layers.Dense(units=16 * 16 * 128, activation="relu"),
            tf.keras.layers.Reshape(target_shape=(16, 16, 128)),
            tf.keras.layers.Conv2DTranspose(
                filters=128, kernel_size=5, strides=(2, 2), padding="SAME"
            ),
            tf.keras.layers.LeakyReLU(alpha=0.2),
            tf.keras.layers.Conv2DTranspose(
                filters=64, kernel_size=5, strides=(2, 2), padding="SAME", activation="relu"
            ),
            tf.keras.layers.Conv2DTranspose(
                filters=1, kernel_size=5, strides=(1, 1), padding="SAME", activation="sigmoid"
            ),
        ]

        self._model = Generator(
            gen=generator,
            n_Z=self.N_Z
        )
        self.load_weights()

    def load_weights(self):
        self._model.load_weights("weights")

    def generate_hieroglyph(self, stiffness):
        """
        Generates image with hieroglyph and saves it to local disk
        :return: name of the image file
        """
        name = ""
        stiffness = int(stiffness)
        try:
            # generate sample with random nums
            data = tf.random.normal(shape=(1, self.N_Z))
            # data = np.random.randn(1, self.N_Z)
            if stiffness == 0:
                stiffness = 0.5

            data *= stiffness
            sample = self._model.generate(data)
            generated_image = sample.numpy()[0].squeeze()

            # vanilla noise remover
            generated_image[generated_image < 0.2] = 0
            generated_image[0:12][:] = 0
            generated_image[58:][:] = 0
            generated_image = generated_image.transpose()
            generated_image[:15][:] = 0
            generated_image[56:][:] = 0
            generated_image = generated_image.transpose()

            name = "./app/tmp/" + str(uuid.uuid4()) + ".bmp"
            plt.imsave(name, generated_image, cmap=plt.cm.Greys, format='bmp')
        except Error as er:
            ...
        finally:
            return name


class Generator(tf.keras.Model):
    """
    WGAN Generator Model that extends tensorflow model
    """

    def __init__(self, **kwargs):
        super(Generator, self).__init__()
        self.__dict__.update(kwargs)
        self.gen = tf.keras.Sequential(self.gen)

    def generate(self, z):
        return self.gen(z)
