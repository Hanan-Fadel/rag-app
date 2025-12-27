from .BaseDataModel import BaseDataModel
from .db_schemas import Project
from .enums.DatabaseEnum import DatabaseEnum

class ProjectModel(BaseDataModel):
    def __init__(self, db_client: object):
        super().__init__(db_client=db_client)
        self.collection = self.db_client[DatabaseEnum.COLLECTION_PROJECT_NAME.value]

    async def create_project(self, project: Project):
        result = await self.collection.insert_one(project.dict(by_alias=True, exclude_unset=True))
        project._id = result.inserted_id

        if not result.inserted_id:
            raise Exception("Failed to create project")

        return project
    
    async def get_project_or_create_one(self, project_id: str):
        record = await self.collection.find_one({"project_id": project_id})

        if record is None:
            # create a new project
            project = Project(project_id=project_id) 
            project = await self.create_project(project=project)

            return project
        
        return Project(**record) #convert the record (dictionary) to a Project object

    async def get_all_projects(self, page: int = 1, page_size: int = 10):
        #count the total number of documents in the collection
        total_documants = await self.collection.count_documents({})
        total_pages = total_documants // page_size
        if total_documants % page_size > 0:
            total_pages += 1
        cursor = self.collection.find({}).skip((page - 1) * page_size).limit(page_size)
        
        projects =[]

        async for document in cursor:
            projects.append(Project(**document))
        
        return projects, total_pages
