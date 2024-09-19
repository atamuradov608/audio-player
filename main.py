import pygame
import os
import mimetypes

# Функция для поиска аудиофайлов
def find_audio_files(directory: str = os.getcwd()) -> list[str]:
    audio_files = []
    # Проход по всем файлам и папкам в заданной директории и ее подкаталогах
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)   # Определяем путь к файлу
            mime_type, _ = mimetypes.guess_type(file_path)   # Определяем тип файла (audio/*)
            if mime_type and mime_type.startswith('audio') and file_path.endswith("mp3"):
                audio_files.append(os.path.abspath(file_path))   # Добавляем абсолютный путь к аудиофайлу

    return audio_files

# Функция для сохранения путей найденных аудиофайлов
def save_audio_paths(paths_list: list, open_mode: str = "w") -> None:
    # Переписываем audiopaths
    with open("audiopaths", open_mode) as file:
        for p in paths_list:
            file.write(p + "\n")

path = "/home/daetoya/Загрузки/Telegram Desktop/Eminem – Mockingbird.mp3"


pygame.mixer.init()
pygame.mixer.music.load(path)
pygame.mixer.music.play()

s = ""
while s != "exit":
    s = input("$ ")
    if s == "pause":
        pygame.mixer.music.pause()
    elif s == "unpause":
        pygame.mixer.music.unpause()
    elif s == "stop":
        pygame.mixer.music.stop()
    elif s == "play":
        pygame.mixer.music.play()

print("hello")