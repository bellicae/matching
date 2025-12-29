LARP Host–Player Matching System

Overview:
This project is a matching platform for Live Action Roleplay (LARP) sessions, connecting players with hosts.
Players can browse hosts based on classes, themes, hourly rates, and costume availability. Hosts can advertise their profiles, including base rates, themes, and costumes they own, and respond to custom costume requests.

The system also supports custom quotes for characters not owned by the host.

Features:

Host profiles:

Single class from organization-approved list

Base hourly rate

Themes with included or extra costs

Costumes owned with optional extra cost

Option to accept custom costume requests

Player filters:

Class selection (single, multiple, or all)

Theme requirements (included vs extra)

Hourly rate range

Costume availability and maximum extra cost

Option to request custom costumes

Costume quote workflow:

Players submit a request for any character

Hosts respond with a quoted price and estimated preparation time

Project Structure:
matching/

data/ Hosts, quotes, and configuration files

docs/ Documentation, diagrams, and API references

src/ Source code for models, services, and main program

tests/ Unit tests

README.md This file

requirements.txt Python dependencies

.gitignore

data/README.md contains details about JSON files and folder usage.

src/ contains all Python code, organized into:

models/ – data models like Host and PlayerFilter

services/ – filtering engine, data loader, and quote service

tests/ contains unit tests for models, filtering, and quote workflows

Getting Started:

Install Python dependencies:
pip install -r requirements.txt

Run the main program:
python src/main.py

Load data:
Hosts, quotes, classes, and themes are stored in data/.
Use the data_loader service to read JSON files into Python objects.

Run tests:
pytest tests/

Contribution:

Add new hosts by updating data/hosts.json

Add or update classes/themes in data/config/

Submit costume requests in data/quotes/quote_requests.json and responses in data/quotes/quote_responses.json

Ensure JSON validity when editing files

License & Contact:
This project is developed for [fantassy.app].
For questions or contributions, contact [deercoffe@protonmail.com]
