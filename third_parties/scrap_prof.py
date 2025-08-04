
import os 
import requests
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def get_profile(profile: str, paid_service: bool):
    "fetching the profiles stored on git gist if paid_service = True"
    "Otherwise, it will use the scraping api tool"


    if not profile:
        raise ValueError("Profile name cannot be empty")
    
    if paid_service == True:
         
        response = requests.get(profile, timeout=10)
        return response.json()
    
    else: 
        api_endpoint = "https://api.scrapin.io/v1/enrichment/profile"
        headers = {
            'Content-Type': 'application/json',
            'x-api-key': os.environ.get("SCRAPING_API_KEY")
        }

        payload = {
            "linkedInUrl": profile,
            "include": {}
        }

        response = requests.post(
            api_endpoint,
            json=payload,
            headers=headers,
            timeout=10
        )
        response.raise_for_status()  
        return response.json().get("person")



if __name__ == "__main__":
    profile_data = get_profile("https://www.linkedin.com/in/amonhanshaw/", paid_service=False)
    print(profile_data)