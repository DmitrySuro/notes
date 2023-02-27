from datetime import datetime

class Note:
    def __init__(self, id='', title='', body='', time_create=datetime.now()):
        self.id = id
        self.title = title
        self.body = body
        self.time_create = time_create

    def __print__(self):
        print(
            f"ID: {self.id},Title: {self.title},Body: {self.body},Time: {self.time_create}")


new_note = Note('1', 'new notes', 'check note', '88')
new_note.__print__()
