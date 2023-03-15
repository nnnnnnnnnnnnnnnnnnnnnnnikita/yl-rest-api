from requests import get, post, delete, put


#Received all the works
print(get('http://127.0.0.1:8080/api/jobs').json())

#Getting one job correctly
print(get('http://127.0.0.1:8080/api/jobs/1').json())

#Erroneous request for one job — invalid id
print(get('http://127.0.0.1:8080/api/jobs/2342342423424234').json())

#An erroneous request for one job is a string
print(get('http://127.0.0.1:8080/api/jobs/lmao').json())

#to check the execution
print(get('http://127.0.0.1:8080/api/jobs').json())
#correct POST request
print(post('http://127.0.0.1:8080/api/jobs',
           json={"team_leader": 11, "title": "test", "work_size": 44, "collaborators": '1, 2',
                 "start_date": None, "end_date": None, "is_finished": True}).json())

#to check the execution
print(get('http://127.0.0.1:8080/api/jobs').json())

#duplicate of the previous one - id already exists 
print(post('http://127.0.0.1:8080/api/jobs',
           json={"id": 88, "team_leader": 10, "title": "test", "work_size": 44, "collaborators": '1, 2',
                 "start_date": None, "end_date": None, "is_finished": True}).json())

#wrong POST request, no team-lead
print(post('http://127.0.0.1:8080/api/jobs',
           json={"team_leader": 44433, "title": "test", "work_size": 44, "collaborators": '1, 2',
                 "start_date": None, "end_date": None, "is_finished": True}).json())

#lack of data
print(post('http://127.0.0.1:8080/api/jobs',
           json={"team_leader": 10, "title": "test"}).json())


#to check the execution
print(get('http://127.0.0.1:8080/api/jobs').json())
#true deleting
print(delete('http://127.0.0.1:8080/api/jobs/1').json())

#to check the execution
print(get('http://127.0.0.1:8080/api/jobs').json())

#wrong there is no such id
print(delete('http://127.0.0.1:8080/api/jobs/1232332').json())

#wrong there is no such id
print(delete('http://127.0.0.1:8080/api/jobs/101232323').json())

#to check the execution
print(get('http://127.0.0.1:8080/api/jobs').json())
