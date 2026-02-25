print("🚀 If you can read this, Python is running the right file!")

from smolagents import CodeAgent, InferenceClientModel
from retriever import GuestInfoRetrieverTool
from tools import WeatherInfoTool, HubStatsTool, search_tool

from smolagents import CodeAgent, LiteLLMModel

model = LiteLLMModel(
    model_id="gemini/gemini-2.0-flash", 
    api_key="your api key"
)

guest_info_tool = GuestInfoRetrieverTool()
weather_info_tool = WeatherInfoTool()
hub_stats_tool = HubStatsTool()

# model = InferenceClientModel()
# model = InferenceClientModel(model_id="Qwen/Qwen2.5-Coder-32B-Instruct")

# ============ part 1 and part 2 ================
# alfred = CodeAgent(
#     tools=[guest_info_tool, weather_info_tool, hub_stats_tool, search_tool],
#     model=model
# )

# # # Test Alfred's capabilities
# # query = "What's the weather like in Paris tonight? Will it be suitable for our fireworks display?"
# # print("🎩 Alfred's Response:")
# # print(alfred.run(query))

# query = "What is Facebook? Also, use your hub_stats tool to tell me what their most downloaded model is on the Hugging Face Hub."

# print("🎩 Alfred is thinking...")
# print(alfred.run(query))


# ================================ part 3 =============================
alfred = CodeAgent(
    tools=[guest_info_tool, weather_info_tool, hub_stats_tool, search_tool],
    model=model,
    add_base_tools=True, 
    planning_interval=3  
)

print("🎩 Alfred's First Response:")
response1 = alfred.run("Tell me about Lady Ada Lovelace.")
print(response1)

print("\n🎩 Alfred's Second Response (using memory):")
response2 = alfred.run("What projects is she currently working on?", reset=False) 
print(response2)