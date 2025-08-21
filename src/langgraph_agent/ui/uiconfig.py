from configparser import ConfigParser

class Config:
    def __init__(self,config_file_path='./src/langgraph_agent/ui/uiconfigfile.ini') -> None:
        self.config=ConfigParser()
        self.config.read(config_file_path)

    def get_llm_options(self):
        return self.config["DEFAULT"].get('LLM_OPTIONS').split(', ') # type: ignore
    
    def get_usecase_options(self):
        return self.config["DEFAULT"].get('USECASE_OPTIONS').split(', ') # type: ignore
    
    def get_groq_model_options(self):
        return self.config["DEFAULT"].get('GROQ_MODEL_OPTIONS').split(', ') # type: ignore
    
    def get_page_title(self):
        return self.config["DEFAULT"].get('PAGE_TITLE')