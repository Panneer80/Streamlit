import streamlit as st


st.subheader("Formulas")
st.divider()
col1, col2,col3 = st.columns(3, gap="large")
with col1:
    st.image("modules/civil_boq/images/calculators.jpg", width=300)
with col2:
    st.markdown("##### Formulas used in this website are taken from www.civil-engineering-calculators.com")
    st.page_link("https://www.civil-engineering-calculators.com/Quantity-Estimator/Cement-Concrete-Calculator", label="Concreate Calculator", icon=":material/calculate:")
    st.page_link("https://www.civil-engineering-calculators.com/Quantity-Estimator/Brick-Calculator", label="Masonary Calculator", icon=":material/calculate:")
    st.page_link("https://www.civil-engineering-calculators.com/Quantity-Estimator/Plastering-Calculator", label="Plastering Calculator", icon=":material/calculate:")
    st.page_link("https://www.civil-engineering-calculators.com/Quantity-Estimator/Steel-Weight-Calculator", label="Steel Calculator", icon=":material/calculate:")
