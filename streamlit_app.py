# Import python packages
import streamlit as st
#from st_supabase_connection import SupabaseConnection
from st_supabase_connection import SupabaseConnection, execute_query

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

current_sql = '"' + ques_genre_main + '">0'

if ques_genre_second and len(ques_genre_second)>1:
    current_sql += " AND CHARINDEX('" + ques_genre_second + "', SONGS." + '"tags")>0 '

current_sql += " order by RANDOM();"

#created_dataframe = conn.sql(current_sql)
#conn = st.connection("snowflake")

#session = get_active_session()
#session =  Session.builder.create()

# Initialize connection.
#conn = st.connection("supabase",type=SupabaseConnection)

st_supabase = st.connection(
    name="supabase_connection", 
    type=SupabaseConnection, 
    ttl=None,
    url="https://fzfqjpxfdhlhtcryhwob.supabase.co", 
    key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZ6ZnFqcHhmZGhsaHRjcnlod29iIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjAzMjUyNzEsImV4cCI6MjAzNTkwMTI3MX0.lYpuZUz7UA9D8RNIGOf2gnTVRJ7Szad1tzVw06sV6dk", 
)

# Perform query.
#rows = conn.query("*", table="mytable", ttl="10m").execute()
# rows = st_supabase.query(current_sql, ttl="10m")
#rows = execute_query(st_supabase.table("songs").select("*", count="None"), ttl=None)
#execute_query()

rows = execute_query(st_supabase.table("songs").select("*", count="None").eq("tags", ques_genre_main).order("preview",desc=True).limit(1), ttl=None)


queried_data = rows.data
#queried_data = session.sql(current_sql).to_pandas()

#df = conn.query(current_sql, ttl=600)
# # # Execute the query and convert it into a Pandas dataframe
#queried_data = df.to_pandas()

if not queried_data.count == 0:
    #title
    title = queried_data[0]["name"]
    #image 
    link = queried_data[0]["link"]
    #image 
    image = queried_data[0]["pix"]
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