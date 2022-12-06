from tkinter import *
import speedtest

root = Tk()
root.title("İnternet Hız Testi")
root.geometry("720x430")
root.resizable(False, False)
root.configure(bg = "#1a212d")

def test():
    hız_testi = speedtest.Speedtest()
    upload = round(hız_testi.upload() / (1024 * 1024), 2)
    upload_mpbs.config(text = upload)
    download = round(hız_testi.download() / (1024 * 1024), 2)
    download_mpbs.config(text = download)

icon_img = PhotoImage(file = "speedlogo.png")
root.iconphoto(False, icon_img)

sol_speed = PhotoImage(file = "speedmeter.png")
Label(root, text = "DOWNLOAD", font = ("arial", 15, "bold"), bg = "#1a212d").place(x = 120, y = 10)
Label(root, image = sol_speed, bg = "#1a212d").place(x = 0, y = 50)

sag_speed = PhotoImage(file = "speedmeter2.png")
Label(root, text = "UPLOAD", font = ("arial", 15, "bold"), bg = "#1a212d").place(x = 490, y = 10)
Label(root, image = sag_speed, bg = "#1a212d").place(x = 350, y = 50)

basla_button = PhotoImage(file = "button_basla.png")
buton = Button(root, image = basla_button, bg = "#1a212d", activebackground = "#1a212d", cursor = "hand2", command = test).place(x = 230, y = 365)

Label(root, text = "Download", font = "arial 15 bold", bg = "#141526", fg = "white").place(x = 130, y = 150)
Label(root, text = "Mbps", font = "arial 15 bold", bg = "#141526", fg = "white").place(x = 150, y = 270)

Label(root, text = "Upload", font = "arial 15 bold", bg = "#141526", fg = "white").place(x = 494, y = 150)
Label(root, text = "Mbps", font = "arial 15 bold", bg = "#141526", fg = "white").place(x = 500, y = 270)

download_mpbs = Label(root, text = "", font = "arial 40 bold", bg = "#141526")
download_mpbs.place(x = 120, y = 190)
upload_mpbs = Label(root, text = "", font = "arial 40 bold", bg = "#141526")
upload_mpbs.place(x = 484, y = 190)

root.mainloop()