from TextSummarizer.components.datavalidation import DataValidation
from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.logging import logger


class data_validation_pipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config = data_validation_config)
        data_validation.validate_all_files_exists()
        
