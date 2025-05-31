from langchain_community.tools.tavily_search import TavilySearchResults

def get_profile_url_tavily(name: str):
    """
    Search for a profile URL using Tavily's search results. """
    
    search = TavilySearchResults()
    res = search.run(f"{name} 프로필")
    