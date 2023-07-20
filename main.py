from TextSummarizer.pipeline.stg_01_dataingestion import data_ingestion_pipeline
from TextSummarizer.logging import logger


stage_name = "Data Ingestion Stage"

try:
    logger.info(f"===============> {stage_name} started <===============")
    data_ingestion = data_ingestion_pipeline()
    data_ingestion.main()
    logger.info(f"===============> {stage_name} completed <===============")
except Exception as e:
    logger.exception(e)
    raise e