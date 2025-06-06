import html
from difflib import ndiff

def highlight_differences(original_text, corrected_text):
    """
    Highlights added and removed lines between original and corrected text.
    Additions appear in green; deletions in red strikethrough.
    """
    diff = ndiff(original_text.splitlines(), corrected_text.splitlines())
    highlighted = []

    for line in diff:
        escaped_line = html.escape(line[2:])  # escape HTML characters
        if line.startswith('+ '):
            highlighted.append(f"<span class='added'>{escaped_line}</span>")  # Use CSS class
        elif line.startswith('- '):
            highlighted.append(f"<span class='removed'>{escaped_line}</span>")  # Use CSS class
        elif line.startswith('? '):
            # Ignore '?' helper lines from ndiff
            continue
        else:
            highlighted.append(escaped_line)

    return '<br>'.join(highlighted)
