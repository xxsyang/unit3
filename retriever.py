import datasets
from langchain_core.documents import Document
from langchain_community.retrievers import BM25Retriever
from smolagents import Tool

# 1. Load your local dataset from the 'data' folder
guest_dataset = datasets.load_dataset(
    "parquet", 
    data_files="data/train-00000-of-00001.parquet", 
    split="train"
)

# 2. Format the documents
docs = [
    Document(
        page_content="\n".join([
            f"Name: {guest.get('name', 'Unknown')}",
            f"Relation: {guest.get('relation', 'Unknown')}",
            f"Description: {guest.get('description', 'No description available.')}",
            f"Email Address: {guest.get('email', 'No email available.')}"
        ])
    ) for guest in guest_dataset
]

retriever = BM25Retriever.from_documents(docs)

# 3. Define the tool class that app.py is looking for!
class GuestInfoRetrieverTool(Tool):
    name = "guest_info_retriever"
    description = "Retrieves detailed information about gala guests based on their name or relation."
    inputs = {
        "query": {
            "type": "string",
            "description": "The name or relation of the guest to search for."
        }
    }
    output_type = "string"

    def forward(self, query: str) -> str:
        docs = retriever.invoke(query)
        return "\n\n".join([doc.page_content for doc in docs])