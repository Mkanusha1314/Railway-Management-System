import tkinter as tk
root = tk.Tk()
root.title("Railway Management System")

# User Management UI
label_user = tk.Label(root, text="User Management", font=("Arial", 14))
label_user.grid(row=0, column=0, columnspan=2, pady=10)

label_fname = tk.Label(root, text="First Name")
label_fname.grid(row=1, column=0)
entry_fname = tk.Entry(root)
entry_fname.grid(row=1, column=1)

label_lname = tk.Label(root, text="Last Name")
label_lname.grid(row=2, column=0)
entry_lname = tk.Entry(root)
entry_lname.grid(row=2, column=1)

label_age = tk.Label(root, text="Age")
label_age.grid(row=3, column=0)
entry_age = tk.Entry(root)
entry_age.grid(row=3, column=1)

label_gender = tk.Label(root, text="Gender")
label_gender.grid(row=4, column=0)
entry_gender = tk.Entry(root)
entry_gender.grid(row=4, column=1)

label_phone = tk.Label(root, text="Phone No")
label_phone.grid(row=5, column=0)
entry_phone = tk.Entry(root)
entry_phone.grid(row=5, column=1)

label_city = tk.Label(root, text="City")
label_city.grid(row=6, column=0)
entry_city = tk.Entry(root)
entry_city.grid(row=6, column=1)

label_state = tk.Label(root, text="State")
label_state.grid(row=7, column=0)
entry_state = tk.Entry(root)
entry_state.grid(row=7, column=1)

label_email = tk.Label(root, text="Email")
label_email.grid(row=8, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=8, column=1)

label_password = tk.Label(root, text="Password")
label_password.grid(row=9, column=0)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=9, column=1)

label_userid = tk.Label(root, text="User ID (For Update/Delete)")
label_userid.grid(row=10, column=0)
entry_userid = tk.Entry(root)
entry_userid.grid(row=10, column=1)

btn_add_user = tk.Button(root, text="Add User", command=add_user)
btn_add_user.grid(row=11, column=0)

btn_update_user = tk.Button(root, text="Update User", command=update_user)
btn_update_user.grid(row=11, column=1)

btn_delete_user = tk.Button(root, text="Delete User", command=delete_user)
btn_delete_user.grid(row=12, column=0, columnspan=2)

# Ticket Booking UI
label_booking = tk.Label(root, text="Ticket Booking", font=("Arial", 14))
label_booking.grid(row=13, column=0, columnspan=2, pady=10)

label_trainno = tk.Label(root, text="Train No")
label_trainno.grid(row=14, column=0)
entry_trainno = tk.Entry(root)
entry_trainno.grid(row=14, column=1)

label_sourcestation = tk.Label(root, text="Source Station ID")
label_sourcestation.grid(row=15, column=0)
entry_sourcestation = tk.Entry(root)
entry_sourcestation.grid(row=15, column=1)

label_destinationstation = tk.Label(root, text="Destination Station ID")
label_destinationstation.grid(row=16, column=0)
entry_destinationstation = tk.Entry(root)
entry_destinationstation.grid(row=16, column=1)

label_bookingdate = tk.Label(root, text="Booking Date (YYYY-MM-DD)")
label_bookingdate.grid(row=17, column=0)
entry_bookingdate = tk.Entry(root)
entry_bookingdate.grid(row=17, column=1)

label_journeydate = tk.Label(root, text="Journey Date (YYYY-MM-DD)")
label_journeydate.grid(row=18, column=0)
entry_journeydate = tk.Entry(root)
entry_journeydate.grid(row=18, column=1)

label_seatno = tk.Label(root, text="Seat No")
label_seatno.grid(row=19, column=0)
entry_seatno = tk.Entry(root)
entry_seatno.grid(row=19, column=1)

label_class = tk.Label(root, text="Class")
label_class.grid(row=20, column=0)
entry_class = tk.Entry(root)
entry_class.grid(row=20, column=1)

label_fare = tk.Label(root, text="Fare")
label_fare.grid(row=21, column=0)
entry_fare = tk.Entry(root)
entry_fare.grid(row=21, column=1)

btn_book_ticket = tk.Button(root, text="Book Ticket", command=book_ticket)
btn_book_ticket.grid(row=22, column=0, columnspan=2)

root.mainloop()

