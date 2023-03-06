import requests
import html

level = input('Choose your level - easy/medium/hard: ').lower()

while level != 'easy' and level != 'medium' and level != 'hard':
    level = input('Choose between easy/medium/hard: ')

response = requests.get(f'https://opentdb.com/api.php?amount=12&difficulty={level}&type=boolean')
questions = response.json()
question_data = questions['results']

# For each question (q) in question_data decode the HTML entity eg &quot; and save back in 'question' key on the dictionary
for q in question_data:
    q['question'] = html.unescape(q['question'])
    q['correct_answer'] = html.unescape(q['correct_answer'])