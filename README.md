# Python Code Interpreter & CSV Agent Project

This project is a **multi-agent system** built with **LangChain**,
**OpenAI GPT-4 Turbo**, and experimental utilities.\
It includes two powerful agents: 1. **Python Code Agent** -- Executes
Python code dynamically using a REPL. 2. **CSV Agent** -- Analyzes data
from a CSV file using Pandas with natural language queries.

Both agents are combined into a **Grand Agent**, which decides which
tool to use based on the input prompt.

------------------------------------------------------------------------

## Features

-   **Python Agent**
    -   Converts natural language into Python code.
    -   Executes code in a REPL environment.
    -   Handles errors by retrying execution.
    -   Example: Generate QR Codes, perform calculations, automate
        Python scripts.
-   **CSV Agent**
    -   Reads and queries CSV files.
    -   Uses Pandas for data analysis.
    -   Example: Answer questions like *"How many guests appeared how
        many times across all the seasons?"* from the
        `friends_complete_episodes_database.csv` dataset.
-   **Grand Agent**
    -   Orchestrates between Python Agent and CSV Agent.
    -   Routes user prompts to the right agent depending on the task.

------------------------------------------------------------------------

## Installation

1.  Clone the repository:

    ``` bash
    git clone https://github.com/your-username/python-code-interpreter.git
    cd python-code-interpreter
    ```

2.  Create a virtual environment and activate it:

    ``` bash
    python -m venv venv
    source venv/bin/activate   # Linux / macOS
    venv\Scripts\activate    # Windows
    ```

3.  Install dependencies:

    ``` bash
    pip install -r requirements.txt
    ```

4.  Add your **OpenAI API key** in a `.env` file:

    ``` env
    OPENAI_API_KEY=your_api_key_here
    ```

------------------------------------------------------------------------

## Usage

Run the project using:

``` bash
python main.py
```

### Example Queries

-   **CSV Agent Example**

    ``` text
    How many guests have made how many times appearances across all the seasons?
    ```

-   **Python Agent Example**

    ``` text
    Generate 15 QR Codes that point to my LinkedIn profile https://linkedin.com/in/mouyse/ and save them in the 'LinkedIn_QRCodes' directory.
    ```

-   **Grand Agent Example** The grand agent can decide whether to use
    the Python Agent or CSV Agent automatically:

    ``` text
    "How many guests have made how many times appearances across all the seasons?"
    "Generate 15 QR Codes that point to my LinkedIn profile."
    ```

------------------------------------------------------------------------

## Project Structure

    .
    ├── main.py                        # Main script containing agents
    ├── friends_complete_episodes_database.csv  # Dataset used by the CSV Agent
    ├── .env                           # API key storage
    ├── requirements.txt               
    └── README.md

------------------------------------------------------------------------

## Next Steps

-   Add support for **multiple CSV files** with dynamic selection.
-   Enhance the Python agent with plotting/visualization support.
-   Build a web-based UI to interact with both agents.

------------------------------------------------------------------------

### Tech Stack

-   Python 3.9+
-   LangChain
-   OpenAI GPT-4 Turbo
-   Pandas
-   dotenv

------------------------------------------------------------------------

### License

This project is licensed under the MIT License.
