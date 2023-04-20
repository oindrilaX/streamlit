#importing streamlit library
import streamlit as st

from streamlit_option_menu import option_menu


# 1. as sidebar menu
with st.sidebar:
     selected = option_menu(
          menu_title="Main Menu",#required
          options=["Photo","Video"],#required
          menu_icon="cast",
          default_index=0,


     )
if selected =="Photo":
     st.title(f"You have selected {selected}")
     image_file  = st.file_uploader("Upload Images",type=["png","jpg","jpeg"])
     if image_file is not None:
      #see details 
      st.write(type(image_file))
 #Enter the caption here
     image_caption = st.text_input ("Enter a caption for the image (optional)", value="image_caption")

if selected =="Video":
     st.title(f"You have selected {selected}")
     video_file = st.file_uploader("Choose a video ", type=["mp4","wmv" "avi"])
     if video_file is not None:
      #see details 
       st.write(type(video_file))
 #Enter the caption here
     video_caption = st.text_input ("Enter a caption for the video (optional)", value="video_caption")






