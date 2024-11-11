import streamlit as st
import pandas as pd

def painting_work():
    painting_work_expander =  st.expander("Painting Work", expanded= False, icon=":material/star:")
    if painting_work_expander:
        # painting_work_expander.markdown("##### Enter tiles area in square feet")
        painting_work_form = painting_work_expander.form(key="painting_work_form")
        painting_work_form_container = painting_work_form.container(border=True)  

        items_list = ["Exteriror Paint", "Interior Paint","Wall Putty","Wall Primer","Enamal Paint","Wood Warnish","painting_work_cost"]

        def store_values(pop=True):
                values_list = [st.session_state["Exteriror Paint"],st.session_state["Interior Paint"],st.session_state["Wall Putty"],st.session_state["Wall Primer"],st.session_state["Enamal Paint"],st.session_state["Wood Warnish"],st.session_state.painting_work_cost]
                painting_widgets_df = pd.DataFrame({"Item": items_list,
                                  "Quantity": values_list,
                                  })
                painting_widgets_df.set_index("Item", inplace=True)
                st.session_state.painting_widgets_df = painting_widgets_df
                if pop:
                    st.toast("Done!", icon="👍")                

        def load_values(items_list):
                for item in items_list:
                     st.session_state[item] = st.session_state.painting_widgets_df.loc[item]["Quantity"]

        if "painting_widgets_df" in st.session_state:
                load_values(items_list)   

        col1, col2, col3, col4, col5, col6 = painting_work_form.columns(6)

        exteriror_paint = col1.number_input("Exterior Paint(litre)", min_value=0, max_value=10000, step=10, key="Exteriror Paint")
        interior_paint = col2.number_input("Interior Paint(litre)", min_value=0, max_value=10000, step=10, key="Interior Paint")
        wall_putty = col3.number_input("Putty (Kg)", min_value=0, max_value=10000, step=5, key="Wall Putty")
        wall_primer = col4.number_input("Primer(litre)", min_value=0, max_value=10000, step=10, key="Wall Primer")
        enamal_paint = col5.number_input("Enamal Paint(litre)", min_value=0, max_value=10000, step=5, key="Enamal Paint")                
        wood_warnish = col6.number_input("Wood warnish(litre)", min_value=0, max_value=10000, step=2, key="Wood Warnish")
    
        col1.write("")
        painting_work_cost = painting_work_form.number_input("Total Cost of Painting work including meterial and labour", min_value=0, max_value=10000000, step=1000, key="painting_work_cost")
        # painting_work_form.form_submit_button(label="Update", on_click=store_values)

        store_values(False)
        # store_edited_df()
        painting_work_form.form_submit_button(label="Save", type="primary", on_click=store_values)
