from serpapi import google_search
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
    search = google_search.GoogleSearch(params)
    results = search.get_dict()
    return results.get("jobs_results")


def get_job_data(job_number, data):
    job = data[job_number % 10]
    job_title = job.get("title")
    company_name = job.get("company_name")
    location = job.get("location")
    description = job.get("description")
    related_link = job["related_links"][0].get("link")
    work_from_home = job["detected_extensions"].get("work_from_home")
    time_since_posting = job["detected_extensions"].get("posted_at")
    try:
        salary = job["job_highlights"][2]["items"][0]
    except IndexError:
        salary = None
    qualifications = job["job_highlights"][0]["items"]
    qualifications_string = ''
    index = 0
    for key in qualifications:
        qualifications_string = qualifications_string + qualifications[index]
        index += 1
    job_data = [job_title, company_name, location, description, related_link, work_from_home, time_since_posting,
                salary, job_number]
    return job_data, qualifications_string


def open_database(file_name: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    database_connection = sqlite3.connect(file_name)
    cursor = database_connection.cursor()
    return database_connection, cursor


def setup_database(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS jobs(
        job_title TEXT,
        company_name TEXT,
        location TEXT,
        description TEXT,
        related_link TEXT,
        work_from_home BOOL DEFAULT FALSE,
        time_since_posting TEXT,
        salary TEXT,
        id INTEGER PRIMARY KEY NOT NULL
        );''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS qualifications(
        id INTEGER NOT NULL,
        qualifications TEXT,
        FOREIGN KEY(id) REFERENCES jobs(id)
        );''')


def close_database(connection: sqlite3.Connection):
    connection.commit()
    connection.close()


def insert_job_to_database(job_number, search_results, cursor):
    values, qualifications = get_job_data(job_number, search_results)
    qualifications_data = [job_number, qualifications]
    cursor.executemany('''INSERT INTO jobs VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);''', (values,))
    cursor.executemany('''INSERT INTO qualifications VALUES(?, ?);''', (qualifications_data,))


def insert_jobs_to_database(search_pages_total, cursor):
    search_results = None
    job_number = 0
    while job_number < search_pages_total * 10:
        if job_number % 10 == 0:
            search_results = job_search(job_number)
        insert_job_to_database(job_number, search_results, cursor)
        job_number += 1


def main():
    page_total = 5
    connection, cursor = open_database("job_search.sqlite")
    setup_database(cursor)
    insert_jobs_to_database(page_total, cursor)
    close_database(connection)


if __name__ == "__main__":
    main()
