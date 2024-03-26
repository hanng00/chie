import os
from supabase import create_client, Client, ClientOptions
from chie.config import get_supabase_url_and_key

url, key = get_supabase_url_and_key()
supabase_client: Client = create_client(
    url,
    key,
    options=ClientOptions(
        postgrest_client_timeout=10,
    ),
)
