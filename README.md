Exploring vector db's , 

Chroma : 
 * Installation
     * After installing python, will have PIP, which is a package manager for Python packages.
     * Simply run "pip install chromadb"
     * it will intsall the chromadb
 * Using chromadb
     * As part of chromdb installation, will get the chromadb python client,
     * Which will help us interact with chromadb
     * Collections in chromadb are like table in sql
     * To create the collection in chroma db run "VectorDB/chroma/test/create_collection.py"
     * above will initiate persistent chroma clinet
     * run to insert some data into chroma db "chroma/test/insert_data_to_collection.py"
     * Now query to verify the data inserted by runnung "chroma/test/query_data_from_collection.py"
     * Purging :
       * While adding data into chroma db collection, we will add retentionDate to metadata
       * We have to write a scheduler which will delete the data based on retentionDate
       * Here retention date should be today + retentionDays 
       * Ex : if we want 7 days retention , then today+7 
       * Scheduler will run every date check where retentionDate = today, it will delete the data from chromadb

Notes : 
I have refered https://docs.trychroma.com/usage-guide for chroma

:)
