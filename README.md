Ufaber Test Project Documentations 
Home Page:

dtabase--(serializer)-->Project  API—https://ufabertest.herokuapp.com/projectapi ---→
Home Page View--->homepge.html

Add Project :
 
addprjoject.html----->Add Project  View (projectadded) ---- Project Models  -----> database

Input Fields :- 
	Project Name
	Description
	Start Date
	End Date
	Duration
	Avtar Image


Project Detais Page :
url format :- <domain>/project/<project_id>
dtabase--(serializer)-->Project  API  (https://ufabertest.herokuapp.com/projectapi) +Task API (https://ufabertest.herokuapp.com/taskapi)+Project DetailsView (project)--->project.html


Edit Project :
project.html--->Edit Project View  (projectedit) ---->Project Model ---- > database
Input Fields  :- 
	Project Name
	Description
	Start Date
	End Date
	Duration
	Avtar Image

Add Task
project.html--→Add Task View (taskadd)  ---→Task Model ---- > database
Input Fields  :- 
	Task Name
	Description
	Start Date
	End Date
	Duration
	Assign To


Task Detais Page :
url format :- <domain>/project-<project_id>/task/<task_id>
dtabase--(serializer)-->Task API (https://ufabertest.herokuapp.com/taskapi) ----> Task DetailsView (task) --->task.html

Edit Task :
taskh.html--->Edit Task View  (taskedit) ---→Task Model ---- > database

Input Fields :- 
	Task Name
	Description
	Start Date
	End Date
	Duration
	Assign To

VERSION-
Python version-3.8
Django version-2.2.13
REST framework-3.11.0

Database detail-
Local- sqllite
Heroku-postgresql

