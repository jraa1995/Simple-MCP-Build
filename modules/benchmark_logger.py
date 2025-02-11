import logging
import time
import functools
import numpy as np
import os
from sklearn.metrics import mean_squared_error, r2_score

if not os.path.exists("logs"):
    os.makedirs("logs")

log_file_path = "logs/mcp_benchmark.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file_path, mode="a", encoding="utf-8"),  
        logging.StreamHandler()
    ]
)

logging.getLogger().setLevel(logging.INFO)

class BenchmarkLogger:
    """logs execution benchmarks for MCP processes"""

    @staticmethod
    def log_query_execution(query_type, start_time, end_time, success=True):
        """Logs execution time and success rate for each query"""
        execution_time = end_time - start_time
        status = "SUCCESS" if success else "FAILED"
        log_message = f"QUERY: '{query_type}' executed in {execution_time:.4f} sec - {status}"
        
        logging.info(log_message)
        for handler in logging.getLogger().handlers:
            handler.flush()

    @staticmethod
    def log_model_performance(model_name, actual, predicted):
        """logs model performance metrics"""
        rmse = np.sqrt(mean_squared_error(actual, predicted))
        r2 = r2_score(actual, predicted)
        log_message = f"MODEL: '{model_name}' RMSE: {rmse:.4f}, R2: {r2:.4f}"
        
        logging.info(log_message)
        for handler in logging.getLogger().handlers:
            handler.flush()

    @staticmethod
    def benchmark_function(func):
        """decorator to benchmark function execution time"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
                success = True
            except Exception as e:
                logging.error(f"Error executing function {func.__name__}: {e}")
                success = False
                result = None
            end_time = time.time()
            BenchmarkLogger.log_query_execution(func.__name__, start_time, end_time, success)
            return result
        return wrapper