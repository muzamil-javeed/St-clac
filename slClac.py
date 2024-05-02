import streamlit as st

st.title(":red[Simple Calculator]")
st.markdown(" :red[---------------------------------------------------------------------------------------------------------------------------------------------] ")


container=st.container(height=(50),border=True)

def calculator():
    
    if 'expression' not in st.session_state:
        st.session_state.expression = ""
    expression = st.empty()
    display = st.empty()
    st.write(":red[---------------------------------------------------------------------------------------------------------------------------------------------]")
    
    def update_display(keys):
        st.session_state.expression += str(keys)
        container.write(st.session_state.expression)
    

    def clear_display():
        st.session_state.expression = ""
        container.write(" ")
    def clear_one():
        st.session_state.expression= st.session_state.expression[:-1]
        container.write(st.session_state.expression)
    col1, col2, col3,col4 = st.columns(4)
    
    with col1:
        if st.button("7"):
            update_display(7)
        if st.button("4"):
            update_display(4)
        if st.button("1"):
            update_display(1)
        if st.button("."):
            update_display(".")
    
    
   
    with col2:
        if st.button("8"):
            update_display(8)
        if st.button("5"):
            update_display(5)
        if st.button("2"):
            update_display(2)
        if st.button("0"):
          update_display(0)
        if st.button(":red[AC]"):
           clear_display()
    
    
    with col3:
        if st.button("9"):
            update_display(9)
        if st.button("6"):
            update_display(6)
        if st.button("3"):
           update_display(3)
        if st.button("%"):
            update_display("%")
        if st.button("C"):
          clear_one()
    
    
    with col4:
        if st.button(":heavy_division_sign:"):
            update_display("/")
        if st.button(":heavy_multiplication_x:"):
            update_display("*")
        if st.button(":heavy_minus_sign:"):
            update_display("-")
        if st.button(":heavy_plus_sign:"):
            update_display("+")
        if st.button("√"):
            
            update_display("**")
    
    with col1:
       if st.button("🟰"):
         try:
            result = eval(st.session_state.expression)
            container.write( result )
         except ZeroDivisionError:
            container.write("Error: Zero division")
         except:
            container.write("Error: Input Values First ")

    st.markdown('''<style>
     
         
         .st-emotion-cache-7ym5gk.ef3psqc12
         {
             width:50px
         }
     
     .st-emotion-cache-19rxjzo.ef3psqc12{
         width:50px;}
     .st-emotion-cache-ocqkz7.e1f1d6gn5{
         font-size=24px;
         border:solid 	#ff5e5e 1px;
         border-radius:8%;
         
         padding-left:5rem;
         padding-top:2rem;
         padding-bottom:2rem;
         
         
     }
     .st-emotion-cache-183lzff{
             font-size: 30px;

     }
      </style>          
''',unsafe_allow_html=True)

calculator()


