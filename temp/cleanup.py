import os

# CLEAN CACHE
def clean_cache():

    folder = "temp/cache"

    for file in os.listdir(folder):

        path = os.path.join(
            folder,
            file
        )

        try:

            if os.path.isfile(path):

                os.remove(path)

                print(
                    f"✅ Removed Cache : {file}"
                )

        except Exception as e:

            print(
                f"❌ Cache Error : {e}"
            )

# CLEAN DOWNLOADS
def clean_downloads():

    folder = "temp/downloads"

    for file in os.listdir(folder):

        path = os.path.join(
            folder,
            file
        )

        try:

            if os.path.isfile(path):

                os.remove(path)

                print(
                    f"✅ Removed Download : {file}"
                )

        except Exception as e:

            print(
                f"❌ Download Error : {e}"
            )

# CLEAN DEMO FILES
def clean_demo():

    folder = "temp/demo_temp"

    for file in os.listdir(folder):

        path = os.path.join(
            folder,
            file
        )

        try:

            if os.path.isfile(path):

                os.remove(path)

                print(
                    f"✅ Removed Demo : {file}"
                )

        except Exception as e:

            print(
                f"❌ Demo Error : {e}"
            )

# FULL CLEANUP
def full_cleanup():

    print(
        "🧹 STARTING CLEANUP..."
    )

    clean_cache()

    clean_downloads()

    clean_demo()

    print(
        "🔥 TEMP CLEANUP COMPLETED"
    )

# AUTO RUN
if __name__ == "__main__":

    full_cleanup()
