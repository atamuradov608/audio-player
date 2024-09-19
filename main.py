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

def get_audio_name(path: str) -> str:
    ind = -1
    for i in range(len(path) - 1, -1, -1):
        if path[i] == "/":
            ind = i
            break
    return path[ind + 1:]

class PlayList:
    def __init__(self):
        self.audio_list: list[str] = find_audio_files("/home/")
        self.current_audio_index: int = 0
        pygame.mixer.init()
        self.balance()

    def balance(self):
        pygame.mixer.music.load(self.audio_list[self.current_audio_index])

    def print_playlist(self):
        for i, el in enumerate(self.audio_list, start=1):
            if i == self.current_audio_index + 1:
                print("-> ", end="")
            print(f"{i}) {get_audio_name(el)}")

    def change_audio(self, num: int) -> None:
        self.current_audio_index = num

    def play_audio(self):
        pygame.mixer.music.play()

    def pause_audio(self):
        pygame.mixer.music.pause()

    def unpause_audio(self):
        pygame.mixer.music.unpause()

    def stop_audio(self):
        pygame.mixer.music.stop()

    def next_audio(self):
        self.current_audio_index += 1
        self.balance()
        self.play_audio()

    def previous_audio(self):
        self.current_audio_index -= 1
        self.balance()
        self.play_audio()

    def start_cycle(self):
        commands = {
            "play": self.play_audio,            # воспроизвести аудио
            "pause": self.pause_audio,          # поставить аудио на паузу
            "unpause": self.unpause_audio,      # продолжить воспроизведение
            "stop": self.stop_audio,            # завершить текущее аудио
            "next": self.next_audio,            # запустить следующее аудио
            "previous": self.previous_audio,    # запусить предыдущее аудио
            "playlist": self.print_playlist     # вывести плейлист
        }
        user_input = ""
        while user_input != "exit":
            user_input = input("$ ")
            if commands.__contains__(user_input):
                commands[user_input]()



playlist = PlayList()
playlist.print_playlist()
playlist.start_cycle()