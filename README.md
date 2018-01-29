NSERC Task.py mines a GitHub repository specified by the user. It is written in Python 3.5.2.

This code uses the requests library: https://github.com/requests/requests

Before running the program, the requests library (linked above) must be installed. Then run NSERC Task.py using your preferred method, similar to any other Python file. (Example: python3 "NSERC Task.py") The program will ask the user to enter a GitHub repository name, then ask for the repository owner's username. For example, to run the program on the repository located at https://github.com/chomyc1/nserc-task-test, the repository name is nserc-task-test and the username is chomyc1.

After a valid repository is entered, the program checks the GitHub API for all commits to the repository that include a specific string in their commit message. The default is "Fix" (as specified in the assignment, case sensitive), but it can be changed to a different word in the code. For all of the commits that include this string in their message, the program will write the commit's SHA and message to a file named output.csv.

This code has been tested on https://github.com/django/django, https://github.com/requests/requests, and https://github.com/chomyc1/nserc-task-test. The output files of these tests are included in this repository, and they are named "django output.csv", "requests output.csv", and "nserc-task-test output.csv" respectively.
