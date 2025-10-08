from pydantic import BaseModel, Field, field_validator, EmailStr , model_validator , computed_field
from typing import List, Dict, Annotated


class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str]  # list of strings
    contact_details: Dict[str, str]  # dictionary with string keys and string values


#patient_info = {"name": "John", "age": 30} # dictionary containing patient information

#patient_info= {"name": "Alice", "age": 'thirty'} # dictionary containing patient information
patient_info= {"name":"Zubrist", "age":25, "weight": 75.6, "married": False, "allergies":["dust", "Heat"], 
               "contact_details":{"email":"zubrist@gmail.com","phone":"7890xxxx89"}}

patient1= Patient(**patient_info) # unpacking the dictionary using ** operator to match the fields of the Pydantic model


# lets make a function to insert a patient
def insert_patient(patient:Patient):  # patient is of type Patient
    print(f"Inserting patient: {patient.name}, age: {patient.age}")
    print("Inserted successfully")


# lets test the function
#insert_patient(patient1)
insert_patient(patient1)# this will raise a validation error because age is not an integer



'''
by default all the fields in a Pydantic model are required. If you want to make a field optional, you can use the Optional type from the typing module.

'''
from typing import Optional

class PatientOptional(BaseModel):
    name: str
    age: Optional[int] = None  # age is now optional
    weight: Optional[float] = None  # weight is now optional
    married: Optional[bool] = None  # married is now optional
    allergies: Optional[List[str]] = []  # allergies is now optional
    contact_details: Optional[Dict[str, str]] = {}  # contact_details is now optional

    '''
    when we make a field Optional , we should give a default value None or empty value like [] or {}.
    '''


'''
While create a Pydantic model , we can also give default values to the fields.

'''    
class PatientDefault(BaseModel):
    name: str
    age: int = 30  # default age is 30
    weight: float = 70.0  # default weight is 70.0
    married: bool = False  # default married is False
    allergies: List[str] = []  # default allergies is empty list
    contact_details: Dict[str, str] = {"email": "example@example.com", "phone": "123-456-7890"}  # default contact_details


'''
Custom data validation using Field

'''    

class PatientCustom(BaseModel):
    weight: float = Field(..., gt=0, lt=60, description="Weight must be greater than 0 and less than 60", example=70.5)
    name : str = Field(..., max_length=10, description="Name must be less than 100 characters", example="John Doe")


patient_custom_info= {"weight": 75.6 ,"name":"AKHLAKH AHMED REJA "} # this will raise a validation error because weight is not in the range (0,60) and name is more than 10 characters
#patient_custom_info= {"weight": 55.6 ,"name":"AKHLAKH"} # this will pass the validation
# patient_custom= PatientCustom(**patient_custom_info)
# print(patient_custom)


'''
we also add metadata  to the fields using Field with Annotated
'''

class PatientMeta(BaseModel):
    name: Annotated[str,Field(..., max_length=10, title="name of the patients" ,description="Name must be less than 100 characters", example="John Doe")]
    #     Annotated[data_type , Field(..., constraints and metadata)] , ... represents required field
   
    # we also can add default value instead of ...
    married: Annotated[bool, Field(default=False, title="marital status", description="Marital status of the patient", example=False/True)]
   
    weight: Annotated[float, Field(..., gt=0, lt=300, title="weight of the patient", description="Weight must be greater than 0 and less than 300", example=70.5)]
    # pydantic is smart enough that even if we send weight as string it will convert it to float if possible
    # but we may not want this behavior , we can use strict=True in Field to enforce strict type checking
    weight_strict: Annotated[float, Field(gt=0, lt=300, strict=True, title="strict weight of the patient", description="Weight must be greater than 0 and less than 300 and must be of type float", example=70.5)]


patient_meta_info= {"weight": 75.6 ,"name":"AKHLAKH", "married": False, "weight_strict": "85.6"} # this will raise a validation error because weight_strict is not of type float
#patient_meta_info= {"weight": 55.6 ,"name":"AKHLAKH", "married": False, "weight_strict": 85.6} # this will pass the validation
# patient_meta= PatientMeta(**patient_meta_info)
# print(patient_meta)



'''
Field Validator 

When we need to do some custom validation that is not covered by the built-in validators, we can use the @validator decorator.
for example , we want to check if the email has hdfc.com/icici.com domain


'''

class PatientValidator(BaseModel):
    name: str = Field(..., description="Name of the patient", example="John Doe")
    email:EmailStr


    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        
        valid_domains= ["hdfc.com", "icici.com"]
        #abc@gmail.com
        domain_name = value.split('@')[-1]

        # now checking

        if domain_name not in valid_domains:
            raise ValueError(f"Email domain must be one of {valid_domains}")
        
        return value 

#patient_validator_info= {"name":"Zubrist", "email":"zubrist@gmail.com"} # this will raise a validation error because email domain is not in the valid domains
patient_validator_info= {"name":"Zubrist", "email":"zubrist@hdfc.com"} # this will pass the validation
patient_validator= PatientValidator(**patient_validator_info)
print(patient_validator)


'''
field validator works on two modees : before and after
by default it works in after mode , which means the validation is done after the built-in validation is done.
if we want to do the validation before the built-in validation, we can use mode='before' in the decorator 

import field_validator from pydantic
'''


'''
model validator

suppose we want to validate two fields together , for example we want to check if the age is greater than 18 if the patient is married

'''

class PatientModelValidator(BaseModel):
    name: str = Field(..., description="Name of the patient", example="John Doe")
    age: int = Field(..., gt=0, lt=120, description="Age must be between 0 and 120", example=30)
    married: bool = Field(..., description="Marital status of the patient", example=False)
    contact_details: Dict[str,str] = Field(..., description="Contact details of the patient", example={"email":"john.doe@example.com", "phone":"1234567890"})

    @model_validator(mode='after') # we dont need to specify the field name here as we are validating multiple fields together
    @classmethod
    def check_age_if_married(cls, model):
        age = model.age
        married = model.married

        if married and age < 18:
            raise ValueError("Age must be greater than 18 if the patient is married")


        
        return model
    
    @model_validator(mode='after')
    @classmethod
    def validate_emergency_contact(cls,model):

        if model.age > 60 and 'emergency_contact' not in model.contact_details:
            raise ValueError("Emergency contact is required for patients above 60 years old")
        return model
    

 # lets test the model validator
#patient_model_validator_info= {"name":"Zubrist", "age":65, "married": True, "contact_details":{"email":"zubrist@gmail.com", "phone":"1234567890"}} # this will raise a validation error because age is less than 18 and married is True
patient_model_validator_info= {"name":"Zubrist", "age":25, "married": True, "contact_details":{"email":"zubrist@gmail.com", "phone":"1234567890", "emergency_contact":"9876543210"}}
patient_model_validator= PatientModelValidator(**patient_model_validator_info)
print(patient_model_validator)




'''
computed Field 
sometimes we want to compute a field based on other fields , for example we want to compute the bmi based on weight and height
 for that we need to import computed_field from pydantic
'''


class PatientComputedField(BaseModel):
    name: str = Field(..., description="Name of the patient", example="John Doe")
    weight: float = Field(..., gt=0, lt=300, description="Weight must be greater than 0 and less than 300", example=70.5) # in kg
    height: float = Field(..., gt=0, lt=3, description="Height must be greater than 0 and less than 3", example=1.75) # in meters

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    

# lets test the computed field
patient_computed_field_info= {"name":"Zubrist", "weight":75.6, "height":1.8}
patient_computed_field= PatientComputedField(**patient_computed_field_info)    
print(f"Patient BMI: {patient_computed_field.bmi}")



'''
NESTED MODELS

what ? -> we can have a model inside another model 

how ? -> we can define a model as a field in another model

why ? -> this is useful for representing complex data structures
'''

class Address(BaseModel):
    street: str = Field(..., description="Street address", example="123 Main St")
    city: str = Field(..., description="City", example="Anytown")
    state: str = Field(..., description="State", example="CA")
    zip_code: str = Field(..., description="ZIP code", example="12345")

class PatientNestedModel(BaseModel):
    name: str = Field(..., description="Name of the patient", example="John Doe")
    age: int = Field(..., gt=0, lt=120, description="Age must be between 0 and 120", example=30)
    address: Address  # nested model

# creating object of Address pydantic model
address_info= {"street":"123 Main St", "city":"Anytown", "state":"CA", "zip_code":"12345"}
addressX= Address(**address_info)

# creating object of PatientNestedModel pydantic model
patient_info= {"name":"John Doe", "age":30, "address": addressX}
patient= PatientNestedModel(**patient_info)

print(patient)
print(patient.address.city)  # accessing nested model field
print(patient.address.zip_code)  # accessing nested model field




'''
Serialization of pydantic models

'''

type1 =patient.model_dump() # returns a dictionary
print(type(type1))
print(type1)


type2= patient.model_dump_json() # returns a json string
print(type(type2))
print(type2)

# pydantic aslo give controls of what to include/exclude in the serialization
type3= patient.model_dump(include={'name','age'}) # include only name and age
print(type3)

type4= patient.model_dump(exclude={'age'}) # exclude age
print(type4)