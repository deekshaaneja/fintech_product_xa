# fintech_product
# Run
###### To run the docker: 
```docker-compose up```
###### To run the docker in daemon mode: 
```docker-compose up -d```
###### Note - If the server doesn't start, then it might be because of Mysql taking time for initial setup. In this case, the application will keep retrying until the Mysql is up.To check if Mysql has started or not, use the following command on cli-
```mysql -u root -padmin1234```
###### Moreover, please ensure that port 3306 and 9000 aren't bound to any other process on the host machine.
###### Data Persistence
###### To persist the data,we have created db_data volume on host system
##### Curl Commands to Test:
###### 1.grab_and_save
###### Positive Test Case:
```curl -X POST \ 
  http://localhost:9000/grab_and_save \
  -H 'Accept: */*' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: text/plain' \
  -H 'Host: localhost:9000' \
  -H 'Postman-Token: e01a0e5f-5b88-4392-b4e6-5de1176e02ec,ee4ea78b-b7ec-4071-b9db-d2a3db6fa776' \
  -H 'User-Agent: PostmanRuntime/7.13.0' \
  -H 'accept-encoding: gzip, deflate' \
  -H 'cache-control: no-cache' \
  -H 'content-length: 35' \
  -d '{"currency": "AED", "amount": 9000}'
```
###### Negative Test Case:
```curl -X POST \
  http://localhost:9000/grab_and_save \
  -H 'Accept: */*' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: text/plain' \
  -H 'Host: localhost:9000' \
  -H 'Postman-Token: 868b9929-ef27-44bf-ad16-1bc71386bf49,7f5ed0ae-2419-4be4-9873-ff4f49554b04' \
  -H 'User-Agent: PostmanRuntime/7.13.0' \
  -H 'accept-encoding: gzip, deflate' \
  -H 'cache-control: no-cache' \
  -H 'content-length: 33' \
  -d '{"currency": "AED", "amount": -6}'
 ```
###### last Positive Test Case
``` curl -X GET \
  'http://localhost:9000/last?currency=AED' \
  -H 'Accept: */*' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Host: localhost:9000' \
  -H 'Postman-Token: 16a68fcb-b973-415b-8b01-465511b5bae4,e47040be-f38e-44b9-80f6-7d38267f7853' \
  -H 'User-Agent: PostmanRuntime/7.13.0' \
  -H 'accept-encoding: gzip, deflate' \
  -H 'cache-control: no-cache'
 ```
###### Negative Test Case:
```curl -X POST \
  http://localhost:9000/grab_and_save \
  -H 'Accept: */*' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: text/plain' \
  -H 'Host: localhost:9000' \
  -H 'Postman-Token: 868b9929-ef27-44bf-ad16-1bc71386bf49,0f04db77-4cba-4211-a127-55e381c82af9' \
  -H 'User-Agent: PostmanRuntime/7.13.0' \
  -H 'accept-encoding: gzip, deflate' \
  -H 'cache-control: no-cache' \
  -H 'content-length: 33' \
  -d '{"currency": "AED", "amount": -6}'
 ```
