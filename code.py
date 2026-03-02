import pandas as pd
data = pd.read_csv("CprE_Subject.csv",delimiter=",")
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
def get_info(subject_info,command):
    Name = subject_info['Name'].values[0]
    Credit = subject_info['Credit'].values[0]
    Lecturer = subject_info['Lecturer'].values[0]
    if command == "add":
        info = Name + " (" + Credit[0] + " credits) to " + Lecturer
    elif command == "undo":
        info = Name + " removed from " + Lecturer
    return info

Registered = ListStack()
i = input()
while i != "process_all":
    command = i.split()
    if len(command) == 2:
        if command[0] == "add":
            target_code = command[1]
            subject_info = data[data['CourseCode'] == int(target_code)]
            if not subject_info.empty:
                info = get_info(subject_info,"add")
                Registered.push(subject_info)
            print(f"Added : {info}")

    elif len(command) == 1:
        if command[0] == "undo":
            
            REVERTED = Registered.pop()
            info = get_info(REVERTED, "undo")
            print(f"REVERTED : {info}")

        elif command[0] == "process_all":
            pass



    i = input()

