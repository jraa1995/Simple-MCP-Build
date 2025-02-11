import unittest
import time
import logging
from modules.pipeline_manager import PipelineManager
from modules.benchmark_logger import BenchmarkLogger

class TestPipelineManager(unittest.TestCase):
    """Unit tests for the MCP pipeline execution."""

    @classmethod
    def setUpClass(cls):
        """set up the pipeline before running tests"""
        cls.pipeline = PipelineManager(config_path="config/config.yaml")
        logging.info("pipeline Manager initialized for testing")

    def test_load_datasets(self):
        """test if datasets are loaded correctly"""
        self.pipeline.load_datasets()
        self.assertGreater(len(self.pipeline.datasets), 0, "datasets failed to load")

    def test_pipeline_execution(self):
        """test if the MCP pipeline executes without errors"""
        start_time = time.perf_counter()
        self.pipeline.execute_pipeline()
        end_time = time.perf_counter()

        execution_time = end_time - start_time
        logging.info(f"test pipeline executed in {execution_time:.4f} sec")
        self.assertTrue(execution_time > 0, "pipeline execution failed")

    def test_logging_benchmark(self):
        """test if benchmark logging is working"""
        start_time = time.perf_counter()
        self.pipeline.execute_pipeline()
        end_time = time.perf_counter()

        BenchmarkLogger.log_query_execution("test_pipeline", start_time, end_time)
        with open("logs/mcp_benchmark.log", "r") as log_file:
            logs = log_file.read()

        self.assertIn("test_pipeline", logs, "benchmark logging not functioning")

if __name__ == "__main__":
    unittest.main()
