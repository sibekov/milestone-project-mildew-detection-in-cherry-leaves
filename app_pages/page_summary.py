import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. \n"
        f"* Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree," 
        f"* taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew,"
        f"* the employee applies a specific compound to kill the fungus.\n" 
        f"* the model data can be found at https://www.kaggle.com/datasets/codeinstitute/cherry-leaves,\n"
        f"The time spent applying this compound is 1 minute. The company has thousands of cherry trees, "
        f"located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.\n"
        f"**Project Dataset**\n"
        f"* The available dataset contains 2104 healthy leaves and 2104 powdery mildew leaves making a total of 4208 images")
     

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/sibekov/milestone-project-mildew-detection-in-cherry-leaves/blob/main/README.md).")




    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 -  The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.\n"

        f"* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew."
        )


