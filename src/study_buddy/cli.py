# cli.py
from study_buddy.llm import Conversation

def main():
    quiz = Conversation()
    print("ML Study Buddy. Type 'quit' to exit.\n")
    print(quiz.send("Quiz me on one ML concept. Ask one question and wait."))

    while True:
        user = input("\n> ")
        if not user.strip():
            continue
        if user.strip().lower() in {"quit", "exit"}:
            print("\nBye.")
            break

        print("\n" + quiz.send(user))


if __name__ == "__main__":
    main()