from os.path import join

path_segment_1 = "/Home/User"
path_segment_2 = "Codecademy/videos"
path_segment_3 = "cat_videos/surprised_cat.mp4"

# join all three of the paths here!
print(join(path_segment_1,path_segment_2,path_segment_3))

def myjoin(*args):
  str1=args[0] + "/"
  for i in range(1,len(args)):
    str1+=args[i]
  return str1


print(myjoin(path_segment_1,path_segment_2,path_segment_3))