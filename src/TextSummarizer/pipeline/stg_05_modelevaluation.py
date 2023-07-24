from TextSummarizer.components.modelevaluation import ModelEvaluation
from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.logging import logger


class model_evaluation_pipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config = model_evaluation_config)
        #data_transformation.convert_examples_to_features()
        model_evaluation.evaluate()