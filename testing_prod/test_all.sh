# ------------------USER ACCOUNT MICROSERVICE-------------------------
# create a new user
echo "Creating user...."
curl --location --request POST 	'http://localhost:2015/users/api/v1/resources/users/create' \
--header 'Content-Type: application/json' \
--data-raw '{"email":"gabe@gmail.com","username":"gabe","karma":"0"}' \
--write-out '%{http_code}\n'

echo "Creating user...."
curl --location --request POST 	'http://localhost:2015/users/api/v1/resources/users/create' \
--header 'Content-Type: application/json' \
--data-raw '{"email":"ron@gmail.com","username":"ron","karma":"0"}' \
--write-out '%{http_code}\n'

#Update email
echo "Updating email...."
curl --location --request PUT 	'http://localhost:2015/users/api/v1/resources/users/email' \
--header 'Content-Type: application/json' \
--data-raw '{"username":"gabe","email":"gabe123@gmail.com"}' \
--write-out '%{http_code}\n'

#Increment Karma
echo "Incrementing karma...."
curl --location --request PUT 	'http://localhost:2015/users/api/v1/resources/users/inc' \
--header 'Content-Type: application/json' \
--data-raw '{"username":"gabe"}' \
--write-out '%{http_code}\n'

#Decrement Karma
echo "Decrementing karma...."
curl --location --request PUT 	'http://localhost:2015/users/api/v1/resources/users/dec' \
--header 'Content-Type: application/json' \
--data-raw '{"username":"gabe"}' \
--write-out '%{http_code}\n'

#Deactivate account
echo "Deactivating account...."
curl --location --request DELETE 	'http://localhost:2015/users/api/v1/resources/users/remove' \
--header 'Content-Type: application/json' \
--data-raw '{"username":"ron"}' \
--write-out '%{http_code}\n'

# ------------------POSTING MICROSERVICE-------------------------
# Create a new post
echo "Creating post...."
curl --location --request POST 'http://localhost:2015/posts/api/v1/resources/post/create_post' \
--header 'Content-Type: application/json' \
--data-raw '{"community": "CSUF", "text": "Free candy on Tuesdays!", "title": "Life Hack", "url": "null", "username": "Bill"}' \
--write-out '%{http_code}\n'

# Create a new post
echo "Creating post...."
curl --location --request POST 'http://localhost:2015/posts/api/v1/resources/post/create_post' \
--header 'Content-Type: application/json' \
--data-raw '{"community": "CSUF", "text": "Hidden rabbit in the library", "title": "OMG", "url": "null", "username": "Sally"}' \
--write-out '%{http_code}\n'

# Create a new post
echo "Creating post...."
curl --location --request POST 'http://localhost:2015/posts/api/v1/resources/post/create_post' \
--header 'Content-Type: application/json' \
--data-raw '{"community": "Bleh", "text": "Sample", "title": "Sample", "url": "null", "username": "Meh"}' \
--write-out '%{http_code}\n'

# Create a new post
echo "Creating post...."
curl --location --request POST 'http://localhost:2015/posts/api/v1/resources/post/create_post' \
--header 'Content-Type: application/json' \
--data-raw '{"community": "Blue", "text": "It is a color.", "title": "Colors Man", "url": "null", "username": "Rick"}' \
--write-out '%{http_code}\n'

#Delete an existing post
echo "Deleting postId = 3...."
curl --location --request DELETE 'http://localhost:2015/posts/api/v1/resources/post/delete_post' \
--header 'Content-Type: application/json' \
--data-raw '{"postId": "3"}' \
--write-out '%{http_code}\n'

#Retrieve an existing post
echo "Retrieving postId = 2...."
curl --location --request GET 'http://localhost:2015/posts/api/v1/resources/post/retrieve_post' \
--header 'Content-Type: application/json' \
--data-raw '{"postId": "2"}' \
--write-out '%{http_code}\n'

#List the n most recent posts to a particular community
echo "Listing 2 posts from the Computer community...."
curl --location --request GET 'http://localhost:2015/posts/api/v1/resources/post/listNthToACommunity' \
--header 'Content-Type: application/json' \
--data-raw '{"nth": 2,"community": "Computer"}' \
--write-out '%{http_code}\n'

#List the n most recent posts to any community
echo "Listing 3 posts from all communities...."
curl --location --request GET 'http://localhost:2015/posts/api/v1/resources/post/listNthToAny' \
--header 'Content-Type: application/json' \
--data-raw '{"nth": 3}' \
--write-out '%{http_code}\n'


# ------------------MESSAGING MICROSERVICE-------------------------
#send message
echo "Sending message...."
curl --location --request POST 	'http://localhost:2015/messages/api/v1/resources/message' \
--header 'Content-Type: application/json' \
--data-raw '{"userto":"ben","userfrom":"rick","messagecontents":"Boo!", "messageflag":"favorite"}' \
--write-out '%{http_code}\n'

echo "Sending message...."
curl --location --request POST 	'http://localhost:2015/messages/api/v1/resources/message' \
--header 'Content-Type: application/json' \
--data-raw '{"userto":"rey","userfrom":"kylo","messagecontents":"hello rey :)", "messageflag":"discussion"}' \
--write-out '%{http_code}\n'

echo "Sending message...."
curl --location --request POST 	'http://localhost:2015/messages/api/v1/resources/message' \
--header 'Content-Type: application/json' \
--data-raw '{"userto":"rey","userfrom":"jeff","messagecontents":"Yo.", "messageflag":"discussion"}' \
--write-out '%{http_code}\n'

#show favorite messages
echo "Showing favorite messages...."
curl --location --request GET 	'http://localhost:2015/messages/api/v1/resources/message/favorite' \
--header 'Content-Type: application/json' \
--data-raw '{"messageflag":"favorite"}' \
--write-out '%{http_code}\n'

#delete message
echo "Deleting message...."
curl --location --request DELETE 	'http://localhost:2015/messages/api/v1/resources/message/delete' \
--header 'Content-Type: application/json' \
--data-raw '{"messageid":"2"}' \
--write-out '%{http_code}\n'

# ------------------VOTING MICROSERVICE-------------------------
# Upvote a post
echo "Upvoting post...."
curl --location --request PUT 'http://localhost:2015/votes/api/v1/resources/post/upvote' \
--header 'Content-Type: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{"postId": "1"}'

# Downvote a post
echo "Downvoting post...."
curl --location --request PUT 'http://localhost:2015/votes/api/v1/resources/post/downvote' \
--header 'Content-Type: application/json' \
--data-raw '{"postId": "1"}' \
--write-out '%{http_code}\n'


# Report the number of upvotes and downvotes for a post
echo "Retrieving post score...."
curl --location --request GET 'http://localhost:2015/votes/api/v1/resources/post/retrieve_vote' \
--header 'Content-Type: application/json' \
--data-raw '{"postId": "1"}' \
--write-out '%{http_code}\n'

# List the n top-scoring posts to any community
echo "Retrieving top scored posts...."
curl --location --request GET 'http://localhost:2015/votes/api/v1/resources/post/topNthScore' \
--header 'Content-Type: application/json' \
--data-raw '{"nth": 3}' \
--write-out '%{http_code}\n'

# Given a list of post identifiers, return the list sorted by score.
echo "Retrieving post with identifiers...."
curl --location --request GET 'http://localhost:2015/votes/api/v1/resources/post/sortedByScore' \
--header 'Content-Type: application/json' \
--data-raw '{"list":"1,2"}' \
--write-out '%{http_code}\n'

