# Battery2Life Backend

[TBA.description]

## Running The Server

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


Step 4.a: Run The App

 ``` bash
 docker-compose build
 docker-compose up -d 

 docker-compose logs -f #check for errors
 ```

 Step 4.b: Stop The App

 ```bash
 docker-compose down 
 ```

## Testing Mosquitto MQTT

Step 1: run the app as mentioned above 

Step 2: install a mosquitto client in the terminal
> sudo apt update && sudo apt install mosquitto-clients

Step 3: open a terminal window, paste the following and see if you can read the message in the terminal you have started the app or mosquitto/mosquitto-client.log file 
> mosquitto_pub -t 'hello/topic' -m 'henlo wrold' -u user1 -P user1


## API Documentation

 Run the steps mentioned above, run the app and then visit:
 > localhost:8000/api/schema/swagger-ui/
