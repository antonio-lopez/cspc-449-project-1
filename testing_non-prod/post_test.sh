#Create a new post
echo "Creating post...."
curl --location --request POST 'http://127.0.0.1:5000/api/v1/resources/post/create_post' \
--header 'Content-Type: application/json' \
--data-raw '{"community": "Corona-19", "text": "Things are going better!", "title": "CoronaVirus", "url": "null", "username": "Zexin"}' \
--write-out '%{http_code}\n'

echo "Creating post...."
curl --location --request POST 'http://127.0.0.1:5000/api/v1/resources/post/create_post' \
--header 'Content-Type: application/json' \
--data-raw '{"community": "Computer", "text": "Computers are super cool!", "title": "Computer Status", "url": "null", "username": "Zexin2"}' \
--write-out '%{http_code}\n'

echo "Creating post...."
curl --location --request POST 'http://127.0.0.1:5000/api/v1/resources/post/create_post' \
--header 'Content-Type: application/json' \
--data-raw '{"community": "Computer", "text": "Are Macs good for coding?", "title": "Mac VS PC", "url": "null", "username": "Tony"}' \
--write-out '%{http_code}\n'

echo "Creating post...."
curl --location --request POST 'http://127.0.0.1:5000/api/v1/resources/post/create_post' \
--header 'Content-Type: application/json' \
--data-raw '{"community": "Computer", "text": "RGB is overhyped", "title": "RGB", "url": "null", "username": "Tom"}' \
--write-out '%{http_code}\n'

echo "Creating post...."
curl --location --request POST 'http://127.0.0.1:5000/api/v1/resources/post/create_post' \
--header 'Content-Type: application/json' \
--data-raw '{"community": "Web", "text": "Making a website is easy.", "title": "Websites", "url": "null", "username": "Bob"}' \
--write-out '%{http_code}\n'

echo "Creating post...."
curl --location --request POST 'http://127.0.0.1:5000/api/v1/resources/post/create_post' \
--header 'Content-Type: application/json' \
--data-raw '{"community": "Test", "text": "Testing", "title": "Testing", "url": "null", "username": "Tester"}' \
--write-out '%{http_code}\n'

echo "Creating post...."
curl --location --request POST 'http://127.0.0.1:5000/api/v1/resources/post/create_post' \
--header 'Content-Type: application/json' \
--data-raw '{"community": "Water", "text": "Drink lots of water fam.", "title": "Water Rules", "url": "null", "username": "Bill"}' \
--write-out '%{http_code}\n'

#Delete an existing post
echo "Deleting postId = 6...."
curl --location --request POST 'http://127.0.0.1:5000/api/v1/resources/post/delete_post' \
--header 'Content-Type: application/json' \
--data-raw '{"postId": "6"}' \
--write-out '%{http_code}\n'

#Retrieve an existing post
echo "Retrieving postId = 3...."
curl --location --request POST 'http://127.0.0.1:5000/api/v1/resources/post/retrieve_post' \
--header 'Content-Type: application/json' \
--data-raw '{"postId": "3"}' \
--write-out '%{http_code}\n'

#List the n most recent posts to a particular community
echo "Listing 2 posts from the Computer community...."
curl --location --request POST 'http://127.0.0.1:5000/api/v1/resources/post/listNthToACommunity' \
--header 'Content-Type: application/json' \
--data-raw '{"nth": 2,"community": "Computer"}' \
--write-out '%{http_code}\n'

#List the n most recent posts to any community
echo "Listing 5 posts from all communities...."
curl --location --request POST 'http://127.0.0.1:5000/api/v1/resources/post/listNthToAny' \
--header 'Content-Type: application/json' \
--data-raw '{"nth": 5}' \
--write-out '%{http_code}\n'
