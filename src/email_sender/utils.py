import re
from pathlib import Path


def is_email(email: str) -> bool:
    """Validate whether a given string is a valid email address.

    This function checks if the input string matches the standard email address format 
    using a regular expression.

    ## Args:
        `email (str)`: The email address to validate.

    ## Returns:
        `bool`: True if the input string is a valid email address, False otherwise.

    ## Example:
        >>> is_email("example@example.com")
        True
        >>> is_email("invalid-email")
        False
    """
    EMAIL_REGEX = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(EMAIL_REGEX, email))
    
def get_placeholders(template_text: str, delimiter_pair: tuple[str, str] = ("{{", "}}")) -> list[str]:
    """Extract placeholders enclosed by delimiters from a template string.

    This function identifies and retrieves all placeholders in the given template text 
    that are enclosed by the specified opening and closing delimiters.

    ## Args:
        `template_text (str)`: The string containing placeholders enclosed by delimiters.
        `delimiter_pair (tuple[str, str])`: A tuple containing the opening and closing 
            delimiters that wrap placeholders (e.g., `("{{", "}}")`).

    ## Returns:
        `list[str]`: A list of placeholder names (strings) found in the template, excluding 
        the delimiters.

    ## Example:
        >>> template = "Hello, {{name}}! Welcome to {{place}}."
        >>> delimiters = ("{{", "}}")
        >>> get_placeholders(template, delimiters)
        ['name', 'place']
    """
    return list(set(
        re.findall(rf'{delimiter_pair[0]}(.*?){delimiter_pair[1]}', template_text)
    ))

def get_paths_from_string(text: str) -> list[Path]:
    """Convert a comma-separated string of file paths into a list of `Path` objects.

    This function takes a string containing file paths separated by commas, removes 
    any leading or trailing whitespace, newline characters, or quotes around each path, 
    and returns a list of `Path` objects.

    ## Args:
        `text (str)`: A comma-separated string of file paths. Each path can be enclosed 
            in single or double quotes and may contain leading or trailing whitespace.

    ## Returns:
        `list[Path]`: A list of `Path` objects, each representing a cleaned file path.

    ## Example:
        >>> get_paths_from_string("'file1.txt', 'file2.txt', 'file3.txt'")
        [Path('file1.txt'), Path('file2.txt'), Path('file3.txt')]

        >>> get_paths_from_string('file1.txt, file2.txt , file3.txt')
        [Path('file1.txt'), Path('file2.txt'), Path('file3.txt')]
    """
    return [Path(p.strip("\n\r '\"")) for p in text.strip("\n\r ,").split(",")]
