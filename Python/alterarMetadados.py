import os

# Caminho da pasta
folder_path = "Musics"

# Listar arquivos na pasta
file_names = os.listdir(folder_path)

# Filtrar apenas arquivos (ignorar subpastas)
file_names = [f for f in file_names if os.path.isfile(os.path.join(folder_path, f))]

from mutagen.easyid3 import EasyID3
from mutagen.mp4 import MP4

# Exibir os nomes dos arquivos
for file_name in file_names:
    music_name, artist_name = file_name.split(" - ")

    file_path = f"{folder_path}/{file_name}"

    if "mp3" in file_name:
        artist_name = artist_name.replace(".mp3", "")

        audio = EasyID3(file_path)

        audio['title'] = music_name
        audio['artist'] = artist_name

        audio.save()

    elif "m4a" in file_name:
        artist_name = artist_name.replace(".m4a", "")

        audio = MP4(file_path)

        audio["\xa9nam"] = music_name
        audio["\xa9ART"] = artist_name

        audio.save()