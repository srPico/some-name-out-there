from os import getenv
from dotenv import load_dotenv

load_dotenv()
apiKey = getenv('API_KEY')

print(apiKey)
