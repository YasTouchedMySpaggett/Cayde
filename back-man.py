from marvin.skills import Brain
from marvin import config

config.set('marvin', 'debug', 'true')

class MyAssistant(Brain):
    def __init__(self):
        super().__init__()

        # define intents
        self.add_intent('greeting', self.greeting)
        self.add_intent('search', self.search)
        self.add_intent('news', self.news)

    def greeting(self, intent, session):
        return 'Hello, how can I assist you?'

    def search(self, intent, session):
        query = intent.get('query')
        # code to perform a web search with the query term
        return f"Here are the search results for '{query}'."

    def news(self, intent, session):
        category = intent.get('category')
        # code to fetch the latest news for the given category
        return f"Here are the latest news on {category}."

assistant = MyAssistant()
while True:
    user_input = input('How can I assist you? ')
    response = assistant.process_text(user_input)
    print(response)
