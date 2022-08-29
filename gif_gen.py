from moviepy.editor import VideoFileClip
#You need ffmpeg installed to run this script

def moviepy_gif_maker():
    video_clip = VideoFileClip("wendyflex.mp4")
    video_clip.write_gif("wendyflex.gif", fps=24)
    video_clip.close()


moviepy_gif_maker()
