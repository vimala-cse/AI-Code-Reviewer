import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate


# Load environment variables from .env file
load_dotenv()

# Get GROQ API key
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize the AI model
model = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=groq_api_key
)

# Create prompt template
prompt_template = PromptTemplate(
    input_variables=["code_string"],
    template="""
You are an experienced coding teacher.

Analyze the following Python code and provide:

1. Errors in the code (if any)
2. Suggestions for improvement
3. Explanation of why the suggestion is needed
4. Time complexity
5. Space complexity

Code:
{code_string}
"""
)


# Function to get AI suggestions
def get_ai_suggestion(code_string):

    # Insert code into prompt
    formatted_prompt = prompt_template.format(code_string=code_string)

    # Send prompt to AI model
    result = model.invoke(formatted_prompt)

    # Print AI response
    print("\n--- AI Technical Review ---\n")
    print(result.content)



# Testing Block


# if __name__ == "__main__":

#     sample_code = """
# number = 10


# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
# """

#     get_ai_suggestion(sample_code)