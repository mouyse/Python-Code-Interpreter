from Scripts.pywin32_postinstall import verbose
from dotenv import load_dotenv
from langchain import hub
from langchain_experimental.agents import create_csv_agent
from langchain_experimental.tools import PythonREPLTool
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain.agents import Tool
from langchain_experimental.utilities import PythonREPL

load_dotenv()


def main():
    print("Start")

    instructions = """You are an agent designed to write and execute python code to answer questions.
    You have access to a python REPL, which you can use to execute python code.
    If you get an error, debug your code and try again.
    Only use the output of your code to answer the question.
    You might know the answer without running any code, but you should still run the code to get the answer.
    If it does not seem like you can write code to answer the question, just return "I don't know" as the answer.
    """

    base_prompt = hub.pull("langchain-ai/react-agent-template")
    prompt = base_prompt.partial(instructions=instructions)

    tools = [PythonREPLTool()]

    python_agent = create_react_agent(
        llm = ChatOpenAI(temperature=0, model="gpt-4-turbo"),
        tools = tools,
        prompt=prompt
    )

    python_agent_executor = AgentExecutor(agent=python_agent, tools=tools, verbose=True)
    # python_agent_executor.invoke(input = {
    #     "input": """Generate 15 QR Codes that points to my LinkedIn profile https://linkedin.com/in/mouyse/ and save all 15 QR Code images in the new directory "LinkedIn_QRCodes" within the current working directory. You already have a QR Code package installed."""
    # })

    def python_agent_executor_wrapper(original_prompt: str) -> str:
        return python_agent_executor.invoke({"input": original_prompt})

    csv_agent_executor: AgentExecutor = create_csv_agent(
        llm=ChatOpenAI(temperature=0, model="gpt-4-turbo"),
        path="friends_complete_episodes_database.csv",
        verbose=True,
        allow_dangerous_code=True
    )
    # csv_agent_executor.invoke(
    #     input = {"input": "How many guests have made how many times appearances across all the seasons?"}
    # )

    tools = [
        Tool(
            name="Python Agent",
            func=python_agent_executor_wrapper,
            description="""useful when you need to transform natural language to python and execute the python code, 
                            returning the results of the code execution
                            Does not accept code as an input""",
        ),
        Tool(
            name="CSV Agent",
            func=csv_agent_executor.invoke,
            description="""Useful when you want to perform any sort of data analysis on a friends_complete_episodes_database.csv file. The program takes a question as an input and performs the analysis through pandas and returns the precise result. """
        )
    ]

    prompt = base_prompt.partial(instructions="")
    grand_agent = create_react_agent(
        prompt=prompt,
        llm=ChatOpenAI(temperature=0, model="gpt-4-turbo"),
        tools=tools,
    )
    grand_agent_executor = AgentExecutor(agent = grand_agent, tools=tools, verbose=True)
    grand_agent_executor.invoke(
        input = {"input": "How many guests have made how many times appearances across all the seasons?"}
    )
    grand_agent_executor.invoke(
        input = {"input": "HowGenerate 15 QR Codes that points to my LinkedIn profile https://linkedin.com/in/mouyse/ and save all 15 QR Code images in the new directory 'LinkedIn_QRCodes' within the current working directory. You already have a QR Code package installed."}
    )



if __name__ == "__main__":
    main()