import streamlit as st 

st.title( "My First Streamlit App - Power Calculator" )
st.write( "Hello, Enter a number to calculate its power:" )


number = st.number_input( "Enter a number:", value = 1.0, step = 1.0  )

power = st.number_input( "Enter the power to raise the number to:", value = 2.0, step = 1.0 )

result = number ** power

st.write( f"The result of {number} raised to the power of {power} is: {result}" )
st.write( "Thank you for using the Power Calculator!" )
