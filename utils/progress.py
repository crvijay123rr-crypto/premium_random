import math

# PROGRESS BAR
def progress_bar(current, total):

    percentage = current / total * 100

    filled = math.floor(
        percentage / 10
    )

    empty = 10 - filled

    bar = (
        "█" * filled
        + "░" * empty
    )

    return f"""
{bar}

{percentage:.2f}%
"""
