import streamlit as st
import pickle
import numpy as np
import sklearn

# Function to load the model
def load_model():
    loaded_model = pickle.load(open("liverdisease_model.sav", 'rb'))
    return loaded_model

def normalize(type,val):
    if type=="Age":
        return (val-4.0)/(90.0-4.0)
    elif type=="tbill":
        return (val-0.4)/(75.0-0.4)
    elif type=='dbill':
        return(val-0.1)/(19.7-0.1)
    elif type=='AAP':
        return(val-63.0)/(2110.0-63.0)
    elif type=='SpAA':
        return(val-10.0)/(2000.0-10.0)
    elif type=='SoAA':
        return(val-10.0)/(4929.0-10.0)
    elif type=='tprotein':
        return(val-2.7)/(9.6-2.7)
    elif type=='ALB':
        return(val-0.9)/(5.5-0.9)
    elif type=='A/G ratio':
        return(val-0.3)/(2.8-0.3)


st.set_page_config(page_title="Liver Predictor",page_icon="🧑‍⚕️")
st.title("LIVER DISEASE PREDICTION")
st.sidebar.success("Select a page above")
st.write("---")
st.text("")
#input age
age=st.number_input("Age of patient",min_value=0,max_value=1000)
st.write(age)
st.text("")

#input gender
gender=st.selectbox("Gender",["Select gender","Female","Male","Unkown"],index=0)
st.text("")

#input Total Bilirubin
tbilirubin=st.number_input("Total Bilirubin (mg/dL)",format="%.3f")
st.write(tbilirubin , " mg/dL")
st.text("")

#input Direct Bilirubin
dbilirubin=st.number_input("Direct Bilirubin (mg/dL)",format="%.3f")
st.write(dbilirubin ," mg/dL")
st.text("")

#input  Alkphos Alkaline Phosphotase
alkphos_alk_phos=st.number_input("Alkphos Alkaline Phosphotase(IU/L)",format="%.3f")
st.write(alkphos_alk_phos ," IU/L")
st.text("")

#input  Sgpt Alamine Aminotransferase
sgt_Alam_amino=st.number_input("Sgpt Alamine Aminotransferase(Units per Liter of serum)",format="%.3f")
st.write(sgt_Alam_amino ," Units per Liter of serum")
st.text("")

#input Sgot Aspartate Aminotransferase
sgot_asp_amino=st.number_input("Sgot Aspartate Aminotransferase(Units per Liter of serum)",format="%.3f")
st.write(sgot_asp_amino ," Units per Liter of serum")
st.text("")

#input Total Protiens
tprotein=st.number_input("Total Protiens(g/dL)",format="%.3f")
st.write(tprotein ," g/dL")
st.text("")

#input ALB Albumin
alb=st.number_input("Albumin(g/dL)",format="%.3f")
st.write(alb ," g/dL")
st.text("")

# input A/G Ratio Albumin and Globulin Ratio
ag_ratio=st.number_input("A/G Ratio Albumin and Globulin Ratio",format="%.3f")
st.write(ag_ratio)
st.text("")

adjusted_feature_list=[normalize("Age",age),normalize("tbill",tbilirubin),normalize("dbill",dbilirubin),
                       normalize("AAP",alkphos_alk_phos),normalize("SpAA",sgt_Alam_amino),normalize("SoAA",sgot_asp_amino),
                       normalize("tprotein",tprotein),normalize("ALB",alb),normalize("A/G ratio",ag_ratio),]

user_input=np.array(adjusted_feature_list).reshape(1,-1)


if st.button("PREDICT"):
    st.text("")
    st.subheader(("RESULT"))
    loaded_model=load_model()
    prediction=loaded_model.predict(user_input)
    st.write("Prediction")
    result=""
    if prediction==[[1]]:
        result="The patient HAS Liver Disease."
    elif prediction == [[0]]:
        result="The patient DOES NOT HAVE Liver Disease."

    st.code(result)
    st.text("")

    


