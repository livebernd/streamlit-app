# 1. Add the streamlit library to the project
import streamlit as st

# Add the title to the App
st.title('My Awesome App')

# 3. Run the App
# open the local terminal
# cd into the directory where this file is located: cd Chapter5_GUI
# and run the following command: streamlit run streamlit_intro.py

# 4. Header
st.header('This is a header')

# 5. Subheader
st.subheader('This is a Subheader')

# 6. Text
st.text('This is some text.')

# 7. Markdown
st.markdown('This is some Markdown.')

# 8. Button
st.button('This is a Button')

#9. Checkbox
st.checkbox('This is a Checkbox')

#10. Radio Button
st.radio('Radio', ['Option 1', 'Option 2', 'Option 3'])

#11. Selectbox
st.selectbox('Select', ['Option 1', 'Option 2', 'Option 3'])

#12. File Uploader 
st.file_uploader('File uploader', type=['png','jpg'])

#13. Color Picker
st.color_picker('Color picker')

#14. Date Input
st.date_input('Date input')

#15. Time Input
st.time_input('Time input')

#16. Text Input
st.text_input('Text input', placeholder ='Enter your Name')

#17. Number Input
st.number_input('Number input', min_value=1, max_value=100, value=50)

#18. Text Area
st.text_area('Text area', placeholder= 'Enter your message here')

#19. Slider
st.slider('Slider', min_value=0, max_value=100, value= 50)

""" #20. Progress Bar
import time
my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete +1)

#21. Spinner
    with st.spinner('Waiting...'):
        time.sleep(2) """

# 22. Adding Columns
col1, col2 = st.columns(2)

with col1:
    st.header('Column2')
    st.text('Some Text in Columns 1')

with col2:
    st.header('Column1')
    st.text('Some Text in Column 2')

# Add Image from file uploader and display it
#from PIL import Image
image = st.file_uploader('File uploader', type=['png','jpg'])
if image:
    st.image(image, caption='Uploaded Image', use_column_width=True)


