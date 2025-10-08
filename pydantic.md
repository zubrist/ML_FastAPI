### What is Pydantic?
Pydantic is a data validation and settings management library for Python, built on top of type annotations. It allows you to define data models with type hints, and it automatically validates and parses the data according to the specified types. Pydantic is widely used in FastAPI for request and response validation.

### Why we need Pydantic?
Pydantic is essential in FastAPI for several reasons:
1. type Validation: Pydantic ensures that the data received in requests conforms to the expected types and formats, reducing the risk of errors and inconsistencies.
For example : 
```python
class Item(BaseModel):
    name: str
    price: float = Field(..., gt=0, description="The price must be greater than zero")
    is_offer: bool = None
```
2. data validation: Pydantic provides built-in validation mechanisms, such as constraints on string lengths, numeric ranges, and regex patterns, making it easy to enforce data integrity.
for example:

```python   
class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr # EmailStr is a pydantic type for email validation that ensures the value is a valid email address
    age: int = Field(..., ge=18, le=100)
```


## Pydantic works in three main steps:
1. **Model Definition**: You define a Pydantic model by creating a class that inherits from `BaseModel` that represents the ideal schema of the data.
   You specify the `fields` and their `types` and any `validation constraints` using Pydantic's `Field` function.

2. **Data Parsing**: When you receive data (e.g., from an HTTP request) usually in JSON format, we create an instance of the Pydantic model by passing the data to the model's constructor. Pydantic automatically validates the data and converts it to the specified types.

3. **Passing Validated Data**: If the data is valid, you can access the validated data through the model instance. If the data is invalid, Pydantic raises a `ValidationError`, which you can handle to return appropriate error responses.