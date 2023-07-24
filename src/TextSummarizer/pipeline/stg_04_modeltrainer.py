from TextSummarizer.components.modeltrainer import ModelTrainer
from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.logging import logger


class model_trainer_pipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config = model_trainer_config)
        #data_transformation.convert_examples_to_features()
        model_trainer.train()