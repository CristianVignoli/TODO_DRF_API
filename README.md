# Vinhood TODO APIs

### Registration
- Request URL: /auth/register
- Request Type: POST
- Parameters:
	- username (String)
	- email (String)
	- password (String)
- Authentication: None

### Login
- Request URL: /auth/login
- Request Type: POST
- Parameters:
	- username (String)
	- password (String)
- Authentication: None

### Refresh JWT
- Request URL: /auth/refresh-token
- Request Type: POST
- Parameters:
	- refresh (String, the refresh JWT taken from the login API)
- Authentication: None

### Retrieve user's TODO list
- Request URL: /todo/list/
- Request Type: GET
- Parameters: None
- Authentication: JWT
- Available Queries:
	- ?ordering=value , where value could be:
		- title
		- -title
		- creation_date
		- -creation_date

### Create a new TODO item
- Request URL: /todo/list/
- Request Type: POST
- Parameters:
	- title (String)
	- description (String)
	- deadline (Date String, optional)
- Authentication: JWT

### Replace an existing TODO item
- Request URL: /todo/item/<int: pk>/ (URLs can also be acquired from the list)
- Request Type: PUT
- Parameters:
	- title (String)
	- description (String)
	- deadline (Date String, optional)
- Authentication: JWT

### Partial update an existing TODO item
- Request URL: /todo/item/<int: pk>/ (URLs can also be acquired from the list)
- Request Type: PATCH
- Parameters:
	- title (String, optional)
	- description (String, optional)
	- deadline (Date String, optional)
- Authentication: JWT

### Delete an existing TODO item
- Request URL: /todo/item/<int: pk>/ (URLs can also be acquired from the list)
- Request Type: DELETE
- Parameters: None
- Authentication: JWT

### One more note...
Some dangerous files (e.g. the .env file) are voluntarily left in the Git with the purpose
of allowing the reader to be easily independent in the application setup.