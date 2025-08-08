import streamlit as st 

st.set_page_config(page_title="Layouts Practice", layout='wide')

st.title('Streamlit Layouts') 

# sidebar
sidebar = st.sidebar
sidebar.write('This is my sidebar')


# columns
col1, col2, col3 = st.columns(3)
with col1:
    st.write(' this is columns -1')
    st.image('./media/cat.jpg')
    
with col2:
    st.write(' this is columns -2')
    st.image('./media/dog.jpg')
    
with col3:
    st.write(' this is columns -3')
    st.image('./media/owl.jpg')
    
# tabs
st.header('Display in Tabs')
tab1, tab2, tab3 = st.tabs(['Cat Image','Dog','Owl'])

with tab1:
    st.write('You are in Cat Tab')
    st.image('./media/cat.jpg')
with tab2:
    st.write('You are in Dog Tab')
    st.image('./media/dog.jpg')
    
with tab3:
    st.write('You are in Owl Tab')
    st.image('./media/owl.jpg')
