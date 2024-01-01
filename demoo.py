from moviepy.editor import *

clip1 = VideoFileClip("clip.mp4")
clip2 = VideoFileClip("clip2.mp4")        #change names here
clip3 = VideoFileClip("clip3.mp4")
final_clip = concatenate_videoclips([clip1,clip2,clip3])
final_clip.write_videofile("my_concatenation.mp4")
