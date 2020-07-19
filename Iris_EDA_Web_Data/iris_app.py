import streamlit as st
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image,ImageFilter,ImageEnhance



def main():
    st.title('Iris EDA APP')
    st.subheader('EDA Web App with Streamlit')
    st.markdown("""
    	#### Description
    	+ This is a simple Exploratory Data Analysis  of the Iris Dataset depicting the various species built with Streamlit.
    	#### Purpose
    	+ To show a simple EDA of Iris using Streamlit framework. 
    	""")
    #code beloow
    my_dataset = "iris.csv"
    @st.cache(persist=True)
    def explore_data(dataset):
        df = pd.read_csv(os.path.join(dataset))
        return df

    # load the dataset
    data = explore_data(my_dataset)

    if st.checkbox("Preview DataFrame"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())
        else:
            st.write(data.head(2))

    # Show Entire DataFrame
    if st.checkbox("Show All DataFrame"):
        st.dataframe(data)

    #Show All Columns Name
    if st.checkbox("Show All Column Names"):
        st.text("Columns:")
        st.write(data.columns)

    data_dim = st.radio('What Dimension Do you want to show',('Rows','Columns'))
    if data_dim == 'Rows':
        st.text("Showing Length of Rows")
        st.write(len(data))

    if data_dim == 'Column':
        st.text("Showing Length of Columns")
        st.write(data.shape[1])

    # SHow summary of Dataset
    if st.checkbox("Show Summary of Dataset")
        st.write(data.describe())

    species_option = st.selectbox('Select Columns',('sepal_length','sepal_width','petal_length','petal_width','species'))
    if species_option == 'sepal_length':
        st.write(data['sepal_length'])
    elif species_option =='sepal_width':
        st.write(data['sepal_width'])
    elif species_option =='petal_length':
        st.write(data['petal_length'])
    elif species_option =='petal_width':
        st.write(data['petal_width'])
    elif species_option =='species':
        st.write(data['species'])
    else:
        st.write("Select A Column")

    #show plots
    if st.checkbox("Simple bar plot with Matplotlib"):
        data.plot(kind='bar')
        st.pyplot()

    if st.checkbox("Simple Correlation with Matplotlib"):
        plt.matshow(data.corr())
        st.pyplot()

    if st.checkbox("Simple Correlation with Seaborn"):
        st.write(sns.heatmap(data.corr(),annot=True))
        st.pyplot()

    #Show plots
    if st.checkbox("Bar plot of Groups or Counts"):
        v_counts = data.groupby('species')
        st.bar_chart(v_counts)


    #Iris Image Manipulation
    @st.cache
    def load_img(img):
        im = Image.open(os.path.join(img))
        return im

    species_type = st.radio('What is the Iris Species do you want to see?',('Satosa','Versicolor','Virginica'))
    if species_type =='Setosa':
        st.text("Showing Iris Setosa")
        st.image(load_img('imgs/iris_setosa.jpg'))

    elif species_type =='Versicolor':
        st.text("Showing Iris Versicolor")
        st.image(load_img('imgs/iris_versicolor.jpg'))

    elif species_type == 'Virginica':
        st.text("Showing Iris Virginica")
        st.image(load_img('imgs/iris_virginica.jpg'))

        # Show Image or Hide Image with Checkbox
    if st.checkbox("Show Image/Hide Image"):
        my_image = load_image('iris_setosa.jpg')
        enh = ImageEnhance.Contrast(my_image)
        num = st.slider("Set Your Contrast Number", 1.0, 3.0)
        img_width = st.slider("Set Image Width", 300, 500)
        st.image(enh.enhance(num), width=img_width)

        # About
    if st.button("About App"):
        st.subheader("Iris Dataset EDA App")
        st.text("Built with Streamlit")
        st.text("Thanks to the Streamlit Team Amazing Work")

    if st.checkbox("By"):
        st.text("Ehtisham Raza")
        st.text("EhtishamRaza@gmail.com")

if __name__ == "__main__":
        main()