from modules.pipeline_manager import PipelineManager

if __name__ == "__main__":
    pipeline = PipelineManager("config/config.yaml")
    pipeline.load_datasets()
    pipeline.execute_pipeline()
    print("MCP execution complete.")