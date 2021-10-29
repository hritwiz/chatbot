from nltk.chat.util import Chat, reflections
from flask import Flask, render_template, request

inquiries = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?", ]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there", ]
    ],
    [
        r"what is your name ?",
        ["My name is coronaBot.", ]
    ],
    [
        r"how are you ?",
        ["I'm doing good, How about You ?", ]
    ],
    [

        r"I am fine(.*)|I'm fine|Fine(.*)|i'm (.*) doing good",
        ["Great to hear that, How can I help you?|That's amazing, What can I do for you?:)", ]
    ],
    [
        r"what do you do|help|what can you do|what (.*) do?",
        ["I will question you about your covid status to collect data.", ]
    ],
    [
        r"(.*) age?",
        ["I'm just a computer program. I am 2 months old.", ]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse", ]
    ],
    [
        r"Okay|let's do this|sure|okay let's do this|go ahead",
        ["Have you ever taken covid-19 test?", ]
    ],
	[
        r"Yes I have taken covid test|Yes",
        ["Were You tested positive or Negative?", ]
    ],
    [
        r"Negative",
        ["Have You considered taking Covid-19 Vaccine? ", ]
    ],
    [
        r"Positive",
        ["That must have been tough, So did you get vaccinated?", ]
    ],
    [
        r"Pfizer|AstraZeneca|Moderna",
        ["What were the effects of vaccine on you?", ]
    ],
	[
	    r"I am already vaccinated|Yes I do|I want to get Vaccinated",
	    ["Which vaccine is it ?", ]
    ],
    [
	    r"(.*)",
	    ["Thank You for your response. Much appreciated", ]
    ],
	[
        r"Bye|Ok Thank You| ",
        ["BBye take care. See you soon :) ",
            "It was nice talking to you. See you soon :)"]
    ],
]

reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}


def Conversation(user_input):
    chat = Chat(inquiries, reflections)
    response = str(chat.respond(user_input))
    return response


app = Flask(__name__)
app.static_folder = 'static'


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    ans = Conversation(userText)
    return ans


if __name__ == "__main__":
    app.run()
