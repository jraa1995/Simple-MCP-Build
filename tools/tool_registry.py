import logging

class ToolRegistry: 
    """ 
    a registry for managing tools that our MCP can use
    """
    
    def __init__(self):
        # dictionary storing available tools and their descriptions
        self.tools = {
            "temperature_trends": {
                "description": "analyzes historical temperature trends",
                "module": "models.temperature_trends",
                "function": "get_temperature_trends",
            },
            "scenario_projection": {
                "description": "projects future climate scenarios",
                "module": "models.scenario_projection",
                "function": "project_climate_scenario",
            },
            "temperature_model_test": {
                "description": "runs a temperature model test",
                "module": "models.temperature_model_test",
                "function": "run_test",
            },
            "project_scenario": {
                "description": "projects climate scenarios",
                "module": "models.project_scenario",
                "function": "run_scenario",
            },
            "fetch_external_api": {
                "description": "fetches climate data from external APIs (e.g., NASA, NOAA)",
                "module": "tools.tool_handler",
                "function": "fetch_from_api",
            }
        }
    
    def list_tools(self):
        """returns a dictionary of available tools"""
        return {key: value["description"] for key, value in self.tools.items()}

    def get_tool(self, tool_name):
        """returns the details of a tool if available, else None"""
        return self.tools.get(tool_name, None)