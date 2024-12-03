step 1: write in cmd

- python -m venv venv
- venv\Scripts\activate
- pip install -r req.txt

step 2: create vectorDB

- open embeddings file
- uncommit line # 30
- add file path
- run file by write 'python embeddings.py' in cmd
- check in vectors folder if pdf is added

step 3: get vectorDB

- open llm_chain
- change file path in get_vectorDB() same as you have given in embeddings
- change sytem prompt, if you want to, line # 36
- save the file

step 4: run streamlit in cmd

- streamlit run app.py