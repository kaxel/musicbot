# Import python packages
import streamlit as st
from st_supabase_connection import SupabaseConnection, execute_query

# Write directly to the app
st.title("🤖 Musicbot 🖥️")

# "with" notation
with st.sidebar:
    st.title("Info")
    st.text("Select your genre.")
    st.text(" and choose a tab below.")
    st.text(" ")
    st.text("RSS entries are pulled from")
    st.text("CHILLFILTR.com for now.")
    st.text(" ")
    st.text("This is a proof of concept.")
    st.text("We may add more sources")
    st.text("in the future.")
#setup the space
col1, col2 = st.columns(2)
#get main genre
ques_genre_main = col1.radio(
    "Choose your top genre.",
    ('rock'
    ,'pop'
    ,'folk'
    ,'soul'
    ,'roots'
    ,'electronic'
    ,'hip-hop'
    ,'dance'
    ,'instrumental'))
#get secondary genre
ques_genre_second = col2.radio(
    "Secondary genre.",
    ('.'
    ,'indie'
    ,'commercial'
    ,'post-punk'
    ,'experimental'
    ,'chamber-pop'
    ,'bedroom-pop'
    ,'americana'
    ,'country'
    ,'ambient'
    ,'synthwave'
    ,'downtempo'
    ,'nettwerk'
    ))

st_supabase = st.connection(
    name="supabase_connection", 
    type=SupabaseConnection, 
    ttl=None,
    url="https://fzfqjpxfdhlhtcryhwob.supabase.co", 
    key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZ6ZnFqcHhmZGhsaHRjcnlod29iIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjAzMjUyNzEsImV4cCI6MjAzNTkwMTI3MX0.lYpuZUz7UA9D8RNIGOf2gnTVRJ7Szad1tzVw06sV6dk", 
)

current_sql = "testing"
# Perform query.
if len(ques_genre_second)>1:
  and_tags = f"and(tags.like.%{ques_genre_main}%,tags.like.%{ques_genre_second}%)"
  #secondary is selected
  secondary_selection = f"%{ques_genre_second}%"
  rows = execute_query(st_supabase.table("songs").select("*", count="None").or_(and_tags).order("track",desc=True).limit(6), ttl=None)
  current_sql = f"search {ques_genre_second} in {ques_genre_main}"
else:
  and_tags = f"and(tags.like.%{ques_genre_main}%)"
  #rows = execute_query(st_supabase.table("songs").select("*", count="None").like("tags", [ques_genre_main, ques_genre_second]).order("track",desc=True).limit(5), ttl=None)
  rows = execute_query(st_supabase.table("songs").select("*", count="None").or_(and_tags).order("track",desc=True).limit(6), ttl=None)
  current_sql = f"search {ques_genre_main}"

#and_tags

queried_data = rows.data

if len(queried_data)>0:
    #title
    title = queried_data[0]["name"]
    #image 
    link = queried_data[0]["link"]
    #image 
    image = queried_data[0]["pix"]
    if queried_data[0]["name"]:
      name1 =  queried_data[0]["name"][:18]      
    if 1<len(queried_data):
      name2 =  queried_data[1]["name"][:18]
    else:
      name2 = "--"
    if 2<len(queried_data):
      name3 =  queried_data[2]["name"][:18]
    else:
      name3 = "--"
    if 3<len(queried_data):
      name4 =  queried_data[3]["name"][:18]
    else:
      name4 = "--"
    if 4<len(queried_data):
      name5 =  queried_data[4]["name"][:18]
    else:
      name5 = "--"
    if 5<len(queried_data):
      name6 =  queried_data[5]["name"][:18]
    else:
      name6 = "--"

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([name1, name2, name3, name4, name5, name6])

    if name1:
      with tab1:
        st.header(queried_data[0]["name"])
        subcola1, subcola2 = tab1.columns(2)
        subcola1.image(queried_data[0]["pix"], width=260)
        if ".mp3" in queried_data[0]["link"]:
          subcola2.audio(queried_data[0]["link"], format="audio/mpeg", loop=False)
        else:
          subcola2.video(queried_data[0]["link"])
    else:
        with tab1:
          st.header("no matches")

    if "--" not in name2:
      with tab2:
        st.header(queried_data[1]["name"])
        subcolb1, subcolb2 = tab2.columns(2)
        subcolb1.image(queried_data[1]["pix"], width=260)
        if ".mp3" in queried_data[1]["link"]:
          subcolb2.audio(queried_data[1]["link"], format="audio/mpeg", loop=False)
        else:
          subcolb2.video(queried_data[1]["link"])

    if "--" not in name3:
      with tab3:
        st.header(queried_data[2]["name"])
        subcolc1, subcolc2 = tab3.columns(2)
        subcolc1.image(queried_data[2]["pix"], width=260)
        if ".mp3" in queried_data[2]["link"]:
          subcolc2.audio(queried_data[2]["link"], format="audio/mpeg", loop=False)
        else:
          subcolc2.video(queried_data[2]["link"])

    if "--" not in name4:
      with tab4:
        st.header(queried_data[3]["name"])
        subcold1, subcold2 = tab4.columns(2)
        subcold1.image(queried_data[3]["pix"], width=260)
        if ".mp3" in queried_data[3]["link"]:
          subcold2.audio(queried_data[3]["link"], format="audio/mpeg", loop=False)
        else:
          subcold2.video(queried_data[3]["link"])
    
    if "--" not in name5:
      with tab5:
        st.header(queried_data[4]["name"])
        subcole1, subcole2 = tab5.columns(2)
        subcole1.image(queried_data[4]["pix"], width=260)
        if ".mp3" in queried_data[4]["link"]:
          subcole2.audio(queried_data[4]["link"], format="audio/mpeg", loop=False)
        else:
          subcole2.video(queried_data[4]["link"])

    if "--" not in name6:
      with tab6:
        st.header(queried_data[5]["name"])
        subcolf1, subcolf2 = tab6.columns(2)
        subcolf1.image(queried_data[5]["pix"], width=260)
        if ".mp3" in queried_data[5]["link"]:
          subcolf2.audio(queried_data[5]["link"], format="audio/mpeg", loop=False)
        else:
          subcolf2.video(queried_data[5]["link"])