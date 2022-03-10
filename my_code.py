import sys
import requests
import os

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

sha = ""
if len(sys.argv) >= 1: 
  sha = sys.argv[1]
  url = r"https://api.github.com/repos/wmwilson87/HelloWorld/commits/" + sha
  author = ""
  touchedFiles = []
  receive = requests.get(url)
  if receive.status_code == 200:
    ret = receive.json()
    if "author" in ret.keys() and "login" in ret["author"]:
      author = ret["author"]["login"]
    if "files" in ret.keys():
      for f in ret["files"]:
        if "filename" in f: touchedFiles.append(f["filename"])
    
    print("\n\n%s modified files [\n%s\n]" %(author, ',\n'.join(touchedFiles)))
    
  else:
    print("url: '%s' error in request." %url)
else:
  print("sha not included.")

touchedDirs = [] 
for tF in touchedFiles:
  tF_split = tF.split("/")
  if len(tF_split) >= 1:
    full_tF = os.path.join(tF_split[0], tF_split[1])
    if full_tF not in touchedDirs: touchedDirs.append(full_tF)   
    potential = ""
    if "games" in tF_split[0]:
      print("this is a game: '%s'"%tF_split[1])
      potential = r"2. Implementation\14. Data\TP_config.json"
    elif "casino" in tF_split[0]:
      print("this is a casino: '%s'"%tF_split[1])
      potential = r"2. Implementation\14. Data\TP_config.json"
    else:
      print("this isn't valid and should be ignored.")

    full_tF = os.path.join(full_tF, potential)
    print(full_tF)
    if not os.path.exists(full_tF):
      print("TP_config file not found.  should make one?")
    else:
      print("TP_config file found.  does contain this file in assets?")

print("touched dirs: [\n%s\n]"%(',\n'.join(touchedDirs))) 
