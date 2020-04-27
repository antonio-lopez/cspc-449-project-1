# Upvote a post
echo "Upvoting post...."
curl --location --request PUT 'http://127.0.0.1:5000/api/v1/resources/post/upvote' \
--header 'Content-Type: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{"postId": "2"}'

# Downvote a post
echo "Downvoting post...."
curl --location --request PUT 'http://127.0.0.1:5000/api/v1/resources/post/downvote' \
--header 'Content-Type: application/json' \
--data-raw '{"postId": "3"}' \
--write-out '%{http_code}\n'


# Report the number of upvotes and downvotes for a post
echo "Retrieving post score...."
curl --location --request GET 'http://127.0.0.1:5000/api/v1/resources/post/retrieve_vote' \
--header 'Content-Type: application/json' \
--data-raw '{"postId": "3"}' \
--write-out '%{http_code}\n'

# List the n top-scoring posts to any community
echo "Retrieving top scored posts...."
curl --location --request GET 'http://127.0.0.1:5000/api/v1/resources/post/topNthScore' \
--header 'Content-Type: application/json' \
--data-raw '{"nth": 4}' \
--write-out '%{http_code}\n'

# Given a list of post identifiers, return the list sorted by score.
echo "Retrieving post with identifiers...."
curl --location --request GET 'http://127.0.0.1:5000/api/v1/resources/post/sortedByScore' \
--header 'Content-Type: application/json' \
--data-raw '{"list":"1,3,7"}' \
--write-out '%{http_code}\n'

