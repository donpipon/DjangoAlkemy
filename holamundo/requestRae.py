import requests
from pyrae import dle
import json
import re
from bs4 import BeautifulSoup


def separate_sentences(text: str) -> object:
    sentences = re.findall(r'\d+\.\s*[fm]\.\s*(.*?)(?=\s*\d+\.\s*[fm]\.|$)', text)
    return sentences


def extract_first_sentence(text) -> str:
    # Define a regular expression pattern to match the first sentence
    pattern = r'(?:\d+\. [a-z]+\.\s*)?(.*?)(?=\d+\. [a-z]+\.|$)'

    # Use re.findall to find all matches of the pattern
    sentences = re.findall(pattern, text, flags=re.IGNORECASE | re.DOTALL)

    # Filter out sentences that start with "Definición RAE de «word»"
    filtered_sentences = [sentence.strip() for sentence in sentences if
                          not re.match(r'^Definición RAE de «[^»]+»', sentence)]

    # Return the first non-empty sentence
    for sentence in filtered_sentences:
        if sentence:
            return sentence.strip()

    return None  # Return None if no valid sentence is found

def palabraAleatoria() -> str:
    """

    :rtype: object
    """
    response = requests.get("https://www.palabrasque.com/palabra-aleatoria.php?Submit=Nueva+palabra")
    word = ""
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        font_element = soup.find('font', {'data': 'palabra'})

        pattern = re.compile(r'<font data="palabra" size="6" /><b>(.*?)<\/b><\/font>')
        match = pattern.search(response.text)

        if match:
            word = match.group(1)
            print(f"The word is: {word}")
        else:
            print("Word not found in the HTML.")
    else:
        print(f"Request failed with status code: {response.status_code}")

    r = dle.search_by_word(word)
    definicion = extract_first_sentence(r._meta_description)
    return word, definicion


if __name__ == "__main__":
    correctas: int = 0
    incorrectas: int = 0
    
    while True:
        response = requests.get("https://www.palabrasque.com/palabra-aleatoria.php?Submit=Nueva+palabra")
        # print(response.text)
    
        word: str = ""
    
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            font_element = soup.find('font', {'data': 'palabra'})
    
            pattern = re.compile(r'<font data="palabra" size="6" /><b>(.*?)<\/b><\/font>')
            match = pattern.search(response.text)
    
            if match:
                word = match.group(1)
                # print(f"The word is: {word}")
            else:
                print("Word not found in the HTML.")
        else:
            print(f"Request failed with status code: {response.status_code}")
    
        r = dle.search_by_word(word)
        print(extract_first_sentence(r._meta_description))
    
        definicion = r.to_dict()
        # print(json.dumps(definicion, indent=2))
        # print(definicion.get("articles"))
        # print(separate_sentences(r._meta_description))
        guess = input("Palabra: ")
        if word.lower() == guess.lower():
            print("Correcto!!!")
            correctas += 1
        else:
            print(f'Incorrecto :( la palabra es "{word}"')
            incorrectas += 1
    
        print(f'Aciertos: {correctas} pifies: {incorrectas}')
        play_again = input("Play again? (yes/no): ").lower()
    
        if play_again != "yes":
            print("[ GAME OVER ]")
            break
