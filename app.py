import customtkinter as ctk
import threading
import main  # This refers to your main.py file


class AssistantUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        # 1. Fullscreen & Theme Setup
        self.title("AI Core System")
        self.attributes('-fullscreen', True)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Bind the Escape key to close the app
        self.bind("<Escape>", self.close_app)

        # 2. Main Layout Grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=3)
        self.grid_rowconfigure(4, weight=0)
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # 3. UI Elements
        self.header = ctk.CTkLabel(self, text="YOUR AI ASSISTANT",
                                   font=("Segoe UI", 45, "bold"), text_color="#00e6e6")
        self.header.grid(row=1, column=0, pady=(20, 5))

        self.status_label = ctk.CTkLabel(self, text="SYSTEM OFFLINE",
                                         text_color="gray", font=("Segoe UI", 20, "bold"))
        self.status_label.grid(row=2, column=0, pady=10)

        self.display_box = ctk.CTkTextbox(self, width=900, height=450,
                                          font=("Segoe UI", 24),
                                          fg_color="#1c1c1e", text_color="white",
                                          corner_radius=20, wrap="word", spacing3=10)
        self.display_box.grid(row=3, column=0, pady=30, padx=40)
        self.display_box.insert("0.0", "Waiting for initialization...")

        self.start_btn = ctk.CTkButton(self, text="INITIALIZE SYSTEM",
                                       font=("Segoe UI", 18, "bold"),
                                       fg_color="#006666", hover_color="#00e6e6",
                                       text_color="white", height=55, width=250,
                                       corner_radius=30,
                                       command=self.start_thread)
        self.start_btn.grid(row=4, column=0, pady=20)

        # FIXED LINE: Removed side="bottom"
        self.quit_hint = ctk.CTkLabel(self, text="Press 'ESC' to close system",
                                      font=("Segoe UI", 12), text_color="#555555")
        self.quit_hint.grid(row=5, column=0, pady=20)

    def update_status(self, text, color="#00e6e6"):
        if text.lower() == "idle":
            color = "gray"
        self.status_label.configure(text=text.upper(), text_color=color)

    def show_info(self, text):
        self.display_box.delete("0.0", "end")
        self.display_box.insert("0.0", f"\n{text}")

    def start_thread(self):
        self.start_btn.configure(state="disabled", text="SYSTEM ACTIVE", fg_color="#333333")
        threading.Thread(target=main.run_assistant, args=(self,), daemon=True).start()

    def close_app(self, event=None):
        self.destroy()


if __name__ == "__main__":
    app = AssistantUI()
    app.mainloop()