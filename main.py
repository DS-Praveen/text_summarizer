from TextSummarizer.pipeline.stg_01_dataingestion import data_ingestion_pipeline
from TextSummarizer.pipeline.stg_02_datavalidation import data_validation_pipeline
from TextSummarizer.pipeline.stg_03_datatrasformation import data_transformation_pipeline
from TextSummarizer.pipeline.stg_04_modeltrainer import model_trainer_pipeline
from TextSummarizer.pipeline.stg_05_modelevaluation import model_evaluation_pipeline
from TextSummarizer.logging import logger


stage_name = "Data Ingestion Stage"

try:
    logger.info(f"===============> {stage_name} Started <===============")
    data_ingestion = data_ingestion_pipeline()
    data_ingestion.main()
    logger.info(f"===============> {stage_name} Completed <===============")
    logger.info(f"\n\n =========================>>>>>>>>>>>>>>>>>>>o<<<<<<<<<<<<<<<<<<<=========================\n\n")
except Exception as e:
    logger.exception(e)
    raise e



#========================================================================================================
stage_name = "Data Validation Stage"

try:
    logger.info(f"===============> {stage_name} Started <===============")
    data_validation = data_validation_pipeline()
    data_validation.main()
    logger.info(f"===============> {stage_name} Completed <===============")
    logger.info(f"\n\n =========================>>>>>>>>>>>>>>>>>>>o<<<<<<<<<<<<<<<<<<<=========================\n\n")
except Exception as e:
    logger.exception(e)
    raise e



#========================================================================================================
stage_name = "Data Transformation Stage"

try:
    logger.info(f"===============> {stage_name} Started <===============")
    data_transformation = data_transformation_pipeline()
    data_transformation.main()
    logger.info(f"===============> {stage_name} Completed <===============")
    logger.info(f"\n\n =========================>>>>>>>>>>>>>>>>>>>o<<<<<<<<<<<<<<<<<<<=========================\n\n")
except Exception as e:
    logger.exception(e)
    raise e



#========================================================================================================
stage_name = "Model Training Stage"

try:
    logger.info(f"===============> {stage_name} Started <===============")
    model_trainer = model_trainer_pipeline()
    model_trainer.main()
    logger.info(f"===============> {stage_name} Completed <===============")
    logger.info(f"\n\n =========================>>>>>>>>>>>>>>>>>>>o<<<<<<<<<<<<<<<<<<<=========================\n\n")
except Exception as e:
    logger.exception(e)
    raise e



#========================================================================================================
stage_name = "Model Evaluation Stage"

try:
    logger.info(f"===============> {stage_name} Started <===============")
    model_trainer = model_evaluation_pipeline()
    model_trainer.main()
    logger.info(f"===============> {stage_name} Completed <===============")
    logger.info(f"\n\n =========================>>>>>>>>>>>>>>>>>>>o<<<<<<<<<<<<<<<<<<<=========================\n\n")
except Exception as e:
    logger.exception(e)
    raise e

