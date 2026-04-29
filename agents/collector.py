from utils.io_utils import read_file
from config import DATA_SOURCES
from utils.parser import merge_sources
class CollectorAgent:
    def run(self):
        email = read_file(DATA_SOURCES["email_path"])
        chat = read_file(DATA_SOURCES["chat_path"])
        meeting = read_file(DATA_SOURCES["meeting_path"])
        return merge_sources(email, chat, meeting)
