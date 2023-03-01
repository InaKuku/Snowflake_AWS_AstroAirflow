from unittest import TestCase, main

from project.student import Student

class TestStudent(TestCase):
    def setUp(self):
        self.student = Student("Peter")
        self.studen1 = Student("Ivan", {"maths": ["first_note", "second_note"], "lit": ["some_note", "another_note"]})

    def test_init_without_courses(self):
        self.assertEqual("Peter", self.student.name)
        self.assertEqual({}, self.student.courses)

    # def test_init_with_courses(self):
    #     self.assertEqual("Ivan", self.studen1.name)
    #     self.assertEqual({}, self.studen1.courses)

    def test_enroll_existing_course_new_notes(self):
        self.studen1.enroll("maths", ["third_note", "forth_note"], "")
        self.assertEqual(["first_note", "second_note", "third_note", "forth_note"], self.studen1.courses["maths"])
        self.assertEqual({'maths': ['first_note', 'second_note', 'third_note', 'forth_note'], 'lit': ['some_note', 'another_note']}, self.studen1.courses)

    def test_enroll_new_course_with_notes_without_text(self):
        self.assertEqual("Course and course notes have been added.", self.studen1.enroll("phys", ["phys_note1", "phys_note2"], ""))
        self.assertEqual({'maths': ['first_note', 'second_note'], 'lit': ['some_note', 'another_note'], "phys": ["phys_note1", "phys_note2"]}, self.studen1.courses)

    def test_enroll_new_course_with_notes_with_y(self):
        self.assertEqual("Course and course notes have been added.", self.studen1.enroll("phys", ["phys_note1", "phys_note2"], "Y"))
        self.assertEqual({'maths': ['first_note', 'second_note'], 'lit': ['some_note', 'another_note'], "phys": ["phys_note1", "phys_note2"]}, self.studen1.courses)

    def test_enroll_new_course_without_the_notes(self):
        self.assertEqual("Course has been added.", self.studen1.enroll("phys", ["phys_note1", "phys_note2"], "M"))
        self.assertEqual({'maths': ['first_note', 'second_note'], 'lit': ['some_note', 'another_note'], "phys": []}, self.studen1.courses)

    def test_add_notes_with_existing_course_without_notes(self):
        student2 = Student("Daniel", {"maths": []})
        self.assertEqual("Notes have been updated", student2.add_notes("maths", ["note1", "note2"]))
        self.assertEqual({"maths": [["note1", "note2"]]}, student2.courses)

    def test_add_notes_with_existing_course_with_notes(self):
        self.assertEqual("Notes have been updated", self.studen1.add_notes("maths", ["third_note", "forth_note"]))
        self.assertEqual({"maths": ["first_note", "second_note", ["third_note", "forth_note"]], "lit": ["some_note", "another_note"]}, self.studen1.courses)

    def test_add_notes_without_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("maths", ["third_note", "forth_note"])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_with_existing_course(self):
        self.assertEqual("Course has been removed", self.studen1.leave_course("maths"))
        self.assertEqual({"lit": ["some_note", "another_note"]}, self.studen1.courses)

    def test_leave_course_without_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("maths")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

if __name__ == '__main__':
    main()