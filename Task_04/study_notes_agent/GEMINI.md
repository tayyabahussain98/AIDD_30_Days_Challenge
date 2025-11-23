# Role: Senior Python AI Engineer

**Objective:** Build a "Study Notes Summarizer & Quiz Generator Agent" using Streamlit and the `openagents` SDK.

## 1. Project Overview
The goal is to develop an intelligent web-based agent that processes uploaded PDF notes, generates summaries, and creates quizzes.
* **UI:** Streamlit (Clean, responsive web interface; HTML/CSS allowed as alternative).
* **Model:** Google Gemini model named `gemini-1.5-flash` (via OpenAgents SDK).
* **PDF Handling:** PyPDF2 for text extraction.
* **Memory/Tools:** MCP integration with Context7 for documentation access.

## 2. Critical Technical Constraints
**You must adhere to the following strict configuration rules:**

1.  **Zero-Bloat Protocol (CRITICAL):**
    * **Do NOT write extra code.** Do not add bells, whistles, advanced error handling (unless specified), or unnecessary comments.
    * **Focus strictly on the integration:** Connect the `agent` to `streamlit`. Nothing else.
    * **No "Hallucinated" Features:** If it's not in the SDK docs, do not invent it.
2.  **API Configuration:**
    * Use the **OpenAgents SDK** Python Library configured for Gemini.
    * **Base URL:** `https://generativelanguage.googleapis.com/v1beta/openai/`
    * **API Key:** Load `GEMINI_API_KEY` from environment variables.
    * **Model:** Use `OpenaiChatCompletionModel` adapted for Gemini.
3.  **SDK Specificity:** You are using `openagents` SDK. This is **NOT** the standard `openai` library. You must use the specific syntax provided by the `openagents` SDK.
4.  **Error Recovery Protocol:**
    * If you encounter a `SyntaxError`, `ImportError`, or `AttributeError` related to `openagents` during development, **STOP**.
    * Do not guess the fix. **You MUST call the `get-library-docs` tool again** to re-read the documentation and verify the correct syntax before rewriting the code.
5.  **Dependency Management:** Use `uv` for package management.

## 3. Architecture & File Structure
*Note: The current directory is the root. Do not create a subfolder named `study-notes-agent`.*

```text
.
├── .env                  # Environment variables
├── tools.py              # PDF extraction and utility functions (SDK Specific Format)
├── agent.py              # Agent configuration & tool binding
├── app.py                # Streamlit UI & Event Handlers
├── temp.pdf              # Temporary PDF storage (Auto-created if needed)
└── pyproject.toml        # UV Config