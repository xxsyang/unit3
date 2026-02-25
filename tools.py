import random
from huggingface_hub import list_models
from smolagents import Tool, DuckDuckGoSearchTool

class WeatherInfoTool(Tool):
    name = "weather_info"
    description = "Fetches weather information to schedule the fireworks."
    inputs = {
        "location": {
            "type": "string",
            "description": "The location to get weather information for."
        }
    }
    output_type = "string"

    def forward(self, location: str) -> str:
        # Dummy weather generation logic for the gala
        weather_conditions = ["clear", "cloudy", "raining", "snowing"]
        temp = random.randint(10, 30)
        condition = random.choice(weather_conditions)
        return f"Currently, it's {condition} with a temperature of {temp}°C in {location}."

class HubStatsTool(Tool):
    name = "hub_stats"
    description = "Fetches the most downloaded model from a specific author on the Hugging Face Hub."
    inputs = {
        "author": {
            "type": "string",
            "description": "The username of the model author/organization."
        }
    }
    output_type = "string"

    def forward(self, author: str) -> str:
        models = list_models(author=author, sort="downloads", direction=-1, limit=1)
        model_list = list(models)
        if not model_list:
            return f"No models found for author {author}."
        top_model = model_list[0]
        return f"The most popular model by {author} is {top_model.id} with {top_model.downloads} downloads."

# Initialize standard search tool
search_tool = DuckDuckGoSearchTool()