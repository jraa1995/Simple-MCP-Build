import logging
#will import from models once we have models built 
# from models.model import {model}

logging.basicConfig(level=logging.INFO)

class QueryManager:
    """dynamically routes queries to appropriate functions"""
    
    function_map = {
        #model1:
        #model2:
        #examples
    }

    @staticmethod
    def route_query(query_type, dataset, params):
        """this will route queries to the correct functions"""
        if query_type in QueryManager.function_map:
            function = QueryManager.function_map[query_type]
            return function(dataset, **params)
        logging.error(f"unknown query type: {query_type}")
        return None