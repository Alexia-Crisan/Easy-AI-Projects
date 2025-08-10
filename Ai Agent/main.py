from langchain_core.messages import HumanMessage # high level framework that allows AI integration in apps  
from langchain_openai import ChatOpenAI #allows the usage of openAi within langchain and langgraph
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent # high level framework that allows to build AI agent
from dotenv import load_dotenv

load_dotenv() #loads stuff from .env

def main():
    model = ChatOpenAI(temperature = 0) #the higher the temperature, the more randomness

    tools = []
    agent = create_react_agent(model, tools)

    print("Welcome! I'm your AI assistent. Type 'quit to exit.'")
    print("You can ask me to perform calculations or chat with me.'")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input == "quit":
            break

        print("\nAI Assistant ", end = "")

        for chunk in agent.stream({"messages" : [HumanMessage(content = user_input)]}):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end = "")

if __name__ == "__main__":
    main()