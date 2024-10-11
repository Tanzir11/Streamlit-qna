from langchain_community.vectorstores.azure_cosmos_db import (
    AzureCosmosDBVectorSearch,
    CosmosDBSimilarityType,
    # CosmosDBVectorSearchType,
    )

num_lists = 100
dimensions = 1536
similarity_algorithm = CosmosDBSimilarityType.COS
# kind = CosmosDBVectorSearchType.VECTOR_IVF
kind = "vector-ivf"
m = 16
ef_construction = 64
ef_search = 40
score_threshold = 0.1