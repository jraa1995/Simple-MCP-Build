import logging
from collections import defaultdict

logging.basicConfig(level=logging.INFO)

class ContextManager: 
    """stores execution context memory across function calls"""
    
    def __init__(self):
        self.context = defaultdict(dict)
        
    def store(self, key, value):
        """stores results in context memory"""
        self.context[key] = value
        logging.info(f"stored {key} in context.")
        
    def retrieve(self, key):
        """retrieves stored values from context memory"""
        return self.context.get(key, None)
    
    def clear(self):
        """clears context memory"""
        self.context.clear()
        logging.info("context cleared")
        
context_manager = ContextManager()