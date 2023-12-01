import random
class WordLearning:
        def __init__(self):
            self.dictionary = {}
            self.score_by_word = {}

        def fill_dictionary(self, word, translation):
            self.dictionary[word] = translation
            self.score_by_word[word] = 1000

        def test_knowledge(self):
            score = 0
            total_words = 0

            for i in range(len(self.dictionary)):
                words_not_learned = [word for word in self.dictionary.keys() if self.score_by_word[word] <= 1000]
                if len(words_not_learned) <= 0:
                    print("You have learned all the words! Add more to the dictionary to continue.")
                    break
                word = random.choice(words_not_learned)
                translation = self.dictionary[word]

                user_translation = input(f"What is the translation of '{word}'? ")
                total_words += 1
                if user_translation.lower() == translation.lower():
                    score += 1
                    print("Correct!")
                    self.score_by_word[word] += 1
                else:
                    print(f"Incorrect! The correct translation is '{translation}'.")
                    self.score_by_word[word] -= 1

            print(f"You scored {score/total_words*100}%")
        
        def reset_scores(self):
            for word in self.dictionary.keys():
                self.score_by_word[word] = 1000

def task1():
    print('Task 1:')
    def count_letters(string_):
        letter_count = {}
        for letter in string_:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
        return letter_count
    
    def test_count_letters(string_):
        print(f"Counting letters in '{string_}': ", end="")
        print(count_letters(string_))

    test_count_letters("Banana")
    test_count_letters("Hello World")
    test_count_letters("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris euismod, nisl vitae aliquam lacinia, nunc nulla aliquet ipsum, vitae")

def task2():
    print('Task 2:')
    def convert_to_words(number):
        lookup_table = {
            0:      "\b",
            1:      "one",
            2:      "two",
            3:      "three",
            4:      "four",
            5:      "five",
            6:      "six",
            7:      "seven",
            8:      "eight",
            9:      "nine",
            10:     "ten",
            20:     "twenty",
            30:     "thirty",
            40:     "fourty",
            50:     "fifty",
            60:     "sixty",
            70:     "seventy",
            80:     "eighty",
            90:     "ninety",
            100:    "hundred",
            1000:   "thousand"
        }
        number_list = []
        while number > 0:
            number_list.append(number % 10)
            number //= 10

        word_representation = ""
        for i, number in enumerate(number_list):
            if number in lookup_table.keys():
                if i == 0:
                    word_representation = lookup_table[number] + " " + word_representation
                if i == 1:
                    word_representation = lookup_table[number*10] + " " + word_representation
                if i == 2:
                    word_representation = lookup_table[number] + " " + lookup_table[100] + " " + word_representation
                if i == 3:
                    word_representation = lookup_table[number] + " " + lookup_table[1000] + " " + word_representation
                if i == 4:
                    word_representation = lookup_table[number*10] + " " + word_representation
                if i == 5:
                    word_representation = lookup_table[number] + " " + lookup_table[100] + " " + word_representation
                    
        return word_representation
    
    def test_convert_to_words(number):
        print(f"Converting {number} to words: ", end="")
        print(convert_to_words(number))
    
    test_convert_to_words(1)
    test_convert_to_words(75)
    test_convert_to_words(250)
    test_convert_to_words(870220)

def task3(word_learning: WordLearning):
    print('Task 3:')
    # Added a class at the top of the file to make it easier to read

    def test_word_learning(word_learning: WordLearning):
        word_learning.fill_dictionary("python", "pyton")
        word_learning.fill_dictionary("banana", "banan")
        word_learning.fill_dictionary("pear", "gruszka")
        word_learning.fill_dictionary("text", "tekst")
        word_learning.fill_dictionary("knowledge", "wiedza")
        print("Test you knowledge for the first time:")
        word_learning.test_knowledge()

    test_word_learning(word_learning)

def task4():
    print('Task 4:')
    print("To do...")

def task5(word_learning: WordLearning):
    print('Task 5:')
    print("Test you knowledge for the second time:")
    word_learning.test_knowledge()
    print("Test you knowledge for the third time:")
    word_learning.test_knowledge()
    # Done in task 3

def main():
    task1()
    task2()
    word_learning = WordLearning()
    task3(word_learning)
    task4()
    task5(word_learning)

if __name__ == "__main__":
    main()