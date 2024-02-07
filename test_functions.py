from typing import Tuple

from main import open_database, setup_database, insert_job_to_database, close_database, job_search


def test_database_functionality():
    connection, cursor = open_database("test_database.sqlite")
    setup_database(cursor)
    test_search = test_data_retrieval()
    insert_job_to_database(0, test_search, cursor)
    cursor.execute('''SELECT * FROM jobs;''')
    job: Tuple = cursor.fetchone()
    assert job[0] == test_search[0].get("title")
    assert job[1] == test_search[0].get("company_name")
    cursor.execute('''DROP TABLE jobs;''')
    cursor.execute('''DROP TABLE qualifications;''')
    close_database(connection)


def test_data_retrieval():
    search_results = job_search(0)
    assert search_results is not None
    assert len(search_results) == 10
    return search_results
