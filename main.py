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


def get_jobs_data(jobs):
    jobs_data = []
    index = 0
    while index < 10:
        job = jobs[index]
        job_id = job.get("job_id")
        job_title = job.get("title")
        company_name = job.get("company_name")
        location = job.get("location")
        description = job.get("description")
        related_link = job["related_links"][0].get("link")
        work_from_home = job["detected_extensions"].get("work_from_home")
        time_since_posting = job["detected_extensions"].get("posted_at")
        salary = try_to_get_salary(job)
        qualifications = list_to_string(job["job_highlights"][0]["items"])
        job_data = [job_id, job_title, company_name, location, description, related_link, work_from_home, time_since_posting,
                    salary, qualifications]
        jobs_data.append(job_data)
        index += 1
    return jobs_data


def list_to_string(list_in):
    str_out = ''
    index = 0
    for _ in list_in:
        str_out = str_out + list_in[index]
        index += 1
    return str_out


def try_to_get_salary(job):
    try:
        salary = job["job_highlights"][2]["items"][0]
    except IndexError:
        salary = None
    return salary


def open_database(file_name: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    database_connection = sqlite3.connect(file_name)
    cursor = database_connection.cursor()
    return database_connection, cursor


def setup_database(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS jobs(
        job_id TEXT PRIMARY KEY,
        job_title TEXT,
        company_name TEXT,
        location TEXT,
        description TEXT,
        related_link TEXT,
        work_from_home BOOL DEFAULT FALSE,
        time_since_posting TEXT,
        salary TEXT
        );''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS qualifications(
        job_id TEXT,
        qualifications TEXT,
        FOREIGN KEY (job_id) REFERENCES jobs(job_id)
        );''')


def close_database(connection: sqlite3.Connection):
    connection.commit()
    connection.close()


def insert_job_to_database(job_data, cursor):
    jobs_table_data = job_data[:9]
    qualifications_data = [job_data[0], job_data[9]]
    cursor.executemany('''INSERT INTO jobs
    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);''', (jobs_table_data,))
    cursor.executemany('''INSERT INTO qualifications VALUES(?, ?);''', (qualifications_data,))


def insert_jobs_to_database(jobs_data, cursor):
    for job in jobs_data:
        insert_job_to_database(job, cursor)


def main():
    connection, cursor = open_database("job_search.sqlite")
    setup_database(cursor)
    pages_searched = 0
    total_pages = 1
    while pages_searched < total_pages:
        jobs = job_search(pages_searched * 10)
        jobs_data = get_jobs_data(jobs)
        insert_jobs_to_database(jobs_data, cursor)
        pages_searched += 1
    close_database(connection)


if __name__ == "__main__":
    main()
