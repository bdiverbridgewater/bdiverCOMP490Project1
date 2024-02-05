import json
from serpapi.google_search import GoogleSearch
import secrets
import sqlite3
from typing import Tuple


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


def open_database(file_name: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    database_connection = sqlite3.connect(file_name)
    cursor = database_connection.cursor()
    return database_connection, cursor


def setup_database(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS jobs(
        search_result INTEGER PRIMARY KEY,
        job_title TEXT NOT NULL,
        company_name TEXT NOT NULL,
        location TEXT NOT NULL,
        is_remote BOOLEAN,
        description TEXT,
        date_posted TEXT,
        salary TEXT,
        related_link TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS qualifications(
    FOREIGN KEY (search_result) REFERENCES jobs(search_result))''')


def close_database(connection: sqlite3.Connection):
    connection.commit()
    connection.close()


def main():
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


if __name__ == "__main__":
    main()
