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

## API Documentation

 Run the steps mentioned above, run the app and then visit:
 > localhost:8000/api/schema/swagger-ui/
