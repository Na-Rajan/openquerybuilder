import openai

class QueryGenerator:
    def __init__(self, api_key, schema_metadata):
        openai.api_key = api_key
        self.schema_metadata = schema_metadata

    def generate_query(self, prompt):
        schema_context = "\n".join(
            [f"{row['table_name']}({row['column_name']}:{row['data_type']})"
             for row in self.schema_metadata]
        )
        full_prompt = f"""
        Schema:
        {schema_context}

        User Request:
        {prompt}

        Generate SQL query:
        """
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": full_prompt}]
        )
        return response.choices[0].message["content"]
