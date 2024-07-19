import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data

st.markdown(" # FIFA 2023 OFFICIAL DATASET! ⚽")
st.sidebar.markdown("Desenvolvido por [Emeson Borges](https://www.linkedin.com/in/emeson-borges-1539b3126/)")

btn = st.button("Acessar os dados no Kaggle")
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")
    
st.markdown(
    """
About Dataset
CONTEXT

The Football Player Dataset from 2017 to 2023 provides comprehensive information 
about professional football players. The dataset contains a wide range of attributes, 
including player demographics, physical characteristics, playing statistics, contract details, 
and club affiliations. With over 17,000 records, this dataset offers a valuable resource for 
football analysts, researchers, and enthusiasts interested in exploring various aspects of the
footballing world, as it allows for studying player attributes, performance metrics,
market valuation, club analysis, player positioning, and player development over time.

COLUMNS

ID: A unique identifier for each player.
Name: The name of the player.
Age: The age of the player at the time of data collection.
Photo: A link or reference to the player's photograph.
Nationality: The nationality of the player.
Flag: The national flag associated with the player's nationality.
Overall: The overall rating of the player's skills and abilities.
Potential: The potential rating representing the player's future development.
Club: The current club affiliation of the player.
Club Logo: A link or reference to the logo of the player's club.
Value (£): The estimated market value of the player in pounds (£).
Wage (£): The player's weekly wage in pounds (£).
Special: A numerical value representing the player's special abilities.
Preferred Foot: The player's preferred foot for playing.
International Reputation: A rating indicating the player's international reputation.
Weak Foot: A rating representing the player's weaker foot abilities.
Skill Moves: The number of skill moves the player possesses.
Work Rate: The work rate of the player.
Body Type: The physical build or body type of the player.
Real Face: Indicates whether the player has a real face representation.
Position: The player's preferred playing position.
Joined: The date when the player joined the current club.
Loaned From: The club from which the player is currently on loan.
Contract Valid Until: The date until which the player's contract is valid.
Height (cm.): The height of the player in centimeters.
Weight (lbs.): The weight of the player in pounds.
Release Clause (£): The release clause value of the player in pounds (£).
Kit Number: The player's kit number.
Best Overall Rating: The player's highest overall rating.
Year Joined: The year when the player joined the current club.

""")