import json


"""
Obiekt reprezentujący notatki.
"""


class Note():
    """
    Class representing a note.

    A note within this context means a path to a file that could be a text note or an executable
    script, or an URL address.

    Args:
    - value: a full path or value that is being represented
    - name: a unique name of the note
    - tags: a list of tags that will be used for categorising the note
    """
    def __init__(self, value:str, name:str, tags:list = None):
        self.value = value
        self.name = name
        self.tags = tags

    def contains_tag(self, tag:str):
        return True if tag in self.tags else False

    def get_value(self):
        return self.value

    def save_note(self):
        pass

    def get_tags(self):
        return self.tags

    def copy_note_to_clipboard(self):
        pass


def get_class_from_json(jason):
    j = json.loads(jason)

    note = Note(
        value = j["value"]
        name = j["name"]
        tags = j["tags"]
    )

    return note


def main():
    pass


if __name__ == "__main__":
    main()