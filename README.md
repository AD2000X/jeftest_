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
