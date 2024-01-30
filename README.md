Project written by Brian Diver
COMP490-002

To run this program, you will need to provide your own API key to perform the job searches. Place your API key in a 
locally created project file called "secrets" and create a variable called "api_key" within it. Make sure the secrets
file is ignored by gitHub.This will allow you to use your API key without making it a part of the project that others
can see or use.
The program requires the "GoogleSearch" function from the "serpapi.google_search" package. It also imports the "json" 
package to write the data to a file.
The main function of this program is to use Google job search to save job data to a file locally. In the current build
of the program, 5 searches are done consecutively. Running the program will use 5 of your searches allotted by serpapi.

Exception handling is not done at all during the search process. If for some reason the search is not able to execute, 
the program will either crash or run indefinitely