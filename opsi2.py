import tkinter as tk
from tkinter import messagebox

class KasirApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Aplikasi Kasir")
        self.geometry("400x300")

        self.total_harga = 0
        self.items = []

        self.label_total_harga = tk.Label(self, text="Total Harga: Rp. 0")
        self.label_total_harga.pack()

        self.label_item = tk.Label(self, text="Item:")
        self.label_item.pack()

        self.entry_item = tk.Entry(self)
        self.entry_item.pack()

        self.label_harga = tk.Label(self, text="Harga:")
        self.label_harga.pack()

        self.entry_harga = tk.Entry(self)
        self.entry_harga.pack()

        self.button_tambah = tk.Button(self, text="Tambah", command=self.tambah_item)
        self.button_tambah.pack()

        self.button_selesai = tk.Button(self, text="Selesai", command=self.selesai)
        self.button_selesai.pack()

    def tambah_item(self):
        item = self.entry_item.get()
        harga = self.entry_harga.get()

        if item and harga:
            self.items.append((item, harga))
            self.total_harga += int(harga)

            self.label_total_harga["text"] = "Total Harga: Rp. {}".format(self.total_harga)

            self.entry_item.delete(0, tk.END)
            self.entry_harga.delete(0, tk.END)
        else:
            messagebox.showwarning("Peringatan", "Silakan masukkan item dan harga!")

    def selesai(self):
        if self.items:
            messagebox.showinfo("Selesai", "Total Harga: Rp. {}\nTerima kasih!".format(self.total_harga))
            self.total_harga = 0
            self.items = []
            self.label_total_harga["text"] = "Total Harga: Rp. 0"
        else:
            messagebox.showwarning("Peringatan", "Tidak ada item yang ditambahkan!")

if __name__ == "__main__":
    app = KasirApp()
    app.mainloop()
