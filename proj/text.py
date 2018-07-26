"""Library for processing text."""
import jieba


def cut_text(text):
    r"""Cut text into words.

    Return a list of words. English and Chinese are cut separately.

    Test math\: :math:`\frac{b^2-4ac}{2a}`

    Args:
        text (str): string to be cut

    Return:
        list: list of words

    .. note::
        Test note.

    .. warning::
        Test warning.

    .. todo::
        * Separate English and Chinese.

    Example:
        >>> cut_text('测试')
    """
    return jieba.lcut(text)
