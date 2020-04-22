#send message
echo "Sending message...."
curl --location --request POST 	'http://127.0.0.1:5000/api/v1/resources/message' \
--header 'Content-Type: application/json' \
--data-raw '{"userto":"alice","userfrom":"bob","messagecontents":"hello alice :)", "messageflag":"favorite"}' \
--write-out '%{http_code}\n'

echo "Sending message...."
curl --location --request POST 	'http://127.0.0.1:5000/api/v1/resources/message' \
--header 'Content-Type: application/json' \
--data-raw '{"userto":"rey","userfrom":"kylo","messagecontents":"hello rey :)", "messageflag":"discussion"}' \
--write-out '%{http_code}\n'

#show favorite messages
echo "Showing favorite messages...."
curl --location --request GET 	'http://127.0.0.1:5000/api/v1/resources/message/favorite' \
--header 'Content-Type: application/json' \
--data-raw '{"messageflag":"favorite"}' \
--write-out '%{http_code}\n'

#delete message
echo "Deleting message...."
curl --location --request DELETE 	'http://127.0.0.1:5000/api/v1/resources/message/delete' \
--header 'Content-Type: application/json' \
--data-raw '{"messageid":"1"}' \
--write-out '%{http_code}\n'