# Get auth_token

- Windows

Command:
`Invoke-WebRequest -Uri 'http://localhost:8000/api/auth/token/login/' -Method POST -Headers @{ 'Content-Type' = 'application/json' } -Body(@{ 'username' = 'YOUR_USER_NAME'; 'password' = 'PASSWORD' } | ConvertTo-Json)`

- Linux

Command:
`Invoke-WebRequest -Uri 'http://localhost:8000/api/auth/token/login/' -Method POST -Headers @{ 'Content-Type' = 'application/json' } -Body(@{ 'username' = 'YOUR_USER_NAME'; 'password' = 'PASSWORD' } | ConvertTo-Json)`

Input YOUR_USER_NAME && Input PASSWORD

# GET method by auth_token

- Windows

Command:

`Invoke-WebRequest -Uri 'http://127.0.0.1:8000/api/v1/friends/' -Method GET -Headers @{ 'Authorization' = 'Token 6db0b45879b1f32167969e1d92128025e9a3c4bb' }`

- Linux

Command:

`curl -X GET http://127.0.0.1:8000/api/v1/friends/ -H 'Authorization: Token 6db0b45879b1f32167969e1d92128025e9a3c4bb'`

# [Get Back](https://github.com/Skivel/Tutorial_Django_REST_API/tree/Info)
