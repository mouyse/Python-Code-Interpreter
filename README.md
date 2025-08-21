# Python Code Interpreter Project

This project is a simple Python-based code interpreter built using
**LangChain**, **OpenAI**, and **Python REPL Tool**.\
The interpreter is designed to generate and execute Python code
dynamically to answer queries.

## Features

-   Uses LangChain's `react-agent-template` for reasoning and action.
-   Provides a Python REPL tool to execute generated Python code.
-   Handles debugging automatically by retrying execution when errors
    occur.
-   Can generate QR codes, perform calculations, and execute Python
    scripts as per the user prompt.

## How It Works

1.  The agent receives instructions to always try solving tasks using
    Python code execution.
2.  It runs the generated Python code inside a REPL environment.
3.  The results of execution are returned as the final output.

## Example Task

For example, in the current `main.py`, the agent is asked to: \>
Generate 15 QR Codes pointing to a LinkedIn profile and save them inside
a `LinkedIn_QRCodes` directory.

The agent will: - Write Python code to generate QR codes. - Save them
inside the specified directory. - Return confirmation of execution.

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

## Usage

Run the project using:

``` bash
python main.py
```

You can modify the prompt inside `main.py` to run different Python
tasks.

## Next Steps

The next enhancement will be building a **CSV Agent** that can: - Load
CSV files. - Query and analyze data using natural language. - Return
results directly from the dataset.

------------------------------------------------------------------------

### Tech Stack

-   Python 3.9+
-   LangChain
-   OpenAI GPT-4 Turbo
-   dotenv

------------------------------------------------------------------------

### License

This project is licensed under the MIT License.
