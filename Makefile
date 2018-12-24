install:
		virtualenv venv -p python3 && source venv/bin/activate && sudo pip install -r requirements.txt

run:
		python main.py
