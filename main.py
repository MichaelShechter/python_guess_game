import random

'''
    Author: Michael Shechter
    Date: 30/12/23
'''


def set_sentence_for_gui(backend_sentence: list) -> list:
    """
        creates new list of underscores for the GUI

        Parameters:
        - backend_sentence: list that contains strings

        Returns:
        - list: list of string with underscores.
        """
    new_sentence_list: list
    for i in backend_sentence: selected_sentence_list.append("_" * len(i))
    return selected_sentence_list


def replace_by_index(word: str, index: int, guess):
    return word[:index] + guess + word[index + 1:]


def get_random_sentence(list_of_sentence: list, ) -> list:
    """
            Get random sentence from a list

            Parameters:
            - list_of_sentence: list that sentences

            Returns:
            - list: sentence
            """
    return list_of_sentence[random.randint(0,9)]


def convert_list_str(list_of_sentence) -> str:
    return " ".join(str(x) for x in list_of_sentence)


def find_guss_in_word(tested_word: str, word_index: int, user_guss: str, ):
    """
    find the user guss  in a word

    Parameters:
    - tested_word: word to be tested.
    - word_index: index of the word.
    - user_guss: char

    Returns:
    - list
    """

    for index, val in enumerate(tested_word):
        if user_guss == val:
            list_or_results.append({"word": tested_word, "word_index": word_index, "guess": user_guss, "index": index})
    return list_or_results


def is_reused_guss(user_g: str, guss_list: list) -> bool:
    """
        Check if the user guss is already in the list

        Parameters:
        - user_g: user guss
        - guss_list: list of guss

        Returns:
        - bool
        """

    if user_g in guss_list:
        return True
    else:
        return False


def set_score(is_correct: bool, num_correct_answers: int, user_score: int)-> int:
    """
        set user score

        Parameters:
        - is_correct: is the  user guss correct
        - num_correct_answers:  number of correct answers
        - user_score: user score

        Returns:
        - user score: int
        """
    reduction_number: int = 1
    increment_number: int = 5
    if is_correct:
        user_score += (increment_number * num_correct_answers)
        return user_score
    else:
        if user_score == 0:
            return user_score
        else:
            user_score -= 1
        return user_score


rnd_num: int = random.randint(0, 9)
list_of_sentences: list = [["love", "your", "self"],
                           ["always", "be", "yourself"],
                           ["keep", "it", "cool"],
                           ["just", "do", "it"],
                           ["glory", "man", "united"],
                           ["dreams", "come", "true"],
                           ["never", "give", "up"],
                           ["winners", "never", "quit"],
                           ["success", "breeds", "success"],
                           ["let", "it", "be"],
                           ]



list_of_guesses: list = []
user_score: int = 0
user_guss: str = ""
gui_sentence: str = ""
selected_sentence_list: list = []
list_correct_guesses: list = []
list_or_results: list = []
score: int = 0



selected_sentence_backend = get_random_sentence(list_of_sentences)

print(f"selected_sentence_backend = {selected_sentence_backend}")
selected_sentence_list: str = set_sentence_for_gui(selected_sentence_backend)
while selected_sentence_backend != selected_sentence_list:
    user_guss = str(input(f"Please enter your guess: {convert_list_str(selected_sentence_list)} ")).lower()
    if not user_guss.isalpha():
        print("Please enter only letters")
        continue
    elif len(user_guss) != 1:
        print("Please enter only one letter")
        continue
    elif is_reused_guss(user_guss, list_of_guesses):
        print("You have already guessed this letter, please try again")
        continue
    list_of_guesses.append(user_guss)
    list_or_results.clear()
    for index, word in enumerate(selected_sentence_backend):
        find_guss_in_word(word, index, user_guss, )
    if len(list_or_results) == 0:
        print(f"Wrong guess! {user_guss} in not in the words")
        user_score = set_score(False, 0, user_score)
        print(f"user_score = {user_score}")
    else:
        for item in list_or_results:
            selected_sentence_list[item.get('word_index')] = replace_by_index(
                selected_sentence_list[item.get('word_index')], item.get('index'), item.get('guess'))
        user_score = set_score(True, len(list_or_results), user_score)
        print(f"user_score = {user_score}")
print(f"Well done, you won!!! Your score is {user_score}")
