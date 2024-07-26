import tkinter as tk
from tkinter import messagebox
import pickle

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        
        self.contacts = []  #  to store contacts
        
        # GUI components
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.name_entry = tk.Entry(root, width=30)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        
        self.phone_label = tk.Label(root, text="Phone Number:")
        self.phone_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.phone_entry = tk.Entry(root, width=30)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)
        
        self.email_label = tk.Label(root, text="Email:")
        self.email_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.email_entry = tk.Entry(root, width=30)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)
        
        self.address_label = tk.Label(root, text="Address:")
        self.address_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.address_entry = tk.Entry(root, width=30)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)
        
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)
        
        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=10)
        
        self.search_label = tk.Label(root, text="Search:")
        self.search_label.grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)
        self.search_entry = tk.Entry(root, width=30)
        self.search_entry.grid(row=6, column=1, padx=10, pady=5)
        
        self.search_button = tk.Button(root, text="Search", command=self.search_contact)
        self.search_button.grid(row=7, column=0, columnspan=2, pady=10)
        
        self.contacts_listbox = tk.Listbox(root, width=50, height=10)
        self.contacts_listbox.grid(row=8, column=0, columnspan=2, padx=10, pady=10)
        
        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=9, column=0, columnspan=2, pady=10)
        
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=10, column=0, columnspan=2, pady=10)
        
        
        self.load_contacts()
    
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        
        if name and phone:
            contact = {
                'name': name,
                'phone': phone,
                'email': email,
                'address': address
            }
            self.contacts.append(contact)
            self.save_contacts()
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Name and Phone Number are required fields.")
    
    def view_contacts(self):
        self.contacts_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contacts_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")
    
    def search_contact(self):
        search_term = self.search_entry.get().strip().lower()
        if not search_term:
            messagebox.showerror("Error", "Please enter a search term.")
            return
        
        self.contacts_listbox.delete(0, tk.END)
        found_contacts = []
        for contact in self.contacts:
            if search_term in contact['name'].lower() or search_term in contact['phone']:
                found_contacts.append(f"{contact['name']} - {contact['phone']}")
        
        if found_contacts:
            for contact in found_contacts:
                self.contacts_listbox.insert(tk.END, contact)
        else:
            messagebox.showinfo("Not Found", "No contacts found.")
    
    def update_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select a contact to update.")
            return
        
        selected_contact = self.contacts_listbox.get(selected_index)
        selected_name = selected_contact.split(' - ')[0]
        
        for contact in self.contacts:
            if contact['name'] == selected_name:
                # Update fields
                contact['phone'] = self.phone_entry.get()
                contact['email'] = self.email_entry.get()
                contact['address'] = self.address_entry.get()
                self.save_contacts()
                messagebox.showinfo("Success", "Contact updated successfully!")
                self.clear_entries()
                self.view_contacts()
                return
    
    def delete_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select a contact to delete.")
            return
        
        selected_contact = self.contacts_listbox.get(selected_index)
        selected_name = selected_contact.split(' - ')[0]
        
        for contact in self.contacts:
            if contact['name'] == selected_name:
                self.contacts.remove(contact)
                self.save_contacts()
                messagebox.showinfo("Success", "Contact deleted successfully!")
                self.view_contacts()
                return
    
    def save_contacts(self):
        with open('contacts.pickle', 'wb') as f:
            pickle.dump(self.contacts, f)
    
    def load_contacts(self):
        try:
            with open('contacts.pickle', 'rb') as f:
                self.contacts = pickle.load(f)
        except FileNotFoundError:
            # contacts list
            self.contacts = []
    
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
