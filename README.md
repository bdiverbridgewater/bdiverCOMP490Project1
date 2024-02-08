Project written by Brian Diver
COMP490-002

To run this program, you will need to provide your own API key to perform the job searches. Place your API key in a 
locally created project file called "secrets" and create a variable called "api_key" within it to store your key. 
Make sure the secrets file is ignored by gitHub.This will allow you to use your API key without making it a part of the 
project that others can see or use.
The program requires installation of "serpapi" and "google_search_results" packages as outlined in the 
"requirements.txt" file.
The main function of this program is to use Google job search via serpapi to save job data to a locally created database
("job_search.sqlite"). 
In the current build of the program, 5 searches are done consecutively, with 10 results per search. Running the program
will use 5 of your searches allotted by serpapi. If you attempt to run the program multiple times, the results will be 
added to the already existing database.