from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from third_parties.scrap_prof import get_profile
import json 



# my fake profile: lnkn_profile = get_profile("https://gist.githubusercontent.com/OweenCesar/ff97866065f2bb2d1ddef856316df742/raw/5fffb0ebb313c4e75c933237c73924f1ff37d412/json")


# Professor profile:

lnkn_profile = get_profile("https://www.linkedin.com/in/amonhanshaw/", paid_service=False)
 

profile_text = json.dumps(lnkn_profile, indent=2)

llm = Ollama(model="stablelm-zephyr", temperature=0.8)


template = PromptTemplate.from_template("Q: {question}\nA:")

chain = template | llm


user_input = f"""
Summarize the following LinkedIn profile as a third-person biography. 
Do not mention JSON, do not address the reader as "you," and avoid using second-person pronouns.
Profile data:
{profile_text}
"""


response = chain.invoke({"question": user_input})
print(response)
