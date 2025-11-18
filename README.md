# 🧙‍♂️ RajBot — The Yoda-Style AI Mentor  
A mystical chatbot built with **Gradio**, **LangChain**, and **Gemini 2.5 Flash**.  
Rajbot speaks like **Yoda from Star Wars**, using inverted syntax, cryptic wisdom, and calm Jedi‑master tone.  
He never breaks character — guiding you with philosophical insights.

---

## 🚀 Features

- 🧠 Powered by **Gemini 2.5 Flash LLM**  
- 🌀 Enforced Yoda‑style inverted speech  
- 💬 Clean and interactive **Gradio chat UI**  
- 🔄 Persistent chat history  
- 🎨 Custom avatars for User and Raj  
- 🌗 Soft Gradio theme  
- 🔐 Secure API handling with `.env`  

---

## 🗂️ Project Structure

```
Rajbot/
│
├── main.py                 # Main application
├── user.png                # User avatar
├── Raj.jpeg                # Rajbot avatar
├── .env                    # API keys (ignored in version control)
├── requirements.txt        # Python dependencies
└── README.md               # Documentation
```

---

## 🔐 Environment Setup

Create a `.env` file with:

```env
GEMINI_API_KEY = your_API_goes_here
```

---

## 📦 Installation

```bash
pip install gradio langchain langchain-core langchain-google-genai python-dotenv google-generativeai
```

---

## ▶️ Running the App

```bash
python main.py
```

Then open:

```
http://localhost:7860
```

---

## 🧠 Example Interaction

```
You: Teach me discipline.
Rajbot: Discipline… master it you must. Strength, it brings.
```

---

## 🧩 Possible Enhancements

- 🎤 Add voice mode  
- 🌐 Deploy to HuggingFace Spaces  
- 🧘 Add multiple Jedi/Sith personas  
- 💾 Save chat logs  
- 🎨 Add Dark Mode  

---


## 🪪 License

MIT License  
