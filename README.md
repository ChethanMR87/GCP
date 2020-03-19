**Simple Web API using Flask**
Web API endpoint /info created which returns in JSON format with the following

- [service_name] 
- [version] 
- [git_commit_sha] 
- [environment]

    `Sample JSON response: 


    	{"app_name":"flask_app", 
        "environment":[{"service_port":"5000"},{"log_level":"INFO"}], "git_commit_sha":"aecd027632578627ff8719bfb5d0647b498c86e7", "version":"1.0"}
`
**Programming language used**
Using python 3.6.2

**Configuration**
Service Port log_level git_commit_sha

**Run app**
CMD->mkdir Flask_app folder

C:\NotBackedUp\Flask_app>py -m venv GCP

Activate the environment 

(GCP) C:\NotBackedUp\Flask_app>env\Scripts\activate

Install Flask 

(GCP) C:\NotBackedUp\Flask_app> pip install flask

Read git version
(GCP) C:\NotBackedUp\GCP>git describe --tags >git_version.txt

Read and write git-commit
(GCP) C:\NotBackedUp\GCP>git rev-parse head >git_commit_sha.txt

execute
(GCP) C:\NotBackedUp\GCP>set FLASK_APP=execute.py
