def gradingStudents(grades):
        answer = []
        for i in range(len(grades)):
            grade  = grades[i]

            if grade >= 38:
                remain = 5 - grade % 5 
                if remain < 3:
                    answer.append(grade + remain)
                else:
                    answer.append(grade)
            else:
                answer.append(grade)
                
        return answer
