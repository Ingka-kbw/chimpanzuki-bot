import pyfiglet
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import create_react_agent
from tools import countTools, getTools


# Load environment variables from a .env file
load_dotenv()

# Define memory for model checkpointing
memory = InMemorySaver()

# Model initialization
myModel = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

# Tool for LLM
myTools = getTools()

# For check if tools loads to main correctly
def checkTools(tools):
     if len(tools) == countTools():
          return True
     else: return False

myAgentExecutor = create_react_agent(
    model=myModel,
    tools=myTools,
    checkpointer=memory,
    prompt=ChatPromptTemplate.from_messages(
        [
            (
                "system",
               "You are **Chimpanzuki the Ninja Scribe 🐵🤺** a hyper-intelligent, banana-fueled ninja chimp who masters the arts of knowledge, translation, summarization, and PDF generation."
                
                "Here’s how you behave:"
                "- You are cheeky, cool, cold blood, and incredibly funny. Like if ChatGPT had too many bananas and trained with ancient scrolls in a bamboo dojo."
                "- You crack light jokes 🍌, sprinkle in some ninja references 🥷, and make the user smile while being very smart and chaotic as possible."
                "- You can translate between any languages with precision (and sometimes with a banana pun)."
                "- If the user uploads a PDF, you read it with your keen ninja vision and can summarize it like a scroll master."
                "- If the user wants to write an essay, story, or article, you help structure it and offer funny or clever suggestions (but stay on task)."
                "- If the user asks for a final result, you can package everything neatly into a txt file 📄. "
                "- You NEVER make stuff up. If you don’t have info or can’t access something, you politely say so (perhaps with a dramatic ninja gasp)."
                "- You are fast, fun, hilarious, and fabulous but always focused. 🎯"

                "Never speak in a boring, robotic way. Add flair, ninja wisdom, and a splash of banana-powered humor but always complete the user’s task thoroughly and professionally."
            ),
            MessagesPlaceholder(variable_name="messages")
        ]
        )    
    )

# Configuration for the application
config = {"configurable": {"thread_id": "abc123"}}

# Bot name in a stylized font
def titleFont():
    title = pyfiglet.figlet_format("Chimpanzuki\n the Ninja Scribe", font = "doom")
    return title

def main():
    print(titleFont())
    
    if checkTools(myTools):
         print(f"Tools loaded: {countTools()} tools")
         print(f"Tool types: {[type(tool).__name__ for tool in myTools]}\n")
         for tool in myTools:
              print(f"{type(tool).__name__}: {tool.description}\n")
    else:
         raise Exception("Error on loading tools")

    print("Welcome to Chimpanzuki the Ninja Scribe 🐵🤺 (type 'exit' to quit)\n")
    print("=================================== Conversation begin 🐵🤺 ===================================")
    while True:
        userInput = input("\nyou: ")

        if userInput.strip().lower() == "exit":
                print("\n========================================= Chat end 👋 =========================================")
                print("\nMay wisdom be with you 🐵✨")
                break
        
        try:
            response = myAgentExecutor.invoke({"messages": [HumanMessage(content=userInput)]}, config)
            print(f"\nChimpanzuki 🐵🤺 : {response.get('messages', [])[-1].content}\n")

        except Exception as e:
            print(f"Error occured 😟 : {str(e)}")
            break

if __name__ == "__main__":
    main()