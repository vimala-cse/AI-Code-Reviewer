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

Analyze the following Python code and provide:

1. Syntax or logical errors (if any)
2. Suggestions for improvement
3. Explanation for each suggestion
4. Time complexity
5. Space complexity
6. Naming convention issues as per PEP8 guidelines:
   - Variables and functions should follow snake_case
   - Class names should follow PascalCase

Clearly explain why each naming convention issue is incorrect
and suggest the corrected version.

Code:
{code_string}
"""
)


def get_ai_suggestion(code_string):

    formatted_prompt = prompt_template.format(code_string=code_string)

    result = model.invoke(formatted_prompt)

    print("\n--- AI Technical Review ---\n")
    print(result.content)


if __name__ == "__main__":

    sample_code = """
class studentdata:
    def CalculateSum(a, b):
        resultValue = a + b
        return resultValue
"""

    get_ai_suggestion(sample_code)



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