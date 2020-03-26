#Create user
echo "Creating user...."
curl --location --request POST 	'http://localhost:2015/users/api/v1/resources/users/create' \
--header 'Content-Type: application/json' \
--data-raw '{"email":"bob@gmail.com","username":"bob","karma":"0"}' \
--write-out '%{http_code}\n'

echo "Creating user...."
curl --location --request POST 	'http://localhost:2015/users/api/v1/resources/users/create' \
--header 'Content-Type: application/json' \
--data-raw '{"email":"bill@gmail.com","username":"bill","karma":"0"}' \
--write-out '%{http_code}\n'

echo "Creating user...."
curl --location --request POST 	'http://localhost:2015/users/api/v1/resources/users/create' \
--header 'Content-Type: application/json' \
--data-raw '{"email":"lisa@gmail.com","username":"lisa","karma":"0"}' \
--write-out '%{http_code}\n'

echo "Creating user...."
curl --location --request POST 	'http://localhost:2015/users/api/v1/resources/users/create' \
--header 'Content-Type: application/json' \
--data-raw '{"email":"mayra@gmail.com","username":"mayra","karma":"0"}' \
--write-out '%{http_code}\n'

echo "Creating user...."
curl --location --request POST 	'http://localhost:2015/users/api/v1/resources/users/create' \
--header 'Content-Type: application/json' \
--data-raw '{"email":"jeff@gmail.com","username":"jeff","karma":"0"}' \
--write-out '%{http_code}\n'

echo "Creating user...."
curl --location --request POST 	'http://localhost:2015/users/api/v1/resources/users/create' \
--header 'Content-Type: application/json' \
--data-raw '{"email":"larry@gmail.com","username":"larry","karma":"0"}' \
--write-out '%{http_code}\n'

#Update email
echo "Updating email...."
curl --location --request PUT 	'http://localhost:2015/users/api/v1/resources/users/email' \
--header 'Content-Type: application/json' \
--data-raw '{"username":"bob","email":"b@gmail.com"}' \
--write-out '%{http_code}\n'

#Increment Karma
echo "Incrementing karma...."
curl --location --request PUT 	'http://localhost:2015/users/api/v1/resources/users/inc' \
--header 'Content-Type: application/json' \
--data-raw '{"username":"bob"}' \
--write-out '%{http_code}\n'

#Decrement Karma
echo "Decrementing karma...."
curl --location --request PUT 	'http://localhost:2015/users/api/v1/resources/users/dec' \
--header 'Content-Type: application/json' \
--data-raw '{"username":"bob"}' \
--write-out '%{http_code}\n'

#Deactivate account
echo "Deactivating account...."
curl --location --request DELETE 	'http://localhost:2015/users/api/v1/resources/users/remove' \
--header 'Content-Type: application/json' \
--data-raw '{"username":"bob"}' \
--write-out '%{http_code}\n'
