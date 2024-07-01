# pydantic 

"""
Pydantic is a data validation and settings management library using Python type annotations. 
It enforces type hints at runtime and provides user-friendly error messages
"""

from pydantic import BaseModel, ValidationError

class User(BaseModel):
    id: int
    name: str
    email: str


#valid examples
try:
    user = User(id=1, name='John Doe', email='john.doe@example.com')
    print(user)
except ValidationError as e:
    print(e)

#invalid examples
try:
    user = User(id='one', name=123, email='not-an-email')
except ValidationError as e:
    print(e)



# another one is SonarLint
# install SonarLint
# SonarLint runs in the background of your IDE, 
# so you don’t need to write code specifically for it. 

# def add(a, b):
#     return a + b

# result = add(1, '2')