from openpyxl import load_workbook

from main import (open_database, setup_database, close_database, job_search, get_jobs_data, insert_jobs_to_database,
                  get_excel_jobs, get_salary)
from filter_functions import filter_by_keyword, filter_by_remote, filter_by_location, filter_by_min_salary


def test_database_functionality():
    connection, cursor = open_database("../test_database.sqlite")
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
    try:
        benefits_section = test_search[0]["job_highlights"][2]
    except IndexError:
        benefits_section = None

    min_salary, max_salary = get_salary(benefits_section, test_search[0]["description"])
    assert job[8] == min_salary
    assert job[9] == max_salary
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


def test_filter_by_keyword():
    test_excel_data = get_excel_jobs()
    test_keyword = "Web"
    filtered_test_data = filter_by_keyword(test_excel_data, test_keyword)
    for job in filtered_test_data:
        assert test_keyword in job[1] or job[4]


def test_filter_by_remote():
    test_data = get_jobs_data(job_search(0))
    test_data = filter_by_remote(test_data)
    for job in test_data:
        assert job[6] == 1


def test_filter_by_location():
    test_excel_data = get_excel_jobs()
    test_location = "Ohio"
    filtered_test_data = filter_by_location(test_excel_data, test_location)
    for job in filtered_test_data:
        assert test_location in job[3]


def test_filter_by_min_salary():
    test_excel_data = get_excel_jobs()
    test_salary = 200000
    filtered_test_data = filter_by_min_salary(test_excel_data, test_salary)
    print(len(filtered_test_data))
    for job in filtered_test_data:
        assert job[8] >= test_salary
