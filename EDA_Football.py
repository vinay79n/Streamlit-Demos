import streamlit as st
import pandas as pd
import numpy as np
import base64 
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")



st.title('NFL Football Stats (Rushing) explorer')

st.markdown("""
This app performs simple webscraping of NFL Football player stats data (focusing on Rushing)!
* **Python libraries:** base64, pandas, streamlit, numpy, matplotlib, seaborn
* **Data source:** [pro-football-reference.com](https://www.pro-football-reference.com/).
""")

st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1990,2022))))

# Web Scarping of NFL Player Stats 
# https://www.pro-football-reference.com/years/2022/rushing.htm

@st.cache
def load_adat(year):
    url = "https://www.pro-football-reference.com/years/" + str(year) + "/rushing.htm"
    html = pd.read_html(url, header=1)  # pd.read_html is a function in the pandas library of Python that 
                                        # is used to parse HTML tables in web pages into pandas dataframes.
                                        # header = 0 specifies to use the first row as the column names of the df.
    df = html[0] # Extracts the first table from the page
    raw = df.drop(df[df.Age == "Age"].index) # Deletes repeating headers in content
    raw  = raw.fillna(0) # replacing missing or NaN values with 0(zero)
    playerstats = raw.drop(['Rk'],axis=1) # dropped the "Rk" col
    return playerstats
playerstats = load_adat(selected_year)  # Finally, we apply the load_data function 
                                        # (webScraping and data preprocessing) on the selected year 

# Sidebar - Team selection
sorted_unique_team = sorted(playerstats.Tm.unique()) # sorted all unique team names
selected_team = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team)
# defined a multiselect UI element in the side bar for the user to select / de-select the teams he/she 
# wants or not wants

# Sidebar - Position selection
unique_pos = ['RB','QB','WR','FB','TE']
selected_pos = st.sidebar.multiselect('Position', unique_pos, unique_pos)
# defined a multiselect UI element in the side bar for the user to select / de-select 
# the player positions he/she # wants or not wants

# Filtering data
df_selected_team = playerstats[(playerstats.Tm.isin(selected_team)) & (playerstats.Pos.isin(selected_pos))]
# df_selected_team (& position also) will be used to displaye the player stats on the main page which is
# filtered on the basis of what the user is selected (Team and position)

st.header('Display Player Stats of Selected Team(s)')
st.write('Data Dimension: ' + str(df_selected_team.shape[0]) + ' rows and ' + str(df_selected_team.shape[1]) + ' columns.')
# the data dimension is just displaying the shape and no. of columns of teh filtered df that we made based
# on what user has selected

st.dataframe(df_selected_team) # displaying the final dataframe based on user selectiomn

# Download NBA player stats data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(df_selected_team), unsafe_allow_html=True)
# this above code is implementing the download csv functionality by which user can downlaod the filtered 
# data the he wanted based on his/her team and player position selection into a csv file


# Heatmap
if st.button('Intercorrelation Heatmap'):
    st.header('Intercorrelation Matrix Heatmap')
    df_selected_team.to_csv('output.csv',index=False)
    df = pd.read_csv('output.csv')

    corr = df.corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        f, ax = plt.subplots(figsize=(7, 5))
        ax = sns.heatmap(corr, mask=mask, vmax=1, square=True)
    st.pyplot(f)