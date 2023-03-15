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
