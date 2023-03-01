#coding utf-8
########################################
# きんたまさくらちゃんトゥートBot          #
# 開発：@wakanameko2                　　#
# SPThanks：くすお#xxxx様               #
# 元ネタ：@kintamasakura              　#
########################################
import os
import platform
import PIL
import webbrowser
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from mastodon import Mastodon

AppName = 'きんたまさくらちゃんトゥートBot'
Version = '1.1'
Develop = '@wakanameko2'
Original = 'たまさくらちゃんの金玉 きんたまさくらちゃん(@kintamasakura)'

ur = platform.uname()
print(ur.system)
print(ur.release)
print(ur.version)
print(ur.processor)
print(AppName)
print(Develop)
print(Original)

if ur.system == 'Darwin':os.system('python3 -m pip install Mastodon.py')
if ur.system == 'nt':os.system('pip install Mastodon.py')

#MainWindow
MainWindow = tk.Tk()
MainWindow.geometry('300x450')
MainWindow.resizable(width = False, height = False)
MainWindow.title(f"{AppName} | {Version}")
Menubaa = tk.Menu(MainWindow) 
MainWindow.config(menu=Menubaa)
MainWindow.iconphoto(False, tk.PhotoImage(file="きんたまさくらちゃん.png"))

class Application(tk.Frame):
    def drawLabelPngImg(self):
        global pngImg
        pngImg = tk.PhotoImage(file="きんたまさくらちゃん.png")
        label = tk.Label(dlg_modeless, width=100,height=100,image=pngImg)
        label.pack()

img = ImageTk.PhotoImage(Image.open("きんたまさくらちゃんsmall.png"))

### Load UserData.txt ###
if(os.path.isfile('UserData.txt')):
    UserInfo = open("UserData.txt", "r")
    UserData = UserInfo.read()
    print(UserData)
    #Get Instance
    startI = 'Instance:'
    endI = '\nMailAdress:'
    sI = str(UserData)
    InsData = sI[sI.find(startI)+len(startI):sI.rfind(endI)]
    print(InsData)
    #Get MailAdress
    startM = 'MailAdress:'
    endM = '\nPassWord:'
    sM = str(UserData)
    MailData = sM[sM.find(startM)+len(startM):sM.rfind(endM)]
    print(MailData)
    #Get PassWord
    startP = 'PassWord:'
    endP = '\n'
    sP = str(UserData)
    PassData = sP[sP.find(startP)+len(startP):sP.rfind(endP)]
    print(PassData)
else:
    print('ログイン情報が保存されていません!')
    res = messagebox.showinfo("注意", "ログイン情報が保存されていません!")
### Load UserData.txt ###

#Events
def exitTAMA():
    exit()

def DelInfo():
    if(os.path.isfile('UserData.txt')):
        MSB_DelInfo = tk.messagebox.askquestion('ログイン情報の削除','ログイン情報を削除してもよろしいですか？', icon='warning')
            if MSB_DelInfo == 'yes':
                os.remove('UserData.txt')

def DelAPIKey():
    if(os.path.isfile('API_Keyんたまさくらちゃん.txt')):
        MSB_DelAPI = tk.messagebox.askquestion('APIキーの削除','APIキーを削除してもよろしいですか？', icon='warning')
            if MSB_DelAPI == 'yes':
                os.remove('API_Keyんたまさくらちゃん.txt')

def Delauth():
    if(os.path.isfile('auth.txt')):
        MSB_Delauth = tk.messagebox.askquestion('アクセスキーの削除','アクセスキーを削除してもよろしいですか？', icon='warning')
            if MSB_Delauth == 'yes':
                os.remove('auth.txt')

def SaveInfo():
    txt_ins_get = (txt_ins.get())
    txt_CKey_get = (txt_CKey.get())
    txt_CS_get = (txt_CS.get())
    SIF = open('UserData.txt', 'w', encoding='UTF-8')
    SIF.write(f"Instance:{txt_ins_get}\nMailAdress:{txt_CKey_get}\nPassWord:{txt_CS_get}\n")
    SIF.close()

def Login():
    AppNAME = "きんたまさくらちゃんBot"
    txt_ins_get = (txt_ins.get())
    name = 'きんたまさくらちゃんトゥートBot'
    if not (os.path.isfile('API_Keyんたまさくらちゃん.txt')):
        Mastodon.create_app(name,
        api_base_url = InsData,
        to_file = "API_Keyんたまさくらちゃん.txt"
        )
        print('api_key作成完了')
    else:
        pass
    mastodon = Mastodon(
    client_id="API_Keyんたまさくらちゃん.txt", 
    access_token="auth.txt",
    api_base_url = InsData)
    if not (os.path.isfile('auth.txt')):
        mastodon.log_in(MailData, PassData, to_file = "auth.txt")

def TNow():
    if verK == True:
        
def TNowNK():
    txt_ins_get = (txt_ins.get())
    txt_CKey_get = (txt_CKey.get())
    txt_CS_get = (txt_CS.get())
    if not (os.path.isfile('API_Keyんたまさくらちゃん.txt')):
        Mastodon.create_app('きんたまさくらちゃんトゥートBot',
        api_base_url = InsData,
        to_file = "API_Keyんたまさくらちゃん.txt"
        )
        print('api_key作成完了')
    else:
        pass
    mastodon = Mastodon(
        client_id="API_Keyんたまさくらちゃん.txt", 
        access_token="auth.txt",
        api_base_url = InsData)
    if not (os.path.isfile('auth.txt')):
        mastodon.log_in(MailData, PassData, to_file = "auth.txt")
    mastodon.toot("たまさくらちゃんの金玉　きんたまさくらちゃん")

def TNowK():
    txt_ins_get = (txt_ins.get())
    txt_CKey_get = (txt_CKey.get())
    txt_CS_get = (txt_CS.get())
    if not (os.path.isfile('API_Keyんたまさくらちゃん.txt')):
        Mastodon.create_app('きんたまさくらちゃんトゥートBot',
        api_base_url = InsData,
        to_file = "API_Keyんたまさくらちゃん.txt"
        )
        print('api_key作成完了')
    else:
        pass
    mastodon = Mastodon(
        client_id="API_Keyんたまさくらちゃん.txt", 
        access_token="auth.txt",
        api_base_url = InsData)
    if not (os.path.isfile('auth.txt')):
        mastodon.log_in(MailData, PassData, to_file = "auth.txt")
    mastodon.toot("たまさくらちゃんの金玉、きんたまさくらちゃん")


#Widgeds
Label_wlcm = tk.Label(MainWindow, text = f"{AppName}", font = ("normal", 18, "bold"))
Label_icon = tk.Label(MainWindow, image = img)
Label_Login = tk.Label(MainWindow, text = "ログイン:", font = ("normal", 14, "bold"))
Label_Mail = tk.Label(MainWindow, text = "メールアドレス")
Label_Pass = tk.Label(MainWindow, text = "パスワード")
Label_ins = tk.Label(MainWindow, text = "インスタンス(mstdn.jp等)")
Label_emp = tk.Label(MainWindow, text = " ")
txt_ins = tk.Entry(width=20)
if(os.path.isfile('UserData.txt')):
    txt_ins.insert(tk.END, InsData)
txt_CKey = tk.Entry(width=20)
if(os.path.isfile('UserData.txt')):
    txt_CKey.insert(tk.END, MailData)
txt_CS = tk.Entry(show='*', width=20)
if(os.path.isfile('UserData.txt')):
    txt_CS.insert(tk.END, PassData)
button_Login = tk.Button(MainWindow, text = "ログイン", command = Login, width = 9)
button_SaveInfo = tk.Button(MainWindow, text = "情報を保存", command = SaveInfo, width = 9)
Label_Toot = tk.Label(MainWindow, text = "トゥート:", font = ("normal", 14, "bold"))
chk_K = tkinter.Checkbutton(text='句読点を付ける', variable = varK)
button_TNowNK = tk.Button(MainWindow, text = "トゥート", command = TNow, width = 9)

#MenuBar
menu_file = tk.Menu(MainWindow)
Menubaa.add_cascade(label = f"{AppName}{Version}", menu = menu_file)
menu_file.add_command(label = 'ログイン', command = Login)
menu_file.add_command(label = 'ログイン情報を保存', command = SaveInfo)
menu_file.add_command(label = 'ログイン情報を削除', command = DelInfo)
menu_file.add_separator()
menu_file.add_command(label = 'APIキーを削除', command = DelAPIKey)
menu_file.add_command(label = 'アクセスキーを削除', command = Delauth)
menu_file.add_separator()
menu_file.add_command(label = '閉じる', command = exitTAMA)

menu_Toot = tk.Menu(MainWindow)
Menubaa.add_cascade(label = "トゥート", menu = menu_Toot)
menu_Toot.add_command(label = 'トゥート', command = TNowNK)
menu_file.add_command(label = 'トゥート(句読点あり)', command=TNowK)

#Layouts
Label_wlcm.pack()
Label_icon.pack(anchor = tk.W, padx = 15)
Label_Login.pack(anchor = tk.W, padx = 15, pady = 0)
Label_ins.pack(anchor = tk.W, padx = 15, pady = 0)
txt_ins.pack(anchor = tk.E, padx = 15, pady = 0)
Label_Mail.pack(anchor = tk.W, padx = 15, pady = 0)
txt_CKey.pack(anchor = tk.E, padx = 15, pady = 0)
Label_Pass.pack(anchor = tk.W, padx = 15, pady = 0)
txt_CS.pack(anchor = tk.E, padx = 15, pady = 0)
button_Login.pack(anchor = tk.W, padx = 15, pady = 0)
button_SaveInfo.pack(anchor = tk.W, padx = 15, pady = 0)
Label_emp.pack(anchor = tk.W, padx = 15, pady = 0)
Label_Toot.pack(anchor = tk.W, padx = 15, pady = 0)
chk_K.pack(anchor = tk.W, padx = 15, pady = 0)
button_TNow.pack(anchor = tk.W, padx = 15, pady = 0)

MainWindow.mainloop()
