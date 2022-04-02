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
        st.text(preds)
        output = plot_image(img_array, preds)
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
            st.sidebar.write("The use of plastics is deeply embedded in our daily lives, in everything from grocery bags and cutlery to water bottles and sandwich wrap. But the quest for convenience has gone too far and we are failing to use plastics efficiently, wasting valuable resources and harming the environment. Plastic overconsumption and mismanagement of plastic waste is a growing menace, causing landfills to overflow, choking rivers, and threatening marine ecosystems. This has a negative impact on sectors that are critical to many economies, including tourism, shipping and fisheries.")
      
      elif ana_type =='Glass':
            image2 = Image.open('Waste_Categories/glass.jpeg')
            st.sidebar.image(image2, caption='Glass')
            st.sidebar.write("Glass bottles could have an even bigger impact on the environment than plastic ones, a new study has found. Researchers at the University of Southampton in England set out to determine which common beverage containers cause the most and least harm to the environment. They found that glass is actually more detrimental than plastic because it is mined from rare materials and requires more fossil fuels to produce and ship.")
            
      elif ana_type =='Cardboard':
            image3 = Image.open('Waste_Categories/cardboard.jpeg')
            st.sidebar.image(image3, caption='Cardboard')
            st.sidebar.write("Cardboard is one of the most commonly used materials for packing electronics and food. Because of this, it is one of the items that is recycled along with used clothes, electronics, and plastic. Recycling cardboard helps reduce solid waste, reduce demand on our natural resources, reduce the amount of trash going to the landfill, and contribute to cleaner air. Cardboard ends up In landfill, increases the amount Of methane in The atmosphere, increases natural resource consumption and so on.")
            
      elif ana_type =='Paper':
            image4 = Image.open('Waste_Categories/paper.jpeg')
            st.sidebar.image(image4, caption='Paper')
            st.sidebar.write("Paper constitutes over a third of all litter. It costs states as much as hundreds of thousands of dollars in clean up annually. Areas with litter problems are unattractive to tourists and businesses. Littered areas breed bacteria and attract insects and rodents, which spread the bacteria and cause illness. Paper contains toxins that seep into soil as the paper decomposes. These toxins are carried into waterways via storm water. Animals eat litter and become ill or die. Pedestrians, unsecured trucks and poorly covered trash bins are the main causes of litter.")
      elif ana_type =='Metals':
            image5 = Image.open('Waste_Categories/metal.jpeg')
            st.sidebar.image(image5, caption='Metals')
            st.sidebar.write("Metal is so sturdy and durable that it doesn’t simply break apart and vanish when disposed of. This means that the metal you use today will be the metal haunting the environment and damaging it a hundred years from now. Let’s look a little more specifically at some of the consequences of improper metal disposal. When we don’t take the proper precautions to dispose of our metal, or recycle it if that option is available, you are going to end up doing a disservice to the environment and the people around us. Most metal, scrap or otherwise, will have been treated with chemicals at some point or another. This means that if we improperly dispose or handle the metal, we’ll end up putting chemicals back into the environment. Chemicals can seep into the ground, drift to nearby water sources, and become instantly damaging sources of pollution for humans, animals, and the very world we live in. ")
     
         



if option == 'About Model':
  html_temp = """
        <div style="background-color:blue;padding:10px">
        <h2 style="color:white;text-align:center;">Model Description</h2>
        </div>
        """
  st.markdown(html_temp,unsafe_allow_html=True)
  st.text("")
  st.text("")
  st.subheader("Model Description: ")
  st.markdown('From the project point of view and problem statement, identification of “category” of waste constituents with good precision. YOLO is a fast and accurate object detection algorithm.',unsafe_allow_html=True)
  st.markdown('The YOLO algorithm is very fast so it can detect objects in real-time and it provides accurate results with minimal background errors.',unsafe_allow_html=True)
  st.subheader("Data Centric Approach: ")
  st.markdown('We had a “Data Centric Approach” rather than a model-centric approach. The Data centric approach generalizes the data to be used with any model architectures. In this approach,',unsafe_allow_html=True)
  st.markdown('we cleaned the data, trained the model, and did error analysis. We went back and collected more data, did data pre-processing  based on the result analysis and continue the cycle.',unsafe_allow_html=True)
  st.markdown('Thus we iteratively improve the data and finally the model performance improves tremendously. We did several rounds of training to improve the model. In the first round of training,',unsafe_allow_html=True)
  st.markdown('we used Version v0 data and we were able to find many glitches that were negatively affecting the performance of the model, inorder to handle these we created a second set of data called version 1 (v1_yolo.zip)',unsafe_allow_html=True)
  st.markdown('The different data preprocessing steps done includes balancing data i.e. the classes with higher frequencies were randomly sampled to 500. This helped to handle the overlapping of classes.',unsafe_allow_html=True)
  st.markdown('We split the data into 80% train set and 20% test set. This helped to prevent the model from overfitting and to accurately evaluate the model.',unsafe_allow_html=True)
  st.markdown('We used the state-of-the-Art model Yolo v5s  and YoloR. We custom trained these models on 5 classes of waste categories and the resulting models have high accuracy and faster inference time.',unsafe_allow_html=True)
  st.markdown('We split the data into 80% train set and 20% test set. This helped to prevent the model from overfitting and to accurately evaluate the model. We used mAP score to compare and benchmark the',unsafe_allow_html=True)
  st.markdown('performance of our models. We not only focused on the mAP score alone. Apart from this, we manually reviewed image inference run on these models to perform error analysis and thereby',unsafe_allow_html=True)
  st.markdown('improving the quality of data. This approach helped us to improve the performance of the model tremendously.',unsafe_allow_html=True)
  st.subheader("Types of images: ")
  st.markdown('Images are categorized into 3 types based on the level of difficulty for annotating.',unsafe_allow_html=True)
  st.subheader("Type-1 image: ")
  st.markdown('&nbsp; &nbsp; &nbsp; • White or very simple background.',unsafe_allow_html=True)
  st.markdown('&nbsp; &nbsp; &nbsp; • Containing a single object or multiple objects that do not overlap.',unsafe_allow_html=True)
  st.image('assets/type-1.png')
  st.subheader("Type-2 image: ")
  st.markdown('&nbsp; &nbsp; &nbsp; • Waste in the wild.',unsafe_allow_html=True)
  st.markdown('&nbsp; &nbsp; &nbsp; • Images with different background.',unsafe_allow_html=True)
  st.markdown('&nbsp; &nbsp; &nbsp; • Some of them contain overlapping objects but they can still be correctly annotated.',unsafe_allow_html=True)
  st.image('assets/type-2.png')
  st.subheader("Type-3 image: ")
  st.markdown('&nbsp; &nbsp; &nbsp; • Confusing ones.',unsafe_allow_html=True)
  st.markdown('&nbsp; &nbsp; &nbsp; • Contain a lot of overlapping objects.',unsafe_allow_html=True)
  st.markdown('&nbsp; &nbsp; &nbsp; • Very time-consuming in context of annotations.',unsafe_allow_html=True)
  st.image('assets/type-3.png')
  st.subheader("Final Model-YoloV5m: ")
  st.markdown('The final Yolo 5m model was trained on the v1_yolo  dataset. In Object Detection tasks, an imbalanced training set problem is more significant. Thus, the v1_yolo dataset was created.',unsafe_allow_html=True)
  st.markdown('It is a balanced dataset with 450 samples from higher frequency classes. The model was trained using the training scripts from the Ultralytics Repo. The inference script uses the torch-hub',unsafe_allow_html=True)
  st.markdown('and the saved best pre-trained weights.',unsafe_allow_html=True)
  st.markdown(' Following hyperparameters were used for fine-tuning the Yolov5m model:',unsafe_allow_html=True)
  st.markdown('&nbsp; &nbsp; &nbsp; • Epochs: 30',unsafe_allow_html=True)
  st.markdown('&nbsp; &nbsp; &nbsp; • Batch Size: 32',unsafe_allow_html=True)
  st.markdown('&nbsp; &nbsp; &nbsp; • Image Size: 416',unsafe_allow_html=True)
  st.markdown('&nbsp; &nbsp; &nbsp; • Optimizer: SGD',unsafe_allow_html=True)
  st.markdown('Default augmentation techniques and default values were used for various other hyperparameters such as learning rate, weight decay, and warmup epochs to train the final model. In the inference script,',unsafe_allow_html=True)
  st.markdown('the flexibility is given to the user to set the confidence threshold to control the number of false-positive cases in the prediction. The default value of the confidence threshold is set to 0.5.',unsafe_allow_html=True)
  st.image('assets/model.png')
  st.subheader("Model Insights: ")
  st.markdown('&nbsp; &nbsp; &nbsp; • The model is successfully detecting the different categories of waste  and are able to distinguish between different types of classes from  non overlapping  objects in an  image.',unsafe_allow_html=True)
  st.markdown('&nbsp; &nbsp; &nbsp; • The v1_yolo.zip Data was well balanced i.e. number of images for each of the categories in the training dataset  had equal frequency  which tremendously improved the model performance.',unsafe_allow_html=True)
  st.markdown('&nbsp; &nbsp; &nbsp; • The model is able to detect waste categories from type 1 images only. We have to train model with type 2 and type 3 images for better result for the detections of categories from overlapping images.',unsafe_allow_html=True)
  st.markdown('&nbsp; &nbsp; &nbsp; • Overall data quality should be improved.',unsafe_allow_html=True)
  

if option == 'About Project':
  html_temp = """
        <div style="background-color:blue;padding:10px">
        <h2 style="color:white;text-align:center;">Project Description</h2>
        </div>
        """
  st.markdown(html_temp,unsafe_allow_html=True)
  st.text("")
  st.text("")
  st.markdown('The biggest challenge in recycling/reusing waste is sorting and segregating different types of waste since segregation of waste aids in targeted recycling or even decomposition.',unsafe_allow_html=True)
  st.markdown('As an example, segregating a dry metal can from a metal can containing organic matter eases recycling. The necessary action for proper segregation of the waste on a large scale',unsafe_allow_html=True)
  st.markdown('is to identify various materials first. Once identified, neuromorphic tools could be used to sort things based on the identified parameters. However, while there exist several',unsafe_allow_html=True)
  st.markdown('methods to identify different materials such as visual sensors, olfactory sensors as well as spectroscopic tools, there are very few or no attempts at using artificial',unsafe_allow_html=True)
  st.markdown('intelligence to specifically identify materials from the waste, which could then be applied to ease the segregation process. We, therefore, propose to use visual image',unsafe_allow_html=True)
  st.markdown('recognition to first identify objects, in their full form or by parts in order to be used later for segregation. For example, we envisage the identification of different',unsafe_allow_html=True)
  st.markdown('materials such as plastics, metal and paper in a used milk carton, which could lead to proper recycling of plastics, paper and metal.',unsafe_allow_html=True)
  st.subheader("Learning Outcomes: ")
  st.markdown('In this project, we performed the following steps:',unsafe_allow_html=True)
  st.markdown('&nbsp; &nbsp; &nbsp;  1. Data Collection through web scraping and creation of image library',unsafe_allow_html=True)
  st.markdown('&nbsp; &nbsp; &nbsp;  2. Image Preprocessing for Computer vision',unsafe_allow_html=True)
  st.markdown('&nbsp; &nbsp; &nbsp;  3. Annotating Images to reflect the correct waste category',unsafe_allow_html=True)
  st.markdown('&nbsp; &nbsp; &nbsp;  4. Computer Vision techniques to identify and classify different waste materials',unsafe_allow_html=True)
  st.markdown('&nbsp; &nbsp; &nbsp;  5. Deploying Dashboard and Visualization to make the ML model available to the public',unsafe_allow_html=True)
  st.subheader("Results: ")
  st.image('assets/result1.png')
  st.image('assets/result2.png')
  st.image('assets/result3.png')
  st.image('assets/result4.png')
  st.image('assets/result5.png')

if option == 'Contributors':
      rebecca_IMAGE = "Contributors/rebecca.png"
      anusha_IMAGE = "Contributors/anusha.png"
      alexandre_IMAGE = "Contributors/alexandre.png"
      anmol_IMAGE = "Contributors/anmol.png"
      armielyn_IMAGE = "Contributors/armielyn.png"
      aye_IMAGE = "Contributors/aye.png"
      bridget_IMAGE = "Contributors/bridget.png"
      henry_IMAGE = "Contributors/henry.png"
      jennifer_IMAGE = "Contributors/jennifer.png"
      noel_IMAGE = "Contributors/noel.png"
      payal_IMAGE = "Contributors/payal.png"
      preeja_IMAGE = "Contributors/preej.png"
      pushkaraj_IMAGE = "Contributors/pushkaraj.png"
      rheyAnnMagcalas_IMAGE = "Contributors/rheyAnnMagcalas.png"
      sanjay_IMAGE = "Contributors/sanjay.png"
      surya_IMAGE = "Contributors/surya.png"
      tanisha_IMAGE = "Contributors/tanisha.png"
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
        .anusha-img {
             float:right;
             width:175px;
             height:192px;
             margin: 0px 0px 0px 28px;
        }
        .alexandre-img {
             float:right;
             width:175px;
             height:192px;
             margin: 0px 0px 0px 28px;
        }
        .anmol-img {
             float:right;
             width:175px;
             height:192px;
             margin: 0px 0px 0px 28px;
        }
        .armielyn-img {
             float:right;
             width:175px;
             height:192px;
             margin: 0px 0px 0px 28px;
        }
        .aye-img {
             float:right;
             width:175px;
             height:192px;
             margin: 0px 0px 0px 28px;
        }
        .bridget-img {
             float:right;
             width:175px;
             height:192px;
             margin: 0px 0px 0px 28px;
        }
        .henry-img {
             float:right;
             width:175px;
             height:192px;
             margin: 0px 0px 0px 28px;
        }
        .jennifer-img {
             float:right;
             width:175px;
             height:192px;
             margin: 0px 0px 0px 28px;
        }
        .noel-img {
             float:right;
             width:175px;
             height:192px;
             margin: 0px 0px 0px 28px;
        }
        .payal-img {
             float:right;
             width:175px;
             height:192px;
             margin: 0px 0px 0px 28px;
        }
        .preeja-img {
             float:right;
             width:175px;
             height:192px;
             margin: 0px 0px 0px 28px;
        }
        .pushkaraj-img {
             float:right;
             width:175px;
             height:192px;
             margin: 0px 0px 0px 28px;
        }
        .rheyAnnMagcalas-img {
             float:right;
             width:175px;
             height:192px;
             margin: 0px 0px 0px 28px;
        }
        .sanjay-img {
             float:right;
             width:175px;
             height:192px;
             margin: 0px 0px 0px 28px;
        }
        .surya-img {
             float:right;
             width:175px;
             height:192px;
             margin: 0px 0px 0px 28px;
        }
        .tanisha-img {
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
      st.write("1. [Anusha Thatikonda](https://www.linkedin.com/in/anusha-thatikonda/)")
      st.markdown(
            f"""
            <div class="container">
                  <img class="anusha-img" src="data:image/png;base64,{base64.b64encode(open(anusha_IMAGE, "rb").read()).decode()}">
            </div>
            """,
            unsafe_allow_html=True
      )
      st.write("1. [Alexandre Lang](https://www.linkedin.com/in/alexandre-lang-ds/)")
      st.markdown(
            f"""
            <div class="container">
                  <img class="alexandre-img" src="data:image/png;base64,{base64.b64encode(open(alexandre_IMAGE, "rb").read()).decode()}">
            </div>
            """,
            unsafe_allow_html=True
      )
      st.write("1. [Anmol Kumar](https://www.linkedin.com/in/anmol-kumar-94b5571a2/)")
      st.markdown(
            f"""
            <div class="container">
                  <img class="anmol-img" src="data:image/png;base64,{base64.b64encode(open(anmol_IMAGE, "rb").read()).decode()}">
            </div>
            """,
            unsafe_allow_html=True
      )
      st.write("2. [Armielyn Obinguar](https://www.linkedin.com/in/armielyn-obinguar-9229561b0/)")
      st.markdown(
            f"""
            <div class="container">
                  <img class="armielyn-img" src="data:image/png;base64,{base64.b64encode(open(armielyn_IMAGE, "rb").read()).decode()}">
            </div>
            """,
            unsafe_allow_html=True
      )
      st.write("3. [Aye Nyein Thaw](https://www.linkedin.com/in/aye-nyein-thaw-6040311b3/)")
      st.markdown(
            f"""
            <div class="container">
                  <img class="aye-img" src="data:image/png;base64,{base64.b64encode(open(aye_IMAGE, "rb").read()).decode()}">
            </div>
            """,
            unsafe_allow_html=True
      )
      st.write("3. [Bridget B]()")
      st.markdown(
            f"""
            <div class="container">
                  <img class="bridget-img" src="data:image/png;base64,{base64.b64encode(open(bridget_IMAGE, "rb").read()).decode()}">
            </div>
            """,
            unsafe_allow_html=True
      )
      st.write("3. [Henry Shu](https://www.linkedin.com/in/henry-shu-67b86099/)")
      st.markdown(
            f"""
            <div class="container">
                  <img class="henry-img" src="data:image/png;base64,{base64.b64encode(open(henry_IMAGE, "rb").read()).decode()}">
            </div>
            """,
            unsafe_allow_html=True
      )
      st.write("3. [Jennifer Joseph](https://www.linkedin.com/in/jennifer-joseph-b50776151/)")
      st.markdown(
            f"""
            <div class="container">
                  <img class="jennifer-img" src="data:image/png;base64,{base64.b64encode(open(jennifer_IMAGE, "rb").read()).decode()}">
            </div>
            """,
            unsafe_allow_html=True
      )
      st.write("3. [Noel Simonovici](https://www.linkedin.com/in/noelsimonovici/)")
      st.markdown(
            f"""
            <div class="container">
                  <img class="noel-img" src="data:image/png;base64,{base64.b64encode(open(noel_IMAGE, "rb").read()).decode()}">
            </div>
            """,
            unsafe_allow_html=True
      )
      st.write("4. [Payal Rathod](https://www.linkedin.com/in/payalrrathod-/)")
      st.markdown(
            f"""
            <div class="container">
                  <img class="payal-img" src="data:image/png;base64,{base64.b64encode(open(payal_IMAGE, "rb").read()).decode()}">
            </div>
            """,
            unsafe_allow_html=True
      )
      st.write("5. [Preeja Babu](https://www.linkedin.com/in/preejababu/)")
      st.markdown(
            f"""
            <div class="container">
                  <img class="preeja-img" src="data:image/png;base64,{base64.b64encode(open(preeja_IMAGE, "rb").read()).decode()}">
            </div>
            """,
            unsafe_allow_html=True
      )
      st.write("5. [Pushkaraj Dhoot](https://www.linkedin.com/in/pushkaraj-dhoot-770321166/)")
      st.markdown(
            f"""
            <div class="container">
                  <img class="pushkaraj-img" src="data:image/png;base64,{base64.b64encode(open(pushkaraj_IMAGE, "rb").read()).decode()}">
            </div>
            """,
            unsafe_allow_html=True
      )
      st.write("5. [Rhey Ann Magcalas](https://www.linkedin.com/in/rhey-ann-magcalas-47541490/)")
      st.markdown(
            f"""
            <div class="container">
                  <img class="rheyAnnMagcalas-img" src="data:image/png;base64,{base64.b64encode(open(rheyAnnMagcalas_IMAGE, "rb").read()).decode()}">
            </div>
            """,
            unsafe_allow_html=True
      )
      st.write("5. [Sanjay Sharma](https://www.linkedin.com/in/aerosanjay)")
      st.markdown(
            f"""
            <div class="container">
                  <img class="sanjay-img" src="data:image/png;base64,{base64.b64encode(open(sanjay_IMAGE, "rb").read()).decode()}">
            </div>
            """,
            unsafe_allow_html=True
      )
      st.write("5. [Surya Abhishek](https://www.linkedin.com/in/suryaabhishek/)")
      st.markdown(
            f"""
            <div class="container">
                  <img class="surya-img" src="data:image/png;base64,{base64.b64encode(open(surya_IMAGE, "rb").read()).decode()}">
            </div>
            """,
            unsafe_allow_html=True
      )
      st.write("5. [Tanisha Banik](https://www.linkedin.com/in/tanisha-banik-04b511173/)")
      st.markdown(
            f"""
            <div class="container">
                  <img class="tanisha-img" src="data:image/png;base64,{base64.b64encode(open(tanisha_IMAGE, "rb").read()).decode()}">
            </div>
            """,
            unsafe_allow_html=True
      )
      
