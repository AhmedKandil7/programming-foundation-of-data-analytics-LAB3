def scoreToGrade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


def computeGrades(scores):
    grades = [scoreToGrade(score) for score in scores]
    return grades


A = input('enter values of list : ')
A = list(map(int, A))

G = computeGrades(A)
print(f"Input: {A}")
print(f"Output: {G}")