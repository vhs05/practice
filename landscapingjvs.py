#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

backgroundColor = "#0E4C92"
font = "Roboto"
st.set_page_config(page_title="Landscaping JVS", layout="wide")
# # # Header
st.title("Thank you for choosing Luis and his team.")
# use local css
# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f"(<style>{f.read()}</style>", unsafe_allow_html=True)
# local_css("style/style.css")
with st.container():
    st.subheader("Since 2016, we have transformed outdoor spaces into breathtaking landscapes!")
    st.write("Our team consists of workers who also share Luis's commitment to excellence and customer satisfaction. Each member brings unique skills and a collaborative spirit, ensuring that every project is completed to the highest standards. We firmly believe in personalized service and attention to detail. It is our job to help!")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
    	st.header("Services we offer:")
    	st.write("##")
    	st.write("""
            Lawn Care and Maintenance
            Our lawncare services, include mowing, trimming and edging. Email or call Luis for a quote for fertilization, aeration, weed control, irrigation systems, and seasonal clean-ups.")
            Hardscaping
            Irrigation Systems
            Ensure your plants and lawn receive the right amount of water with our efficient irrigation solutions. We design, install, and maintain systems tailored to your landscape’s needs
            Seasonal Planting and Color Changes
            Keep your garden vibrant throughout the year with our seasonal planting services. We select and plant flowers and foliage that provide year-round color and interest.
            Landscape Renovation
            Revitalize your existing landscape with our renovation services. We update and enhance your outdoor space to meet your needs and preferences.
        """)

with st.container():
    st.write("---")
    st.header("Send Luis a message regarding feedback or any questions!")
    st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/help.landscapingjvs@gmail.com" method="POST">
        <input type="hidden" name ="_captcha" value="false">
        <input type="text" placeholder="Name:" required>
        <input type="email" placeholder="Email and number" required>
        <textarea name="message" placeholder="Message" required>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

