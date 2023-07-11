import streamlit as st
import numpy as np
import pandas as pd


def generate_random_dataframe(m, n):
    # Generate the random numbers using NumPy
    random_data = np.random.rand(n, m)

    # Create the DataFrame using Pandas
    df = pd.DataFrame(random_data)

    return df


# Example usage
m = 4  # Number of columns
n = 5  # Number of rows
random_df = generate_random_dataframe(m, n)
random_df

# st.line_chart(data=None, *, x=None, y=None, width=0, height=0, use_container_width=True)
st.line_chart(data=random_df)
