# Battery2Life Backend

[TBA.description]

## Testing The App:

### Running The Server

Step 1: Clone the Repository

```bash
git clone https://isense-gitlab.iccs.gr/battery2life/backend
```

Step 2: Navigate to the branch you need

```bash
git branch -a 
git checkout -b [BranchName] origin/[BranchName] 
```

Step 3: Add necessary files
```bash
./create_necessary_files.sh
# add necessary variables in the battery2life/.env.dev
```


Step 4.a: Create services

 ``` bash
 docker-compose up -d --build --force-recreate 

# follow service logs
 docker logs [ServiceName] -f 
 ```

 Step 4.b: Stop and remove Services

 ```bash
 # brings down services removes every volume, network and container created 
 docker-compose down -v
 ```

### Testing Mosquitto MQTT

Step 1: run the app as mentioned above 

Step 2: install a mosquitto client in the terminal
> sudo apt update && sudo apt install mosquitto-clients

Step 3: 
i. open a terminal window  
ii. paste the following
iii. see if you can read the message in the terminal or in the mosquitto/mosquitto-client.log file 
> mosquitto_pub -t 'hello/topic' -m 'henlo wrold' -u user1 -P user1


### API Documentation

 Run the steps mentioned above, run the app and then visit:
 > localhost:8000/api/schema/swagger-ui/



### Admin Credentials
- username: Admin
- password: Admin


### PostgreSQL schema view

Step 1:
``` bash 
    docker-compose --build --force-recreate db api
```

Step 2:
```bash
    docker exec -it db bash
```

Step 3:
```bash
    # connect to used db b2l
    psql -U root -d b2l
```

Step 4:
```bash
    # show all tables
    \dt
```

### Endpoints
Step 1: Test api/cells
- make a post request with a list of cell_ids like [0, 1, 2, 3]

Step2: Test api/eis
- send a post request to endpoint with body
{
    "status": "success",
    "event_id": "207_1",
    "cell_id": 0,
    "frequency": 25.11886432,
    "amplitude": 0.00033255133178403194,
    "phase": 0.085914587975807,
    "current_offset": 2,
    "v_start": 3.5,
    "v_end": 3.5,
    "temperature": 25
}

Step 3: Test api/measurements
- send a post request to endpoint with body
{
    "cell_ids": [0, 1, 2, 3],
    "voltage": [3.934999943, 3.950999975, 3.816999912, 3.948999882],
    "temperature": [18.5, 19.39999962, 17.29999924, 16.60000038],
    "current": [0, 0, 0, 0],
    "sot": [0.1, 0.2, 0.3, 0.4],
    "phase": [93, 34, 21, 59],
    "soc": [69.66569519, 70.92323303, 59.74949265, 70.6905365]
} 
