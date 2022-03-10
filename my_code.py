import sys
import requests

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
    
    print("\n\n'%s' modified files [\n%s\n]" %(author, ',\n'.join(touchedFiles)))
    
  else:
    print("url: '%s' error in request." %url)
else:
  print("sha not included.")


