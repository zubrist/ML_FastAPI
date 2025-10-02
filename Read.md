## What is API ?

APIs are mechanisms that allow different software applications ( such as frontend and backend ) to communicate with each other. They define a set of rules and protocols( HTTP, REST, GraphQL, etc. ) for how data should be exchanged between systems, enabling them to work together seamlessly. APIs can be used for various purposes, such as accessing data from a web service, integrating with third-party applications, or building complex software systems.

```bash
+-----------------+                    +-----------------+
|   Frontend      | >-- Request--->    |    Backend      |
+-----------------+                    +-----------------+
|  User Interface | <--- Response---<  |  API Endpoints  |
+-----------------+      API           +-----------------+
```
```bash
Analogy

+-----------------+                    +-----------------+
|   Restaurant    | >-- Order--->      |    Kitchen      |
+-----------------+                    +-----------------+
|  Customer       | <--- Food--------< |  Chef           |
+-----------------+     Waiter         +-----------------+
``` 

## why API needed ?
> lets talk about pre-API era ..

Before APIs, software applications were often built as monolithic systems, where all components were tightly integrated and interdependent. This made it difficult to update or modify individual parts of the system without affecting the entire application. Additionally, integrating with third-party services or accessing external data sources was often a complex and time-consuming process.

> Problems with monolithic systems:
1. **Tight Coupling**: Components within a monolithic application are tightly coupled, making it difficult to change or update one part without affecting others.
2. **Scalability Issues**: Scaling a monolithic application can be challenging, as the entire application must be scaled together, even if only one component requires additional resources.
3. **Limited Flexibility**: Monolithic systems often lack the flexibility to integrate with new technologies or services, making it difficult to adapt to changing business needs.
4. **Slower Development Cycles**: The complexity of monolithic systems can lead to longer development cycles, as changes must be carefully coordinated and tested across the entire application.
5. **Difficult Maintenance**: Maintaining and updating a monolithic application can be cumbersome, as even small changes may require extensive testing and deployment processes.

Now lets take IRCTC as an example which uses monolithic architecture , but now many other ticket booking platforms like MakemyTrip, Yatra, Goibibo wants to know the trains between two stations so they can provide the same service to their users. So how can they do that ?
> Solution : IRCTC has to somehow provide access of their database where the information of trains between those two stations is stored . But this is not possible as it can lead to security issues and also IRCTC will not want to share their database with other platforms. So the solution to this problem is API. IRCTC can create an API which will provide the information of trains between two stations and other platforms can use this API to get the required information without having access to the database.

For this IRCTC has to decoupled thier monolithic architecture , they developed a separate backend service which will handle all the requests from other platforms and provide the required information. This backend service is called API service. Now other platforms can send requests to this API service and get the required information without having access to the database.


# API - ML Perspective
In the context of Machine Learning (ML), APIs play a crucial role in deploying and serving ML models. Once a machine learning model is trained and validated, it needs to be integrated into applications or services so that it can be used to make predictions on new data. This is where APIs come into play.
APIs provide a standardized way for applications to interact with the ML model, allowing them to send input data and receive predictions in return. This enables seamless integration of ML models into various applications, such as web apps, mobile apps, or other backend services.


## Why FastAPI 
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints. Here are some reasons why FastAPI is a great choice for building web applications and APIs:
1. **High Performance**: FastAPI is one of the fastest Python web frameworks available, thanks to its use of asynchronous programming and the Starlette framework. It can handle a large number of requests per second, making it suitable for high-performance applications.
2. **Easy to Use**: FastAPI is designed to be easy to use and learn. It has a simple and intuitive syntax that allows developers to quickly create APIs with minimal boilerplate code.
3. **Automatic Documentation**: FastAPI automatically generates interactive API documentation using Swagger UI and Redoc. This makes it easy for developers to explore and test the API endpoints.
4. **Type Hints and Validation**: FastAPI leverages Python's type hints to provide automatic request validation and serialization. This helps catch errors early and ensures that the data being processed is in the expected format.
5. **Dependency Injection**: FastAPI has a built-in dependency injection system that makes it easy to manage and reuse components such as database connections, authentication, and other services.
6. **Asynchronous Support**: FastAPI fully supports asynchronous programming, allowing developers to write non-blocking code that can handle multiple requests concurrently. This is particularly useful for I/O-bound operations such as database queries and external API calls.
7. **Extensibility**: FastAPI is highly extensible and can be easily integrated with other libraries and frameworks. It supports middleware, custom request/response handling, and third-party plugins.
8. **Community and Ecosystem**: FastAPI has a growing community and a rich ecosystem of libraries and tools that can be used to enhance its functionality. This includes support for databases, authentication, testing, and more.
9. **Production Ready**: FastAPI is designed to be production-ready out of the box. It includes features such as automatic HTTPS, CORS support, and security best practices.
10. **Great for Microservices**: FastAPI's lightweight nature and high performance make it an excellent choice for building microservices and serverless applications. Its modular design allows developers to create small, focused services that can be easily deployed and scaled. 



## Fundamentals of FastAPI 
FastAPI is built upon two famous Python libraries: Starlette and Pydantic.
1. **Starlette**: Starlette is a lightweight ASGI (Asynchronous Server Gateway Interface) framework that provides the core functionality for building web applications and APIs. It handles routing, middleware, request/response handling, and other essential web features. FastAPI leverages Starlette's capabilities to provide a high-performance and asynchronous web framework.
2. **Pydantic**: Pydantic is a data validation and settings management library that uses Python type annotations. It allows developers to define data models with type hints, and it automatically validates and serializes data based on these models. FastAPI uses Pydantic to handle request and response data validation, ensuring that the data being processed is in the expected format.


## Philosophy of FastAPI
>> what was missing in other frameworks ? 
- **performance** : Other frameworks like Flask and Django are synchronous in nature, which can lead to performance bottlenecks when handling a large number of concurrent requests. 
- **unnecessary boilerplate code** : Other frameworks often require a lot of boilerplate code to set up routes, handle requests, and validate data. This can lead to longer development times and increased complexity.

>> What FastAPI offers ?

- **Fast to Run** : FastAPI is designed to be fast to run, with minimal overhead. This makes it suitable for building high-performance applications that require low latency and high throughput.
- **Fast to Code** : FastAPI is designed to be easy to use and learn, with a simple and intuitive syntax. This allows developers to quickly create APIs with minimal boilerplate code, reducing development time and complexity.


### Why FastAPI is fast to Run ?

>> Scenario :

``` bash

+------------+
|  Client    |
+------------+
      |
      |  interacts             
      |                                
      |                         
      |                        
      |                         content-length: 12       
      v
+------------------+
|  Web Server      |        
+------------------+
      |                       the request is a HTTP request , which looks something like this
      |                         GET /items/ HTTP/1.1
      |                         Host: example.com
      |                         Content-Type: application/json 
      |  Request                Content-Length: 12
      |                         { "item_id": 123 }    
      v
+------------+
|  SGI       |              Now the server gateway interface (SGI ) converts the HTTP request into a Python dictionary so that
|            |             our python code can understand it.
+------------+             this looks something like this :
      |
      |                        Request.method = "GET"
      |                        Request.url = ".../items/"
      |                        Request.headers = { "Content-Type": "application/json", ... }
      |                        Request.json = { "item_id": 123 }
      |
      |
      v
+------------------+
|  API code        |          Now FastAPI takes this dictionary and maps it to the appropriate   API endpoint and function.
+------------------+         It also validates the input data using Pydantic models, ensuring that the data is in the expected
      |                       format.
      |
      |
      |                        def get_item(item_id: int):
      |                            # process the request
      |                            return { "item_id": item_id, "name": "Item Name" }
      |
      v
+------------+
|  SGI       |              After processing the request, the API code returns a response dictionary, which looks something like
|            |             this :
|            |             Response.status_code = 200
|            |             Response.headers = { "Content-Type": "application/json", ... }
|            |             Response.json = { "item_id": 123, "name": "Item Name" }
+------------+
      |
      |                        The SGI then converts this response dictionary back into an HTTP response format that can be sent
      |                        back to  the client.
      |
      v 
+------------------+
|  Web Server      |          This looks something like this :
+------------------+         HTTP/1.1 200 OK
      |                       Content-Type: application/json
      |                       Content-Length: 34
      |                       
      |                       { "item_id": 123, "name": "Item Name" }
      |
      v 
+------------+
|  Client    |              Finally, the web server sends the HTTP response back to the client
+------------+
```



### comparing with Flask

- **Flask** has the same flow as above but the SGI used by Flask is WSGI (Web Server Gateway Interface) which is synchronous in nature. This means that it can only handle one request at a time, which can lead to performance bottlenecks when handling a large number of concurrent requests. This is because WSGI uses a thread-based model, where each request is handled by a separate thread. When a thread is blocked (for example, waiting for a database query to complete), it cannot handle any other requests until it is unblocked. This can lead to a situation where many threads are blocked, causing the server to become unresponsive.
    - Flask uses `werkzeug` library for WSGI implementation. It uses `Gunicorn` or `uWSGI` as the production server.

- **FastAPI** uses ASGI (Asynchronous Server Gateway Interface) which is asynchronous in nature. This means that it can handle multiple requests concurrently, even when some of them are blocked. This is because ASGI uses an event loop model, where a single thread can handle multiple requests by switching between them when they are blocked. This allows the server to remain responsive even when handling a large number of concurrent requests.
    - FastAPI uses the `Starlette` library for ASGI implementation. It uses `Uvicorn` or Hypercorn as the production server.      
    - FastAPI supports asynchronous programming using `async` and `await` keywords, allowing developers to write non-blocking code that can handle multiple requests concurrently. This is particularly useful for I/O-bound operations such as database queries and external API calls.


### Why FastAPI is fast to Code ?
- **Automatic Data Validation** : FastAPI uses `Pydantic` models to automatically validate and serialize request and response data based on Python type hints. This means that developers do not have to write custom validation code, reducing boilerplate and potential errors.    
- **Automatic Interactive Documentation** : FastAPI **automatically** generates **interactive** API documentation using `Swagger UI` and `Redoc`. This allows developers to explore and test API endpoints without having to write separate documentation or testing code.
- **Dependency Injection** : FastAPI has a built-in dependency injection system that makes it easy to manage and reuse components such as database connections, authentication, and other services. This reduces boilerplate code and improves code organization.
- **Seamless Integration** : It seamlessly integrated with modern Ecosystem like ML/DL libraries ( TensorFlow, PyTorch, Scikit-learn ), OAuth2, JWT authentication, databases ( SQLAlchemy, Tortoise-ORM ), Docker , Kuberneres and more .  This allows developers to quickly add functionality to their applications without having to write custom integration code.