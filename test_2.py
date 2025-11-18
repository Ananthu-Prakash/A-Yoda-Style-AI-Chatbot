from dotenv import load_dotenv
import os
import datetime
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

system_prompt = """
You are Yoda AKA Rajbot from Star Wars. Always speak in Yoda-style inverted syntax, 
wise and calm. Provide mystical, philosophical guidance. Use short, cryptic sentences. 
Never break character or speak normally. Respond like a Jedi master.
"""

gemini_key = os.getenv("GEMINI_API_KEY")

llm=ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    google_api_key = gemini_key,
    temperature = 0.5
    )

prompt = ChatPromptTemplate.from_messages([
    ("system",system_prompt),
    MessagesPlaceholder("history"),
    ("user", "{input}")
])

chain= prompt | llm | StrOutputParser()

from datetime import datetime
# from zoneinfo import ZoneInfo

print("✨ Rajbot I am. Guide you, I shall.✨")

history = []
while True:
    user_input = input("You:" )
    if user_input in ("Exit", "exit"):
        print("Farewell Young one! 👋")
        break

    response = chain.invoke({
        "input": user_input,
        "history": history
    })   
    print("RajBot: ", response + "\n")
    history.append(HumanMessage(content= user_input))
    history.append(AIMessage(content= response))