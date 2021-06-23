from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.recording = False
        self.courses = set()

    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):
        if tag != 'td':
            return
        if self.recording:
            self.recording = True
            return
        for name, value in attrs:
            if name == 'class' and value == 'subjectNumberColumnValue nowrap ':
                break
            else:
                return
        self.recording = True

    def handle_endtag(self, tag):
        if tag == 'td' and self.recording:
            self.recording = False

    def handle_data(self, data):
        if self.recording:
            course_name = str(data).strip()
            if len(course_name) != 0:
                self.courses.add(course_name)
