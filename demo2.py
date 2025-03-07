from moviepy.editor import *
start=input("enter the starting tinme in s")
end=input("enter the endtime in s ")
clip = VideoFileClip("clip.mp4").subclip(start,end)
txt_clip = TextClip("bharath",fontsize=70,color='white')   #error as not able to import *
txt_clip = txt_clip.set_pos('center').set_duration(end-start)
clip = CompositeVideoClip([clip, txt_clip])
clip.write_videofile("myHolidays_edited.webm")
