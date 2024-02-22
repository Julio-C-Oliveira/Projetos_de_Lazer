from datetime import date, datetime as time
import os

ffmpeg_paste = 'C:\\Users\\julio\\OneDrive\\Área de Trabalho\\Julio\\FFMPEG\\FFMPEG\\bin'
input_path = 'C:\\Users\\julio\\OneDrive\Área de Trabalho\\Julio\\Animes\\_Opening\\Editor\\Original'
output_path = 'C:\\Users\\julio\\OneDrive\\Área de Trabalho\\Julio\\Animes\\_Opening\\Editor\\Editado'

files_list = os.listdir(input_path)
video_files = []
setting_files = []

start_time = f"{time.now().hour}:{time.now().minute}:{time.now().second}"

for file in files_list:
    if "txt" in file:
        setting_files.append(file)
    else:
        video_files.append(file)

if len(setting_files) == len(video_files):
    print("\n###################################\n")
    print(f"Configurações: {setting_files}")
    print(f"OPs: {video_files}")
    print("\n###################################")

    os.system("powercfg -change -monitor-timeout-ac 0")
    os.system("powercfg -change -monitor-timeout-dc 0")
    os.system("powercfg -change -standby-timeout-ac 0")
    os.system("powercfg -change -standby-timeout-dc 0")

    number_of_videos = len(video_files)

    for i_video in range(number_of_videos):
        print("\n###################################\n")
        print(video_files[i_video])
        print(setting_files[i_video])
        print("\n###################################\n")

        video_path_input = f"{input_path}\\{video_files[i_video]}"
        video_path_output = f"{output_path}\\{video_files[i_video]}"
        setting_path = f"{input_path}\\{setting_files[i_video]}"

        with open(setting_path) as s:
            settings = s.read().split("\n")

        codec = f"-c:v {settings[0]}" if settings[0] != "none" else "-c:v libx264"
        subtitle = f"-c:s {settings[1]} -map 0:0 -map 0:1 -map 0:2" if settings[1] != "none" else "none"
        preset = f"-preset {settings[2]}" if settings[2] != "none" else "-preset veryslow"
        bit_rate = f"-b:v {settings[3]}" if settings[3] != "none" else  " "
        crf = f"-crf {settings[4]}" if settings[4] != "none" else  "-crf 18"
        start = settings[5]
        end = settings[6]
        extra = settings[7] if settings[7] != "none" else ""

        print(f"Entrada: {video_path_input}")
        print(f"Saída: {video_path_output}")

        if subtitle == "none":
            os.system(f"cd {ffmpeg_paste} && ffmpeg -i \"{video_path_input}\" {codec} -map 0:0 -map 0:1 {preset} {bit_rate} {crf} -ss {start} -to {end} -y \"{video_path_output}\"")
        else:
            os.system(f"cd {ffmpeg_paste} && ffmpeg -i \"{video_path_input}\" {codec} {subtitle} {extra} {preset} {bit_rate} {crf} -c:a aac -b:a 256k -ss {start} -to {end} -y \"{video_path_output}\"")
            #os.system(f"cd {ffmpeg_paste} && ffmpeg -i \"{video_path_input}\" {codec} -map 0:0 -map 0:1 {extra} {preset} {bit_rate} {crf} -c:a aac -b:a 256k -ss {start} -to {end} -y \"{video_path_output}\"")

    os.system("powercfg -change -monitor-timeout-ac 5") # Desligamento da tela em 5min quando conectado ao carregador
    os.system("powercfg -change -monitor-timeout-dc 5") # Desligamento da tela em 5min quando não conectado ao carregador
    os.system("powercfg -change -standby-timeout-ac 5") # Suspensão em 5 min quando conectado ao carregador
    os.system("powercfg -change -standby-timeout-dc 5") # Suspensão em 5 min quando não conectado

    end_time = f"{time.now().hour}:{time.now().minute}:{time.now().second}"

    with open("_log_.txt", "a+") as file:
        file.write(f"Day: {date.today()} | Start: {start_time} | End: {end_time} | Files: {video_files}\n")

    os.system('shutdown /s /t 20')

    answer = input("You want a cancel the turn off? Y or N: ").upper()[:1]

    if answer == "Y":
        os.system('shutdown /a')
        print("Cancelado")

else:
    print("ERRO, o número de arquivos de video é diferente do número de configurações.")