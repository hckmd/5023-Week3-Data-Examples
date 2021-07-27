import json
marks = [{'name': 'Ben', 'English': 80}]
with open('marks.json','w') as file:
  json.dump(marks, file)
