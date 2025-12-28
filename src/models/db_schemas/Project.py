from pydantic import BaseModel, Field, validator
from typing import Optional
from bson.objectid import ObjectId


class Project(BaseModel):
    id: Optional[ObjectId] = Field(None, alias="_id")
    project_id: str = Field(..., min_length=1)

    @validator('project_id') #custom validator on the schema
    def validate_project_id(cls, value):
        if not value.isalnum(): #project id should be alphanumeric
            raise ValueError("Project ID should be alphanumeric")
        return value

    class Config:
        arbitrary_types_allowed = True  #allow to use ObjectId in the schema as a field type

    @classmethod #static method
    def get_indexes(cls):
        return [
            {
                "key":[
                    ("project_id", 1)
                ],
                "name": "project_id_index_1",
                "unique": True, #unique index on the project_id field
            }
        ]
