# Updating Componenets
import os
import urllib.request as request
import zipfile
from TextSummarizer.logging import logger
from TextSummarizer.utils.common import get_size
import requests
from pathlib import Path
from TextSummarizer.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    """
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename= self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size : {get_size(Path(self.config.local_data_file))}")

    """
    def download_file(self):
        fname = "data.zip"
        if not os.path.exists(self.config.local_data_file):
            res = requests.get(self.config.source_URL)

            if res.status_code == 200:
                
                content = res.content

                with open (fname, "wb") as file:
                    file.write(content)
            logger.info(f"{fname} downloaded successfully...!")
        
        else:
            logger.info(f"{fname} already exists of size : {get_size(Path(self.config.local_data_file))}")


    def extract_zip(self):
        unzipped_path = self.config.unzip_dir
        os.makedirs(unzipped_path, exist_ok= True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzipped_path)