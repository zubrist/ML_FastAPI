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