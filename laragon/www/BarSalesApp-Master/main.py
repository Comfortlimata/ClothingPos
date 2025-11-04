from tkinter import messagebox


def create_cashier_interface(main_frame, root, view_sales_modern_func=None):
    # Add these lines to ensure the functions are available in the local scope
    def show_quantity_dialog(item_name, unit_price):
        """Show dialog to select quantity and add to cart"""
        dialog = tk.Toplevel(root)
        dialog.title(f"Add {item_name}")
        dialog.geometry("300x250")
        dialog.configure(bg='#ffffff')
        dialog.transient(root)
        dialog.grab_set()

        # Center the dialog
        dialog.geometry("+%d+%d" % (root.winfo_rootx() + 100, root.winfo_rooty() + 100))

        # Item info
        tk.Label(dialog, text=item_name, font=('Arial', 14, 'bold'), 
                bg='#ffffff', fg='#2c3e50').pack(pady=(15, 10))

        tk.Label(dialog, text=f"ZMW {unit_price:.2f}", font=('Arial', 12),
                bg='#ffffff', fg='#27ae60').pack(pady=(0, 15))

        # Quantity frame
        qty_frame = tk.Frame(dialog, bg='#ffffff')
        qty_frame.pack(pady=10)

        qty_var = tk.StringVar(value="1")

        def validate_qty(P):
            """Validate quantity - only allow positive integers"""
            if P == "":
                return True
            try:
                val = int(P)
                return val > 0
            except ValueError:
                return False

        vcmd = (dialog.register(validate_qty), '%P')

        # Decrease quantity button
        dec_btn = tk.Button(qty_frame, text="-", font=('Arial', 16, 'bold'), 
                          bg='#e74c3c', fg='white', width=2, command=lambda: update_qty(-1))
        dec_btn.pack(side='left', padx=(0, 5))

        # Quantity entry
        qty_entry = tk.Entry(qty_frame, textvariable=qty_var, font=('Arial', 14), 
                           width=4, justify='center', validate='key', validatecommand=vcmd)
        qty_entry.pack(side='left')

        # Increase quantity button
        inc_btn = tk.Button(qty_frame, text="+", font=('Arial', 16, 'bold'), 
                          bg='#27ae60', fg='white', width=2, command=lambda: update_qty(1))
        inc_btn.pack(side='left', padx=(5, 0))

        def update_qty(delta):
            """Update quantity by delta"""
            try:
                current = int(qty_var.get() or "1")
                new_val = current + delta
                if new_val > 0:
                    qty_var.set(str(new_val))
            except ValueError:
                qty_var.set("1")

        # Notes field
        tk.Label(dialog, text="Notes (optional):", bg='#ffffff', anchor='w').pack(anchor='w', padx=20)
        notes_entry = tk.Entry(dialog, font=('Arial', 11), width=30)
        notes_entry.pack(padx=20, pady=(0, 10), fill='x')

        # Buttons
        btn_frame = tk.Frame(dialog, bg='#ffffff')
        btn_frame.pack(pady=15)

        cancel_btn = tk.Button(btn_frame, text="Cancel", command=dialog.destroy,
                              bg='#95a5a6', fg='white', font=('Arial', 11))
        cancel_btn.pack(side='left', padx=10)

        def add_and_close():
            """Add item to cart and close dialog"""
            try:
                quantity = int(qty_var.get() or "1")
                notes = notes_entry.get().strip()
                add_to_cart(item_name, quantity, unit_price, notes)
                dialog.destroy()
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid quantity")

        add_btn = tk.Button(btn_frame, text="Add to Order", command=add_and_close,
                         bg='#3498db', fg='white', font=('Arial', 11, 'bold'))
        add_btn.pack(side='left', padx=10)

        # Add hover effects
        add_hover_effect(dec_btn, '#e74c3c', '#c0392b')
        add_hover_effect(inc_btn, '#27ae60', '#2ecc71')
        add_hover_effect(add_btn, '#3498db', '#2980b9')
        add_hover_effect(cancel_btn, '#95a5a6', '#7f8d8d')

        # Select all text when focusing on qty entry
        qty_entry.bind("<FocusIn>", lambda e: qty_entry.selection_range(0, tk.END))
        qty_entry.focus_set()

        # Bind Enter key to add
        qty_entry.bind("<Return>", lambda e: add_and_close())
        notes_entry.bind("<Return>", lambda e: add_and_close())

    def view_sales_modern():
        # Copied from the existing view_sales_modern function in the same scope
        import sqlite3
        from tkinter import Toplevel, Frame, StringVar, Button, Label, ttk
        from datetime import date, timedelta

        # UI Configuration (same as in the original function)
        BG_COLOR = '#f4f7ff'
        CARD_COLOR = '#ffffff'
        TEXT_COLOR = '#333333'
        GREEN_COLOR = '#3DDC97'
        BLUE_COLOR = '#4C7EFF'
        FONT_FAMILY = "Poppins"

        win = Toplevel(root)
        win.title("View Sales")
        win.configure(bg=BG_COLOR)
        try:
            win.state('zoomed')
        except Exception:
            win.geometry("1400x850")

        # Rest of the function remains the same as in the original code
        # ... [include the entire original view_sales_modern function body]
