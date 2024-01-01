from moviepy.editor import *

clip=VideoFileClip("C:\\Users\\Bharath K\\Documents\\video editor\\clip.mp4")
clip2=VideoFileClip("C:\\Users\\Bharath K\\Documents\\video editor\\clip2.mp4")
clip3=VideoFileClip("C:\\Users\\Bharath K\\Documents\\video editor\\clip3.mp4")

aclip=AudioFileClip("C:\\Users\\Bharath K\\Documents\\video editor\\aclip.mp3")
aclip2=AudioFileClip("C:\\Users\\Bharath K\\Documents\\video editor\\aclip2.mp3")
aclip3=AudioFileClip("C:\\Users\\Bharath K\\Documents\\video editor\\aclip3.mp3")

def rotate():               #contains rotating,downsizing,adding margin
    clip1 = VideoFileClip("clip.mp4") # add 10px contour(margin like)
    rot=int(input("do u want to rotate the video along 1)x-axisc2)y-axis\n 3)x \nand y-axis"))
    if rot==1:
        clip2 = clip1.fx( vfx.mirror_x)
        final_clip = clips_array([[clip1, clip2]])
    elif rot==2:
        clip2 = clip1.fx( vfx.mirror_y)
        final_clip = clips_array([[clip1, clip2]])
    else:
        clip2 = clip1.fx( vfx.mirror_x)
        clip3 = clip1.fx( vfx.mirror_y)
        final_clip = clips_array([[clip1, clip2,clip3]])
    resp=input("do u want to downsize the video \n1)yes \n2)no")
    if resp=='yes':
        d=input("enter the downsize%\n")
        dp=d/100
        clip4 = final_clip.resize(dp) #clip4 = clip1.resize(0.60) # downsize 60% downsize 60%
    else:
        pass
    final_clip.resize(width=480).write_videofile("my_stack.mp4")

def volchange():
    e=int(input("enter the volume change magnitude\n")) #anything above 100% increases volume
    ep=e/100
    final_clip1 = clip.volumex(ep)
    final_clip1.write_videofile("volume_change.mp4")

def addoverlay():
    start=input("enter the starting tinme in s\n")
    end=input("enter the endtime in s \n")
    clip = VideoFileClip("C:\\Users\\Bharath K\\Documents\\video editor\\clip.mp4").subclip(start,end)
    txt_clip = TextClip("bharath",fontsize=70,color='white')   #error as not able to import *
    txt_clip = txt_clip.set_pos('center').set_duration(10)
    clip = CompositeVideoClip([clip, txt_clip])
    clip.write_videofile("myHolidays_edited.webm")

def concatenaite():
    clip1 = VideoFileClip("C:\\Users\\Bharath K\\Documents\\video editor\\clip.mp4")
    clip2 = VideoFileClip("C:\\Users\\Bharath K\\Documents\\video editor\\clip2.mp4")        #change names here
    clip3 = VideoFileClip("C:\\Users\\Bharath K\\Documents\\video editor\\clip3.mp4")
    final_clip = concatenate_videoclips([clip1,clip2,clip3])
    final_clip.write_videofile("my_concatenation.mp4")

def delay():
    clip=VideoFileClip("clip.mp4")
    clip2=VideoFileClip("clip2.mp4")
    clip3=VideoFileClip("clip3.mp4")
    strt=int(input("enter the delay time for clip2\n"))
    strt1=int(input("enter the delay time for clip3\n"))
    final_clip= CompositeVideoClip([clip, # starts at t=0
                            clip2.set_start(strt),
                            clip3.set_start(strt1)])
    final_clip.write_videofile("delay_clip.mp4")

def crossfade():
    clip=VideoFileClip("C:\\Users\\Bharath K\\Documents\\video editor\\clip.mp4")
    clip2=VideoFileClip("C:\\Users\\Bharath K\\Documents\\video editor\\clip2.mp4")
    clip3=VideoFileClip("C:\\Users\\Bharath K\\Documents\\video editor\\clip3.mp4")
    str=int(input("enter the delay time for clip2\n"))
    str2=int(input("enter the delaytime for clip3\n"))
    crsfd1=int(input("enter the crossfade period for clip2\n"))
    crsfd2=int(input("enter the crossfade period for clip3\n"))
    final_clip = CompositeVideoClip([clip, # starts at t=0
                            clip2.set_start(str).crossfadein(crsfd1),
                            clip3.set_start(str2).crossfadein(crsfd2)])
    final_clip.write_videofile("crossfade_clip.mp4")
    
def positioning():
    
    final_clip = CompositeVideoClip([clip,
                           clip2.set_position((45,150)),
                           clip3.set_position((90,100))])
    final_clip.write_videofile("positioning_clip.mp4")


def audioedit():
    aclip=AudioFileClip("C:\\Users\\Bharath K\\Documents\\video editor\\aclip.mp3")
    aclip2=AudioFileClip("C:\\Users\\Bharath K\\Documents\\video editor\\aclip2.mp3")
    aclip3=AudioFileClip("C:\\Users\\Bharath K\\Documents\\video editor\\aclip3.mp3")
    v1=int(input("enter the volume change'%' for clip1\n "))
    v1p=v1/100
    s2=int(input("enter the start time for clip2\n"))
    v2=int(input("enter the volume change'%' for clip2 \n"))
    v2p=v2/100
    s3=int(input("enter the start time for clip3\n"))
    v3=int(input("enter the volume change'%' for clip3\n "))
    v3p=v3/100
    concat = concatenate_audioclips([aclip,aclip2,aclip3])
    compo = CompositeAudioClip([aclip.volumex(v1p),
                            aclip2.set_start(s2).volumex(v2p), # start at t=5s
                            aclip3.set_start(s3).volumex(v3p)])
    concat.write_audiofile("audiofile1.mp3")
    #compo.write_audiofile("audiofile2.mp3")

print("what would you want to do to your video\n")
print("following are the options\n")
print("""1) rotate/downsize/add margin
2) change the volume of the video
3) add overlay
4)concatenate
5)add delays
6)add crossfade
7) positioning
8)edit your audio file
""")
n=int(input())
if n==1:
    rotate()
elif n==2:
    volchange()
elif n==3:
    addoverlay()
elif n==4:
    concatenaite()
elif n==5:
    delay()
elif n==6:
    crossfade()
elif n==7:
    positioning()
elif n==8:
    audioedit()
else:
    print("invalid choice")

    

