# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.session import Session
import snowflake.connector as snowconnect
conn = st.connection("snowflake")

# Write directly to the app
st.title("🤖 Musicbot 🖥️")
st.write(
    """Drill down and discover your favorite genres of music.
    """
)
#conn = snowconnect.connection
# Get the current credentials
col1, col2 = st.columns(2)
#get main genre
ques_genre_main = col1.radio(
    "Choose your top genre.",
    ('indie-rock',
    'indie-pop',
    'folk-pop',
    'roots',
    'americana',
    'soul',
    'electronic',
    'hip-hop',
    'dance',
    'instrumental'))
ques_genre_second = col2.radio(
    "Secondary genre.",
    ('.'
    ,'chamber-pop'
    ,'jazz'
    ,'ambient'
    ,'synthwave'
    ,'country'
    ,'downtempo'
    ,'americana'
    ,'blues'
    ,'folk'))

current_sql = 'SELECT * from NEWSONGS where "' + ques_genre_main + '">0'

if ques_genre_second and len(ques_genre_second)>1:
    current_sql += " AND CHARINDEX('" + ques_genre_second + "', NEWSONGS." + '"taginfo")>0 '

current_sql += " order by RANDOM();"

#created_dataframe = conn.sql(current_sql)
#conn = st.connection("snowflake")

#session = get_active_session()
session =  Session.builder.create()
queried_data = session.sql(current_sql).to_pandas()

#df = conn.query(current_sql, ttl=600)
# # # Execute the query and convert it into a Pandas dataframe
#queried_data = df.to_pandas()

if not queried_data.shape[0] == 0:
    #title
    title = queried_data.iloc[0,0] 
    #image 
    link = queried_data.iloc[0,10]
    #image 
    image = queried_data.iloc[0,11]
else:
    title="no matches found."
    link=""
    image=""
st.subheader(title)
if len(image)>2:
    st.image(image)
col1.button("REFRESH")
col2.write(current_sql)

md_link = '[listen](' + link + ')'
col1.markdown(md_link, unsafe_allow_html=True)