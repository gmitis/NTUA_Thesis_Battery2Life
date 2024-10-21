# Battery2Life Backend

[TBA.description]

## Running The Server 

Step 1: Clone the Repository
```
 git clone https://isense-gitlab.iccs.gr/battery2life/backend
```

Step 2: Navigate to the branch you need
```
git branch -a 
git branch remotes/origin/[BranchName] 
git checkout [BranchName] 
```

Step 3.a: Run The App
 ``` docker
 docker-compose build
 docker-compose up -d 

 docker-compose logs -f #check for errors
 ```

 Step 3.b: Stop The App
 ```
 docker-compose down 
 ```

 ## API Documentation
 Run the steps mentioned above, run the app and then visit:
 > localhost:8000/api/schema/swagger-ui/
