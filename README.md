# flask-messages-api

API backend system for handling messages between users.

API Server : https://abra-messages-api.herokuapp.com/ <br>
Postman documentation : https://documenter.getpostman.com/view/14762526/UUxz9Sw3

# Getting started

- In order to achieve the functionality of the API, you must first:
  <br>1. sign-up using '/sign-up' endpoint.
  <br>2. login using POST '/login' endpoint.
- Then, all requests will be performed for the logged-in user.

# Registered users

- User 1 : email : "yehuda@gmail.com" , password: "1234567"
- User 2 : email : "yuval@gmail.com" , password: "12345678"

# API Requests

API capabilities:

- Sign up user.
- Login user.
- Retrieve logged in user.
- logout.
- Post message.
- Retrieve user's sent messages.
- Read message - Mark message status as 'read' .
- Unread message - Mark message status as 'unread' .
- Retrieve message - Retrieve message data.
- Retrieve user's received messages
- Retrieve user's unread messages.
- Retrieve user's read messages.
- Delete message.

<br><br> Please note the request to delete a message:<br>

- If the DELETE request is sent by the user who received the message, the message will be deleted only for him.<br>
- If the DELETE request is sent by the user who sent the message, the message will be deleted both for him and for the
  user who received the message.