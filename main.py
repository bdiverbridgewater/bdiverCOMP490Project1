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
    return results


def get_job_data(search_result_number, data):
    job = data["jobs_results"][search_result_number % 10]
    job_title = job.get("title")
    company_name = job.get("company_name")
    location = job.get("location")
    description = job.get("description")
    related_link = job["related_links"][0].get("link")
    job_data = [search_result_number, job_title, company_name, location, description, related_link]
    return job_data


def open_database(file_name: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    database_connection = sqlite3.connect(file_name)
    cursor = database_connection.cursor()
    return database_connection, cursor


def setup_database(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS jobs(
        search_result INTEGER PRIMARY KEY,
        job_title TEXT,
        company_name TEXT,
        location TEXT,
        description TEXT,
        related_link TEXT);''')


def close_database(connection: sqlite3.Connection):
    connection.commit()
    connection.close()


def main():
    connection, cursor = open_database("job_search.sqlite")
    setup_database(cursor)
    job_number = 0
    search_results = None
    while job_number < 50:
        if job_number % 10 == 0:
            search_results = job_search(job_number)
        values = get_job_data(job_number, search_results)
        cursor.executemany('''INSERT INTO jobs VALUES(?, ?, ?, ?, ?, ?);''', (values,))
        job_number += 1
    close_database(connection)


if __name__ == "__main__":
    main()
