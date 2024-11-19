import streamlit as st

from sqlalchemy.sql import text, select
conn = st.connection('counter_db', type='sql')

def increment_counter_not_in_use():
    if "visiter_counted" not in st.session_state:
        with conn.session as s:
            s.execute(text("CREATE TABLE IF NOT EXISTS counter (id INTEGER,curcount INTEGER);"))
            db_count = conn.query("select curcount from counter;")
            # print(db_count)
            if db_count['curcount'].iloc[0] > 0:
                new_count = (db_count["curcount"].iloc[0]) + 1
                s.execute(text("UPDATE counter SET curcount=:n where id=0;"),{"n": new_count })
                s.commit()
                st.session_state["visiter_counted"] = True
                st.session_state["visitor_count"] = new_count

            else: 
                s.execute(
                        s.execute("INSERT INTO counter (curcount) VALUES (:n);", {"n": 1})

                    )
                s.commit()
                st.session_state["visiter_counted"] = True

count = conn.query('select curcount from counter')
st.session_state["visitor_count"] = count['curcount'].iloc[0]
