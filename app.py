#streamlit 
# project by unit_converter

import streamlit as st

st.title("unit converter")
st.write("easily convert between different unit of lenght , weight, or temperature.")

# bar menu
conversion_type= st.sidebar.selectbox("choose measurement type",["lenght","weight","temperture"])
value = st.number_input("enter your value ",value =0.0,min_value=0.0)
col1, col2 = st.columns(2)

if conversion_type == "lenght":
    with col1:
        from_unit = st.selectbox("from",["meters","kilograms","centimeters","milimetrs","miles","yards","inches"])
    with col2:
        to_unit= st.selectbox("to",["meters","kilograms","centimeters","milimeters","miles","yards","inches"])

elif conversion_type=="weight" :
    with col1:
        from_unit=st.selectbox("from",["kilograms","grams","millimeters","pounds","ounces"])  
    with col2:
        to_unit= st.selectbox("to",["kilograms","grams","millimeters","pounds","ounces"]) 
elif conversion_type== "temperature":
    with col1:
        from_unit=st.selectbox("from",["celsius","kelvin","farenheit"])
    with col2:
        to_unit=st.selectbox("to",["celsius","kelvin","farenheit"])


def lenght_converter(value,from_unit,to_unit):
    lenght_units={
        "meters":1,"kilograms":0.001,"centimeters":100,"millimeters":1000,
         "miles":0.000621371,"yards":1.09361,"inches":39.37,
    }
    return (value/lenght_units[from_unit])*lenght_units[to_unit]

def weight_converter(value,from_unit,to_unit):
    weight_units={
        "kilograms":1, "grams" :1000,"millimeters":1000000,"pounds":2.2046, "ounces":35.27,
    }
    return (value/weight_units[from_unit])*weight_units[to_unit]

def temperature_converter (value,from_unit,to_unit):
    if from_unit== "celsius":
        return(value* 9/5 +32)if to_unit=="farenheit"else value +273.15 if to_unit== "kelvin" else value
    elif from_unit== "farenheit":
        return (value - 32)* 5/9 if to_unit == "celsius" else(value -32)* 5/9 +273.15 if to_unit == "kelvin"else value
    elif from_unit == "kelvin":
        return (value - 273.15)if to_unit== "celsius" else (value - 273.15) * 9/5 +32 if to_unit=="farenheit" else value
    return value


# button conversion

if st.button("convert"):
    if conversion_type == "lenght":
        result = lenght_converter(value , from_unit,to_unit)
    elif conversion_type =="weight":
        result = weight_converter(value,from_unit,to_unit)
    elif conversion_type =="temperature":
        result = temperature_converter(value, from_unit,to_unit)


    st.write(f"{value}{from_unit}= {result}{to_unit}")

st.write("""    created by syeda Sehar Fatima    """)