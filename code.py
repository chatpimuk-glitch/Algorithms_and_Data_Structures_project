import pandas as pd
data = pd.read_csv("CprE_Subject.csv",delimiter=",")
target_code = input("Course ID:")
subject_info = data[data['CourseCode'] == int(target_code)]
if not subject_info.empty:
    name = subject_info['Name'].values[0]
    credit = subject_info['Credit'].values[0]

    print(f"วิชา: {name}")
    print(f"หน่วยกิต: {credit}")

