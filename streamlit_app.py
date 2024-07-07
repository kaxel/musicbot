# Import python packages
import streamlit as st
from st_supabase_connection import SupabaseConnection, execute_query
import random

#print(random.randint(3, 9))
# Write directly to the app
st.title("🤖 Musicbot 🖥️")

# "with" notation
with st.sidebar:
    st.title("Stats")

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

st_supabase = st.connection(
    name="supabase_connection", 
    type=SupabaseConnection, 
    ttl=None,
    url="https://fzfqjpxfdhlhtcryhwob.supabase.co", 
    key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZ6ZnFqcHhmZGhsaHRjcnlod29iIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjAzMjUyNzEsImV4cCI6MjAzNTkwMTI3MX0.lYpuZUz7UA9D8RNIGOf2gnTVRJ7Szad1tzVw06sV6dk", 
)

# Perform query.
rows = execute_query(st_supabase.table("songs").select("*", count="None").like("tags", ques_genre_main).order("track",desc=True).limit(5), ttl=None)

queried_data = rows.data

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


tab1, tab2, tab3 = st.tabs(["A1", "B2", "C3"])

with tab1:
   st.header(queried_data[0]["name"])
   st.image(queried_data[0]["pix"], width=200)
   if ".mp3" in queried_data[0]["link"]:
    st.audio(queried_data[0]["link"], format="audio/mpeg", loop=False)
   else:
    st.video(queried_data[0]["link"])

with tab2:
   st.header(queried_data[1]["name"])
   st.image(queried_data[1]["pix"], width=200)
   if ".mp3" in queried_data[0]["link"]:
    st.audio(queried_data[1]["link"], format="audio/mpeg", loop=False)
   else:
    st.video(queried_data[1]["link"])

with tab3:
   st.header(queried_data[2]["name"])
   st.image(queried_data[2]["pix"], width=200)
   if ".mp3" in queried_data[2]["link"]:
    st.audio(queried_data[2]["link"], format="audio/mpeg", loop=False)
   else:
    st.video(queried_data[2]["link"])

col2.write(current_sql)