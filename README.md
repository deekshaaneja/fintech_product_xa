# fintech_product
# Run
###### To run the docker: docker-compose up
###### To run the docker in daemon mode: docker-compose up -d
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
