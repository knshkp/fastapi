from pydantic import BaseModel
class User(BaseModel):
    name:str
    email:str
    password:str
    phone:int
    IsActive:bool
    Aadhar:int
    Pan:str
    GstNo:str
    isValidate:bool


