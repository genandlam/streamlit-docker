# streamlit-docker
Creating streamlit in docker with table visualisation

[starting out docker commands] (https://docs.streamlit.io/knowledge-base/tutorials/deploy/docker#prerequisites)

### commands for docker
docker build --no-cache -t streamlit-docker:new .    
docker run -p 8800:8800 streamlit-docker:new 
docker cp location_of data folder  <Image-name>:"/app"


### local 
streamlit run streamlit_app.py