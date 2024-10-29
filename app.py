import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from typing import Tuple, List

# --- DATA LOADING AND PROCESSING ---
def load_data(file_path: str) -> pd.DataFrame:
    """Load and preprocess JEF data from Excel file."""
    try:
        jef_data = pd.read_excel(file_path)
    except FileNotFoundError:
        st.error("Data file not found. Please check file path.")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"An error occurred while loading the data: {e}")
        return pd.DataFrame()
    
    # Convert age and IQ to numeric, handling errors
    jef_data['age'] = pd.to_numeric(jef_data['age'], errors='coerce')
    jef_data['est_IQ'] = pd.to_numeric(jef_data['est_IQ'], errors='coerce')
    
    # Remove rows with NaN values in critical columns
    jef_data = jef_data.dropna(subset=['age', 'est_IQ'])
    
    # Remove unnecessary columns
    jef_df = jef_data.drop(['experimenter', 'study', 'participant'], axis=1, errors='ignore')
    return jef_df

# --- STATISTICAL CALCULATIONS ---
def calculate_stats(filtered_df: pd.DataFrame, patient_scores: List[float]) -> Tuple[pd.DataFrame, List[float]]:
    """Calculate means, SDs, and z-scores for JEF metrics."""
    if filtered_df.empty:
        st.warning("No data available for the selected age and IQ range.")
        return pd.DataFrame(), []
    
    # Calculate means and SDs for filtered data
    means = filtered_df.iloc[:, :9].mean()
    sds = filtered_df.iloc[:, :9].std()
    
    # Calculate z-scores for patient, handling cases where SD is zero
    z_scores = []
    for score, mean, sd in zip(patient_scores, means, sds):
        if sd == 0 or np.isnan(sd):
            z_scores.append(np.nan)  # Avoid division by zero
        else:
            z_scores.append((score - mean) / sd)
    
    # Create descriptive statistics dataframe
    jef_constructs = ["PL", "PR", "ST", "CT", "AT", "EBPM", "ABPM", "TBPM", "AVG"]
    stats_df = pd.DataFrame({
        'construct': jef_constructs,
        'mean': means,
        'sd': sds,
        'z_score': z_scores
    })
    
    return stats_df, z_scores

# --- PLOTTING ---
def create_zscore_plot(stats_df: pd.DataFrame, age_range: Tuple[float, float], 
                      iq_range: Tuple[float, float], n_samples: int) -> go.Figure:
    """Create z-score visualization plot."""
    fig = go.Figure()
    
    # Add bars
    fig.add_trace(go.Bar(
        x=stats_df['construct'],
        y=stats_df['z_score'],
        marker_color='#CC3333',
        marker_line_color='black',
        marker_line_width=1,
        width=0.6
    ))
    
    # Add reference lines
    fig.add_hline(y=-2, line_dash="dash", line_color="#0099FF", line_width=2)
    fig.add_hline(y=0, line_color="black", line_width=0.5)
    
    # Update layout
    fig.update_layout(
        yaxis_title="Z-score",
        yaxis_range=[-5, 1],
        yaxis_tickmode='linear',
        yaxis_dtick=1,
        xaxis_tickmode='array',
        xaxis_ticktext=stats_df['construct'],
        xaxis_tickvals=list(range(len(stats_df))),
        plot_bgcolor='white',
        showlegend=False,
        margin=dict(t=50),
        annotations=[
            dict(text=f"N = {n_samples}", x=1, y=-4.8, showarrow=False, xanchor='right'),
            dict(text=f"Age range: {age_range[0]} ~ {age_range[1]}", x=1, y=-4.4, showarrow=False, xanchor='right'),
            dict(text=f"IQ range: {iq_range[0]} ~ {iq_range[1]}", x=1, y=-4, showarrow=False, xanchor='right')
        ]
    )
    
    return fig

# --- MAIN APP ---
def main():
    st.title('JEF Assessment System')
    
    # Load data
    jef_df = load_data("JEF.data.xlsx")  # Update path as needed
    if jef_df.empty:
        return
    
    # Sidebar inputs
    st.sidebar.title('Input Parameters')
    
    # Age and IQ sliders
    age_range = st.sidebar.slider(
        'Age',
        min_value=int(jef_df['age'].min()),
        max_value=int(jef_df['age'].max()),
        value=(18, 120)
    )
    
    iq_range = st.sidebar.slider(
        'IQ',
        min_value=int(jef_df['est_IQ'].min()),
        max_value=int(jef_df['est_IQ'].max()),
        value=(70, 180)
    )
    
    # Score inputs
    col1, col2 = st.sidebar.columns(2)
    
    with col1:
        pl = st.number_input('PL', value=50)
        st_score = st.number_input('ST', value=50)
        at = st.number_input('AT', value=0)
        abpm = st.number_input('ABPM', value=75)
    
    with col2:
        pr = st.number_input('PR', value=100)
        ct = st.number_input('CT', value=25)
        ebpm = st.number_input('EBPM', value=25)
        tbpm = st.number_input('TBPM', value=50)
    
    avg = st.sidebar.number_input('AVG', value=46.9)
    
    calculate = st.sidebar.button('Calculate')
    
    if calculate:
        # Filter data based on age and IQ
        filtered_df = jef_df[
            (jef_df['age'].between(age_range[0], age_range[1])) &
            (jef_df['est_IQ'].between(iq_range[0], iq_range[1]))
        ]
        
        # Get patient scores
        patient_scores = [pl, pr, st_score, ct, at, ebpm, abpm, tbpm, avg]
        
        # Validate patient scores (ensure no NaN values)
        if any(pd.isna(patient_scores)):
            st.error("Please enter valid scores for all parameters.")
            return
        
        # Calculate statistics
        stats_df, z_scores = calculate_stats(filtered_df, patient_scores)
        if stats_df.empty:
            return
        
        # Create and display plot
        fig = create_zscore_plot(
            stats_df,
            age_range,
            iq_range,
            len(filtered_df)
        )
        
        st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
