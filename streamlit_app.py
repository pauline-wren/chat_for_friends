from openai import OpenAI
import streamlit as st



# openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')
openai_api_key=st.secrets.OPENAI_API_KEY
password =  st.sidebar.text_input('Give me password', type='password')
openai_api_key=st.secrets.PASSWORD


st.title('💬Chat for Friends')
st.caption("LODox Concept Chat powered by OpenAI LLM")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
    if password != st.secrets.PASSWORD:
        st.info("密码错误，别试了")
        st.stop()
    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
