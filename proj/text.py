"""Library for processing text."""
import jieba


def cut_text(text):
    """Cut text into words.

    Return a list of words. English and Chinese are cut separately.

    Args:
        text(str): string to be cut

    Return:
        :words:`list`: list of words
    """
    # TODO: separate English and Chinese
    return jieba.lcut(text)
