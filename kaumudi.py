import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(layout='wide')

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

#lottie_coder=load_lottieurl("https://lottie.host/42c15a90-3d3b-4bac-9d19-2a21b4f019e0/4P1dHZoC2h.json")
lottie_woman=load_lottieurl("https://lottie.host/1c62f9b9-1f61-4caa-95bb-aa698a05977c/zIxxRLsY4E.json")
#lottie_woman=load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_glp2wakj.json")
lottie_skills=load_lottieurl("https://lottie.host/e42378d8-8048-4242-b544-20b9ac52579d/cyCum5jtZf.json")
contact=load_lottieurl("https://lottie.host/ab711571-f946-4587-ba4c-6035416c0d2f/e7h81dlqxp.json")
#photo=Image.open(r"D:/Webpage/Original_Photo.jpg")
flight=Image.open(r"D:/Webpage/image/Flight_fare.jpg")
fifa=Image.open(r"D:/Webpage/image/Fifa20.jpg")
salary=Image.open(r"D:/Webpage/image/Texas_salary.jpg")
spam=Image.open(r"D:/Webpage/image/spam.png")
reviews=Image.open(r"D:/Webpage/image/Amazon_Reviews_analysis.jpg")
applied_ai=Image.open(r"D:/Webpage/image/applied_ai.png")
#Rubixe=Image.open(r"D:/Webpage/rubixe_logo.jpg")
experience=Image.open(r"D:/Webpage/image/experience1.jpg")
#certification=Image.open(r"D:/Webpage/certification.jpg")
iabac=Image.open(r"D:/Webpage/image/iabac_logo.jpg")
datamites=Image.open(r"D:/Webpage/image/datamites.png")
hackerrank=Image.open(r"D:/Webpage/image/HackerRank.png")
st.write("##")


#------HEADER SECTION------#
with st.container():
    col1,col2=st.columns(2)
    with col1:
        st.write("##")
        st.header("Hey Guys :wave:")
        st.subheader("I am Kaumudi Katkar ")
        st.write("""
                Aspiring Data Scientist/ Machine Learning Engineer
                | Certified in Data Science
                | Passionate About Data-Driven Solutions""")
    with col2:
        st_lottie(lottie_woman,key='data science')
        #st.image(photo)

st.write("---")
with st.container():
    selected= option_menu(
        menu_title= None,
        options= ['About','Portfolio','Contact'],
        icons= ['person','code-slash','chat-left-text-fill'],
        orientation= 'horizontal'
    )

if selected=='About':

 #-----Skills-----#
    with st.container():
        st.write("###")
        right_column,left_column=st.columns(2)
        with right_column:
            st_lottie(lottie_skills,height=500)

        with left_column:
            col5,col6=st.columns(2)
            with col5:
                st.subheader("Skills Which I have")
                st.write(
                    """
                    - Programming Language \n
                        - Pyhton \n
                        - C++ \n
                    - Technology \n
                        - Machine Learning \n
                        - Deep Learning \n
                    - Libraries \n
                        - Pandas \n
                        - Numpy \n
                        - Seaborn \n
                        - Matplotlib \n 
                    """)
            with col6:
                st.write("###")         
                st.write(
                    """ 
                    - Database skills \n
                        - SQL \n
                        - MySQL \n
                        - Oracle DB \n  
                    - Development Tools & Methodologies \n
                        - Git (Version Control, Git Workflow) \n
                        - Streamlit \n
                    - Data Visualization \n
                        - Microsoft PowerBi \n
                        - Tableau \n            
                    """)
if selected=='Portfolio':  
    st.write("###")
#---Projects---#

    #--- Flight Fare Prediction----#
    with st.container():
        #st.write("---")
        st.header("My Projects")
        image_column,text_column=st.columns((1,2))
        with image_column:
           st.image(fifa,width=300)
        with text_column:
           st.subheader("Fifa20")
           st.write(" Explore football skills from given FIFA 20 data and cluster football players based on their skills.")    
           st.markdown("[Visit Github Repo](https://github.com/Kaumudi919/FiFa20)")


    #--- Flight Fare Prediction----#
    with st.container():
        st.write("###")
        #st.header("My Projects")
    
        col5,col6=st.columns((1,2))
        with col5:
            st.image(flight,width=300)
        with col6:
            st.subheader("Flight Fare Prediction")
            st.write(" The main goal is to create a predictive model which will help the customers to predict future flight prices and plan their journey accordingly.")   
            st.markdown("[Visit Github Repo](https://github.com/Kaumudi919/Flight-Fare-Prediction)")


    #---Texas Salary Prediction---#
    with st.container():
        st.write("###")
        image_column,text_column=st.columns((1,2))
        with image_column:
           st.image(salary,width=300)
        with text_column:
           st.subheader("Texas Salary Prediction")
           st.write(" The objective of this project is to create a predictive model which will help the Texas state government team to know the payroll information of employees of the state of Texas.")    
           st.markdown("[Visit Github Repo](https://github.com/Kaumudi919/Texas-Salary-Prediction)")


    #---Spam Mail Detection---#       

    with st.container():
        st.write("###")
        image_column,text_column=st.columns((1,2))
        with image_column:
           st.image(spam,width=300)
        with text_column:
           st.subheader("Spam Mail Detection")
           st.write(" In this project i have performed feature extraction on the dataset and detected weather the mail is spam or not.")    
           st.markdown("[Visit Github Repo](https://github.com/Kaumudi919/Spam-Message-Detection)")


    #---Amazon Fine Food Reviews Analysis---#

    with st.container():
        st.write("###")
        image_column,text_column=st.columns((1,2))
        with image_column:
           st.image(reviews,width=300)
        with text_column:
           st.subheader("Amazon Fine Food Reviews Analysis")
           st.write("The goal of this project is from given reviews determine whether the reviews is positive or negative..")    
           st.markdown("[Visit Github Repo](https://github.com/Kaumudi919/Amazon-Fine-Food-Reviews-Analysis)")


#---Experience---#
    with st.container():
        st.write("---")
        st.header("Experience")
        #st.write("---")
        st.write("###")

        #with st.container():
        image_column,text_column=st.columns((1,2))
        with image_column:
                st.image(experience,width=300)
        with text_column:
            st.subheader("Data Scientist Intern")
            st.write("Company-Rubixe")
            st.write("January 2024- Present")
            st.write("Working on different projects and performing Data Exploration, Cleaning, preprocessing, visualization and Model building to solve business problems which finds meaningful insights.")
   


        #--- Certification---#

    #with st.container():

        #st.write("---")
        #st.header("Certifications")
        #text_column,image_column=st.columns(2)
        #with text_column:
           # st.write("Certified Data Scientist")
            #st.write("IABAC")   
            #st.markdown("[View](https://acrobat.adobe.com/id/urn:aaid:sc:AP:85ff594d-3405-4485-91cd-1adebf357e66)")
            #st.write("##")
            #st.write("Certified Data Scientist Certification Training")
            #st.write("DataMites")
            #st.markdown("[View](https://acrobat.adobe.com/id/urn:aaid:sc:AP:f79a0aed-c80e-455e-884b-40a77390a489)")
            #with st.container():
        #with image_column:
            #text_column,image_column=st.columns((1,2))
            #with image_column:
                #st.image(certification,width=400)
            #with text_column:
             #   st.subheader("Certified Data Scientist")
              #  st.write("IABAC")   
               # st.markdown("[View](https://acrobat.adobe.com/id/urn:aaid:sc:AP:85ff594d-3405-4485-91cd-1adebf357e66)")
            #st.write("##")
                #st.subheader("Certified Data Scientist Certification Training")
                #st.write("DataMites")
                #st.markdown("[View](https://acrobat.adobe.com/id/urn:aaid:sc:AP:f79a0aed-c80e-455e-884b-40a77390a489)")

    with st.container():
        st.write("---")
        st.header("Certifications")
        st.write("###")
        image_column,text_column=st.columns((1,2))
        with image_column:
            st.image(iabac,width=150)
        with text_column:
            st.subheader("Certified Data Scientist")
            st.write("International Association of Business Analytics Certification (IABAC)")   
            st.markdown("[Certificate of completion](https://acrobat.adobe.com/id/urn:aaid:sc:AP:85ff594d-3405-4485-91cd-1adebf357e66)")

    with st.container():
        #.header("Certifications")
        st.write("###")
        image_column,text_column=st.columns((1,2))
        with image_column:
            st.image(datamites,width=150)
        with text_column:
            st.subheader("Certified Data Scientist certification training")
            st.write("DataMites")   
            st.markdown("[Certificate of completion](https://acrobat.adobe.com/id/urn:aaid:sc:AP:f79a0aed-c80e-455e-884b-40a77390a489)")


    with st.container():
    #st.header("Certifications")
        st.write("###")
        image_column,text_column=st.columns((1,2))
        with image_column:
            st.image(applied_ai,width=150)
        with text_column:
            st.subheader("Applied Machine Learning Course")
            st.write("Applied AI")   
            st.markdown("[Certificate of completion](https://www.appliedaicourse.com/certificate/b98b2cae3c)")



#---Other---#
    with st.container():
        st.write("---")
        st.header("Additional Information")
    #st.write("##")
        with st.container():
            image_column,text_column=st.columns(2)
            with image_column:
                st.image(hackerrank,width=400)
            with text_column:
                st.subheader("HackerRank Profile")
                st.markdown("[View](https://www.hackerrank.com/profile/kaumudikatkar191)")



#---Contact---#

if selected=='Contact':  
    st.write("###")  
    with st.container():
        #st.write("---")
        left_column, right_column = st.columns(2)
        with right_column:
            st.header("Contact me")
            st.write("##")
            st.write("Email Id: katkarkp2017@gmail.com")
            st.write("Connect with me on linkedin:-https://www.linkedin.com/in/kaumudi-katkar-50640b192/""")
            st.write("Here is My GitHub Profile link:- https://github.com/Kaumudi919")
        
        with left_column:
            st_lottie(contact, height=300, key="contact")

   