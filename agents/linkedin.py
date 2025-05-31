import os
import requests
from dotenv import load_dotenv

load_dotenv()

def lookup_linkedin_profile(profile_url: str) -> dict:
    return "https://www.linkedin.com/in/eden-marco"

# new*
def scrape_linkedin_profile(lonkedin_profile_url: str, mock: bool = False):
    """
    Scrape LinkedIn profile information from a given URL.
    
    Args:
        lonkedin_profile_url (str): The URL of the LinkedIn profile to scrape.
        mock (bool): If True, return mock data instead of scraping.
    
    Returns:
        dict: A dictionary containing the scraped profile information.
    """
    if mock:
        return {
            "name": "John Doe",
            "headline": "Software Engineer at Example Corp",
            "location": "San Francisco, CA",
            "summary": "Experienced software engineer with a passion for building scalable applications.",
            "skills": ["Python", "JavaScript", "React"],
            "experience": [
                {
                    "title": "Software Engineer",
                    "company": "Example Corp",
                    "duration": "2 years"
                }
            ],
            "education": [
                {
                    "degree": "Bachelor of Science in Computer Science",
                    "school": "Example University"
                }
            ]
        }
    
    # Actual scraping logic would go here
    # For now, we will just return an empty dictionary
    return {}