import os
import pprint
from autogen import ConversableAgent

api_key = os.environ["OPENAI_API_KEY"]

assassin_agent = ConversableAgent(
    name="assassin_agent",
    system_message="You are a expert.",
    llm_config={"config_list": [{"model": "gpt-3.5-turbo-1106", "api_key": api_key}]},
)
murder_agent = ConversableAgent(
    name="murder_agent",
    system_message="You are a murder.",
    llm_config={"config_list": [{"model": "gpt-3.5-turbo-1106", "api_key": api_key}]},
)

chat_result = assassin_agent.initiate_chat(
    murder_agent,
    message="Let's discuss the murder p",
    summary_method="reflection_with_llm",
    max_turns=4,
)

print(chat_result.summary)

print(ConversableAgent.DEFAULT_SUMMARY_PROMPT)

pprint.pprint(chat_result.chat_history)

pprint.pprint(chat_result.cost)



