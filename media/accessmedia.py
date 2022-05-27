"""
THIS MODULE DEALS WITH THE MEDIA FILES
"""
from iovoice.input import voiceinput
from iovoice.output import speak
from .downloadmedia import searchonline

import os

def searchandplay(term,/):
    """
        looks for file containing the term in its name
    """

    walk_result = list(os.walk(
        os.path.join(
            os.getcwd(),
            "downloads"
        )
    ))

    if walk_result:
        ch = voiceinput("No result found with given term. Would you like me to search it online?")
        if 'yes' in ch:
            searchonline(term)
    else:
        pass