### the Path() function
The `Path()` function is used to define and validate path parameters in FastAPI. It allows you to specify constraints and metadata for the parameters. 
like : Title, Description, Minimum and Maximum values, Regex patterns, Examples,  ge , le , gt,lt etc.



### HTTP status codes
HTTP status codes are 3-digit numbers that indicate the result of an client's  HTTP request. They are grouped into `five` categories:
- 1xx (Informational): Request received, continuing process.
- 2xx (Successful): The request was successfully received, understood, and accepted (e.g., 200 OK, 201 Created).
- 3xx (Redirection): Further action needs to be taken to complete the request (e.g., 301 Moved Permanently, 302 Found).
- 4xx (Client Error): The request contains bad syntax or cannot be fulfilled (e.g., 400 Bad Request, 404 Not Found).
- 5xx (Server Error): The server failed to fulfill a valid request (e.g., 500 Internal Server Error, 503 Service Unavailable).


>> commmonly used status codes:
- 200 OK: The request was successful, and the server returned the requested data.
- 201 Created: The request was successful, and a new resource was created.
- 204 No Content: The request was successful, but there is no content to return (typically used for DELETE operations).
- 400 Bad Request: The server could not understand the request due to invalid syntax.
- 401 Unauthorized: The client must authenticate itself to get the requested response.
- 403 Forbidden: The client does not have access rights to the content.
- 404 Not Found: The server can not find the requested resource.
- 500 Internal Server Error: The server has encountered a situation it doesn't know how to handle.
- 503 Service Unavailable: The server is not ready to handle the request (e.g., it is down for maintenance or overloaded).


### HTTPException class
The `HTTPException` class in FastAPI is used to raise HTTP exceptions with specific status codes and detail messages. It allows you to handle errors and return appropriate HTTP responses to the client.

Instead of returning a standard response, you can raise an `HTTPException` to indicate an error condition.
This is particularly useful for handling cases like 
 - resource not found (404), 
 - unauthorized access (401), or 
 - bad requests (400).



 ### Query Parameters 
Query parameters are `optional` key-value pairs that are appended to the URL after a question mark (?) to pass additional data to the server in a HHTP request . 
They are used to filter, sort, or paginate data in API requests. In FastAPI, you can define query parameters by adding function parameters to your endpoint functions.
example url: 
```bash
http://example.com/view/?sort_by=weight&order=desc&gender=F

```
In this example, `sort_by`, `order`, and `gender` are query parameters. You can access their values in your FastAPI endpoint function by defining them as function parameters with default values.
Each Parameter is optional and is a key-value pair. 
multiple query parameters can be included in a single URL, separated by the ampersand (&) symbol.

### Query() 
Query() is a function provided by FastAPI that allows you to define and validate query parameters in your API endpoints. It provides a way to specify metadata, constraints, and default values for query parameters.
You can use the `Query()` function to set properties such as:   
- Title                 ( displayed in the API documentation)
- Description           ( detailed explation in Swagger UI)
- Default value         ( Set a default value if the parameter is not provided)
- Min and max values    ( Set minimum and maximum values for numeric parameters)
- Regex                 ( Validate string parameters against regex patterns)
- Examples              ( Provide example values for query parameters)




