# from models import Events, Members
# import os
# import getpass



# if __name__ == "__main__":
#     members_manager = Members()
#     events_manager = Events()


# class Admin: 
#     def __init__(self):
#         self.username = 'zabiullah'
#         self.password = os.getenv("ADMIN_PASSWORD") 

#     def login(self): 
#         entered_username = input("Enter username: ") 
#         # Use getpass to mask the password input 
#         entered_password = getpass.getpass("Enter password: ") 
#         if entered_username == self.username and entered_password == self.password:
#             print("Login successful!") 
#             return True 
#         else:
#             print("Incorrect username or password.")

# admin = Admin()

# while(1):
#     if admin.login():
#     # Run the main program
#         while True:
#             print("\n========= University Society Management =========")
#             print("1. Members Management")
#             print("2. Events Management")
#             print("3. Single Event Management")
#             print("4. Exit")
#             choice = input("Choose an option: ")

#             if choice == '1':
#                 members_manager.show_member_menu()
#             elif choice == '2':
#                 events_manager.show_event_menu()
#             elif choice == '3':
#                 events_manager.show_single_event_management_menu(members_manager.members)
#             elif choice == '4':
#                 print("Exiting the system. Goodbye!")
#                 break
#             else:
#                 print("Invalid choice. Please try again.")
#     else:
#         print("Admin login failed. Exiting.")
    


import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 7))

# Draw rectangles for each step
ax.add_patch(mpatches.FancyBboxPatch((0.1, 0.8), 0.8, 0.1, boxstyle="round,pad=0.1", edgecolor='blue', facecolor='lightblue'))
ax.text(0.5, 0.85, 'Data Collection', ha='center', va='center', fontsize=12)

ax.add_patch(mpatches.FancyBboxPatch((0.1, 0.65), 0.8, 0.1, boxstyle="round,pad=0.1", edgecolor='blue', facecolor='lightblue'))
ax.text(0.5, 0.7, 'Data Preprocessing', ha='center', va='center', fontsize=12)

ax.add_patch(mpatches.FancyBboxPatch((0.1, 0.5), 0.8, 0.1, boxstyle="round,pad=0.1", edgecolor='blue', facecolor='lightblue'))
ax.text(0.5, 0.55, 'Model Selection', ha='center', va='center', fontsize=12)

ax.add_patch(mpatches.FancyBboxPatch((0.1, 0.35), 0.8, 0.1, boxstyle="round,pad=0.1", edgecolor='blue', facecolor='lightblue'))
ax.text(0.5, 0.4, 'Training the Model', ha='center', va='center', fontsize=12)

ax.add_patch(mpatches.FancyBboxPatch((0.1, 0.2), 0.8, 0.1, boxstyle="round,pad=0.1", edgecolor='blue', facecolor='lightblue'))
ax.text(0.5, 0.25, 'Model Evaluation', ha='center', va='center', fontsize=12)

ax.add_patch(mpatches.FancyBboxPatch((0.1, 0.05), 0.8, 0.1, boxstyle="round,pad=0.1", edgecolor='blue', facecolor='lightblue'))
ax.text(0.5, 0.1, 'Prediction', ha='center', va='center', fontsize=12)

# Arrows between the steps
ax.annotate('', xy=(0.5, 0.75), xytext=(0.5, 0.7), arrowprops=dict(arrowstyle="->", lw=2, color="black"))
ax.annotate('', xy=(0.5, 0.6), xytext=(0.5, 0.55), arrowprops=dict(arrowstyle="->", lw=2, color="black"))
ax.annotate('', xy=(0.5, 0.45), xytext=(0.5, 0.4), arrowprops=dict(arrowstyle="->", lw=2, color="black"))
ax.annotate('', xy=(0.5, 0.3), xytext=(0.5, 0.25), arrowprops=dict(arrowstyle="->", lw=2, color="black"))
ax.annotate('', xy=(0.5, 0.15), xytext=(0.5, 0.1), arrowprops=dict(arrowstyle="->", lw=2, color="black"))

# Set axis limits and hide axes
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Title for the diagram
plt.title('Steps in Classification Model Construction', fontsize=14)

# Save the plot as PNG
plt.savefig('classification_model_construction.png', format='png')

# Show the plot (optional)
plt.show()
