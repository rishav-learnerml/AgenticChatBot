import streamlit as st
import os

from src.langgraph_agent.ui.uiconfig import Config ## Imports this way as we have used __init__.py -> works like a package

class LoadStreamlitUI:
    def __init__(self):
        self.config=Config()
        self.user_controls={}

    def load_streamlit_ui(self):
        st.set_page_config(page_title="🤖 "+self.config.get_page_title(),layout='wide') #type:ignore
        st.header("🤖 "+self.config.get_page_title()) #type:ignore

        with st.sidebar:
            # config options
            llm_options=self.config.get_llm_options()
            usecase_options=self.config.get_usecase_options()

            # LLM selection
            self.user_controls['selected_llm']=st.selectbox('Select LLM',llm_options)

            if self.user_controls['selected_llm']=='Groq':
                # model selection
                model_options = self.config.get_groq_model_options()
                self.user_controls['selected_groq_model']=st.selectbox("Select Model",model_options)
                self.user_controls['GROQ_API_KEY']=st.session_state['GROQ_API_KEY']=st.text_input("API Key",type='password')
                #Validate API key
                if not self.user_controls['GROQ_API_KEY']:
                    st.warning(" ⚠️ Please enter your GROQ API key to proceed. Don't have? refer : https://console.groq.com/keys ")

            # Use case selection
            self.user_controls['selected_usecases']=st.selectbox('Select Usecases',usecase_options)

        return self.user_controls
    

                