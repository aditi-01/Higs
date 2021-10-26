import streamlit as st
from model import predict_class
import numpy as np

st.set_page_config(page_title="Higgs Boson Prediction  App", layout="wide")


with st.form("prediction_form"):

    st.header("Enter the Deciding Factors:")

    DER_sum_pt = st.number_input("DER_sum_pt: ")
    DER_pt_ratio_lep_tau = st.number_input("DER_pt_ratio_lep_tau: ")
    PRI_met_sumet = st.number_input("PRI_met_sumet: ")
    PRI_jet_num = st.number_input("PRI_jet_num: ", min_value=0, max_value=3, value=0,format="%d")
    Weight = st.number_input("Weight: ")

    submit_val = st.form_submit_button("Predict Class")

if submit_val:
    # If submit is pressed == True
    attribute = np.array([DER_sum_pt, DER_pt_ratio_lep_tau, PRI_met_sumet,
                        PRI_jet_num, Weight]).reshape(1,-1)


    if attribute.shape == (1,5):
        print("attrubutes valid")
        

        value = predict_class(attributes= attribute)
        if value==1:
            p='b'
        else:
            p='s'

        st.header("Here are the results:")
        st.success(f"The Class predicted is {p} ")