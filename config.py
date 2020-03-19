import os

def port():
	service_port="5000"
	return service_port
def log_level():
	log_level="INFO"
	return log_level
def git_commit_sha():
	 f = open("C:/NotBackedUp/GCP/git_commit_sha.txt", "r")
	 git_commit_sha=f.read()
	 f.close()
	 return git_commit_sha
def git_version():
	 f = open("C:/NotBackedUp/GCP/git_version.txt", "r")
	 git_version=f.read()
	 f.close()
	 return git_version	 
