from browser import Browser


class Utils (Browser):

    def nav(self ,url):
        self.drive.get(url)