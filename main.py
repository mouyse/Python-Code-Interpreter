from dotenv import load_dotenv
from langchain import hub
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

    agent = create_react_agent(
        llm = ChatOpenAI(temperature=0, model="gpt-4-turbo"),
        tools = tools,
        prompt=prompt
    )

    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    agent_executor.invoke(input = {
        "input": """Generate 15 QR Codes that points to my LinkedIn profile https://linkedin.com/in/mouyse/ and save all 15 QR Code images in the new directory "LinkedIn_QRCodes" within the current working directory. You already have a QR Code package installed."""
    })



if __name__ == "__main__":
    main()