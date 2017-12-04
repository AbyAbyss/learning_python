import student


class HighSchoolStudent(student.Student):
	school_name = "An International High School"

	def get_school_name(self):
		return "this is high School"

	def get_name_capitalize(self):
		original_value = super().get_name_capitalize()
		return original_value + "-HS"
