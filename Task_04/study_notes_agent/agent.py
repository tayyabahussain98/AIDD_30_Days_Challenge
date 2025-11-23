import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled
from tools import extract_text_from_pdf

load_dotenv()
set_tracing_disabled(True)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")

client = AsyncOpenAI(
    api_key = GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=client
)

study_agent = Agent(
    name="Study Assistant",
    instructions=(
        "A helpful assistant that can summarize study notes and generate quizzes from them. It can extract text from PDF files."
        "You are a helpful assistant for students. Your goal is to summarize study notes and create quizzes based on them. "
        "When given a path to a PDF file, first use the 'extract_text_from_pdf' tool to read its content. "
        "After extracting the text, you can either summarize it or generate a quiz as requested by the user."
    ),
    tools=[extract_text_from_pdf],
    model=model
)

# We export the agent and the Runner class, so app.py can use them.
__all__ = ["study_agent", "Runner"]