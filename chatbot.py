
import os

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "chatbot_project.settings"
)

import django
django.setup()

from chatterbot import ChatBot
from chatterbot.trainers import (
    ChatterBotCorpusTrainer,
    ListTrainer,
)


def main():
    # Initialize the chatbot and store conversations locally.
    chatbot = ChatBot(
        "Biox",
        storage_adapter="chatterbot.storage.SQLStorageAdapter",
        database_uri="sqlite:///chatbot.sqlite3",
        logic_adapters=[
            {
                "import_path": "chatterbot.logic.BestMatch",
                "default_response": "I'm still learning. Can you ask me differently?",
                "maximum_similarity_threshold": 0.90,
            }
        ],
    )

    # Train using existing English conversation datasets.
    corpus_trainer = ChatterBotCorpusTrainer(chatbot)
    corpus_trainer.train("chatterbot.corpus.english.greetings")
    corpus_trainer.train("chatterbot.corpus.english.conversations")

    # Add custom examples to improve common responses.
    trainer = ListTrainer(chatbot)

    conversations = [
        ["Hello", "Hi! How are you doing?"],
        ["Hi", "Hello! Nice to meet you."],
        ["Good morning", "Good morning! How are you?"],
        ["Morning", "Good morning! Hope you're doing well."],
        ["How are you?", "I'm doing great, thanks for asking!"],
        ["How you doing", "I'm doing well! How about you?"],
        ["What is your name?", "My name is Biox."],
        ["Who are you?", "I'm Biox, a conversational AI chatbot."],
        ["What can you do?", "I can chat with you and answer simple questions."],
        ["I am good", "That's great to hear!"],
        ["Nice", "Thank you!"],
        ["I like this", "I'm glad you like it!"],
        ["Thank you", "You're welcome!"],
        ["What is AI?", "AI stands for Artificial Intelligence."],
        ["Who created you?", "I was developed using Python, Django, and ChatterBot."],
        ["Goodbye", "Goodbye! Have a wonderful day!"],
    ]

    for conversation in conversations:
        trainer.train(conversation)

    # Disable learning during the interactive session.
    chatbot.read_only = True

    print("\n" + "=" * 45)
    print("          Welcome to Biox AI Chatbot")
    print("=" * 45)
    print("Type 'exit' to end the conversation.\n")

    while True:
        try:
            user_input = input("user: ").strip()

            if user_input.lower() in ("exit", "quit"):
                print("bot: Goodbye!")
                break

            if not user_input:
                print("bot: Please enter a message.\n")
                continue

            response = chatbot.get_response(user_input)
            print(f"bot: {response}\n")

        except (KeyboardInterrupt, EOFError):
            print("\nbot: Goodbye!")
            break


if __name__ == "__main__":
    main()
