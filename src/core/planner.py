from langchain_core.messages import HumanMessage, AIMessage
from src.chains.itenary_chain import generate_itinerary
from src.utils.logger import get_logger
from src.utils.custom_exception import CustomException

logger = get_logger(__name__)

class TravelPlanner:
    def __init__(self):
        self.messages = []
        self.city = ""
        self.interests = []
        self.itinerary = ""

        logger.info("Initialized Travel planner agent")
    
    def set_city(self, city:str):
        try:
            self.city = city
            self.messages.append(HumanMessage(content=city))
            logger.info("City set successfully")
        except Exception as e:
            logger.error(f"Error while setting city {e}")
            CustomException("Failed to set city", e)

    def set_interests(self, interests_str:str):
        try:
            self.interests = [i.strip() for i in interests_str.split(',')]
            self.messages.append(HumanMessage(content=interests_str))
            logger.info("Interests set successfully")
        except Exception as e:
            logger.error(f"Error while setting interests {e}")
            CustomException("Failed to set Interests", e)
    
    def create_itinerary(self):
        try:
            logger.info(f"Creating itinerary for City: {self.city} and interests {self.interests}")
            itinerary = generate_itinerary(self.city, self.interests)
            self.itinerary = itinerary
            self.messages.append(AIMessage(content = itinerary))
            logger.info("Itinerary generated successfully")
            return itinerary
        except Exception as e:
            logger.error("Error while generating itinerary {e}")
            CustomException("Failed to generate itinerary", e)
