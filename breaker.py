from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv  # Add this import

# Load environment variables from .env file
load_dotenv()  # This line is crucial!

information = "Alice is a software engineer with a passion for open-source projects. She has contributed to several high-profile repositories and enjoys mentoring junior developers. In her free time, Alice loves hiking and photography, often combining the two by capturing nature's beauty through her lens."

if __name__ == "__main__":
    print("Testing")
    summary_template = """
    Given the information {information} about a person from I want you to create:
    1. a short summary of the person 
    2. two interesting facts about the person

    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
    )

    print("API Key:", os.getenv("OPENAI_API_KEY"))  # Debug line

    lllm = ChatOpenAI(
        temperature=0.5,
        model="gpt-4o",
    )

chain = (
    summary_prompt_template | lllm
)  # pipe operation, takes the value from the prompt template and passes it to the LLM like an api call

res = chain.invoke(input={"information": information})
