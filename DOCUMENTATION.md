
Documentation for REST API  
Flask User Management App

This documentation provides details on how to use the Flask User Management API. This API allows you to create, retrieve, update, and delete user records in a SQLite database.

Base URL
________
The base URL for all API endpoints is:

https://restapi-1.mubaraquthman.repl.co

Endpoints:

To create a New User
_______________________
Endpoint: POST /api/user/<name>

Create a new user with the provided name.
Request:
<name> (string, required): The name of the user to be created.

POST /api/user/Alice
Response:
Status Code: 201 Created
JSON Response Body:
{
    "message": "User created successfully"
}


Fetch All Users:
_______________________
Endpoint: GET /api/users
Retrieve a list of all users in the database.

Request: None
Example Request:
GET /api/users

Response:
Status Code: 200 OK
JSON Response Body: An array of user objects, where each user object has the following format:
{
    "id": 1,
    "name": "Ramon"
}

Retrieve a Specific User by Name
________________________________
Endpoint: GET /api/user/<name>

Request:
<name> (string, required): The name of the user to retrieve.
Example Request:
GET /api/user/Ramon

Response:
Status Code: 200 OK
JSON Response Body: The user object with the specified name, in the following format:
{
    "id": 1,
    "name": "Ramon"
}

Status Code: 404 Not Found (if the user with the specified name does not exist)
JSON Response Body:
{
    "message": "User not found"
}

Update a Specific User by Name
______________________________
Endpoint: PUT /api/user/<name>
Request:
<name> (string, required): The name of the user to update.

Request Body (JSON):
new_name (string, required): The new name for the user.

Example Request:
PUT /api/user/Ramon

Request Body:
{
    "new_name": "Tinubu"
}

Response:

Status Code: 200 OK

JSON Response Body:
{
    "message": "User updated successfully"
}

Status Code: 400 Bad Request (if the new_name is not a valid string)
JSON Response Body:
{
    "error": "New name should be a valid string"
}

Status Code: 404 Not Found (if the user with the specified name does not exist)

JSON Response Body:
{
    "message": "User not found"
}

Delete a Specific User by Name
______________________________
Endpoint: DELETE /api/user/<name>

Request:
<name> (string, required): The name of the user to delete.

Example Request:
DELETE /api/user/Ramon

Response:
Status Code: 200 OK

JSON Response Body:
json
Copy code
{
    "message": "User deleted successfully"
}

Status Code: 404 Not Found (if the user with the specified name does not exist)
JSON Response Body:
json
Copy code
{
    "message": "User not found"
}

Error Handling
_______________
If a request is made with an invalid name (not a valid string), the API will respond with a 400 Bad Request error and provide an error message in the response body.

If a request is made for a user that does not exist, the API will respond with a 404 Not Found error and provide an error message in the response body.

Running the API
To run the REST API, execute the following command:

python app.py
By default, the API will run on http://localhost:5000 with debugging enabled (debug=True). Make sure to change the configuration settings (e.g., database URI) as needed for your deployment environment.

Conclusion
___________
This documentation provides comprehensive information on how to use the Flask User Management API to perform CRUD operations on user records. Use the provided endpoints to interact with the API and manage user data in the SQLite database.