import os
from urllib import request
from zipfile import ZipFile
import tensorflow as tf
import time
from src.coccidiosis_chicken_disease_classifier.entity.config_entity import PrepareCallbacksConfig

class PrepareCallbacks:
    def __init__(self, config: PrepareCallbacksConfig):
        self.config = config

    
    @property
    def _create_tb_callbacks(self):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        tb_log_dir = os.path.join(self.config.tensorboard_log_dir, f"tb_logs_{timestamp}")
        tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=tb_log_dir)
        return tensorboard_callback
    
    @property
    def _create_ckpt_callbacks(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=self.config.checkpoint_model_dir,
            save_best_only=True
        )
    
    def get_tb_ckpt_callbacks(self):
        return [self._create_tb_callbacks, self._create_ckpt_callbacks]


