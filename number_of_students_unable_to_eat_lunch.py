class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        s = 0
        n = len(students)
        while students:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                s = 0
            else:
                t = students.pop(0)
                students.append(t)
                s += 1
                if s == n:
                    break
        return len(students)

