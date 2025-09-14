# Create a quiz game using classes to organize questions and track scores

# Create a class called question. That is going to be a class. You´re going to then create instances
# of which are going to be all the questions for the quiz game, and this question class is then
# going to include properties for the prompt which is going to be the question as well as the
# anwer, so what is the correct answer for this question.
# Then we´re going to create a second class called quiz, this is going to include a property called
# questions which is going to be a list of objects of this class question that we defined before,
# and then it´s going to include a second property called score which is supposed to iniatilize as
# zero and then increment as you run through the game.

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


class Quiz:
    def __init__(self, questions):
        self.questions = questions  # list of Question objects
        self.score = 0

    def run(self):
        for question in self.questions:
            print(question.prompt)
            user_answer = input("Your answer: ")
            if user_answer.lower() == question.answer.lower():
                print("✅ Correct!\n")
                self.score += 1
            else:
                print(f"❌ Wrong! The correct answer was: {question.answer}\n")

        print(f"🎯 You got {self.score}/{len(self.questions)} correct!")


# Example usage
question_prompts = [
    "What is the capital of France?\n(a) Paris\n(b) London\n(c) Rome\n\n",
    "Which planet is known as the Red Planet?\n(a) Venus\n(b) Mars\n(c) Jupiter\n\n",
    "What is 5 + 3?\n(a) 5\n(b) 8\n(c) 10\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "b"),
]

quiz = Quiz(questions)
quiz.run()
