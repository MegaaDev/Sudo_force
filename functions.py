import typer
import random
import time
import os


app = typer.Typer()


def tossCoin():
    return (random.choice(["H", "T"]))


def find_audio_folders(search_path):
    command = (
        f"find {search_path} -type f -exec file --mime-type {{}} + | "
        "grep -E 'audio/(mp3|wav|flac)' | cut -d: -f1 | sort -u"
    )
    try:
        result = os.popen(command).read()
        folders = result.strip().split('\n')
        return folders
    except Exception as e:
        print(f"Error: {e}")
        return None


def playMusic():
    music_folder_current_user = os.path.join(os.path.expanduser("~"), "Music")
    print("Music Folder for Current User:", music_folder_current_user)

    files = os.listdir(music_folder_current_user)

    audio_file_extensions = ['.mp3', '.wav',
                             '.flac', '.mp4', '.mkv', '.webm', '.mov']
    audio_files = [file for file in files if any(
        file.lower().endswith(ext) for ext in audio_file_extensions)]
    audio_files = sorted(audio_files, key=lambda x: os.path.getmtime(
        os.path.join(music_folder_current_user, x)), reverse=True)

    for file in audio_files:
        print(file)

    while True:
        verify_folder = input("Choose a different folder? (y/n)")
        if verify_folder.lower() == "y":
            music_folder_current_user = input(
                "Enter the path to your music folder: ")
            files = os.listdir(music_folder_current_user)
            files = sorted(files, key=lambda x: os.path.getmtime(
                os.path.join(music_folder_current_user, x)), reverse=True)
            for file in files:
                print(file)
        else:
            break

    file_index = int(input("Enter the index of the file you want to play: "))
    if os.name == 'nt':
        os.startfile(os.path.join(
            music_folder_current_user, files[file_index]))
    elif os.name == 'posix':
        file_path = os.path.join(music_folder_current_user, files[file_index])
        quoted_file_path = f'"{file_path}"'
        command = f"open {quoted_file_path}"
        os.system(command)
    else:
        print("Platform not recognized.")


def dateAndTime(command):

    if ("date" in command) and ("time" in command):
        print(time.strftime('%Y-%m-%d %H:%M:%S'), end='\r')
    elif ("date" in command):
        print(time.strftime('%Y-%m-%d'), end='\r')
    elif ("time" in command):
        print(time.strftime('%H:%M:%S'), end='\r')
    else:
        print(time.strftime('%Y-%m-%d %H:%M:%S'), end='\r')
    print()


def countdown(seconds):
    start = int(time.time()) + int(seconds)
    while start >= int(time.time()):
        remaining_time = start - int(time.time())
        formatted_time = time.strftime("%H:%M:%S", time.gmtime(remaining_time))
        print(formatted_time, end='\r')
        time.sleep(0.1)
    print()


def stopwatch():
    start_time = int(time.time())
    while True:
        elapsed_time = int(time.time()) - start_time
        formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
        print(formatted_time, end='\r')
        time.sleep(0.1)
