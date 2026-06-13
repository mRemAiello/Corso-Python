#!/usr/bin/env python3
"""Desktop GUI for PDF anonymization."""

from __future__ import annotations

import threading
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk

from pdf_anonymizer import anonymize_pdf


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("PDF Anonymizer")
        self.geometry("760x360")
        self.minsize(700, 320)

        self.input_var = tk.StringVar()
        self.output_var = tk.StringVar()
        self.blur_enabled_var = tk.BooleanVar(value=True)
        self.blur_radius_var = tk.StringVar(value="18.0")
        self.status_var = tk.StringVar(value="Pronto")

        self._build_ui()

    def _build_ui(self) -> None:
        container = ttk.Frame(self, padding=16)
        container.pack(fill=tk.BOTH, expand=True)
        container.columnconfigure(1, weight=1)

        ttk.Label(container, text="PDF input").grid(row=0, column=0, sticky="w", pady=(0, 8))
        ttk.Entry(container, textvariable=self.input_var).grid(
            row=0, column=1, sticky="ew", padx=(8, 8), pady=(0, 8)
        )
        ttk.Button(container, text="Sfoglia", command=self._browse_input).grid(
            row=0, column=2, sticky="ew", pady=(0, 8)
        )

        ttk.Label(container, text="PDF output").grid(row=1, column=0, sticky="w", pady=(0, 8))
        ttk.Entry(container, textvariable=self.output_var).grid(
            row=1, column=1, sticky="ew", padx=(8, 8), pady=(0, 8)
        )
        ttk.Button(container, text="Salva come", command=self._browse_output).grid(
            row=1, column=2, sticky="ew", pady=(0, 8)
        )

        options = ttk.LabelFrame(container, text="Opzioni", padding=12)
        options.grid(row=2, column=0, columnspan=3, sticky="ew", pady=(8, 8))
        options.columnconfigure(1, weight=1)

        blur_check = ttk.Checkbutton(
            options,
            text="Blur immagini",
            variable=self.blur_enabled_var,
            command=self._toggle_blur_fields,
        )
        blur_check.grid(row=0, column=0, sticky="w")

        ttk.Label(options, text="Raggio blur").grid(row=0, column=1, sticky="e", padx=(20, 8))
        self.radius_entry = ttk.Entry(options, textvariable=self.blur_radius_var, width=10)
        self.radius_entry.grid(row=0, column=2, sticky="w")

        self.run_button = ttk.Button(container, text="Anonimizza PDF", command=self._run)
        self.run_button.grid(row=3, column=0, columnspan=3, sticky="ew", pady=(12, 8))

        status_frame = ttk.Frame(container)
        status_frame.grid(row=4, column=0, columnspan=3, sticky="ew", pady=(8, 0))
        status_frame.columnconfigure(0, weight=1)

        ttk.Label(status_frame, textvariable=self.status_var).grid(row=0, column=0, sticky="w")

    def _toggle_blur_fields(self) -> None:
        state = "normal" if self.blur_enabled_var.get() else "disabled"
        self.radius_entry.configure(state=state)

    def _browse_input(self) -> None:
        chosen = filedialog.askopenfilename(
            title="Seleziona PDF input",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")],
        )
        if not chosen:
            return

        self.input_var.set(chosen)
        if not self.output_var.get():
            input_path = Path(chosen)
            default_name = f"{input_path.stem}_anon.pdf"
            self.output_var.set(str(input_path.with_name(default_name)))

    def _browse_output(self) -> None:
        chosen = filedialog.asksaveasfilename(
            title="Seleziona PDF output",
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")],
        )
        if chosen:
            self.output_var.set(chosen)

    def _validate(self) -> tuple[bool, float]:
        input_path = self.input_var.get().strip()
        output_path = self.output_var.get().strip()

        if not input_path:
            messagebox.showerror("Errore", "Seleziona un PDF di input.")
            return False, 0.0
        if not Path(input_path).exists():
            messagebox.showerror("Errore", "Il file di input non esiste.")
            return False, 0.0
        if not output_path:
            messagebox.showerror("Errore", "Specifica un percorso di output.")
            return False, 0.0

        blur_radius = 18.0
        if self.blur_enabled_var.get():
            try:
                blur_radius = float(self.blur_radius_var.get().strip())
            except ValueError:
                messagebox.showerror("Errore", "Raggio blur non valido.")
                return False, 0.0

            if blur_radius < 0.0:
                messagebox.showerror("Errore", "Il raggio blur deve essere >= 0.")
                return False, 0.0

        return True, blur_radius

    def _set_running(self, running: bool) -> None:
        state = "disabled" if running else "normal"
        self.run_button.configure(state=state)

    def _run(self) -> None:
        valid, blur_radius = self._validate()
        if not valid:
            return

        input_path = self.input_var.get().strip()
        output_path = self.output_var.get().strip()
        blur_images = self.blur_enabled_var.get()

        self._set_running(True)
        self.status_var.set("Elaborazione in corso...")

        def worker() -> None:
            try:
                anonymize_pdf(
                    input_path,
                    output_path,
                    blur_radius=blur_radius,
                    blur_images=blur_images,
                )
            except Exception as exc:
                self.after(0, lambda: self._on_error(str(exc)))
                return

            self.after(0, lambda: self._on_success(output_path))

        threading.Thread(target=worker, daemon=True).start()

    def _on_success(self, output_path: str) -> None:
        self._set_running(False)
        self.status_var.set("Completato")
        messagebox.showinfo("Completato", f"PDF anonimizzato salvato in:\n{output_path}")

    def _on_error(self, error_text: str) -> None:
        self._set_running(False)
        self.status_var.set("Errore")
        messagebox.showerror("Errore durante l'elaborazione", error_text)


def main() -> None:
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
