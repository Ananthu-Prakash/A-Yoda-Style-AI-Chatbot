from dotenv import load_dotenv
import os
import gradio as gr
from gradio.themes import Soft
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

print("✨ Rajbot I am. Guide you, I shall.✨")

def chat(user_input, hist):

    langchain_history = []
    for item in hist:
        if item['role']== "user":
            langchain_history.append(HumanMessage(content= item['content']))
        elif item['role'] == "assistant":
            langchain_history.append(AIMessage(content= item['content']))

    response = chain.invoke({
        "input": user_input,
        "history": langchain_history
    })   
    
    return "",hist + [{'role':'user', 'content':user_input},
                  {'role':'assistant', 'content':response}]

def clear_chat():
    return "",[]

page = gr.Blocks(
    title="Chat with Raj",
    theme= Soft()
    )

with page:
    gr.Markdown(
        """
        ## **Chat with Raj, yes. Talk we shall, hmmm**
        """
    )

    chatbot = gr.Chatbot(type= "messages", 
                         avatar_images=['user.png','Raj.jpeg'])

    msg = gr.Textbox(show_label= False, placeholder=" Ask, Young Padwan...")
    
    msg.submit(chat, [msg, chatbot], [msg, chatbot])

    clear = gr.Button("Clear Chat")
    clear.click(clear_chat, outputs=[msg, chatbot])

page.launch()