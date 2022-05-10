DEFAULT_DIAGRAM = "VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV"

default_students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred",
                    "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]


def student_index(name, students):
    return sorted(students).index(name)


class Garden:
    diagram = []
    students = []
    plants_list = ["Clover", "Grass", "Radishes", "Violets"]

    def __init__(self, diagram=DEFAULT_DIAGRAM, students=default_students):
        self.diagram = diagram.split("\n")
        self.students = students

    def plants(self, name):
        positions = (2 * student_index(name, self.students), 2 * student_index(name, self.students) + 1)
        students_plants_chars = []
        students_plants = []
        for row in self.diagram:
            for index in positions:
                students_plants_chars.append(row[index])
        for char in students_plants_chars:
            for word in self.plants_list:
                if char == word[0]:
                    students_plants.append(word)
        return students_plants

