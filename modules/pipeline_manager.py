import yaml
import logging
from modules.data_loader import DataLoader
from models.temperature_trends import TemperatureTrends
from models.scenario_projection import ScenarioProjection
from modules.benchmark_logger import BenchmarkLogger
from modules.query_manager import QueryManager

logging.basicConfig(level=logging.INFO)

class PipelineManager:
    """manages mcp"""
    
    def __init__(self, config_path):
        with open(config_path, "r") as config_file:
            self.config = yaml.safe_load(config_file)
        self.datasets = {}
        self.pipeline_steps = self.config.get("pipeline_steps", [])

    def load_datasets(self):
        """load datasets based on the config"""
        for key, path in self.config.get("data_paths", {}).items():
            try:
                if path.endswith(".csv"):
                    self.datasets[key] = DataLoader.load_csv(path)
                elif path.endswith(".json"):
                    self.datasets[key] = DataLoader.load_json(path)
                elif path.endswith(".xlsx"):
                    self.datasets[key] = DataLoader.load_excel(path)
                logging.info(f"Dataset '{key}' loaded from {path}.")
            except Exception as e:
                logging.error(f"Error loading dataset '{key}' from {path}: {e}")
                self.datasets[key] = None
        logging.info("Datasets loaded.")

    @BenchmarkLogger.benchmark_function
    def execute_pipeline(self):
        """execution pipeline > config.yaml"""
        if not hasattr(self, "pipeline_steps"):
            logging.error("check pipeline_steps")
            return

        for step in self.pipeline_steps:
            query_type = step["query_type"]
            dataset_key = step["dataset"]
            params = step.get("params", {})

            if dataset_key not in self.datasets or self.datasets[dataset_key] is None:
                logging.error(f"Dataset '{dataset_key}' not found or not loaded.")
                continue

            result = None 

            if query_type == "temperature_trends":
                result = TemperatureTrends.get_temperature_trends(self.datasets[dataset_key], **params)
            elif query_type == "scenario_projection":
                result = ScenarioProjection.project_climate_scenario(self.datasets[dataset_key], **params)
            else:
                logging.error(f"unknown query type: {query_type}")

            logging.info(f"execution result for {query_type}: {result}")