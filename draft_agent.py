from langchain.agents import create_agent


agent = create_agent(
    model="ollama:gemma4:31b-cloud",
    tools=[],
    system_prompt="You are a helpful AI email draft agent!"
)


query =input("Email draft idea:")

messages = [
    {"role":"user","content":query}
]
response = agent.invoke({"message":messages})
print(response["messages"][-1].text)
