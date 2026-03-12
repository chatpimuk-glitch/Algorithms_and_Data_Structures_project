import csv

def build_hash_table(file_path):
    hash_table = {}

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            code = row['CourseCode']

            if code not in hash_table:
                hash_table[code] = []

            hash_table[code].append({
                'Name': row['Name'],
                'Type': row['Type'],
                'Credit': row['Credit'],
                'Semester': row['Semester'],
                'Lecturer': row['Lecturer']
            })
    return hash_table



class ListStack:
  def __init__(self):
    self._s = []
  def push(self,n):
    self._s.append(n)

  def top(self):
    return self._s[-1]

  def pop(self):
    if len(self) >= 1:
      return self._s.pop()
    raise Exception("stack is empty")

  def is_empty(self):
    return len(self._s) == 0

  def __str__(self):
     return '<'+str(self._s)+'>'

  def __len__(self):
    return len(self._s)

table = build_hash_table('CprE_Subject.csv')
Registered = ListStack()

while True:
    i = input()
    command = i.split()
    if len(command) == 2:
        if command[0] == "add":
            target_code = command[1]
            if target_code in table:
                subject = table[target_code][1]
                Registered.push(subject)
                print("Added:",subject['Name'],"("+subject['Credit'],"credits) to",subject['Lecturer'])

    elif len(command) == 1:
        if command[0] == "undo":
            pass


        elif command[0] == "process_all":
            print(Registered)
            break



