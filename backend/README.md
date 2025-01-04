# general-store-RAG

## Quick Setup
In order to install the correct dependencies and the database, run the following code. I would recommend using a python venv with Python 3.11, or 3.12. Other versions should work, but these were what I used to test it. There is type hinting so at least Python 3.10 is required.<br>

### Setting up a venv


#### On Mac/Linux:

``` bash
python -m venv myenv
source myenv/bin/activate
```

#### On Windows:

``` powershell
python -m venv myenv 
myenv\Scripts\activate
```

### Installing Dependencies and Populating Vector Database
In order to install the required Python packages, setup the .env folder, and run the builder script for the vector db, execute the following code into your terminal:
```
touch .env 
pip install --upgrade pip 
pip install -r requirements.txt  
```
From there, the open ai api keys need to be added to the .env file.



## Usage
With the setup completed, to run the RAG execute `python app.py`s in the project root directory.


