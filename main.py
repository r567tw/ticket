from helpers import notify
from TRA import ticket as TRA
from dotenv import load_dotenv



load_dotenv()
message = TRA.get()
notify.send(message=message)