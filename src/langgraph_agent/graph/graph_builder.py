from langgraph.graph import StateGraph,START,END
from src.langgraph_agent.state.state import State
from src.langgraph_agent.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraph_agent.tools.search_tool import get_tools, create_tool_node
from langgraph.prebuilt import tools_condition, ToolNode
from src.langgraph_agent.nodes.chatbot_with_tool_node import ChatbotWithToolNode


class GraphBuilder:
    def __init__(self,model) -> None:
        self.llm=model
        self.graph_builder=StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using LangGraph.
        This method initializes a chatbot node using the `BasicChatbotNode` class
        and integrate it into the graph. The chatbot node is set as both the
        entry and exit point of the graph.
        """

        self.basic_chatbot_node = BasicChatbotNode(self.llm)

        self.graph_builder.add_node('chatbot',self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START,'chatbot')
        self.graph_builder.add_edge('chatbot',END)

    def chatbot_with_tools_build_graph(self):
        """
        Builds an advanced chatbot graph with tool integration.
        This method creates a chatbot graph that includes both a chatbot node
        and a tool node. It defines tools, initializes the chatbot with tool
        capabilities, and sets up conditional and direct edges between nodes.
        The chatbot node is set as the entry point.
        """
        #define the tool and tool node
        tools=get_tools()
        tool_node=create_tool_node(tools)

        #define the llm
        llm=self.llm

        #define the chatbot node

        obj_chatbot_with_node=ChatbotWithToolNode(llm)
        chatbot_node=obj_chatbot_with_node.create_chatbot(tools)

        ## add nodes
        self.graph_builder.add_node("chatbot",chatbot_node)
        self.graph_builder.add_node("tools",tool_node)

        ## add edges
        self.graph_builder.add_edge(START,'chatbot')
        self.graph_builder.add_conditional_edges('chatbot',tools_condition)
        self.graph_builder.add_edge('tools','chatbot')
    
    def setup_graph(self, usecase:str):
        """
        Sets up the graph for the selected use case.
        """

        if usecase=="Basic Chatbot":
            self.basic_chatbot_build_graph()
        elif usecase=="Chatbot with Tool":
            self.chatbot_with_tools_build_graph()

        return self.graph_builder.compile()