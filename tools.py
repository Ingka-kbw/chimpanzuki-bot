import os
from datetime import datetime
from dotenv import load_dotenv
from langchain_core.tools import BaseTool
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.document_loaders.parsers import TesseractBlobParser
from tavily import TavilyClient
from typing import List

#  Load environment variables from .env file
load_dotenv()

# Tool to get current date and time information
class DateTimeTool(BaseTool):
    """Tool to get current date and time information"""
    name: str = "get_datetime"
    description: str = "Get current date and time information. Use this when you need to know the current date, time, or calculate relative dates."
    
    def _run(self, query: str = "") -> str:
        """Get current datetime information"""
        now = datetime.now()
        
        info = {
            "current_date": now.strftime("%Y-%m-%d"),
            "current_time": now.strftime("%H:%M:%S"),
            "current_datetime": now.strftime("%Y-%m-%d %H:%M:%S"),
            "day_of_week": now.strftime("%A"),
            "month": now.strftime("%B"),
            "year": now.year
        }
        
        return f"Current datetime information:\n" + "\n".join([f"- {k}: {v}" for k, v in info.items()])

# Tool to search the web using Tavily
class TavilySearchTool(BaseTool):
    """Tool to search the web using Tavily"""
    name: str = "search_web"
    description: str = "Search the web for current general information. Use this for recent news or any topic that requires up-to-date information."

    def _run(self, query: str) -> str:
        """Search the web and return human-readable results"""
        try:
            tvly_YOUR_API_KEY = os.getenv("TAVILY_API_KEY")
            tavily_client = TavilyClient(api_key=tvly_YOUR_API_KEY)
            response = tavily_client.search(query=query, max_results=5)
            
            allResults = ""
            rawResults = response['results']
            for result in rawResults:
                string = f"Title: {result['title']}\nContent: {result['content']}\nURL: {result['url']}\n\n"
                allResults += string
            
            if not rawResults:
                return "No search results found for your query."
            
            return allResults
            
        except Exception as e:
            return f"Error searching the web: {str(e)}"

# Tool to open and read PDF files
class OpenPDFTool(BaseTool):
    """Tool to handle PDF files"""
    name: str = "open_pdf"
    description: str = "Open and read PDF files. Use this when you need to extract text, image, and table or summarize content from a PDF document. Pass in a file path."

    def _run(self, filePath: str) -> str:
        """Read and summarize PDF content"""
        try:
            loader = PyMuPDFLoader(filePath, mode="single",
                                   extract_tables="markdown", 
                                   images_inner_format="markdown-img",
                                   images_parser=TesseractBlobParser())
            doc = loader.load()
            content = ""
            for text in doc[0].page_content:
                content += text
            
            if not text.strip():
                return "The PDF is empty or contains no readable text 🧐."
            
            # Return only 2000 characters to avoid overload
            return f"Extracted text from {filePath}:\n{content[:2000]}" 
        except Exception as e:
            return f"Error reading PDF: {str(e)}"
        
# Tool to open and read txt files
class OpenTxtTool(BaseTool):
    """Tool to handle txt files"""
    name: str = "open_txt"
    description: str = "Open and read txt files. Use this when you need to extract text or summarize content from a txt file. Pass in a file path."

    def _run(self, filePath: str) -> str:
        """Read and summarize txt content"""
        try:
            content = ""
            with open(filePath, 'r') as txt:
                for text in txt:
                    content += text

            if not content.strip():
                return "This txt file is empty or contains no readable text 🧐."
            
            # Return only 2000 characters to avoid overload
            return f"Extracted text from {filePath}:\n{content[:2000]}"
        except Exception as e:
            return f"Error reading txt: {str(e)}"


# Tool to generate txt files from text content
class TxtGenerationTool(BaseTool):
    """Tool to generate txt files from text content"""
    name: str = "generate_txt"
    description: str = "Generate a txt file from the provided text content. Use this to create a simple text file with the given content like essay, article, story, etc."

    def _run(self, content: str, file_name: str = "output.txt") -> str:
        """Generate a txt file from the provided content"""
        try:
            with open(file_name, 'w') as txt:
                txt.write(content)
            return f"Text file '{file_name}' generated successfully."
        except Exception as e:
            return f"Error generating txt file: {str(e)}"

# Create instances of all tools
def getTools() -> List[BaseTool]:
    """Return a list of all available tools"""
    return [
        DateTimeTool(),
        TavilySearchTool(),
        OpenPDFTool(),
        OpenTxtTool(),
        TxtGenerationTool()
    ]

# Count for tools in getTools()
def countTools():
    """Return a number of available tools. If not count corrected, will return 0"""
    countByHuman = int(5)
    num = len(getTools())

    if num == countByHuman:
        return int(num)
    else:
        return int(0)