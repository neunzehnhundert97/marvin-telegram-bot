import re
from datetime import datetime
from typing import Hashable, Any

import aiotask_context


class User:
    """
    A wrapper around the user information which are by default contained in a dictionary
    """

    def __init__(self, user: dict):
        # Safe all usefull information as attributes
        self.id = user.get("id")
        self.is_bot = user.get('is_bot')
        self.first_name = user.get('first_name')
        self.last_name = user.get('last_name', "")
        self.username = user.get('username', "")
        self.language_code = user.get('language_code', "")

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __repr__(self):
        return "{} ({} {} [{}])".format(self.username, self.first_name, self.last_name, self.id)


class Message:
    """
    A wrapper around the message information which are by default contained in a dictionary
    """

    def __init__(self, msg: dict):
        # Safe all usefull information as attributes
        self.date = datetime.fromtimestamp(msg['date'])
        self.text = msg.get('text', None)


class Sticker:
    """
    A wrapper around the sticker information which are by default contained in a dictionary
    """

    def __init__(self, sticker: dict):
        # Safe all usefull information as attributes
        self.emoji = sticker['emoji']
        self.file_id = sticker['file_id']
        self.file_size = sticker['file_size']
        self.heigth = sticker['height']
        self.set_name = sticker['set_name']


class Context:
    """
    A wrapper around the aiotask_context to use additional functions
    """

    @staticmethod
    def get(key: Hashable) -> Any:
        return aiotask_context.get(key)

    @staticmethod
    def set(key: Hashable, value: Any) -> None:
        aiotask_context.set(key, value)

    @staticmethod
    def __getitem__(key: Hashable) -> Any:
        return aiotask_context.get(key)

    @staticmethod
    def __setitem__(key: Hashable, value: Any) -> Any:
        aiotask_context.set(key, value)


# Source: https://djangosnippets.org/snippets/309/
class RegExDict(object):
    """A dictionary-like object for use with regular expression keys.
    Setting a key will map all strings matching a certain regex to the
    set value.

    One caveat: the order of the iteration over items is unspecified,
    thus if a lookup matches multiple keys, it is unspecified which
    value will be returned - still, one such value will be returned.
    """

    def __init__(self):
        self._regexes = {}

    def __getitem__(self, name):
        for regex, value in self._regexes.items():
            m = regex.match(name)
            if m is not None:
                return value
        raise KeyError('Key does not match any regex')

    def __contains__(self, item):
        try:
            self[item]
        except KeyError:
            return False
        else:
            return True

    def __setitem__(self, regex, value):
        self._regexes[re.compile(regex)] = value
