import streamlit as st  # pyright: ignore[reportMissingImports]
import os
import uuid
import asyncio
from agent import study_agent
from agent import Runner

# Ensure the temp directory exists
if not os.path.exists("temp"):
    os.makedirs("temp")

st.set_page_config(layout="wide")
st.title("📚 Study Notes Summarizer & Quiz Generator")


# -----------------------------------------
# Utility: Handle coroutine / non-coroutine
# -----------------------------------------
def run_maybe_coroutine(maybe_coro):
    if asyncio.iscoroutine(maybe_coro):
        try:
            return asyncio.run(maybe_coro)
        except RuntimeError:
            loop = asyncio.new_event_loop()
            return loop.run_until_complete(maybe_coro)
    return maybe_coro


# -----------------------------------------
# Utility: Extract text from RunResult
# -----------------------------------------
def extract_text_from_result(res):
    if res is None:
        return None

    if isinstance(res, str):
        return res

    for attr in ("output_text", "final_output", "text", "content"):
        if hasattr(res, attr):
            value = getattr(res, attr)
            if isinstance(value, str):
                return value
            return repr(value)

    if hasattr(res, "messages"):
        msgs = res.messages
        if isinstance(msgs, list) and msgs:
            msg = msgs[0]
            if hasattr(msg, "content"):
                return msg.content
            if isinstance(msg, dict) and "content" in msg:
                return msg["content"]
            return repr(msg)

    return repr(res)


# -----------------------------------------
# QUIZ Formatting Function
# -----------------------------------------
def format_quiz(text):
    if not text:
        return ""

    lines = text.split("\n")
    formatted = ""
    question_block = []

    for line in lines:
        clean = line.strip()

        # Question line
        if clean.lower().startswith(("q", "question")):
            if question_block:
                formatted += "\n".join(question_block)
                formatted += "\n" + ("-" * 60) + "\n\n"
                question_block = []
            question_block.append(clean)

        # Options
        elif any(clean.startswith(opt) for opt in ["A", "B", "C", "D"]):
            question_block.append("  " + clean)

        # Correct Answer
        elif "correct" in clean.lower():
            question_block.append("\n" + clean)

    # Add last question
    if question_block:
        formatted += "\n".join(question_block)

    return formatted


# -----------------------------------------
# File Upload
# -----------------------------------------
uploaded_file = st.file_uploader("Upload your PDF notes here", type="pdf")


if uploaded_file:

    unique_filename = f"temp_{uuid.uuid4().hex}.pdf"
    temp_pdf_path = os.path.abspath(os.path.join("temp", unique_filename))

    with open(temp_pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"PDF uploaded successfully and saved to {temp_pdf_path}")

    st.subheader("Generate Summary and Quiz")


    # --------------------------
    # SUMMARY
    # --------------------------
    if st.button("Generate Summary"):
        with st.spinner("Generating summary..."):
            try:
                prompt = f"""
Summarize the content of the PDF located at '{temp_pdf_path}'.
Write the summary in clear bullet points.
"""

                raw = Runner.run(study_agent, prompt)
                result = run_maybe_coroutine(raw)

                summary_text = extract_text_from_result(result)

                st.success("Summary Generated!")
                st.write(summary_text)

            except Exception as e:
                st.error(f"Error generating summary: {e}")


    # --------------------------
    # QUIZ
    # --------------------------
    if st.button("Generate Quiz"):
        with st.spinner("Generating quiz..."):
            try:
                prompt = f"""
Generate a 5-question multiple-choice quiz from the PDF located at '{temp_pdf_path}'.

IMPORTANT: Follow this EXACT structure:
    
Q1: Question text here

A) Option A
B) Option B
C) Option C
D) Option D

Correct Answer: B

Q2: Question text here

A) Option A
B) Option B
C) Option C
D) Option D

Correct Answer: C

Q3: Question text here

A) Option A
B) Option B
C) Option C
D) Option D

Correct Answer: A

Q4: Question text here

A) Option A
B) Option B
C) Option C
D) Option D

Correct Answer: C

Q5: Question text here

A) Option A
B) Option B
C) Option C
D) Option D

Correct Answer: B

RULES:
- ALWAYS include question lines (Q1, Q2, Q3)
- ALWAYS include four options A–D
- ALWAYS include “Correct Answer: X”
- DO NOT combine question + options in one line
- DO NOT skip questions
"""

                raw = Runner.run(study_agent, prompt)
                result = run_maybe_coroutine(raw)

                quiz_text = extract_text_from_result(result)
                pretty_quiz = format_quiz(quiz_text)

                st.success("Quiz Generated!")
                st.text(pretty_quiz)

            except Exception as e:
                st.error(f"Error generating quiz: {e}")


    # Delete temp PDF
    if os.path.exists(temp_pdf_path):
        try:
            os.remove(temp_pdf_path)
        except:
            pass
