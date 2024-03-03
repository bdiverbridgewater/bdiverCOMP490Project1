Project written by Brian Diver
COMP490-002

To run this program, you will need to provide your own API key to perform the job searches. Place your API key in a 
locally created project file called "key_secrets" and create a variable called "api_key" within it to store your key. 
Make sure the secrets file is ignored by gitHub.This will allow you to use your API key without making it a part of the 
project that others can see or use.
The program requires installation of all packages outlined in "requirements.txt".
The main function of this program is to use Google job search via serpapi to save job data to a locally created database
("job_search.sqlite"). A separate Excel file containing job data is also read for jobs to add to the database.
The data is then viewable in a GUI program as a list, or on a map.
In the current build of the program, 5 searches are done consecutively, with 10 results per search. Running the program
will use 5 of your searches allotted by serpapi. If you attempt to run the program multiple times, the results will be 
added to the already existing database.
The database has 2 tables. The table called "jobs" has 8 columns of job data, each row referencing a different search 
result. The table called qualifications contains information about qualifications for a job based on a foreign key 
referencing the "jobs" table.

Currently, the filter button within the GUI doesn't work. Pressing the button has no effect.

The map takes a very long time to load as the program requests the geolocation of every single job before opening.