import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
from elevenlabs.types import ConversationConfig

load_dotenv()

AGENT_ID = os.getenv("AGENT_ID")
API_KEY = os.getenv("API_KEY")

user_name = "Ramez"
schedule = "Project meeting with Shehnaz at 13:00; Interview with Microsoft at 16:00"
prompt = f"Your conversationalist has the following schedule: {schedule}."
first_message = f"Hello {user_name}, how can I help you today?"

