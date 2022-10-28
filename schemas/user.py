def userEntity(item) -> dict:
    return {
        "id":item["_id"],
        "phone":item["phone"],
        "name":item["name"],
        "email":item["email"],
        "password":item["password"],
        "IsActive":item["isActive"],
        "Aadhar":item["AAdhar"],
        "Pan":item["Pan"],
        "GstNo":item["GstNo"],
        "isValidate":item["IsValidate"]

    }
def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]
#Best way
def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}
def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]