from datetime import datetime

# FORMAT TIME
def format_time():

    return datetime.utcnow().strftime(
        "%d-%m-%Y %H:%M:%S"
    )

# CLEAN TEXT
def clean_text(text):

    return text.strip()

# HUMAN SIZE
def human_size(size):

    for unit in [
        "B",
        "KB",
        "MB",
        "GB",
        "TB"
    ]:

        if size < 1024:
            return f"{size:.2f} {unit}"

        size /= 1024
