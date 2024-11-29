import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class DaftarAkunGameOnline:
    def __init__(self, root):
        self.root = root
        self.root.title("Daftar Akun Game Online")
        self.root.geometry("700x600")
        
        self.akun_list = []
        
        frame_input = tk.Frame(self.root)
        frame_input.pack(pady=10)

        tk.Label(frame_input, text="Username").grid(row=0, column=0, padx=5, pady=5)
        self.entry_username = tk.Entry(frame_input)
        self.entry_username.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_input, text="Nama Game").grid(row=1, column=0, padx=5, pady=5)
        self.entry_game = tk.Entry(frame_input)
        self.entry_game.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_input, text="Level").grid(row=2, column=0, padx=5, pady=5)
        self.entry_level = tk.Entry(frame_input)
        self.entry_level.grid(row=2, column=1, padx=5, pady=5)

        btn_tambah = tk.Button(frame_input, text="Tambah Akun", command=self.tambah_akun)
        btn_tambah.grid(row=3, column=0, columnspan=2, pady=10)

        frame_tree = tk.Frame(self.root)
        frame_tree.pack(pady=10)

        columns = ("No", "Username", "Game", "Level")
        self.tree = ttk.Treeview(frame_tree, columns=columns, show="headings")
        self.tree.heading("No", text="No")
        self.tree.heading("Username", text="Username")
        self.tree.heading("Game", text="Game")
        self.tree.heading("Level", text="Level")
        self.tree.column("No", width=50, anchor="center")
        self.tree.column("Level", width=80, anchor="center")
        self.tree.pack()

        btn_simpan = tk.Button(self.root, text="Simpan ke File", command=self.simpan_ke_file)
        btn_simpan.pack(pady=5)

        btn_hapus = tk.Button(self.root, text="Hapus Akun", command=self.hapus_akun)
        btn_hapus.pack(pady=5)

    def tambah_akun(self):
        username = self.entry_username.get()
        game = self.entry_game.get()
        level = self.entry_level.get()

        if username and game and level:
            try:
                level = int(level)
                self.akun_list.append({'username': username, 'game': game, 'level': level})
                self.update_treeview()
                self.entry_username.delete(0, tk.END)
                self.entry_game.delete(0, tk.END)
                self.entry_level.delete(0, tk.END)
                messagebox.showinfo("Sukses", "Akun berhasil ditambahkan!")
            except ValueError:
                messagebox.showerror("Error", "Level harus berupa angka.")
        else:
            messagebox.showwarning("Peringatan", "Semua kolom harus diisi!")

    def update_treeview(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for idx, akun in enumerate(self.akun_list):
            self.tree.insert("", "end", values=(idx + 1, akun['username'], akun['game'], akun['level']))

    def simpan_ke_file(self):
        try:
            with open("daftar_akun_game.txt", "w") as file:
                for akun in self.akun_list:
                    file.write(f"{akun['username']} - {akun['game']} - Level {akun['level']}\n")
            messagebox.showinfo("Sukses", "Data berhasil disimpan ke file!")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menyimpan file: {e}")

    def hapus_akun(self):
        selected_item = self.tree.selection()
        if selected_item:
            confirm = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus akun yang dipilih?")
            if confirm:
                for item in selected_item:
                    item_index = self.tree.index(item)
                    self.akun_list.pop(item_index)
                    self.tree.delete(item)
                self.update_treeview()
                messagebox.showinfo("Sukses", "Akun berhasil dihapus!")
        else:
            messagebox.showwarning("Peringatan", "Pilih akun yang ingin dihapus!")

if __name__ == "__main__":
    root = tk.Tk()
    app = DaftarAkunGameOnline(root)
    root.mainloop()
