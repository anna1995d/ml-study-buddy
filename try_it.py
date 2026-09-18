from study_buddy.llm import Conversation

quiz = Conversation()
print(quiz.send("Quiz me on one ML concept."))
print(quiz.send("My answer: it prevents overfitting by dropping neurons."))
print(quiz.send("Was I right?"))