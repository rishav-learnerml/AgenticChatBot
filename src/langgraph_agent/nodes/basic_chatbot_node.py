from src.langgraph_agent.state.state import State

class BasicChatbotNode:
    """
    Basic chatbot login implementation
    """
    def __init__(self,model) -> None:
        self.llm=model

    def process(self, state:State)->dict:
        """
        Processes the input state and generates a chatbot response.
        """
        return {'messages':self.llm.invoke(state['messages'])} #type:ignore