# Battery2Life Backend

[TBA.description]

## Running The Server 

Step 1: Clone the Repository
```
 git clone https://isense-gitlab.iccs.gr/battery2life/
```

Step 2: Navigate to the branch you need
```
git branch -a 
git branch remotes/origin/[BranchName] 
git checkout [BranchName] 
```

Step 3: Create and Activate Virtual Environment
 ```
 cd battery2life 
 python -m venv venv
 source venv/bin/activate
 ```

Step 4: Run Database Migrations
```
python manage.py migrate

```

Step 1: Run The App
 ``` docker
 cd ../
 docker-compose build
 docker-compose up -d 

 docker-compose logs -f #check for errors
 ```

 Step 2: Stop The App
 ```
 docker-compose down 
 ```
