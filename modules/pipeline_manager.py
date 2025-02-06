import yaml
import logging
from modules.data_loader import DataLoader
from modules.query_manager import QueryManager

logging.basicConfig(level=logging.INFO)

class PipelineManager:
    """manages execution of mcp components"""
    
    def __init__(self, config_path):
        with open(config_path, "r") as config_file:
            self.config = yaml.safe_load(config_file)
        self.datasets = {}

    def load_datasets(self):
        """loads datasets based on the configuration file"""
        for key, path in self.config.get("data_paths", {}).items():
            if path.endswith(".csv"):
                self.datasets[key] = DataLoader.load_csv(path)
            elif path.endswith(".json"):
                self.datasets[key] = DataLoader.load_json(path)
            elif path.endswith(".xlsx"):
                self.datasets[key] = DataLoader.load_excel(path)
        logging.info("datasets loaded")

    def execute_pipeline(self):
        """executes the configured mcp steps"""
        steps = self.config.get("pipeline_steps", [])
        for step in steps:
            query_type = step.get("query_type")
            dataset_key = step.get("dataset")
            params = step.get("params", {})

            if dataset_key in self.datasets:
                result = QueryManager.route_query(query_type, self.datasets[dataset_key], params)
                logging.info(f"execution result for {query_type}: {result}")
            else:
                logging.error(f"dataset {dataset_key} not found")

