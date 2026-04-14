# External 
import pandas as pd
import numpy as np
import os
#local
import visualizer

SUBJECT_CREDITS = {
    'PH-101': 3,
    'ME-102': 2,
    'CS-111': 3,
    'PH-102': 1,
    'MA-111': 3,
    'ME-101': 3,
    'HS-103': 2,
    'HS-101': 2,
    'HS-102': 1
}

def analyze_results(file_path):
    print("\n" + "="*50)
    print("  NIT HAMIRPUR - SEMESTER RESULT  ")
    print("="*50)
    
    try:
        df = pd.read_csv(file_path)
        df = df.fillna(0)
        subjects = list(SUBJECT_CREDITS.keys())
        
        df['Total_Marks'] = df[subjects].sum(axis=1)
        max_marks = len(subjects) * 100
        df['Percentage'] = (df['Total_Marks'] / max_marks) * 100
        
        df.to_csv("final_results.csv", index=False)
        print(f"Success: Full marks report saved to 'final_results.csv'")
        
        return df, subjects

    except Exception as e:
        print(f"Error: {e}")
        return None, None

def search_portal(df, subjects):
    print("\n" + "-"*50)
    print("         NITH STUDENT SEARCH PORTAL         ")
    print("-"*50)
    
    while True:
        user_input = input("\nEnter Roll No (e.g., 25DEC024) or 'exit': ").strip().upper()
        
        if user_input == 'EXIT': break
        
        student = df[df['RollNo'] == user_input]
        if not student.empty:
            s = student.iloc[0]
            print("\n" + "*"*40)
            print(f" NAME:        {s['Name']}")
            print(f" FATHER NAME: {s['FatherName']}")
            print(f" ROLL NUMBER: {s['RollNo']}")
            print("-" * 40)
            print(f" TOTAL MARKS: {s['Total_Marks']} / {len(subjects) * 100}")
            print(f" PERCENTAGE:  {s['Percentage']:.2f}%")
            print("*"*40)
            
            print("\nSUBJECT-WISE MARKS:")
            marks_list = []
            for sub in subjects:
                print(f" {sub}: {s[sub]}")
                marks_list.append(s[sub])
            
            visualizer.plot_student_result(s['Name'], s['RollNo'], subjects, marks_list)
        else:
            print(f"❌ Roll No {user_input} not found.")

if __name__ == "__main__":
    df, subjects = analyze_results("marks.csv")
    if df is not None:
        search_portal(df, subjects)
