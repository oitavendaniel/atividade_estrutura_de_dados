from providers.supabase_provider import SupabaseProvider

class ProviderFactory:
    @staticmethod
    def get_provider(provider_type: str):
        if provider_type == "supabase":
            return SupabaseProvider()
        
        # Se no futuro criar um mock ou SQL puro, adiciona aqui:
        # elif provider_type == "sql":
        #     return SQLProvider()
        
        raise ValueError(f"Provider '{provider_type}' não é suportado.")