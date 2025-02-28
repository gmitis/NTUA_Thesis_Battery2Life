<!-- TASK: fill read more link-->

# Baterry2Life Cloud Platform - Backend
<!-- [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) -->
<!-- [![GitHub contributors](https://img.shields.io/github/contributors/coderjojo/creative-profile-readme)](https://github.com/coderjojo/creative-profile-readme/graphs/contributors) -->
<br>


## Table of Contents
- [Project Description](#project-description)
- [File Structure](#file-structure)
- [System Installation](#system-deployment)
- [Usage](#usage)
- [Tools Used](#tools-used)
- [Contributors](#contributors)
- [Licence](#license)
<!-- - [System Description](#system-description) -->

<br><br>


## Project Description
[TBF]

>  
[read more](thesis_url)

<br><br>


<!-- ## System Description 
[TBF: Define resources] -->
 <!-- VM       | Cores |          CPU type     | System RAM | Disk Size | Disk Type     | Role                | Additional processes | Cluster Nodes (Docker Swarm) | -->
<!-- |:--------:|:-----:|:---------------------:|:----------:|:---------:|:-------------:|:-------------------:|:--------------------:|:----------------------------:| -->
<!-- | 1    | N     | CPU_coretype | ram_space       | disk_space     | disk_type            | cluster_role_if_any         |         service_that_runs_here            |  pod node?                     | -->
<!-- | 2    | N     | CPU_coretype | ram_space       | disk_space     | disk_type            | cluster_role_if_any             | service_that_runs_here              |  pod node?                      | -->
<!-- | 3    | N     | CPU_coretype | ram_space       | disk_space     | disk_type            | cluster_role_if_any             | service_that_runs_here            |  pod node?                      | -->
<!-- | 4    | N     | CPU_coretype | ram_space       | disk_space     | disk_type            | cluster_role_if_any             | service_that_runs_here           |  pod node?                      | -->


## File Structure

### Structure
```bash
.
├── README.md
├── battery2life
│   ├── Dockerfile
│   ├── api_schema.yaml
│   ├── app.log
│   ├── batteries
│   │   ├── __pycache__
│   │   ├── admin.py
│   │   ├── api
│   │   │   ├── __pycache__
│   │   │   ├── serializers.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   ├── apps.py
│   │   ├── management
│   │   ├── migrations/
│   │   ├── mixins.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── utils.py
│   │   └── views.py
│   ├── battery2life
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── app.log
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── db.sqlite3
│   ├── manage.py
│   ├── requirements.txt
│   └── venv
├── create_necessary_files.sh
├── database
│   ├── data
│   ├── database_erd.mmd
│   ├── dummy_data
│   │   ├── batteries_cell_cell_chemistry.csv
│   │   ├── battery.csv
│   │   ├── cell.csv
│   │   ├── chemical.csv
│   │   ├── dimension.csv
│   │   ├── eis.csv
│   │   ├── manufacturer.csv
│   │   ├── material.csv
│   │   ├── measurement.csv
│   │   ├── module.csv
│   │   └── safety_feature.csv
│   ├── init.sql
│   ├── pgdata
│   └── populate_dummy.sql
├── docker-compose.yaml
├── mosquitto
│   ├── config  
│   ├── data  
│   └── log  
├── mosquitto-client
│   ├── Dockerfile
│   ├── mosquitto-client.log
│   └── mosquitto_client.py
├── node_modules
├── startup.sh
├── .gitignore
└── testing
    ├── data
    │   ├── invalid_input.json
    │   ├── valid_input.json
    │   └── valid_output.json
    ├── main.js
    ├── modules
    │   ├── config.js
    │   ├── helpers.js
    │   ├── metrics.js
    │   └── test.js
    ├── package-lock.json
    ├── package.json
    └── test_data
        ├── invalid_input.json
        ├── valid_input.json
        └── valid_output.json
```

### Explanation

For the entire system, all the files inside the \texttt{./} directory, the most vital files are:
- docker-compose.yaml: This is the most important file and contains the definitions for all of the available services in a format that makes them really easy to deploy.
- .gitignore: the file states which files are to be ignored from git tracking their history 
- create_necessary_files.sh: script the create the files necessary for logging since the logging files contain sensitive information and are not tracked by git.

#### Django App

The entire API resides on to ./battery2life directory.
The most important files are:
- Dockerfile: This is the custom docker image we built to run the app
- manage.py: This is the basic script that allows us to perform database management actions and create new apps
- requirements.txt: This file is used for the bookkeeping of the modules used in our app. The Dockerfile image uses it to install any module necessary for the running of our app.

*Main App*:
Our main app is the one on the ./battery2life/battery2life directory.
It contains the following files.
- settings.py: is the main settings folder containing setting for loggers, the database, authentication etc
- urls.py: is the main part for URLs of our resources   

*API App*:
The app that implements the main functionalities is in the directory ./battery2life/batteries
It contains the following files and directories.
- admin.py: includes the definitions for the database models to be used by the admin control panel
- api/ : includes app views (they parse the request), serializers (they translate the JSON to a know python format and the other way around) and urls (they lead the way to which view to use for which endpointurl) 
- migrations/ : contains the database version history
- models.py: defines the Django ORM models for the database

<br>

#### PostgreSQL Database

The necessary files for the database are located in ./database directory.
The most important ones are:
- database_erd.mmd: this is the entity relational schema of our database done in mermaid markup language
- init.sql: is the script that is run by the db service when the container starts in order to initialize the database
- pgdata: this is the volume that is mapped by docker that contains all the data of the database
- dummy_data/ : this is the directory that contains all of the dummy data useful for testing the api and the database
- populate_dummy.sql: this is the script that populates the database with dummy data

<br>

#### Mosquitto Broker

The necessary files for the Mosquitto message broker are located in ./mosquitto directory.
The most important ones are:
- config/ : contains the mosquitto.conf which is the configuration data for the broker and the passwd file used for authentication of clients
- data/ : contains the data the persist when we get a message
- log/ : contains the log data from the broker

<br>

#### Mosquitto Client

The necessary files for the Mosquitto Client are located in ./mosquitto-client directory.
The most important ones are:
- Dockerfile: the custom image create in order for the client to be able to use a python logger
- mosquitto_client.py: the implementation of the mosquitto client together with the client logger

<br>

#### Testing

[TBF]

<br> <br>

## System Installation

### Step 1: Install dependencies

#### Install Docker
```bash
# install docker on linux
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common

echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

sudo apt install docker-ce


# verify installation
docker --version

# enable docker to run automatically on every startup
sudo systemctl start docker
sudo systemctl enable docker

# run docker without sudo
sudo groupadd docker
sudo usermod -aG docker $USER
sudo reboot
```

#### Install docker-compose
```bash
sudo apt update
sudo apt install curl
sudo curl -L "https://github.com/docker/compose/releases/download/$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r .tag_name)/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

# verify the installation
docker-compose --version
```

#### Install k6
```bash
# fetch the GPG key and concert it to binary
curl -fsSL https://dl.k6.io/key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/k6-archive-keyring.gpg

# add k6 to apt resources
echo "deb [signed-by=/usr/share/keyrings/k6-archive-keyring.gpg] https://dl.k6.io/deb stable main" | sudo tee /etc/apt/sources.list.d/k6.list

# install k6
sudo apt update
sudo apt install k6
```

<br>

### Step 2: Clone necessary repository
```bash
# install git
sudo apt update && sudo apt install git

# clone repository
cd ~/
git clone https://isense-gitlab.iccs.gr/battery2life/backend

# navigate to the necessary repository
git branch -a 
git checkout -b [BranchName] origin/[BranchName] 
```

<br>

### Step 3: Create necessary files
Run the following commands to check if cluster is setup correctly
```bash
# run automated creation script
chmod +x create_necessary_files.sh
./create_necessary_files.sh
```


<br><br>


## Usage

### Initialize Services
```bash
# start all of the services
cd ~/
docker-compose up -d --build --force-recreate

# start some of the services
docker-compose up -d --build --force-recreate  [ {service_name1} {service_name2} ... {service_nameN} ]

```

<br>

### Stop Services
```bash
# stop all of the services and remove all containers and networks  
cd ~/
docker-compose down 

# stop all of the services and remove all containers, networks  and volumes
cd ~/
docker-compose down -v

# stop some of the services
cd ~/
docker-compose down [ {service_name1} {service_name2} ... {service_nameN} ]

```

<br>

### Testing

#### API
Step 1: Navigate to the API documentation
> Start the app and go to http://localhost:8000/api/schema/swagger-ui/

Step 2: Authenticate
- Click on the /api/token/ endpoint 
- Make a POST request with your username and passworf
- Copy the access token from the response of the request
- On the top right corner of the page click Authorize (green frame with a lock), paste your access token into the value placeholder, click the Authorize button and then press the close button

Step 3: Test endpoints
- Click on an endpoint 
- Click on try it out 
- Fill in the required HTTP method information (id, body)
- Click on the blue execute button
- Inspect the response headers, url, status code and body below on the "Response" section

Step 4 (Optional): Request example payloads
> You can find example payloads for every endpoint in the thesis chapter: Syster Model, endpoints section
> You can also see example response to compare if your response was valid

<br>

#### Database
To populate the database with dummy data for testing:
```bash
# remove previous volumes, containers, networks 
docker-compose down -v

# start db and api to generate the db tables
 docker-compose up -d db api

# populate tables with dummy data
# in order to populate the database with real data you should place your data to the folder ./database/data and change the mount volume in the docker-compose file
docker exec -it db psql -U root -d b2l -f /populate_dummy.sql
```

The populate.dummy.sql file populates the database and sets the automatic id variables to the current amount of data inserted.

<br>

#### Mosquitto MQTT
Step 1: run the app as mentioned above 

Step 2: install a mosquitto client in the terminal
```bash
sudo apt update && sudo apt install mosquitto-clients
```

Step 3: 
i. open a terminal window  
ii. paste the following
iii. see if you can read the message in the terminal or in the mosquitto/mosquitto-client.log file 
```bash
mosquitto_pub -t 'hello/topic' -m 'henlo wrold' -u user1 -P user1
```

<br> <br>

## Troubleshooting 

### API
i. It possible when starting the app for the api docker service to see that the db is not running therefore stop. In this case run the same command again and it will only start the api

ii. It's possible if the necessary files are not create for the docker-compose tool to interpret these files as folders and create the corresponding folders and mount them as volumes. In that case delete the folders, delete the volumes of the api service, run the files creation script and the start the service again.

<br>

### Database
See the schema of the database with:
```bash
# create services
docker-compose up --build --force-recreate db api

# run a bash terminal inside the database container
docker exec -it db bash

# connect to used db b2l
psql -U root -d b2l

# show all tables
\dt
```

See the attributes of a table:
```bash
# first connect to the user db as shown above

# then run the following command
\d {table_name}
```

<br><br>


## Tools used 
![Git Badge](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![SQL Badge](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=sqlite&logoColor=white)
![DRF Badge](https://img.shields.io/badge/DRF-ff1709?style=for-the-badge&logo=django&logoColor=white)
![Bash Badge](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)
![GitLab Badge](https://img.shields.io/badge/GitLab-FC6D26?style=for-the-badge&logo=gitlab&logoColor=white)
![Python Badge](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django Badge](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Docker Badge](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Swagger Badge](https://img.shields.io/badge/Swagger_UI-85EA2D?style=for-the-badge&logo=swagger&logoColor=black)
![PostgreSQL Badge](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Mosquitto MQTT Badge](https://img.shields.io/badge/Mosquitto_MQTT-3C5280?style=for-the-badge&logo=eclipsemosquitto&logoColor=white)

<br><br>


## Contributors
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/gmitis">
        <img src="https://github.com/identicons/mwhite.png" width="100px;" alt="gmitis"/>
        <br />
        <sub><b>Yanis Mytis</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://isense-gitlab.iccs.gr/tsougiannis">
        <img src="https://snipboard.io/Gu7MgA.jpg" width="100px;" alt="AntonisZakynthinos"/>
        <br />
        <sub><b>Vangelis Tsougiannis</b></sub>
      </a>
    </td>
</table>

<br><br>

## License
[TBF]
