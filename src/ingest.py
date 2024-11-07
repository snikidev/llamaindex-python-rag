import setup
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import StorageContext


def ingest():
    documents = SimpleDirectoryReader("data").load_data()
    storage_context = StorageContext.from_defaults(vector_store=setup.store)
    VectorStoreIndex.from_documents(
        documents,
        # TODO: add custom metadata to the documents, e.g. title
        transformations=[SentenceSplitter(chunk_size=1024, chunk_overlap=20)],
        storage_context=storage_context
    )


ingest()
