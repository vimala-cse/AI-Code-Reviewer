import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate


load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

model = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=groq_api_key
)

prompt_template = PromptTemplate(
    input_variables=["code_string"],
    template="""
You are an experienced coding teacher.

Analyze the following Python code and provide feedback in plain text only.
No markdown, no hashtags (#), no asterisks (*), no code blocks.

Your response must have exactly these sections:

ANALYSIS:
1. Errors (if any)
2. Improvements (max 3 points)
3. Time Complexity
4. Space Complexity
5. PEP8 issues (if any)

CORRECTED_CODE:
Write only the corrected version of the code here. No explanation.

Code:
{code_string}

Remember: Plain text only. No special formatting. Be concise.
"""
)


def get_ai_suggestion(code_string):

    formatted_prompt = prompt_template.format(code_string=code_string)

    result = model.invoke(formatted_prompt)

    return result