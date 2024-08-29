import streamlit as st

st.title("Hello World")
with st.sidebar:
    st.header("Side Heading")
    st.write("some random text")
tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.radio("Select one:", [1, 2])

with tab2:
    expand = st.expander("My label", icon=":material/info:")
    expand.write("Inside the expander.")
    pop = st.popover("Button label")
    pop.checkbox("Show all")





