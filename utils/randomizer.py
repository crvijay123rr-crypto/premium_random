import random

# RANDOM VIDEO
def random_video(videos):

    if not videos:
        return None

    return random.choice(videos)
