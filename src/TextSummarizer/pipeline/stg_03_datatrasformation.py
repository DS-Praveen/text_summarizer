from TextSummarizer.components.datatransformation import DataTransformation
from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.logging import logger


class data_transformation_pipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_trasnformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config = data_trasnformation_config)
        #data_transformation.convert_examples_to_features()
        data_transformation.convert()