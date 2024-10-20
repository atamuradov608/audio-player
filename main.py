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

# Основной класс для работу с аудио
class PlayList:
    def __init__(self):
        #self.audio_list: list[str] = find_audio_files("/home/")  # Находим все аудиофайлы
        #self.current_audio_index: int = 0     # Выбираем самое первое найденное аудио
        pygame.mixer.init()       # запускаем mixer для работу со звуком
        #self.balance()      # загружаем в mixer выбранное аудио

    def all_audio(self):
        self.audio_list: list[str] = find_audio_files("/home/")  # Находим все аудиофайлы
        self.current_audio_index: int = 0     # Выбираем самое первое найденное аудио
        self.balance()  # загружаем в mixer выбранное аудио

    # Функция для загрузки в mixer выбранное аудио
    def balance(self):
        pygame.mixer.music.load(self.audio_list[self.current_audio_index])

    # Фукция для вывода полного плейлиста в консоль
    def print_full_playlist(self):
        for i, el in enumerate(self.audio_list, start=1):
            if i == self.current_audio_index + 1:
                print("-> ", end="")
            print(f"{i}) {get_audio_name(el)}")

    # Функция для вывода части плейлиста
    def print_playlist_part(self, audio_count_radius: int = 7):
        audio_count_radius = min(audio_count_radius, (len(self.audio_list) - 1) // 2)
        num1 = max(0, self.current_audio_index - audio_count_radius)
        num2 = min(len(self.audio_list), self.current_audio_index + audio_count_radius + 1)
        for i, el in enumerate(self.audio_list[num1:num2], start=num1+1):
            if i == self.current_audio_index + 1:
                print("-> ", end="")
            print(f"{i}) {get_audio_name(el)}")

    # Выбрать другое аудио
    def change_audio(self, num: int) -> None:
        self.current_audio_index = num    # Выбираем номер нужного аудио
        self.balance()          # обновляем аудио
        self.play_audio()     # включаем выбранное аудио

    # включить аудио
    def play_audio(self):
        pygame.mixer.music.play()

    # поставить текущее аудио на паузу
    def pause_audio(self):
        pygame.mixer.music.pause()

    # убрать с паузы
    def unpause_audio(self):
        pygame.mixer.music.unpause()

    # завершить текущее аудио
    def stop_audio(self):
        pygame.mixer.music.stop()

    # запустить следующее аудио
    def next_audio(self):
        self.change_audio(self.current_audio_index + 1)

    # запустить предыдущее аудио
    def previous_audio(self):
        self.change_audio(self.current_audio_index - 1)

    # запуск программы
    def start_cycle(self):
        # пользовательские консольные команды
        commands = {
            "play": self.play_audio,                 # воспроизвести аудио
            "pause": self.pause_audio,               # поставить аудио на паузу
            "unpause": self.unpause_audio,           # продолжить воспроизведение
            "stop": self.stop_audio,                 # завершить текущее аудио
            "next": self.next_audio,                 # запустить следующее аудио
            "previous": self.previous_audio,         # запусить предыдущее аудио
            "full": self.print_full_playlist,        # вывести плейлист
            "playlist": self.print_playlist_part     # вывести часть плейлиста
        }
        user_input = ""
        while user_input != "exit":
            user_input = input("$ ")
            if commands.__contains__(user_input):
                commands[user_input]()
            elif user_input.isdigit() and int(user_input) <= len(self.audio_list):
                self.change_audio(int(user_input) - 1)



playlist = PlayList()
playlist.all_audio()
playlist.print_full_playlist()
playlist.start_cycle()
