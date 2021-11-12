from html.parser import HTMLParser


class ASUCoursesHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.recording = False
        self.courses = set()
        self.candidate_course = ""

    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):
        if tag != 'td' and tag != 'i':
            return
        if self.recording:
            self.recording = True
            return
        for name, value in attrs:
            if name == 'class' and value == 'subjectNumberColumnValue nowrap ':
                self.recording = True
            if name == 'class' and value == 'fa fa-circle green':
                if len(self.candidate_course) != 0:
                    self.courses.add(self.candidate_course)

    def handle_endtag(self, tag):
        if tag == 'td' and self.recording:
            self.recording = False

    def handle_data(self, data):
        if self.recording:
            course_name = str(data).strip()
            if len(course_name) != 0:
                self.candidate_course = course_name
