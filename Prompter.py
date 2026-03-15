from enum import Enum, auto
from openai import OpenAI
from Config import Config

class PromptCategory(Enum):
    SYSTEM = auto()
    USER = auto()

class Prompter:
    def __init__(self, _api_key='', _model='deepseek-chat', _stream=False, _temperature=0.3, _max_tokens=750):
        self.models_url = {
            'deepseek-chat' : 'https://api.deepseek.com'
        }
        self.model = _model
        self.api_key = _api_key
        self.client = OpenAI(api_key=self.api_key, base_url=self.models_url[self.model])
        self.response = None

        self.messages = []
        self.stream = _stream
        self.temperature = _temperature
        self.max_tokens = _max_tokens
    
    def send(self):
        self.response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            stream=self.stream,
            max_tokens=self.max_tokens,
            temperature=self.temperature
        )
        return self
    
    def stream_content(self, _choices=0):
        for chunk in self.response:
            if chunk.choices[_choices].delta.content:
                yield chunk.choices[0].delta.content
    
    def content(self, _choices=0):
        if self.stream:
            return self.stream_content(_choices)
        return self.response.choices[_choices].message.content
                    

    def push(self, category: PromptCategory, msg: str):
        role_map = {
            PromptCategory.SYSTEM: "system",
            PromptCategory.USER: "user"
        }

        self.messages.append({
            "role": role_map[category],
            "content": msg
        })

        return self

    def push_system_prompt(self, _msg:str):
        self.messages.append({
            'role' : 'system',
            'content' : _msg
        })
        return self

    def push_user_prompt(self, _msg:str):
        self.messages.append({
            'role' : 'user',
            'content' : _msg
        })
        return self

if __name__ == '__main__':
    # Test
    pr = Prompter(Config.AI_API_KEY, Config.MODEL)
    
    pr.push(PromptCategory.SYSTEM, 'Your are a AI chat Bot.')
    pr.push(PromptCategory.SYSTEM, 'Your task: Answer the user\'s questions.')
    
    prompt = input('Your Prompt: ')

    pr.push(PromptCategory.USER, prompt)
    pr.send()
    content = pr.content()

    print(content)