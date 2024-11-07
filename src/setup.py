import os
import pymongo
import logging
import sys
from dotenv import load_dotenv
from llama_index.llms.azure_openai import AzureOpenAI
from llama_index.embeddings.azure_openai import AzureOpenAIEmbedding
from llama_index.core import Settings
from llama_index.vector_stores.azurecosmosmongo import (
    AzureCosmosDBMongoDBVectorSearch,
)


load_dotenv()


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


Settings.llm = AzureOpenAI(
    engine="gpt-4o-mini",
    api_key=os.environ.get('AZURE_OPENAI_API_KEY'),
    azure_endpoint=os.environ.get('AZURE_OPENAI_ENDPOINT'),
    api_version="2024-05-01-preview",
)


Settings.embed_model = AzureOpenAIEmbedding(
    model="text-embedding-3-small",
    deployment_name="text-embedding-3-small",
    api_key=os.environ.get('AZURE_OPENAI_API_KEY'),
    azure_endpoint=os.environ.get('AZURE_OPENAI_EMBEDDING_ENDPOINT'),
    api_version='2023-05-15',
)


mongodb_client = pymongo.MongoClient(os.environ.get("AZURE_COSMOSDB_URI"))


store = AzureCosmosDBMongoDBVectorSearch(
    mongodb_client=mongodb_client,
     db_name="gambitai",
     collection_name="uk",
)