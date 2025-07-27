class QueryBuilderError(Exception):
    pass

class SchemaFetchError(QueryBuilderError):
    pass

class QueryGenerationError(QueryBuilderError):
    pass
