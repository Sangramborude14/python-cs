import matplotlib.pyplot as plt

def plot_student_result(student_name, roll_no, subjects, marks):
    plt.figure(figsize=(10, 6))
    plt.bar(subjects, marks, color='skyblue', edgecolor='navy')
    plt.xlabel('Subjects')
    plt.ylabel('Marks')
    plt.title(f'Result for {student_name} ({roll_no})')
    plt.ylim(0, 100)
    for i, v in enumerate(marks):
        plt.text(i, v + 1, str(v), ha='center')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
