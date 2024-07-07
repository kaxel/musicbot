# Import python packages
import streamlit as st
from st_supabase_connection import SupabaseConnection, execute_query
import random

#print(random.randint(3, 9))
# Write directly to the app
st.title("🤖 Musicbot 🖥️")

# "with" notation
with st.sidebar:
    st.title("Info")
    st.text("Select your genre and choose a tab below.")

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

st_supabase = st.connection(
    name="supabase_connection", 
    type=SupabaseConnection, 
    ttl=None,
    url="https://fzfqjpxfdhlhtcryhwob.supabase.co", 
    key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZ6ZnFqcHhmZGhsaHRjcnlod29iIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjAzMjUyNzEsImV4cCI6MjAzNTkwMTI3MX0.lYpuZUz7UA9D8RNIGOf2gnTVRJ7Szad1tzVw06sV6dk", 
)

# Perform query.
if len(ques_genre_second)>1:
  rows = execute_query(st_supabase.table("songs").select("*", count="None").like("tags", ques_genre_second).order("track",desc=True).limit(5), ttl=None)
else:
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

name1 =  queried_data[0]["name"][:18]
name2 =  queried_data[1]["name"][:18]
name3 =  queried_data[2]["name"][:18]
name4 =  queried_data[3]["name"][:18]

tab1, tab2, tab3, tab4 = st.tabs([name1, name2, name3, name4])

with tab1:
   st.header(queried_data[0]["name"])
   subcola1, subcola2 = tab1.columns(2)
   subcola1.image(queried_data[0]["pix"], width=200)
   if ".mp3" in queried_data[0]["link"]:
    subcola2.audio(queried_data[0]["link"], format="audio/mpeg", loop=False)
   else:
    subcola2.video(queried_data[0]["link"])

with tab2:
   st.header(queried_data[1]["name"])
   subcolb1, subcolb2 = tab2.columns(2)
   subcolb1.image(queried_data[1]["pix"], width=200)
   if ".mp3" in queried_data[1]["link"]:
    subcolb2.audio(queried_data[1]["link"], format="audio/mpeg", loop=False)
   else:
    subcolb2.video(queried_data[1]["link"])

with tab3:
   st.header(queried_data[2]["name"])
   subcolc1, subcolc2 = tab3.columns(2)
   subcolc1.image(queried_data[2]["pix"], width=200)
   if ".mp3" in queried_data[2]["link"]:
    subcolc2.audio(queried_data[2]["link"], format="audio/mpeg", loop=False)
   else:
    subcolc2.video(queried_data[2]["link"])

with tab4:
   st.header(queried_data[3]["name"])
   subcold1, subcold2 = tab4.columns(2)
   subcold1.image(queried_data[3]["pix"], width=200)
   if ".mp3" in queried_data[3]["link"]:
    subcold2.audio(queried_data[3]["link"], format="audio/mpeg", loop=False)
   else:
    subcold2.video(queried_data[3]["link"])
