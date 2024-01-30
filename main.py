from job_search import job_search
import json
total_pages = 5
if __name__ == "__main__":
    current_pages = 0
    search_results = open('search_results.txt', 'a')
    print('Starting job search now...')
    while current_pages < total_pages:
        # There are 10 results per page, so multiplying the current page by 10 gives the right offset to search the
        # 2nd and 3rd page etc.
        page_results = json.dumps(job_search(current_pages * 10))
        search_results.write(page_results)
        current_pages += 1
    search_results.close()
    print('Search Complete. Results saved to "search_results.txt"')
