# Feeby
Feeby is a tool that allows students to receive feedback in an organised and fast manner from teachers and experts in their field.

## Git workflow
### Main branch
No direct pushes, only MR’s are allowed
Production ready, no bugs allowed
### Dev branch
No direct pushes, only MR’s are allowed
Semi-production ready, bugs are allowed but must be fixed before they get pushed to the main prod branch.
### Creating a feature or bugfix branch
Go to the user story in Jira and open it. Click on create branch and copy the git command. Run this command in your terminal and start working. Finally, create a pull request in to dev and let it get reviewed by a team member.

## Running the tool locally
### Docker
run `make start` or the equivalent `make` to launch the development environment.

run `make prod-start` to test your code, build and run the production environment locally on your machine.

run `make down` or `make prod-down` to stop the respective environments.

These are the most important commands to know but you should take a look in the makefile to see what all the commands do. 

### Locally
Read the README within the backend and frontend folders to look at how to run this tool without docker.