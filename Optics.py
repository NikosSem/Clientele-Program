import tkinter as tk
import csv
import tkinter.messagebox

# Button dimensions
button_width = 350
button_height = 350

### ADDING CLIENTS ###
def open_add_popup():
    # "Προσθήκη" popup
    add_popup = tk.Toplevel(root)
    add_popup.title("Νέα Παραγγελία")
    add_popup.configure(bg="#333333")
    add_popup.attributes('-topmost', True)
    add_popup.iconbitmap("C:\\Users\\nicks\\Desktop\\optics_logo.ico")


    add_popup.geometry("450x835")
    fields_frame = tk.Frame(add_popup, bg="#333333")
    fields_frame.pack(padx=20, pady=20)

    # Store Entries
    add_popup_entries = []

    # Input Fields
    fields = ["Όνομα", "Τηλέφωνο", "Διεύθυνση", "Email", "Ημερομηνία", "Συν. Οράσεως", "Συν. Φ.Ε.", "Σκελετός", "Παραγγελία", "Τιμή", "Σχόλια"]

    additional_fields_sight = ["Additional Sight Field 1", "Additional Sight Field 2"]
    additional_fields_ref = ["Additional Refraction Field 1", "Additional Refraction Field 2"]
    additional_field_after_skeletos = ["Additional Field after Σκελετός"]
    additional_field_after_paraggelia = ["Additional Field after Παραγγελία"]

    index_sight = fields.index("Συν. Οράσεως")
    index_ref = fields.index("Συν. Φ.Ε.")
    index_skeletos = fields.index("Σκελετός")
    index_paraggelia = fields.index("Παραγγελία")

    # Update the fields list
    fields = (
        fields[:index_sight + 1] + additional_fields_sight +
        fields[index_sight + 1:index_ref + 1] + additional_fields_ref +
        fields[index_ref + 1:index_skeletos + 1] +
        [additional_field_after_skeletos[0]] + 
        fields[index_skeletos + 1:index_paraggelia + 1] +
        [additional_field_after_paraggelia[0]] +  
        fields[index_paraggelia + 1:]
    )
    # Labels and Entry Fields
    add_popup_entries = []
    for i, field in enumerate(fields):
        label = tk.Label(fields_frame, text=field, fg="white", bg="#333333", font=("Times New Roman", 18))
        entry = tk.Entry(fields_frame, bg="white", fg="#333333", font=("Times New Roman", 18))

        # Determine if a separator should be inserted
        if field in ["Τηλέφωνο", "Διεύθυνση", "Email", "Ημερομηνία", "Συν. Οράσεως", "Συν. Φ.Ε.", "Σκελετός", "Παραγγελία", "Τιμή", "Σχόλια"]:
            separator = tk.Frame(fields_frame, height=2, bg="grey")
            separator.grid(row=i * 2 -1, column=0, columnspan=2, sticky='ew')

        # Place labels and entry fields in the grid
        label.grid(row=i * 2, column=0, padx=5, pady=5, sticky='w')
        entry.grid(row=i * 2, column=1, padx=5, pady=5, sticky='e')

        # Hide labels for additional fields
        if field in additional_fields_sight or field in additional_fields_ref or field in additional_field_after_skeletos or field in additional_field_after_paraggelia:
            label.grid_forget()

        add_popup_entries.append(entry)

    # Save icon
    icon_path_save = "C:\\Users\\nicks\\Desktop\\save.png"
    save_icon = tk.PhotoImage(file=icon_path_save).subsample(15)

    save_button = tk.Button(add_popup, image=save_icon, command=lambda: submit_info(add_popup_entries, fields, add_popup), bg="#333333", relief=tk.FLAT, activebackground="#666666")
    save_button.image = save_icon
    save_button.pack(side=tk.RIGHT, padx=10, pady=10, anchor="sw")

labels_written = False

### SAVE ###
def submit_info(entries, fields, popup):
    client_info = [entry.get() for entry in entries]

    file_exists = False
    file_has_labels = False

    # Check if the file already exists and contains labels
    try:
        with open('Clients.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            first_row = next(reader)
            if first_row == fields:
                file_exists = True
                file_has_labels = True
    except FileNotFoundError:
        pass

    # Check for missing fields and update the fields list
    if not file_exists or (file_exists and not file_has_labels):
        with open('Clients.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(fields)
            elif file_exists and not file_has_labels:
                writer.writerow(fields)

    # If the length of client_info is less than the length of fields (including additional fields),
    # fill in empty strings for missing data
    if len(client_info) < len(fields):
        client_info.extend([''] * (len(fields) - len(client_info)))

    # Append client information to the CSV file
    with open('Clients.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(client_info)

    print("Information saved to Clients.csv:")
    print(client_info)

    popup.destroy()

def open_popup(title):
    if title == "Προσθήκη":
        open_add_popup()

### CLIENT BUTTONS ###
def rounded_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1 + radius, y1,
              x1 + radius, y1,
              x2 - radius, y1,
              x2 - radius, y1,
              x2, y1,
              x2, y1 + radius,
              x2, y1 + radius,
              x2, y2 - radius,
              x2, y2 - radius,
              x2, y2,
              x2 - radius, y2,
              x2 - radius, y2,
              x1 + radius, y2,
              x1 + radius, y2,
              x1, y2,
              x1, y2 - radius,
              x1, y2 - radius,
              x1, y1 + radius,
              x1, y1 + radius,
              x1, y1]
    return canvas.create_polygon(points, **kwargs, smooth=True)

### CLIENTS ###
def open_clients_popup():
    # Create the clients popup window
    global popup_width
    clients_popup = tk.Toplevel(root)
    clients_popup.title("Πελατολόγιο")
    clients_popup.attributes('-topmost', True)
    clients_popup.iconbitmap("C:\\Users\\nicks\\Desktop\\optics_logo.ico")
    
    # Change the background color
    clients_popup.configure(bg="#333333")
    
    # Dimensions of the popup
    popup_width = 500
    popup_height = 835
    screen_width = root.winfo_screenwidth()
    x_position = screen_width - popup_width - 50
    y_position = 50
    clients_popup.geometry(f"{popup_width}x{popup_height}+{x_position}+{y_position}")

    # Create a frame for search bar and search button
    search_frame = tk.Frame(clients_popup, bg="#333333")
    search_frame.pack(padx=20, pady=20, fill=tk.X)

    # Search Entry
    search_entry = tk.Entry(search_frame, bg="white", fg="black", font=("Times New Roman", 18))
    search_entry.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.X, expand=True)

    # Create a scrollbar
    scrollbar = tk.Scrollbar(clients_popup, orient=tk.VERTICAL)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Create a small canvas below the search bar
    canvas = tk.Canvas(clients_popup, bg="#333333", highlightbackground="white", highlightthickness=0, width=popup_width - 40, height=popup_height - 100, yscrollcommand=scrollbar.set)
    canvas.pack(padx=20, pady=20)
    
    # Configure the scrollbar to control the canvas scrolling
    scrollbar.config(command=canvas.yview)
    canvas.configure(scrollregion=canvas.bbox("all"))
    
    # Read client names from the CSV file
    client_names = []
    try:
        with open('Clients.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                    client_names.append(row['Όνομα'].strip())
    except FileNotFoundError:
        print("Clients.csv file not found!")

    # Function to display client info
    def show_client_info(event):
        x, y = event.x, event.y + canvas.canvasy(0)
        clicked_item = event.widget.find_closest(x, y)[0]
        item_tags = event.widget.gettags(clicked_item)
    
        # Find the item tag that corresponds to the client's name
        name = None
        for tag in item_tags:
            if tag.strip() in client_names:
                name = tag.strip()
                break
    
        if name:
            # Read the CSV file and find client information
            try:
                with open('Clients.csv', mode='r', newline='', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    clients_data = list(reader)
            except FileNotFoundError:
                print("Clients.csv file not found!")
                return

            # Find the index of the selected client
            selected_index = None
            for index, client in enumerate(clients_data):
                if client['Όνομα'] == name:
                    selected_index = index
                    break

            if selected_index is not None:
                display_client_info(selected_index, clients_data)


    def display_client_info(client_row, clients_data):
        selected_client_info = clients_data[client_row]

        add_popup = tk.Toplevel(root)
        add_popup.title("Στοιχεία Παραγγελίας")
        add_popup.configure(bg="#333333")
        add_popup.attributes('-topmost', True)
        add_popup.iconbitmap("C:\\Users\\nicks\\Desktop\\optics_logo.ico")


        fields_frame = tk.Frame(add_popup, bg="#333333")
        fields_frame.pack(padx=20, pady=20)

        fields = ["Όνομα", "Τηλέφωνο", "Διεύθυνση", "Email", "Ημερομηνία", "Συν. Οράσεως", "Additional Sight Field 1", "Additional Sight Field 2", "Συν. Φ.Ε.", "Additional Refraction Field 1", "Additional Refraction Field 2", "Σκελετός", "Additional Field after Σκελετός", "Παραγγελία", "Additional Field after Παραγγελία", "Τιμή", "Σχόλια"]

        entry_values = [selected_client_info.get(field, "") for field in fields]

        row_counter = 0

        entries = []
        additional_fields_to_hide = ["Additional Sight Field 1", "Additional Sight Field 2", "Additional Refraction Field 1", "Additional Refraction Field 2", "Additional Field after Σκελετός", "Additional Field after Παραγγελία"]

        for i, value in enumerate(entry_values):
            label = tk.Label(fields_frame, text=fields[i], fg="white", bg="#333333", font=("Times New Roman", 18))
            label.grid(row=row_counter * 2, column=0, padx=5, pady=5, sticky='w')

            entry = tk.Entry(fields_frame, bg="white", fg="#333333", font=("Times New Roman", 18))
            entry.grid(row=row_counter * 2, column=1, padx=5, pady=5, sticky='e')

            separator = tk.Frame(fields_frame, height=2, bg="grey")
            separator.grid(row=row_counter * 2 + 1, column=0, columnspan=2, sticky='ew')

            entry.insert(tk.END, value if value else '')  # Ensures 'None' values are handled
            entry.configure(state='readonly')  # Make the entry read-only if no value

            # Check if the field should be hidden
            if fields[i] in additional_fields_to_hide:
                label.grid_forget()

            row_counter += 1
            entries.append(entry)

        def edit_client_info():
            for entry in entries:
                entry.configure(state='normal')  # Make the entry fields editable

            edit_button.configure(state='disabled')  # Disable the Edit button after clicking
            save_button.configure(state='normal')   # Enable the Save button after clicking Edit

        def save_client_info():
            updated_info = [entry.get() for entry in entries]  # Get the updated information from the entry fields

            # Read the entire CSV content
            try:
                with open('Clients.csv', mode='r', newline='', encoding='utf-8') as file:
                    reader = csv.reader(file)
                    data = list(reader)

                # Update the specific client's information
                if client_row + 1 < len(data):
                    data[client_row + 1] = updated_info

                # Write the updated data back to the CSV file
                with open('Clients.csv', mode='w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerows(data)

                save_button.configure(state='disabled')  # Disable the Save button after saving
                for entry in entries:
                    entry.configure(state='readonly')  # Make the entry fields read-only after saving
                edit_button.configure(state='normal')  # Re-enable the Edit button after saving

                # Clear the existing canvas
                canvas.delete("all")

                # Read client names and dates from the updated CSV file
                client_data = []
                try:
                    with open('Clients.csv', mode='r', newline='', encoding='utf-8') as file:
                        reader = csv.DictReader(file)
                        for row in reader:
                            client_data.append({
                                'name': row['Όνομα'].strip(),
                                'date': row['Ημερομηνία'].strip()
                            })
                except FileNotFoundError:
                    print("Clients.csv file not found!")
                    return

                # Display client names and dates in the canvas
                button_y = 0
                for item in client_data:
                    name = item['name']
                    date = item['date']

                    button_tag = f"client_{name}"  # Adding a prefix to the tag for unique identification
                    rounded_rectangle(canvas, button_x_start, button_y, button_x_end, button_y + button_height, radius=10, fill="white", outline="black", tags=button_tag)
                    canvas.create_text((button_x_start + button_x_end) / 2, button_y + 15, text=name, fill="black", font=("Times New Roman", 18), tags=(button_tag, name))
                    canvas.create_text((button_x_start + button_x_end) / 2, button_y + button_height - 15, text=date, fill="black", font=("Times New Roman", 16), tags=(button_tag, f"{name}_date"))
                    canvas.tag_bind(button_tag, '<Button-1>', show_client_info)
                    button_y += button_height + 20

                # Refresh canvas display
                canvas.update()
                canvas.configure(scrollregion=canvas.bbox("all"))

            except FileNotFoundError:
                print("Clients.csv file not found!")

        def delete_client():
            try:
                nonlocal add_popup  # Access the add_popup from the outer scope
                with open('Clients.csv', mode='r', newline='', encoding='utf-8') as file:
                    reader = list(csv.DictReader(file))

                # Delete the selected client
                del reader[client_row]

                # Write the updated data back to the CSV file
                with open('Clients.csv', mode='w', newline='', encoding='utf-8') as file:
                    fieldnames = reader[0].keys() if reader else []
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(reader)

                # Close the current client's info popup
                add_popup.destroy()

                # Show a message box indicating successful deletion
                tkinter.messagebox.showinfo("Διαγραφή", "Ο πελάτης διαγράφηκε επιτυχώς.")

                # Clear the canvas
                canvas.delete("all")

                # Read client names and dates from the updated CSV file
                client_data = []
                try:
                    with open('Clients.csv', mode='r', newline='', encoding='utf-8') as file:
                        reader = csv.DictReader(file)
                        for row in reader:
                            client_data.append({
                                'name': row['Όνομα'].strip(),
                                'date': row['Ημερομηνία'].strip()
                            })
                except FileNotFoundError:
                    print("Clients.csv file not found!")
                    return

                # Display client names and dates in the canvas
                button_y = 0
                for item in client_data:
                    name = item['name']
                    date = item['date']

                    button_tag = f"client_{name}"  # Adding a prefix to the tag for unique identification
                    rounded_rectangle(canvas, button_x_start, button_y, button_x_end, button_y + button_height, radius=10, fill="white", outline="black", tags=button_tag)
                    canvas.create_text((button_x_start + button_x_end) / 2, button_y + 15, text=name, fill="black", font=("Times New Roman", 18), tags=(button_tag, name))
                    canvas.create_text((button_x_start + button_x_end) / 2, button_y + button_height - 15, text=date, fill="black", font=("Times New Roman", 16), tags=(button_tag, f"{name}_date"))
                    canvas.tag_bind(button_tag, '<Button-1>', show_client_info)
                    button_y += button_height + 20

                # Refresh canvas display
                canvas.update()
                canvas.configure(scrollregion=canvas.bbox("all"))

            except FileNotFoundError:
                print("Clients.csv file not found!")

        # Load the icons for Edit and Save buttons
        icon_path_edit = "C:\\Users\\nicks\\Desktop\\pencil.ico"
        icon_path_save = "C:\\Users\\nicks\\Desktop\\save.png"
        icon_path_delete = "C:\\Users\\nicks\\Desktop\\delete.png"
        icon_edit = tk.PhotoImage(file=icon_path_edit).subsample(10)
        icon_save = tk.PhotoImage(file=icon_path_save).subsample(15)
        icon_delete = tk.PhotoImage(file=icon_path_delete).subsample(10)

        # Create a frame to contain the buttons for better alignment
        button_frame = tk.Frame(add_popup, bg="#333333")
        button_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=20)

        # Create an 'Edit' button with the icon
        edit_button = tk.Button(button_frame, image=icon_edit, command=edit_client_info, bg="#333333", bd=0)
        edit_button.image = icon_edit  # Keep a reference to the image to prevent garbage collection
        edit_button.grid(row=0, column=0, padx=(0, 10))  # Use grid layout for better positioning

        # Create a 'Save' button with the icon
        save_button = tk.Button(button_frame, image=icon_save, command=save_client_info, bg="#333333", bd=0, state='disabled')
        save_button.image = icon_save  # Keep a reference to the image to prevent garbage collection
        save_button.grid(row=0, column=1, padx=(10, 0))  # Use grid layout for better positioning

        delete_button = tk.Button(button_frame, image=icon_delete, command=delete_client, bg="#333333", bd=0)
        delete_button.image = icon_delete
        delete_button.grid(row=0, column=3, padx=(250, 0))


                            
    # Clients Button Layouts
    button_width = 300
    button_height = 50
    button_y = 0
    button_x_start = (popup_width - button_width) / 2.5
    button_x_end = button_x_start + button_width

    for name in client_names:
        # Calculate positions for client name and date
        client_name_y = button_y + 15  # Adjust Y position for client name
        date_y = button_y + button_height - 15  # Adjust Y position for date

        # Create rounded rectangle for client name
        button_tag = f"client_{name}"  # Adding a prefix to the tag for unique identification
        rounded_rectangle(canvas, button_x_start, button_y, button_x_end, button_y + button_height, radius=10, fill="white", outline="black", tags=button_tag)
        canvas.create_text((button_x_start + button_x_end) / 2, client_name_y, text=name, fill="black", font=("Times New Roman", 18), tags=(button_tag, name))
        canvas.tag_bind(button_tag, '<Button-1>', show_client_info)

        # Retrieve client's date from the CSV file
        client_date = None
        try:
            with open('Clients.csv', mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['Όνομα'].strip() == name:
                        client_date = row['Ημερομηνία'].strip()
                        break
        except FileNotFoundError:
            print("Clients.csv file not found!")

        # Display client date below the client name
        canvas.create_text((button_x_start + button_x_end) / 2, date_y, text=client_date, fill="black", font=("Times New Roman", 16), tags=(button_tag, f"{name}_date"))

        button_y += button_height + 20

    canvas.update()
    canvas.configure(scrollregion=canvas.bbox("all"))

    ### SEARCH BAR ###
    def perform_search(event):
        query = search_entry.get().lower()
        canvas.delete("all")

        # Read client data from the CSV file
        client_data = []
        try:
            with open('Clients.csv', mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    client_data.append({
                        'name': row['Όνομα'].strip(),
                        'date': row['Ημερομηνία'].strip().lower()  # Convert date to lowercase for case-insensitive search
                    })
        except FileNotFoundError:
            print("Clients.csv file not found!")
            return

        # Filter client data based on the query (matching either name or date)
        filtered_data = [
            item for item in client_data
            if query in item['name'].lower() or query in item['date']
        ]

        # Display filtered client names and dates in the canvas
        button_width = 300
        button_height = 50
        button_y = 0
        button_x_start = (popup_width - button_width) / 2.5
        button_x_end = button_x_start + button_width

        for item in filtered_data:
            name = item['name']
            date = item['date']

            button_tag = f"client_{name}"  # Adding a prefix to the tag for unique identification
            rounded_rectangle(canvas, button_x_start, button_y, button_x_end, button_y + button_height, radius=10, fill="white", outline="black", tags=button_tag)
            canvas.create_text((button_x_start + button_x_end) / 2, button_y + 15, text=name, fill="black", font=("Times New Roman", 18), tags=(button_tag, name))
            canvas.create_text((button_x_start + button_x_end) / 2, button_y + button_height - 15, text=date, fill="black", font=("Times New Roman", 16), tags=(button_tag, f"{name}_date"))
            canvas.tag_bind(button_tag, '<Button-1>', show_client_info)
            button_y += button_height + 20

        canvas.update()
        canvas.configure(scrollregion=canvas.bbox("all"))

    # Bind the search function to the key release event in the search bar
    search_entry.bind('<KeyRelease>', perform_search)

    def on_mouse_wheel(event):
        canvas_height = canvas.winfo_height()

        # Check if scrolling down or if top item is at the top of the canvas
        if event.delta < 0 or canvas.canvasy(0) >= 0:
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        else:
            canvas.yview_moveto(0)  # Stop scrolling further up

    # Bind the mouse wheel event to the canvas
    canvas.bind_all("<MouseWheel>", on_mouse_wheel)




# Create the main window
root = tk.Tk()
root.title("Optics")
root.iconbitmap("C:\\Users\\nicks\\Desktop\\optics_logo.ico")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set window size slightly smaller than the screen size
window_width = screen_width - 450
window_height = screen_height - 250

root.geometry(f"{window_width}x{window_height}+0+0")
root.configure(bg="#333333")

# Load icons/images
icon_path_add = "C:\\Users\\nicks\\Desktop\\add.ico" 
icon_path_clients = "C:\\Users\\nicks\\Desktop\\clients.ico"

icon_add = tk.PhotoImage(file=icon_path_add)
icon_clients = tk.PhotoImage(file=icon_path_clients)

# Create frame to hold buttons with more padding
frame = tk.Frame(root, bg="#333333", padx=50)
frame.pack(expand=True)

# Create the "Προσθήκη" button
btn_add = tk.Button(frame, text="Προσθήκη", command=lambda: open_popup("Προσθήκη"), bg="white", fg="#333333", font=("Arial", 20), width=button_width, height=button_height, bd=0, relief=tk.RIDGE)
btn_add.pack(side=tk.LEFT, padx=30, pady=10, expand=True)
btn_add.config(image=icon_add, compound=tk.TOP)

# Create the "Πελάτες" button
btn_clients = tk.Button(frame, text="Πελάτες", command=open_clients_popup, bg="white", fg="#333333", font=("Arial", 20), width=button_width, height=button_height, bd=0, relief=tk.RIDGE)
btn_clients.pack(side=tk.RIGHT, padx=30, pady=10, expand=True)
btn_clients.config(image=icon_clients, compound=tk.TOP)

# Run the application
root.mainloop()