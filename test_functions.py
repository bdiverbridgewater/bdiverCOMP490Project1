from openpyxl import load_workbook
from main import (open_database, setup_database, close_database, job_search, try_to_get_salary, get_jobs_data,
                  insert_jobs_to_database, get_excel_jobs)


def test_database_functionality():
    connection, cursor = open_database("test_database.sqlite")
    setup_database(cursor)
    test_search = test_data_retrieval()
    test_jobs_data = get_jobs_data(test_search)
    insert_jobs_to_database(test_jobs_data, cursor)
    excel_data = get_excel_jobs()
    insert_jobs_to_database(excel_data, cursor)
    cursor.execute('''SELECT * FROM jobs;''')
    job = cursor.fetchone()
    assert job[0] == test_search[0].get("job_id")
    assert job[1] == test_search[0].get("title")
    assert job[2] == test_search[0].get("company_name")
    assert job[3] == test_search[0].get("location")
    assert job[4] == test_search[0].get("description")
    assert job[5] == test_search[0].get("related_links")[0].get("link")
    assert job[6] == test_search[0]["detected_extensions"].get("work_from_home")
    assert job[7] == test_search[0]["detected_extensions"].get("posted_at")
    assert job[8] == try_to_get_salary(test_search[0])
    cursor.execute('''DROP TABLE jobs;''')
    cursor.execute('''DROP TABLE qualifications;''')
    close_database(connection)


def test_data_retrieval():
    search_results = job_search(0)
    assert search_results is not None
    assert len(search_results) == 10
    return search_results


def test_excel_data_retrieval():
    wb = load_workbook('Sprint3Data.xlsx')
    sheet = wb['Comp490 Jobs']
    test_excel_data = get_excel_jobs()
    test_job = test_excel_data[0]
    assert sheet[2][0].value == test_job[2]
    assert sheet[2][2].value == test_job[0]
    assert sheet[2][4].value == test_job[3]
    assert sheet[2][9].value == test_job[1]
