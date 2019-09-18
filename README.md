# fintech_product
# Run
###### To run the docker: docker-compose up
###### To run the docker in daemon mode: docker-compose up -d
###### Note - If the server doesn't start, then it might be because of Mysql taking time for initial setup. In this case, the application will keep retrying until the Mysql is up.To check if Mysql has started or not, use the following command on cli-
mysql -u root -padmin1234
###### Moreover, please ensure that port 3306 and 9000 aren't bound to any other process on the host machine.
###### Data Persistence
###### To persist the data,we have created db_data volume on host system
##### Curl Commands to Test:
###### 1.grab_and_save
###### Positive Test Case:
