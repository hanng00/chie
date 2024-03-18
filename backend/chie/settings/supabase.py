import os
from supabase import create_client, Client, ClientOptions


class SupabaseClient:
    def __init__(self):
        self.url = None
        self.key = None
        self.client = None

    def get_client(self):
        if self.client is None:
            try: 
                self._load_env_vars()
            except ValueError as e:
                return

            self.client = create_client(
                self.url,
                self.key,
                options=ClientOptions(
                    postgrest_client_timeout=10,
                ),
            )
        return self.client

    def _load_env_vars(self):
        url = os.environ.get("SUPABASE_URL")
        if url is None:
            raise ValueError("SUPABASE_URL is not set")

        key = os.environ.get("SUPABASE_KEY")
        if key is None:
            raise ValueError("SUPABASE_KEY is not set")
        
        self.url = url
        self.key = key

supabase_client: Client = SupabaseClient().get_client()
