# Model Context Protocal (MCP) Implementation
This repository includes the **Model Context Protocol (MCP)** framework that ClimateGPT Team 1 is developing. 

### 📂 **Project Structure**
/mcp-framework
    ├── modules/                      # Core MCP components
    │   ├── context_manager.py        # Stores execution context memory
    │   ├── data_loader.py            # Handles dataset loading
    │   ├── query_manager.py          # Routes queries dynamically
    │   ├── pipeline_manager.py       # Executes MCP steps
    ├── models/                       # Test EDA / initial models for MCP framework checking
    │   ├── scenario_projection.py    # Temp trend analysis
    │   ├── temperature_trends.py     # Climate scenario projections
    │   ├── Model3.py                 # Model 3
    ├── config/                       # Configuration settings
    │   ├── config.yaml               # Defines dataset paths and pipeline steps
    ├── logs/                         # Execution logs
    │   ├── mcp_execution.log
    ├── tests/                        # Unit tests for MCP validation
    ├── main.py                       # Entry point for MCP execution
    ├── requirements.txt              # Python dependencies
    ├── README.md                     # Project documentation

### **How to run MCP Framework**
1. **Clone the repository** (if not already cloned):
    ```sh
    git clone https://github.com/ newsconsole/GMU_DAEN_2025_01_A.git
    ```

2. **Switch to the ClimateGPT Team 1 Branch**:
    ```sh 
    git checkout ClimateGPT_Team1
    ```

3. **Make sure to set up venv (Virtual Env)**
    ```sh
    1. python -m venv venv
    2. venv\Scripts\Activate
    ```
4. **Install dependencies (requirements.txt)**:
    ```sh
    pip install -r requirements.txt
    ```

5. **Run the MCP Pipeline**
    ```sh
    python main.py 
    ```

### **Configuration & Execution**
- The **MCP pipeline** is dynamically controlled by `config/config.yaml` which defines the datasets and pipeline steps
- Logs are stored in `logs/mcp_execution.log` for debugging and tracking execution results

### **Recent Updates**
- **Implemented initial MCP Framework with modular design**
- **Added dynamiic query routing & context memory**
