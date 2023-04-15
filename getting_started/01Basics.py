import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="Streamlit basics", layout='wide')

st.title("Streamlit Basics")

st.title("Working with data")
st.write('Creating tables')
# Creating a table
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

# displaying without calling streamlit.write
df

dataframe = pd.DataFrame(
    np.random.rand(10, 20),
    columns=('col %d' % i for i in range(20))
)
st.write('Displaying using streamlit.dataframe')
# displaying by calling streamlit.dataframe
st.dataframe(dataframe.style.highlight_max(axis=0))

st.write("Displaying by using streamlit.table")
st.table(dataframe)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.write("Display line_chart")
st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)

st.write('Displaying map')
st.map(map_data)

st.title('Working with widgets')
x = st.slider('x')
st.write(x, 'squared is', x * x)

st.write("Working with keys")
st.text_input("Your name", key="name")
st.session_state.name

st.write("Checkbox")
if st.checkbox("Show dataframe"):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    chart_data


st.write("Using selectbox to select from elements in df['first column']")
option = st.selectbox(
    "Which number would you like best?",
    df['first column']
)
st.write("You selected", str(option))

with st.sidebar:
    st.markdown('# Main page')
    add_selectbox = st.selectbox(
        "How would you like to be contacted?",
        ("Email", 'Home phone', 'Mobile phone')
    )
    add_slider = st.slider(
        "Select a range of values",
        0.0, 100.0, (25.0, 75.0)
    )
    st.write(f'Median of {add_slider[0]} and {add_slider[1]}  :  {np.median(np.array(add_slider))}')

left_column, right_column = st.columns(2)
if left_column.button("Press me"):
    st.write("You clicked the button")

with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Griffindor", 'Ravenclaw', 'Hufflepuff', 'Slytherin')
    )
    st.write(f'You are in {chosen} house!')

st.write("Starting a long computation")
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
latest_iteration.text("Process is now done")
