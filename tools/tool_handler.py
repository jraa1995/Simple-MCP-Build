import logging
import importlib
from tools.tool_registry import ToolRegistry

class ToolHandler:
    """
    handles tool execution requests dynamically based on registered tools.
    """
    
    def __init__(self):
        self.registry = ToolRegistry()
        
    def execute_tool(self, tool_name, dataset=None, **params):
        """
        execute registered tool - ex., tool_name > dataset > addtl params
        
        then return:
        str: result/s of the tool exec
        """
        tool_info = self.registry.get_tool(tool_name)
        if not tool_info:
            logging.error(f"Tool not found: {tool_name} in registry")
            return f"Error: Tool '{tool_name}' not found."
        
        module_name = tool_info["module"]
        function_name = tool_info["function"]
        
        try: 
            # dynamically import the module
            module = importlib.import_module(module_name)
            # get the function from the module
            function = getattr(module, function_name)
            # execute the function with the provided params
            return function(dataset, **params)
        
        except Exception as e:
            logging.error(f"error executing tool {tool_name}: {e}")
            return f"error executing tool '{tool_name}': {str(e)}"