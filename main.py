import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from ciphers import vigenere_encrypt, vigenere_decrypt, playfair_encrypt, playfair_decrypt, hill_encrypt, hill_decrypt

class CipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("APLIKASI CIPHER BY MUHAMMAD THORIKIN ZUNIARTO")
        self.root.geometry("600x750")
        self.root.configure(bg="#2C3E50")
        self.create_widgets()

    def create_widgets(self):
        # Title Frame
        title_frame = tk.Frame(self.root, bg="#34495E", pady=10)
        title_frame.pack(fill="x")

        self.title_label = tk.Label(title_frame, text="Cipher ENCRYPTION & DECRYPTION", font=("Helvetica", 20, "bold"), bg="#34495E", fg="#ECF0F1")
        self.title_label.pack()

        # Cipher Selection Frame
        cipher_frame = tk.Frame(self.root, bg="#2C3E50", pady=10)
        cipher_frame.pack(fill="x", padx=20)

        self.cipher_label = tk.Label(cipher_frame, text="Select Cipher:", font=("Helvetica", 14), bg="#2C3E50", fg="#ECF0F1")
        self.cipher_label.grid(row=0, column=0, sticky="w", padx=10)

        self.cipher_type = tk.StringVar(value="vigenere")
        self.vigenere_radio = ttk.Radiobutton(cipher_frame, text="Vigenère Cipher", variable=self.cipher_type, value="vigenere")
        self.playfair_radio = ttk.Radiobutton(cipher_frame, text="Playfair Cipher", variable=self.cipher_type, value="playfair")
        self.hill_radio = ttk.Radiobutton(cipher_frame, text="Hill Cipher", variable=self.cipher_type, value="hill")

        self.vigenere_radio.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.playfair_radio.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        self.hill_radio.grid(row=1, column=2, padx=10, pady=5, sticky="w")

        # Key Entry Frame
        key_frame = tk.Frame(self.root, bg="#2C3E50", pady=10)
        key_frame.pack(fill="x", padx=20)

        self.key_label = tk.Label(key_frame, text="MASUKKAN KUNCI (min 12 KARAKTER):", font=("Helvetica", 14), bg="#2C3E50", fg="#ECF0F1")
        self.key_label.grid(row=0, column=0, sticky="w", padx=10)

        self.key_entry = ttk.Entry(key_frame, width=40, font=("Helvetica", 12))
        self.key_entry.grid(row=1, column=0, padx=10, pady=5)

        # Input Method Frame
        input_frame = tk.Frame(self.root, bg="#2C3E50", pady=10)
        input_frame.pack(fill="x", padx=20)

        self.input_type_label = tk.Label(input_frame, text="PILIH METODE INPUT:", font=("Helvetica", 14), bg="#2C3E50", fg="#ECF0F1")
        self.input_type_label.grid(row=0, column=0, sticky="w", padx=10)

        self.input_type = tk.StringVar(value="keyboard")
        self.keyboard_radio = ttk.Radiobutton(input_frame, text="KETIK LANGSUNG", variable=self.input_type, value="keyboard")
        self.file_radio = ttk.Radiobutton(input_frame, text="UPLOAD FILE", variable=self.input_type, value="file")

        self.keyboard_radio.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.file_radio.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Text Input Frame
        text_frame = tk.Frame(self.root, bg="#2C3E50", pady=10)
        text_frame.pack(fill="x", padx=20)

        self.text_label = tk.Label(text_frame, text="MASUKKAN TEKS JIKA PILIH KETIK LANGSUNG:", font=("Helvetica", 14), bg="#2C3E50", fg="#ECF0F1")
        self.text_label.grid(row=0, column=0, sticky="w", padx=10)

        self.text_entry = tk.Text(text_frame, height=5, width=55, font=("Helvetica", 12))
        self.text_entry.grid(row=1, column=0, padx=10, pady=5)

        # Encrypt/Decrypt Frame
        action_frame = tk.Frame(self.root, bg="#2C3E50", pady=20)
        action_frame.pack(fill="x", padx=20)

        self.encrypt_button = ttk.Button(action_frame, text="Encrypt", command=self.encrypt, width=20)
        self.decrypt_button = ttk.Button(action_frame, text="Decrypt", command=self.decrypt, width=20)

        self.encrypt_button.grid(row=0, column=0, padx=10, pady=10)
        self.decrypt_button.grid(row=0, column=1, padx=10, pady=10)

        # Output Frame
        output_frame = tk.Frame(self.root, bg="#2C3E50", pady=10)
        output_frame.pack(fill="x", padx=20)

        self.output_label = tk.Label(output_frame, text="Output:", font=("Helvetica", 14), bg="#2C3E50", fg="#ECF0F1")
        self.output_label.grid(row=0, column=0, sticky="w", padx=10)

        self.output_text = tk.Text(output_frame, height=5, width=55, font=("Helvetica", 12))
        self.output_text.grid(row=1, column=0, padx=10, pady=5)

        # Footer Frame for Creator's Name
        footer_frame = tk.Frame(self.root, bg="#2C3E50", pady=10)
        footer_frame.pack(fill="x")

        self.creator_label = tk.Label(footer_frame, text="Dibuat oleh: Muhammad Thorikin Zuniarto", font=("Helvetica", 12, "italic"), bg="#2C3E50", fg="#ECF0F1")
        self.creator_label.pack()

    def encrypt(self):
        key = self.key_entry.get()
        if len(key) < 12:
            messagebox.showerror("Error", "Key must be at least 12 characters long!")
            return

        text = self.get_input_text()
        if not text:
            return

        cipher_type = self.cipher_type.get()
        if cipher_type == "vigenere":
            result = vigenere_encrypt(text, key)
        elif cipher_type == "playfair":
            result = playfair_encrypt(text, key)
        else:
            result = hill_encrypt(text, key)

        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, result)

    def decrypt(self):
        key = self.key_entry.get()
        if len(key) < 12:
            messagebox.showerror("Error", "Key must be at least 12 characters long!")
            return

        text = self.get_input_text()
        if not text:
            return

        cipher_type = self.cipher_type.get()
        if cipher_type == "vigenere":
            result = vigenere_decrypt(text, key)
        elif cipher_type == "playfair":
            result = playfair_decrypt(text, key)
        else:
            result = hill_decrypt(text, key)

        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, result)

    def get_input_text(self):
        if self.input_type.get() == "keyboard":
            return self.text_entry.get("1.0", tk.END).strip()
        else:
            file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
            if not file_path:
                messagebox.showerror("Error", "No file selected!")
                return None
            with open(file_path, "r") as file:
                return file.read().strip()

if __name__ == "__main__":
    root = tk.Tk()
    app = CipherApp(root)
    root.mainloop()
