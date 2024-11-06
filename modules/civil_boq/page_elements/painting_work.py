import streamlit as st
import pandas as pd

def painting_work():
    painting_work_expander =  st.expander("Painting Work", expanded= False, icon=":material/star:")
    if painting_work_expander:
        # painting_work_expander.markdown("##### Enter tiles area in square feet")
        painting_work_form = painting_work_expander.form(key="painting_work_form")
        painting_work_form_container = painting_work_form.container(border=True)  

        items_list = ["exteriror_paint", "interior_paint","wall_putty","wall_primer","enamal_paint","wood_warnish","painting_work_cost"]

        def store_values():
                values_list = [st.session_state.exteriror_paint,st.session_state.interior_paint,st.session_state.wall_putty,st.session_state.wall_primer,st.session_state.enamal_paint,st.session_state.wood_warnish,st.session_state.painting_work_cost]
                painting_widgets_df = pd.DataFrame({"Item": items_list,
                                  "Value": values_list,
                                  })
                painting_widgets_df.set_index("Item", inplace=True)
                st.session_state.painting_widgets_df = painting_widgets_df

        def load_values(items_list):
                for item in items_list:
                     st.session_state[item] = st.session_state.painting_widgets_df.loc[item]["Value"]

        if "painting_widgets_df" in st.session_state:
                load_values(items_list)   

        col1, col2, col3, col4, col5, col6 = painting_work_form.columns(6)

        exteriror_paint = col1.number_input("Exterior Paint(litre)", min_value=0, max_value=10000, step=10, key="exteriror_paint")
        interior_paint = col2.number_input("Interior Paint(litre)", min_value=0, max_value=10000, step=10, key="interior_paint")
        wall_putty = col3.number_input("Putty (Kg)", min_value=0, max_value=10000, step=5, key="wall_putty")
        wall_primer = col4.number_input("Primer(litre)", min_value=0, max_value=10000, step=10, key="wall_primer")
        enamal_paint = col5.number_input("Enamal Paint(litre)", min_value=0, max_value=10000, step=5, key="enamal_paint")                
        wood_warnish = col6.number_input("Wood warnish(litre)", min_value=0, max_value=10000, step=2, key="wood_warnish")
    
        col1.write("")
        painting_work_cost = painting_work_form.number_input("Total Cost of Painting work including meterial and labour", min_value=0, max_value=10000000, step=1000, key="painting_work_cost")
        # painting_work_form.form_submit_button(label="Update", on_click=store_values)


        # store_edited_df()
        if painting_work_form.form_submit_button(label="Save"):
            store_values()
            st.toast("Done!", icon="👍")        