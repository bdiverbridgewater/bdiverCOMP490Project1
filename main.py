import json
from serpapi.google_search import GoogleSearch
import secrets


def job_search(result_offset) -> dict:
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
    return results["jobs_results"]


def write_dict_to_file(dict_input: dict, write_file):
    dict_as_string = json.dumps(dict_input)
    write_file.write(dict_as_string)


if __name__ == "__main__":
    total_pages = 5
    results_per_page = 10
    current_pages = 0
    search_results_file = open('search_results.txt', 'a')
    print('Starting job search now...')
    while current_pages < total_pages:
        # There are 10 results per page, so multiplying the current pages by 10 gives the right offset to search the
        # 2nd and 3rd page etc.
        page_results = job_search(current_pages * results_per_page)
        write_dict_to_file(page_results, search_results_file)
        current_pages += 1
    search_results_file.close()
    print(f'Search Complete. Results saved to "{search_results_file.name}"')
