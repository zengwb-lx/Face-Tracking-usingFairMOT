import os

out_video = './result.mp4'
cmd_str = 'ffmpeg -f image2 -i {}/%05d.jpg -b 5000k -c:v mpeg4 {}'.format(os.path.join('.', 'frame'), out_video)
os.system(cmd_str)