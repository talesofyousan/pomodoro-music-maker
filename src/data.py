

class MusicTime():
    def __init__(self, music_time):
        self.music_time = music_time

class MusicList():
    def __init__(self, list_music_time):
        self.list_music_time : list[int] = list_music_time

    def append_music_time(self, music_time):
        if isinstance(music_time, int):
            self.list_music_time.append(music_time)
        elif isinstance(music_time, list):
            self.list_music_time += music_time


class PlayList():
    def __init__(self, play_list):
        self.play_list : list[MusicList] = play_list

    def append_music_time(self, music_list):
        self.play_list.append(music_list)