# JEF Assessment System

This is a Streamlit application for visualizing and analyzing JEF metrics using z-scores.

## Project Structure
- `app.py`: The main application script for the Streamlit dashboard.
- `JEF.data.xlsx`: The Excel file containing the input data.
- `requirements.txt`: Contains the necessary dependencies to run this application.

## How to Run
1. Clone the repository to your local machine:
   ```
   git clone <your-repository-url>
   ```
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

## Deployment
To deploy this application on Streamlit Cloud:
1. Push all changes to the GitHub repository.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and create a new app linked to this repository.
3. Select the `main` branch and specify `app.py` as the entry point.
4. Click 'Deploy' and wait for the deployment to complete.

## Note
Make sure that the `JEF.data.xlsx` file is included in your repository if it is needed for the initial data load.


# JEF Assessment System Project Overview

## Main Functionalities

- **Loading and preprocessing JEF assessment data**
- **Filtering data based on age and IQ ranges**
- **Calculating statistical measures (means, standard deviations, Z-scores)**
- **Generating interactive Z-score visualizations**
- **Providing a user-friendly web interface for parameter input and results display**

## Technologies and Tools

### Streamlit
- `import streamlit as st` for building web applications and interactive controls.
- Functions like `st.title()` and `st.sidebar.*()` create user interfaces and sidebar input fields.
- `st.error()`, `st.warning()`, `st.number_input()`, and `st.button()` handle error messages, warnings, user parameter inputs, and calculation trigger buttons.
- `st.plotly_chart()` displays Plotly-generated charts in the interface.

### Pandas
- `import pandas as pd` for data reading and preprocessing.
- `pd.read_excel()` reads Excel format data.
- `DataFrame` objects handle data filtering and processing using methods like `dropna()`, `drop()`, `to_numeric()`.
- Statistical calculations using methods like `DataFrame.mean()` and `DataFrame.std()`.

### Numpy
- `import numpy as np` for numerical computations and basic array operations.
- `np.isnan()` checks for NaN values.
- Performs fundamental mathematical operations, such as z-score calculations.

### Plotly Graph Objects
- `import plotly.graph_objects as go` for creating interactive data visualizations.
- `go.Figure()` creates plotting objects.
- Methods like `go.Bar()` and `fig.add_hline()` draw bar charts and reference lines.

### Typing
- `from typing import Tuple, List` for providing type hints to enhance code readability and maintainability.
- Uses `Tuple` and `List` to add type annotations for function parameters and return values.
- Helps developers understand data structures and expected input/output types.
