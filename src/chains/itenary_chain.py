from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.config.config import GROQ_API_KEY


llm = ChatGroq(
    groq_api_key = GROQ_API_KEY,
    model_name='llama-3.3-70b-versatile',
    temperature=0.3
)

itinerary_prompt = ChatPromptTemplate(
    messages=[("system","You are a helpful travel asssistant. Create a day trip itinerary for {city} based on user's interest : {interests}. Provide a brief , bulleted itineary"),
              ("user", "Create an itinerary for a day trip")]
)

def generate_itinerary(city:str, interests:str) -> str:
    response = llm.invoke(
        itinerary_prompt.format_messages(city=city, interests=' ,'.join(interests))
    )
    return response.content

