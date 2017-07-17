
"""The hello command."""


from json import dumps
from .base import Base

from .header import headerString


class Hello(Base):
    """Say hello, world!"""

    def run(self):
        print(headerString)
        print('Salut Julien!')
