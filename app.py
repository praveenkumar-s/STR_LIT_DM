import streamlit as st


st.write("""
# Hike Karadi
a calculator for hike percentage
""")

current_value = st.text_input('Current base salary','1000000')
recomended_bonus = float(current_value)*0.15
st.write("Current Base Pay:   {0}".format(current_value))
st.write("Current Bonus Pay:  {0}".format(recomended_bonus))
st.write("Total: "+ str(float(current_value)+recomended_bonus))
percentage = st.slider('slider_pc',0.0,100.0,12.0,0.10)
new_base_pay = float(current_value)+((percentage/100)*float(current_value))
new_bonus = new_base_pay*0.15
st.write("Updated Base Pay:   {0}".format(str(new_base_pay)))
st.write("Updated Bonus Pay:  {0}".format(str(new_bonus)))
st.write("Total: "+ str(new_base_pay+recomended_bonus))



