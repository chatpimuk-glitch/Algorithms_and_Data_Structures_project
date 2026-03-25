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

def merge(left, right):
    sorted_arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        val_left = 0 if left[i]['Type'] == 'Sec' else 1
        val_right = 0 if right[j]['Type'] == 'Sec' else 1

        if val_left <= val_right:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr

def manual_sort_subjects(data_list):
    if len(data_list) <= 1:
        return data_list

    mid = len(data_list) // 2
    left_half = manual_sort_subjects(data_list[:mid])
    right_half = manual_sort_subjects(data_list[mid:])

    return merge(left_half, right_half)

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
n = 3
while True:
    i = input()
    command = i.split()
    if len(command) == 2:
        if command[0] == "add":
            target_code = command[1]
            if target_code in table:
                subject = table[target_code][0]
                Registered.push(subject)
                print("Added:",subject['Name'],"("+subject['Credit'],"credits) to",subject['Lecturer'])
                if n < 3 :
                    n += 1
            else:
                print("try again")

    elif len(command) == 1:
        if command[0] == "undo":
            if n > 0 :
                REVERTED = Registered.pop()
                print(REVERTED['Name'],"removed from", REVERTED['Lecturer'])
                if n > 0:
                    n -= 1
            else:
                print("can't undo")

        elif command[0] == "process_all":
            all_subjects = Registered._s

            sorted_list = manual_sort_subjects(all_subjects)

            print("--- Final Processed List ---")
            for sub in sorted_list:
                print(f"{sub['Name']} ({sub['Type']}) - {sub['Lecturer']}")
            break

    else:
        print("try again")