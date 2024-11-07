import setup
from llama_index.core import VectorStoreIndex

def query(query: str):
    index = VectorStoreIndex.from_vector_store(vector_store=setup.store)
    query_engine = index.as_query_engine()
    return query_engine.query(query)


file = open("test/test.txt", "r")
content = file.read()

response = query(
    """
    You are acting on behalf of the Gambling Commission of the United Kingdom. 
    You need to go through that content and analyse if any of the sections, words, 
    images or more break any rules or laws. 
    Go through the content find what should not be there and report why. 
    You can also suggest what should be there instead.

    Here is the content: {}
    """.format(content))
file.close()

print(response)