import os, glob, shutil
from os import path

all_files = glob.glob('*.jpg')
# print(all_files)

# <div class="card">
#   <img class="card-img-top img-fluid" src="static/images/photo1.jpg" alt="Card image cap">            
# </div>

html = ''

for index, filename in enumerate(all_files):

    # file rename
    # current_filename = path.realpath(filename)
    # print(current_filename)
    # new_filename = str(index + 1) + '.jpg'
    # os.rename(current_filename, new_filename)

    # html generation
    h = '<div class="card">' + '<img class="card-img-top img-fluid" src="static/images/Travel Diaries/'+filename+'" alt="Card image cap">' + '</div>'
    # h = '<div class="card">' +  '<img class="card-img-top img-fluid" src="static/images/'+filename+'.jpg" alt="Card image cap">' +          
    #        '</div>'
    html = html + h

print(html)
f = open('s.html', 'w')
f.write(html)