for i in {1..100}; do \
    curl --location --request POST 	'http://127.0.0.1:5000/api/v1/resources/users/create' \
    --header 'Content-Type: application/json' \
    --data-raw '{"email":"sample'$i'@gmail.com","username":"sample'$i'","karma":"1"}' \
    --write-out '%{http_code}\n'
done