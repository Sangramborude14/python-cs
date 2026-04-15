import pandas as pd
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

def marks_to_grade_point(marks):
    """Converts raw marks (0-100) into a standard 10-point grade scale."""
    if marks >= 85: return 10
    elif marks >= 75: return 9
    elif marks >= 65: return 8
    elif marks >= 55: return 7
    elif marks >= 45: return 6
    elif marks >= 35: return 5
    else: return 0  

def analyze_results(file_path):
    print("\n" + "="*50)
    print("  NIT HAMIRPUR - SEMESTER RESULT (SGPA)  ")
    print("="*50)
    
    try:
        df = pd.read_csv(file_path)
        df = df.fillna(0)
        subjects = list(SUBJECT_CREDITS.keys())
        
        df['Total_Marks'] = df[subjects].sum(axis=1)
        
        total_credits = sum(SUBJECT_CREDITS.values()) 
        df['Total_Credit_Points'] = 0 
        
        for sub, credits in SUBJECT_CREDITS.items():
            grade_points = df[sub].apply(marks_to_grade_point)
            df['Total_Credit_Points'] += (grade_points * credits)
            
        df['SGPA'] = (df['Total_Credit_Points'] / total_credits).round(2)
        
        df.to_csv("final_results.csv", index=False)
        print(f"Success: Full SGPA report saved to 'final_results.csv'")
        
        return df, subjects

    except Exception as e:
        print(f"Error: {e}")
        return None, None

def search_portal(df, subjects):
    print("\n" + "-"*50)
    print("        NITH STUDENT SEARCH PORTAL        ")
    print("-"*50)
    
    while True:
        user_input = input("\nEnter Roll No (e.g., 25DEC024) or 'exit': ").strip().upper()
        
        if user_input == 'EXIT': break
        
        student = df[df['RollNo'] == user_input]
        if not student.empty:
            s = student.iloc[0]
            print("\n" + "*"*40)
            print(f" NAME:        {s['Name']}")
            print(f" FATHER'S NAME: {s['FatherName']}")
            print(f" ROLL NUMBER: {s['RollNo']}")
            print("-" * 40)
            print(f" TOTAL MARKS: {s['Total_Marks']}")
            print(f" SGPA:        {s['SGPA']} / 10.00") 
            print("*"*40)
            
            print("\nSUBJECT-WISE BREAKDOWN:")
            marks_list = []  
            for sub in subjects:
                raw_mark = s[sub]
                gp = marks_to_grade_point(raw_mark)
                print(f" {sub}: {raw_mark:3} marks (Grade Point: {gp})")
                marks_list.append(raw_mark) 
                
            visualizer.plot_student_result(s['Name'], s['RollNo'], subjects, marks_list)
                
        else:
            print(f"❌ Roll No {user_input} not found.")

if __name__ == "__main__":
    df, subjects = analyze_results("marks.csv")
    if df is not None:
        search_portal(df, subjects)