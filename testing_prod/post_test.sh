#create post
echo "Creating post...."
curl --location --request POST 'http://localhost:2015/posts/api/v1/resources/post/create_post' \
--header 'Content-Type: application/json' \
--data-raw '{"community": "Corona-19", "text": "Things are going better!", "title": "CoronaVirus", "url": "null", "username": "Zexin"}' \
--write-out '%{http_code}\n'

echo "Creating post...."
curl --location --request POST 'http://localhost:2015/posts/api/v1/resources/post/create_post' \
--header 'Content-Type: application/json' \
--data-raw '{"community": "Computer", "text": "Computers are super cool!", "title": "Computer Status", "url": "null", "username": "Zexin2"}' \
--write-out '%{http_code}\n'

echo "Creating post...."
curl --location --request POST 'http://localhost:2015/posts/api/v1/resources/post/create_post' \
--header 'Content-Type: application/json' \
--data-raw '{"community": "Computer", "text": "Are Macs good for coding?", "title": "Mac VS PC", "url": "null", "username": "Tony"}' \
--write-out '%{http_code}\n'

echo "Creating post...."
curl --location --request POST 'http://localhost:2015/posts/api/v1/resources/post/create_post' \
--header 'Content-Type: application/json' \
--data-raw '{"community": "Computer", "text": "RGB is overhyped", "title": "RGB", "url": "null", "username": "Tom"}' \
--write-out '%{http_code}\n'

echo "Creating post...."
curl --location --request POST 'http://localhost:2015/posts/api/v1/resources/post/create_post' \
--header 'Content-Type: application/json' \
--data-raw '{"community": "Web", "text": "Making a website is easy.", "title": "Websites", "url": "null", "username": "Bob"}' \
--write-out '%{http_code}\n'

echo "Creating post...."
curl --location --request POST 'http://localhost:2015/posts/api/v1/resources/post/create_post' \
--header 'Content-Type: application/json' \
--data-raw '{"community": "Test", "text": "Testing", "title": "Testing", "url": "null", "username": "Tester"}' \
--write-out '%{http_code}\n'

echo "Creating post...."
curl --location --request POST 'http://localhost:2015/posts/api/v1/resources/post/create_post' \
--header 'Content-Type: application/json' \
--data-raw '{"community": "Water", "text": "Drink lots of water fam.", "title": "Water Rules", "url": "null", "username": "Bill"}' \
--write-out '%{http_code}\n'

echo "Deleting postId = 6...."
curl --location --request DELETE 'http://localhost:2015/posts/api/v1/resources/post/delete_post' \
--header 'Content-Type: application/json' \
--data-raw '{"postId": "2"}' \
--write-out '%{http_code}\n'

echo "Retrieving postId = 3...."
curl --location --request GET 'http://localhost:2015/posts/api/v1/resources/post/retrieve_post' \
--header 'Content-Type: application/json' \
--data-raw '{"postId": "3"}' \
--write-out '%{http_code}\n'

echo "Listing 2 posts from the Computer community...."
curl --location --request GET 'http://localhost:2015/posts/api/v1/resources/post/listNthToACommunity' \
--header 'Content-Type: application/json' \
--data-raw '{"nth": 2,"community": "Computer"}' \
--write-out '%{http_code}\n'

echo "Listing 5 posts from all communities...."
curl --location --request GET 'http://localhost:2015/posts/api/v1/resources/post/listNthToAny' \
--header 'Content-Type: application/json' \
--data-raw '{"nth": 5}' \
--write-out '%{http_code}\n'

