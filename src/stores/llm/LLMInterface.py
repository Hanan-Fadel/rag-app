from abc import ABC, abstractmethod

class LLMInterface(ABC):
    
    @abstractmethod #this is a abstract method, so it must be implemented in the child class
    def set_generation_model(self, model_id: str):
        pass #no implementation here, just a declaration
    
    @abstractmethod
    def set_embedding_model(self, model_id: str, embedding_size: int):
        pass
    
    @abstractmethod
    def generate_text(self, prompt: str, chat_history: list = [], max_output_tokens: int = None, temperature: float = None):
        pass
    
    @abstractmethod
    def embed_text(self, text: str, document_type: str = None):
        pass
    
    @abstractmethod
    def construct_prompt(self, prompt: str, role: str):
        pass