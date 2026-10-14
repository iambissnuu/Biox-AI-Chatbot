# Biox AI Chatbot

A simple terminal-based AI chatbot developed using Python, Django, and ChatterBot for Assignment 3 of the Advanced Artificial Intelligence course at the University of the Cumberlands.

## Project Description

This project demonstrates how a conversational chatbot can interact with users through a terminal interface. The chatbot uses ChatterBot to generate responses based on English conversation datasets and custom training examples.

## Technologies Used

- Python
- Django
- ChatterBot
- ChatterBot Corpus
- SQLite
- spaCy

## Features

- Interactive terminal-based conversation
- Responses generated using trained conversation data
- English corpus and custom conversation training
- Simple text-based user interface
- Exit and quit commands

## Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/iambissnuu/Biox-AI-Chatbot.git
cd Biox-AI-Chatbot
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Download the spaCy English model**

```bash
python -m spacy download en_core_web_sm
```

**4. Run the chatbot**

```bash
python chatbot.py
```

## Example Conversation

```text
Welcome to Biox AI Chatbot!

user: morning
bot: Thank you kindly.

user: how you doing
bot: Good

user: nice
bot: Thank you. You too.

user: exit
bot: Goodbye!
```
