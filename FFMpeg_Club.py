# file 'part1.mp4'
# file 'part2.mp4'
# file 'part3.mp4'
# file 'part4.mp4'
# file 'part5.mp4'
# file 'part6.mp4'
# file 'part7.mp4'
# file 'part8.mp4'
# file 'part9.mp4'
# file 'part10.mp4'
# file 'part11.mp4'
# file 'part12.mp4'
# file 'part13.mp4'
# file 'part14.mp4'
# file 'part15.mp4'
# file 'part16.mp4'
# file 'part17.mp4'
# file 'part18.mp4'
# file 'part19.mp4'
# file 'part20.mp4'
# file 'part21.mp4'
# in -> file_list.txt

import subprocess

# List of ffmpeg commands to be executed
commands = [
    "ffmpeg -i input.mp4 -ss 00:05:13 -to 00:08:27 -force_key_frames 00:05:13 -c copy part1.mp4",
    "ffmpeg -i input.mp4 -ss 00:10:08 -to 00:10:50 -force_key_frames 00:10:08 -c copy part2.mp4",
    "ffmpeg -i input.mp4 -ss 00:15:20 -to 00:15:31 -force_key_frames 00:15:20 -c copy part3.mp4",
    "ffmpeg -i input.mp4 -ss 00:16:34 -to 00:23:00 -force_key_frames 00:16:34 -c copy part4.mp4",
    "ffmpeg -i input.mp4 -ss 00:37:54 -to 00:38:02 -force_key_frames 00:37:54 -c copy part5.mp4",
    "ffmpeg -i input.mp4 -ss 00:39:01 -to 00:39:13 -force_key_frames 00:39:01 -c copy part6.mp4",
    "ffmpeg -i input.mp4 -ss 00:41:40 -to 00:42:00 -force_key_frames 00:41:40 -c copy part7.mp4",
    "ffmpeg -i input.mp4 -ss 01:04:14 -to 01:04:46 -force_key_frames 01:04:14 -c copy part8.mp4",
    "ffmpeg -i input.mp4 -ss 01:04:54 -to 01:05:45 -force_key_frames 01:04:54 -c copy part9.mp4",
    "ffmpeg -i input.mp4 -ss 01:13:46 -to 01:14:01 -force_key_frames 01:13:46 -c copy part10.mp4",
    "ffmpeg -i input.mp4 -ss 01:15:37 -to 01:23:50 -force_key_frames 01:15:37 -c copy part11.mp4",
    "ffmpeg -i input.mp4 -ss 01:25:08 -to 01:25:59 -force_key_frames 01:25:08 -c copy part12.mp4",
    "ffmpeg -i input.mp4 -ss 01:26:49 -to 01:27:40 -force_key_frames 01:26:49 -c copy part13.mp4",
    "ffmpeg -i input.mp4 -ss 01:48:21 -to 01:50:34 -force_key_frames 01:48:21 -c copy part14.mp4",
    "ffmpeg -i input.mp4 -ss 01:51:11 -to 01:52:55 -force_key_frames 01:51:11 -c copy part15.mp4",
    "ffmpeg -i input.mp4 -ss 01:53:21 -to 01:54:01 -force_key_frames 01:53:21 -c copy part16.mp4",
    "ffmpeg -i input.mp4 -ss 01:54:45 -to 01:55:03 -force_key_frames 01:54:45 -c copy part17.mp4",
    "ffmpeg -i input.mp4 -ss 01:55:43 -to 02:00:07 -force_key_frames 01:55:43 -c copy part18.mp4",
    "ffmpeg -i input.mp4 -ss 02:00:24 -to 02:01:20 -force_key_frames 02:00:24 -c copy part19.mp4",
    "ffmpeg -i input.mp4 -ss 02:01:47 -to 02:02:10 -force_key_frames 02:01:47 -c copy part20.mp4",
    "ffmpeg -i input.mp4 -ss 02:11:31 -to 02:15:07 -force_key_frames 02:11:31 -c copy part21.mp4"
]

# Function to execute a single ffmpeg command
def execute_command(command):
    print(f"Executing: {command}")
    result = subprocess.run(command, shell=True)
    
    if result.returncode == 0:
        print("Command executed successfully.")
    else:
        print(f"Error executing: {command}")

# Execute each ffmpeg command sequentially
for cmd in commands:
    execute_command(cmd)

# ffmpeg -f concat -safe 0 -i file_list.txt -c copy output.mp4