import datetime
import random
import time

# -------------------------
# DATA
# -------------------------

user_name = ""
question_count = 0

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Python went to school and became a smart snake.",
    "Debugging: removing bugs from code and creating new ones."
]

motivation = [
    "Keep learning. Small progress matters.",
    "Practice daily and you'll improve.",
    "Consistency beats motivation."
]

# -------------------------
# UTILITIES
# -------------------------

def typing(text):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(0.02)
    print()


def save_chat(user, bot):
    with open("chat_history.txt", "a", encoding="utf-8") as f:
        f.write(f"You: {user}\n")
        f.write(f"Bot: {bot}\n\n")


def calculate(expression):
    try:
        return str(eval(expression))
    except:
        return None


def show_menu():
    print("\n===== COMMANDS =====")
    print("hi / hello")
    print("how are you")
    print("my name is ____")
    print("your name")
    print("time")
    print("date")
    print("joke")
    print("motivate me")
    print("happy / sad")
    print("history")
    print("count")
    print("calculator (example: 10+20)")
    print("help")
    print("bye")
    print("====================\n")


# -------------------------
# CHATBOT
# -------------------------

def chatbot():

    global user_name
    global question_count

    typing("🤖 Welcome to Smart RuleBot")
    typing("Type HELP to see commands")

    while True:

        user = input("\nYou: ").strip().lower()
        question_count += 1

        bot = ""

        # greeting
        if user in ["hi", "hello", "hey"]:
            if user_name:
                bot = f"Hello {user_name}! Nice to see you."
            else:
                bot = "Hello! Tell me your name."

        # name
        elif "my name is" in user:
            user_name = user.replace("my name is", "").strip().title()
            bot = f"Nice to meet you {user_name}"

        elif user == "your name":
            bot = "I am Smart RuleBot"

        # time
        elif user == "time":
            bot = datetime.datetime.now().strftime(
                "Current Time: %H:%M:%S"
            )

        # date
        elif user == "date":
            bot = datetime.datetime.now().strftime(
                "Today's Date: %d-%m-%Y"
            )

        # joke
        elif user == "joke":
            bot = random.choice(jokes)

        # motivation
        elif user == "motivate me":
            bot = random.choice(motivation)

        # mood
        elif user == "happy":
            bot = "Great! Keep that energy."

        elif user == "sad":
            bot = "Things can improve. Keep going."

        # count
        elif user == "count":
            bot = f"You sent {question_count} messages."

        # help
        elif user == "help":
            show_menu()
            continue

        # history
        elif user == "history":
            try:
                with open(
                    "chat_history.txt",
                    "r",
                    encoding="utf-8"
                ) as f:
                    print("\n------ CHAT HISTORY ------")
                    print(f.read())
                    print("--------------------------")
            except:
                print("No history found")
            continue

        # calculator
        elif (
            "+" in user
            or "-"
            in user
            or "*"
            in user
            or "/"
            in user
        ):
            answer = calculate(user)

            if answer:
                bot = "Answer = " + answer
            else:
                bot = "Invalid expression"

        # status
        elif user == "how are you":
            bot = "I am working perfectly."

        # exit
        elif user == "bye":
            bot = "Goodbye! Chat saved."

            print("\nBot:", bot)
            save_chat(user, bot)
            break

        else:
            bot = (
                "I don't understand. Type HELP."
            )

        print("\nBot:", bot)
        save_chat(user, bot)


# -------------------------
# START
# -------------------------

chatbot()