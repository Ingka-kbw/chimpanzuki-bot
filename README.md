# 🐵🤺 Chimpanzuki the Ninja Scribe — CS50P Final Project
#### Video Demo:  <URL HERE>

#### Description:
> 🧠 What is Chimpanzuki?
Chimpanzuki is a ninja-themed AI chatbot agent built entirely in Python, designed for CS50P's final project. I got inspired by the idea of combining AI tools with personality, Chimpanzuki (also inspired by Chimpanzini Bananini) behaves like a cheeky, clever ninja monkey who helps users with various tasks in the terminal while cracking jokes and speaking like a dojo-trained assistant 🐵🥷🍌.

This terminal-based Python chatbot uses **LangChain + Gemini 2.0 Flash + custom tools** to:
- Chat with you like a funny ninja AI
- Summarize and extract content from **PDF** and **TXT** files
- Search the web using **Tavily**
- Tell the current date/time
- Generate `.txt` documents from your input
- Use only **free** API key; Google Gemini, Tavily

It runs entirely in a `.py` file which simple, modular, and interactive. It perfect for terminal use and easy to extend in the future.

Chimpanzuki is designed to be fun, helpful, and extensible. You can easily add new tools, replace the LLM, or upgrade it into a web app in the future.

## 📁 Project Structure

```bash
project/
│
├── main.py             # Main app loop and agent executor
├── tools.py            # Custom tools for search, file handling, etc.
├── .env                # Secret API keys (Tavily key and Google API key required)
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## 🧐 How to Use

### 1. 📦 Install the Required Libraries
First, make sure you have Python 3 installed.
Then, navigate to the project folder and run:

```bash
pip install -r requirements.txt
```

### 2. 🔐 Set Up Your API Keys
Create a `.env` file in the root directory of your project and add the following:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
```
These are required for the AI model (Gemini) and web search tool (Tavily).

### 3. 🏃 Run the AI Agent
Run the chatbot from the terminal with:

```bash
python project.py
```
You’ll see a fun ASCII welcome banner from Chimpanzuki, the Ninja Scribe 🐵🤺


### 4. 💬 Interact with the Bot
Once started, you can type in natural language commands like:

- `What day is it today?`
- `Search the web for AI in education`
- `Summarize this PDF: path/to/your/file.pdf or your_file_name.pdf`
- `Generate a text file with this poem: Roses are red...`

Chimpanzuki will respond with flair, often with ninja puns, jokes, or wise quotes. He's also getting the job done.

### 5. 🚪 Exit the Chat

To leave the chat at any time, simply type:

```
exit
```

Chimpanzuki will bid you farewell with a dramatic ninja outro 🥷✨

## 🗒️ Final Notes

This is a final project submission for CS50P.
Thanks for trying out **Chimpanzuki the Ninja Scribe 🐵🤺**!
