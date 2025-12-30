from fastapi import FastAPI
from routes import base, data
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings, Settings
from stores.llm.LLMProviderFactory import LLMProviderFactory

app_settings = get_settings()

app = FastAPI() 

mongo_client = AsyncIOMotorClient(app_settings.MONGODB_URL)
mongo_db = mongo_client[app_settings.MONGODB_DATABASE]

llm_provider_factory = LLMProviderFactory(app_settings)

#generation client
app.generation_client = llm_provider_factory.create(provider=app_settings.GENERATION_BACKEND)
app.generation_client.set_generation_model(model_id=app_settings.GENERATION_MODEL_ID)

#embedding client
app.embedding_client = llm_provider_factory.create(provider=app_settings.EMBEDDING_BACKEND)
app.embedding_client.set_embedding_model(model_id=app_settings.EMBEDDING_MODEL_ID, embedding_size=app_settings.EMBEDDING_MODEL_SIZE)

async def startup_db_client():
    app.mongo_conn = AsyncIOMotorClient(app_settings.MONGODB_URL)
    app.db_client = app.mongo_conn[app_settings.MONGODB_DATABASE]

async def shutdown_db_client():
   app.mongo_conn.close()

@app.on_event("startup")
async def startup_event():
    await startup_db_client()

@app.on_event("shutdown")
async def shutdown_event():
    await shutdown_db_client()

app.include_router(base.base_router)
app.include_router(data.data_router)