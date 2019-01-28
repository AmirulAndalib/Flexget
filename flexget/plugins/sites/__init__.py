"""
Utilities for search plugins, please try to avoid adding new ones.
"""
import re
from unicodedata import normalize


def normalize_unicode(text):
    if isinstance(text, str):
        # Convert to combined form for better search results
        return normalize('NFC', text)
    return text


def normalize_scene(text):
    """Normalize string according to scene standard.
    Mainly, it replace accented chars by their 'normal' couterparts
    and removes special chars.
    https://en.wikipedia.org/wiki/Standard_(warez)#Naming for more information
    """
    # Allowed chars in scene releases are:
    #     ABCDEFGHIJKLMNOPQRSTUVWXYZ
    #     abcdefghijklmnopqrstuvwxyz
    #     0123456789-._()
    return re.sub(r'[^a-zA-Z0-9 \-._()]',
                  '',
                  normalize('NFKD', text).encode('ASCII', 'ignore').decode())


def torrent_availability(seeds, leeches):
    """Returns a rating based on seeds and leeches for a given torrent.
    :param seeds: Number of seeds on the torrent
    :param leeches: Number of leeches on the torrent
    :return: A numeric rating
    """
    return seeds * 2 + leeches
