#!/usr/bin/python3
"""
UTF-8 Validation"""


def validUTF8(data):
    """
    Check if the given data is a valid UTF-8 encoding.

    :param data: list of integers representing the bytes of the data
    :return: True if the data is a valid UTF-8 encoding, False otherwise
    """
    count = 0
    for byte in data:
        if count == 0:
            if (byte >> 5) == 0b110:
                count = 1
            elif (byte >> 4) == 0b1110:
                count = 2
            elif (byte >> 3) == 0b11110:
                count = 3
            elif (byte >> 7):
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            count -= 1
    return count == 0
