Use Postman or any similar tool to test the implemented APIs:

User creation: Send a POST request to http://localhost:8000/users/ with the user data in the request body.
User deletion: Send a DELETE request to http://localhost:8000/users/<user_id>/.
User update: Send a PUT request to http://localhost:8000/users/<user_id>/ with the updated user data in the request body.
User login: Send a POST request to http://localhost:8000/login/ with the username and password in the request body.
Game creation: Send a POST request to http://localhost:8000/users/<user_id>/games/.
Get game board: Send a GET request to http://localhost:8000/games/<game_id>/board/.
Update game board: Send a PUT request to http://localhost:8000/games/<game_id>/board/ with the character to be appended in the request body.
List games: Send a GET request to http://localhost:8000/games/.
Note: Make sure to replace <user_id> and <game_id> with the actual user and game IDs in the URLs.