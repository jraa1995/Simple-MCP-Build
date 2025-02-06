from modules.pipeline_manager import PipelineManager

if __name__ == "__main___":
    pipeline = PipelineManager("config/config.yaml")
    pipeline.load_datasets()
    pipeline.execute_pipeline()