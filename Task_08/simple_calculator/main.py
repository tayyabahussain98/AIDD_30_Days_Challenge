import streamlit as st
import calculator_logic

def main():
    st.title("Simple Calculator")

    if 'num1' not in st.session_state:
        st.session_state.num1 = 0.0
    if 'num2' not in st.session_state:
        st.session_state.num2 = 0.0
    if 'result' not in st.session_state:
        st.session_state.result = None
    if 'operation' not in st.session_state:
        st.session_state.operation = "Add"

    col1, col2 = st.columns(2)

    with col1:
        st.session_state.num1 = st.number_input("Enter first number", value=st.session_state.num1, key="input1")
    with col2:
        st.session_state.num2 = st.number_input("Enter second number", value=st.session_state.num2, key="input2")

    operation_buttons = st.columns(4)
    with operation_buttons[0]:
        if st.button("Add", key="btn_add"): st.session_state.operation = "Add"
    with operation_buttons[1]:
        if st.button("Subtract", key="btn_sub"): st.session_state.operation = "Subtract"
    with operation_buttons[2]:
        if st.button("Multiply", key="btn_mul"): st.session_state.operation = "Multiply"
    with operation_buttons[3]:
        if st.button("Divide", key="btn_div"): st.session_state.operation = "Divide"

    st.write(f"Selected Operation: {st.session_state.operation}")

    if st.button("Equals", key="btn_equals"):
        if st.session_state.operation == "Add":
            st.session_state.result = calculator_logic.add(st.session_state.num1, st.session_state.num2)
        elif st.session_state.operation == "Subtract":
            st.session_state.result = calculator_logic.subtract(st.session_state.num1, st.session_state.num2)
        elif st.session_state.operation == "Multiply":
            st.session_state.result = calculator_logic.multiply(st.session_state.num1, st.session_state.num2)
        elif st.session_state.operation == "Divide":
            st.session_state.result = calculator_logic.divide(st.session_state.num1, st.session_state.num2)

    if st.button("Clear", key="btn_clear"):
        st.session_state.num1 = 0.0
        st.session_state.num2 = 0.0
        st.session_state.result = None
        st.session_state.operation = "Add"

    if st.session_state.result is not None:
        st.header("Result")
        st.subheader(st.session_state.result)

if __name__ == "__main__":
    main()
