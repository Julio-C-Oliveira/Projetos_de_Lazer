import os

ffmpeg_paste = 'C:\\Users\\julio\\OneDrive\\Área de Trabalho\\Julio\\FFMPEG\\FFMPEG\\bin'
input_path = 'C:\\Users\\julio\\OneDrive\Área de Trabalho\\Julio\\Animes\\_Opening\\Editor\\Standby'

files_list = os.listdir(input_path)
video_files = []

for file in files_list:
    video_files.append(file)

print(video_files)

number_of_videos = len(video_files)

for i_video in range(number_of_videos):
    print("\n###################################\n")
    print(video_files[i_video])
    print("\n###################################\n")

    video_path_input = f"{input_path}\\{video_files[i_video]}"

    os.system(f"cd {ffmpeg_paste} && ffmpeg -i \"{video_path_input}\" -y \"{video_path_input}.ass\"")