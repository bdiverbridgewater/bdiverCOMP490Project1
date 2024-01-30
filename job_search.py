from serpapi import GoogleSearch
import secrets


def job_search(result_offset):
    params = {
        "api_key": secrets.api_key,
        "engine": "google_jobs",
        "google_domain": "google.com",
        "q": "Software Engineer",
        "hl": "en",
        "gl": "us",
        "location": "Boston, Massachusetts, United States",
        "start": result_offset
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    return results
