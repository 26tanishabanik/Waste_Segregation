import streamlit as st
import numpy as np
from PIL import Image, ImageOps
import base64
from detect import *
    
st.balloons()
# option = st.sidebar.radio("Menu",['Home', 'About','Contributors'])
st.sidebar.markdown('<h1 style="margin-left:8%; color:	#FF9933 ">Menu </h1>',
                    unsafe_allow_html=True)
option = st.sidebar.radio(" ",('Home', 'About Model','About Project','Contributors'))


if option == 'Home':
      
      col1,col2,col3 = st.columns([50,100,1])
    
      # col2.image('chapter_logo.png')
      st.markdown(
          """
          <style>
          .container1 {
          display: flex;
        }
        .logo-img1 {
             float:right;
             width:350px;
             height:350px;
             margin: 0px 0px 0px 170px;
        }
        </style>
        """,
        unsafe_allow_html=True
      )
      st.markdown(
          """
          <style>
          .container2 {
          display: flex;
        }
        .img {
             float:right;
             width:300px;
             height:350px;
             margin: 0px 0px 0px 200px;
        }
        </style>
        """,
        unsafe_allow_html=True
      )
      st.markdown(
          f"""
          <div class="container1">
               <img class="logo-img1" src="data:image/png;base64,{base64.b64encode(open('chapter_logo.png', "rb").read()).decode()}">
          </div>
          """,
          unsafe_allow_html=True
      )
      # st.title('Omdena - France Chapter')
      st.markdown("<h1 style='text-align: center; color: white;'>Omdena - France Chapter</h1>", unsafe_allow_html=True)
      st.text("")
      st.text("")
      st.text("")
      html_temp = """
        <div style="background-color:blue;padding:10px">
        <h2 style="color:white;text-align:center;">Improve sorting and segregation of waste using machine learning</h2>
        </div>
        """
      st.markdown(html_temp,unsafe_allow_html=True)
      st.text("")
      st.text("")
      st.text("")

      def upload_image_ui():
          uploaded_image = st.file_uploader("Please upload an image file", type=["png", "jpg", "jpeg"])
          if uploaded_image is not None:
            try:
                image = Image.open(uploaded_image)
                #  image = ImageOps.grayscale(image)
            except Exception:
                st.error("Error: Invalid image")
            else:
                img_array = np.array(image)
                return img_array
        
      img_array = upload_image_ui()
      st.text("")
      st.text("")

      if isinstance(img_array, np.ndarray):
        preds = predict(img_array)
        output = plot_image(img_array[..., ::-1], preds)
        st.image(output)
        #  for instance, confidence in zip(instances, conf):
              #  st.subheader("Our model is "+ str(round((confidence * 100), 2))+ "% sure that the image contains a " + instance.split(':')[0])
              #  st.text("")
        
      
      ana_type = st.sidebar.selectbox(
        "To know more about Waste Categories ",
        ("Select a waste category","Plastic","Glass","Cardboard","Paper","Metals"))
        
      if ana_type == 'Plastic':
            image1 = Image.open('Waste_Categories/plastic.jpeg')
            st.sidebar.image(image1, caption='Plastic')
            st.sidebar.write("Give description for plastic")
      
      elif ana_type =='Glass':
            image2 = Image.open('Waste_Categories/glass.jpeg')
            st.sidebar.image(image2, caption='Glass')
            st.sidebar.write("Give description for glass")
            
      elif ana_type =='Cardboard':
            image3 = Image.open('Waste_Categories/cardboard.jpeg')
            st.sidebar.image(image3, caption='Cardboard')
            st.sidebar.write("Give description for cardboard")
            
      elif ana_type =='Paper':
            image4 = Image.open('Waste_Categories/paper.jpeg')
            st.sidebar.image(image4, caption='Paper')
            st.sidebar.write("Give description for paper")
      elif ana_type =='Metals':
            image5 = Image.open('Waste_Categories/metal.jpeg')
            st.sidebar.image(image5, caption='Metals')
            st.sidebar.write("Give description for metals")
     
         



if option == 'About Model':
  html_temp = """
        <div style="background-color:blue;padding:10px">
        <h2 style="color:white;text-align:center;">Model Description</h2>
        </div>
        """
  st.markdown(html_temp,unsafe_allow_html=True)
  st.text("")
  st.text("")
  st.subheader("Model Name Description: ")
  st.markdown('model',unsafe_allow_html=True)
  

if option == 'About Project':
  html_temp = """
        <div style="background-color:blue;padding:10px">
        <h2 style="color:white;text-align:center;">Project Description</h2>
        </div>
        """
  st.markdown(html_temp,unsafe_allow_html=True)
  st.text("")
  st.text("")
  st.markdown('write description',unsafe_allow_html=True)
  

if option == 'Contributors':
      rebecca_IMAGE = "Contributors/rebecca.jpeg"
      html_temp = """
            <div style="background-color:blue;padding:10px">
            <h2 style="color:white;text-align:center;">Team</h2>
            </div>
            """
      st.markdown(
          """
          <style>
          .container {
          display: flex;
        }
        .rebecca-img {
             float:right;
             width:175px;
             height:192px;
             margin: 0px 0px 0px 28px;
        }
        
        </style>
        """,
        unsafe_allow_html=True
      )
      st.markdown(html_temp,unsafe_allow_html=True)
      st.subheader("Project Manager")
      st.write("• &nbsp;  &nbsp;    [Rebecca Alexander](https://www.linkedin.com/in/rebecca-alexander/)")
      st.markdown(
            f"""
            <div class="container">
                  <img class="rebecca-img" src="data:image/png;base64,{base64.b64encode(open(rebecca_IMAGE, "rb").read()).decode()}">
            </div>
            """,
            unsafe_allow_html=True
      )
      st.subheader("Contributors")
      
