import os
from supabase import create_client, Client
from dotenv import load_dotenv
from providers.base import DatabaseProvider

# Carrega as variáveis do arquivo .env
load_dotenv()

class SupabaseProvider(DatabaseProvider):
    def __init__(self):
        url: str = os.environ.get("SUPABASE_URL")
        key: str = os.environ.get("SUPABASE_KEY")
        
        if not url or not key:
            raise ValueError("Erro: SUPABASE_URL e SUPABASE_KEY precisam estar configuradas no arquivo .env")
        
        # Inicializa o cliente oficial do Supabase
        self.client: Client = create_client(url, key)

    def get_all(self, table: str):
        """Busca todos os registros de uma tabela específica"""
        try:
            response = self.client.table(table).select("*").execute()
            return response.data
        except Exception as e:
            print(f"Erro ao buscar dados no Supabase: {e}")
            return []

    def create(self, table: str, data: dict):
        """Insere um novo registro em uma tabela específica"""
        try:
            response = self.client.table(table).insert(data).execute()
            return response.data
        except Exception as e:
            print(f"Erro ao inserir dados no Supabase: {e}")
            return None