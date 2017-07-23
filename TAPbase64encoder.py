#! python3
# """
# TAP media base64 encoder version 1.3.1
# Being Improved
# 23 July 2017
#   fix lang... error
#   use "from sys import exit" instead of "import sys"
# 22 July 2017
#   handle error: IOError, urllib.error.URLError, urllib.error.HTTPError, ValueError
#
#   still have error in "get file name":
#     need to continue to type in file name after find that the past file entered not valid
#
#      have error when select language, not type in anything, just "Enter"
#         Traceback (most recent call last):
#       File "TAPbase64encoder.py", line 250, in <module>
#         main()
#       File "TAPbase64encoder.py", line 178, in main
#         print ("\n",lang[4],lang[5],lang[6],lang[7],lang[8],)
#     NameError: name 'lang' is not defined
#
# 21 July 2017
#   add Vietnamese
#   add Continue() function
# 20 July 2017
#   improve user prompts
# 17 July 2017
#   fix error
#   run perfectly
# 16 July 2017
#   use functions
#   add encode video function
#   error:
#       Traceback (most recent call last):
#     File "TAPimageBase64encoder_1.2.py", line 71, in <module>
#       EncodeBase64(fileName, fileType, mediaType)
#     File "TAPimageBase64encoder_1.2.py", line 39, in EncodeBase64
#       file = open(fileName, 'rb')
# TypeError: expected str, bytes or os.PathLike object, not NoneType
# 15 July 2017
#   use with any image file type
#   output to .txt file and clipboard
# Preference:
# https://code.tutsplus.com/tutorials/base64-encoding-and-decoding-using-python--cms-25588
# """
from sys import exit
import os, base64, pyperclip, urllib.request
en = [
    "Url?\n",
    "File Name or File Path?\n",
    "File Type?\n",
    "What would you like to do? ",
    "\t1. Encode Local Image\n",
    "\t2. Encode Online Image\n",
    "\t3. Encode Local Video\n",
    "\t4. Encode Online Video\n",
    "\t5. Exit\n",
    "\nNot Valid Choice!",
    "\n\tTry again!",
    "Do you want to delete downloaded files? [y/n]\t",
    "\n\tFiles deleted!",
    "\n\tFiles NOT deleted!",
    "\n\tTask Completed!",
    "\n\tThank you!\n\tGoodbye! - TAP Team",
    "Do you want to encode other file? [y/n]",
    "\n\tNo such file or directory!",
    "File Name or File Path to save this file?\n",
    """\n\tNo connection could be made because the target machine actively refused it\n\tor There is not such file""",
    "\n\tUnknown URL type",
    "\n\tYou must type a number between 1 and 5!",
    ]
vi = [
    "Link download file?\n",#0
    "Ten hoac dia chi file?\n",#1
    "Dinh dang cua file?\n",#2
    "Ban muon lam gi? ",#3
    "\t1. Ma hoa file hinh tren may\n",#4
    "\t2. Ma hoa file hinh online\n",#5
    "\t3. Ma hoa file video tren may\n",#6
    "\t4. Ma hoa file video online\n",#7
    "\t5. Thoat\n",#8
    "\n\tLua chon sai!",#9
    "\n\tHay nhap lai!",#10
    "Ban co muon xoa cac file vua tai khong? [y/n]\t",#11
    "\n\tDa XOA!",#12
    "\n\tCac file chua xoa!",#13
    "\n\tCong viec hoan tat!",#14
    "\n\tCam on ban da dung phan mem nay\n\tTam biet - TAP Team",#15
    "Ban co muon ma hoa file nao nua khong? [y/n]",#16
    "\n\tKhong co file hay dia chi nhu vay",#17
    "Ten hoac dia chi file ban muon luu vao?\n",#18
    "\n\tKhong the tai vi trang web khong cho phep\n\tHoac khong ton tai file nay",#19
    "\n\tDinh dang URL khong chinh xac",#20
    "\n\tHay nhap lua chon la cac so tu 1 toi 5!",#21
    ]
def GetUrl():
  _url = input(lang[0])
  return _url

def GetFileName(_fileNameprompt):
  _fileName = input(_fileNameprompt)
  return _fileName

def GetFileType():
  _fileType = input(lang[2])
  return _fileType

def DownloadFile(_url, _fileName):
  with urllib.request.urlopen(_url) as response, open(_fileName, 'wb') as out_file:
      data = response.read() # a `bytes` object
      out_file.write(data)

def DeleteFile():
  prompt = input(lang[11])
  if prompt.upper() == "Y" or prompt.upper() == "YES":
    os.remove(fileName)
    os.remove("Base64output.txt")
    print(lang[12])
  elif prompt.upper() == "N" or prompt.upper() == "NO":
    print(lang[13])
  else :
    print(lang[9])

def Completed():
  print(lang[14])

def EncodeBase64(_fileName, _fileType, _mediaType):
  # read input file
  file = open(_fileName, 'rb') #open binary file in read mode
  file_read = file.read()
  # encode file
  file_64_encode = base64.encodestring(file_read)
  file_64_encode_string = file_64_encode.decode(encoding='UTF-8')
  # get full format text
  full_string = "data:"
  full_string += _mediaType
  full_string += "/"
  full_string += _fileType
  full_string += ";base64,"
  full_string += file_64_encode_string
  # copy text to clipboard
  pyperclip.copy(full_string)
  # write text to .txt file
  with open("Base64output.txt", "w") as txt_file:
    txt_file.write(full_string)

def Continue():
  cont = True
  while cont:
      cont = input(lang[16])
      if cont == "y" or cont == "Y" or cont == "yes" or cont == "Yes":
        main()
      elif cont == "n" or cont == "N" or cont == "no" or cont == "No":
        print(lang[15])
        exit()
      else :
        print(lang[9])

def language():
  global lang
  langChoice = True
  while langChoice:
      print ("""\tChon ngon ngu cua ban
      \tChose Your Language\n
      \t1. Tieng Viet
      \t2. English
      """)
      langChoice = input("\t")
      if langChoice == "1" or langChoice.upper() == "VI" or langChoice.upper() == "V" or langChoice.upper() == "TIENG VIET":
        lang = vi
        langChoice = False
      elif langChoice == "2" or langChoice.upper() == "EN" or langChoice.upper() == "E" or langChoice.upper() == "ENGLISH":
        lang = en
        langChoice = False
      else:
        langChoice = True
        print("\tLua chon sai! Hay nhap lai\n\tNot Valid Choice! Try again\n")

def main():
  global fileName
  ans = 0
  while ans not in range(1,6): # ans >=1 ; ans <=5
      print ("\n",lang[4],lang[5],lang[6],lang[7],lang[8],)
      try:
        ans = int(input(lang[3]))
      except ValueError:
         print(lang[21])
      else:
        if ans == 1:
          print(lang[4])
          fileName = GetFileName(lang[1])
          fileType = GetFileType()
          mediaType = "image"
          try:
            EncodeBase64(fileName, fileType, mediaType)
          except IOError:
            print(lang[17],"\n",lang[10])
            ans = 0
          else:
            Completed()
            Continue()

        elif ans == 2:
          print(lang[5])
          url = GetUrl()
          fileName = GetFileName(lang[18])
          fileType = GetFileType()
          mediaType = "image"
          try:
            DownloadFile(url, fileName)
          except (urllib.error.URLError, urllib.error.HTTPError):
            print(lang[19], lang[10])
            ans = 0
          except ValueError:
            print(lang[20], lang[10])
            ans = 0
          else:
            EncodeBase64(fileName, fileType, mediaType)
            DeleteFile()
            Completed()
            Continue()
        elif ans == 3:
          print(lang[6])
          fileName = GetFileName(lang[1])
          fileType = GetFileType()
          mediaType = "video"
          try:
            EncodeBase64(fileName, fileType, mediaType)
          except IOError:
            print(lang[17],"\n",lang[10])
            ans = 0
          else:
            Completed()
            Continue()
        elif ans == 4:
          print(lang[7])
          url = GetUrl()
          fileName = GetFileName(lang[18])
          fileType = GetFileType()
          mediaType = "video"
          try:
            DownloadFile(url, fileName)
          except (urllib.error.URLError, urllib.error.HTTPError):
            print(lang[19], lang[10])
            ans = 0
          except ValueError:
            print(lang[20], lang[10])
            ans = 0
          else:
            EncodeBase64(fileName, fileType, mediaType)
            DeleteFile()
            Completed()
            Continue()
        elif ans == 5:
          print(lang[8], lang[15])
          exit()
        else:
          print(lang[9])

print("""
\t<|----------------------------------|>
\t<|             TAPtele.com          |>
\t<| TAP Base64 Encoder version 1.3.1 |>
\t<|----------------------------------|>
""")
language()
main()