import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# aisa code likh k do jis main jo parameter pass hu raha hai uska naam print krna hai , means k jo parameter pass hua wo naam of the variable

# models.py
def only_letters(text):
    for i in text:
        if not ('A' <= i <= 'Z' or 'a' <= i <= 'z'):
            return -1
    return 0  # Return 0 if all characters are letters

def only_numbers(text):
    for i in text:
        if not ('0' <= i <= '9'):
            return -1
    return 0  # Return 0 if all characters are numbers

def only_date(text):
    if len(text) != 10 or text[4] != '-' or text[7] != '-':
        return -1
    
    year, month, day = text[:4], text[5:7], text[8:]
    if not (only_numbers(year) == 0 and only_numbers(month) == 0 and only_numbers(day) == 0):
        return -1
    
    return 0  # Return 0 if date format is valid



class Mail_Automation:
    def send_email(self, subject, body, to_email):
        # Gmail SMTP server details
        smtp_server = "smtp.gmail.com"
        smtp_port = 587  # Use 465 for SSL, 587 for TLS
        # Your email credentials (Gmail example)
        from_email = "zabigujjar9900@gmail.com"  #  email
        from_password = "eevh kyia qkun hnnh"  #  app password
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        # Attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))
        try:
            # Connect to Gmail's SMTP server
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()  # Start TLS encryption
            server.login(from_email, from_password)
            # Send the email
            text = msg.as_string()
            server.sendmail(from_email, to_email, text)
            print(f"Email successfully sent to {to_email}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            server.quit()
    def send_event_notification(member, event):
        # Email subject and body
        subject = f"{event.title} - Upcoming Event Information"
        body = f"""
        Dear {member.name},
        We are excited to inform you about the upcoming event titled '{event.title}' scheduled on {event.event_date}.
    
        Event Details:
        - Event: {event.title}
        - Date: {event.event_date}
        - Attendees: {', '.join([attendee.name for attendee in event.attendees])}
    
        We look forward to seeing you there!
        Best regards,
        The University Society Team
        """
        Mail_Automation.send_email(subject, body, member.email)
        # Send the email
    def send_member_notification(self, member):
        subject = f"Welcome to our community, {member.name}!"
        body = f"""
        Dear {member.name},
        Welcome to our community! We are excited to have you join us.
        Best regards,
        The University Society Team
        """
        self.send_email(subject, body, member.email)
mail  =  Mail_Automation()


class Member:
    def __init__(self, name, id, email, join_date, role="attendee"):
        self.name = name
        self.id = id
        self.email = email
        self.join_date = join_date
        self.role = role  # Default role is "attendee"

    def __str__(self):
        return f"ID: {self.id} | Name: {self.name} | Email: {self.email} | Role: {self.role}| Join Date: {self.join_date}"

    def to_csv(self):
        # Returns a string that can be written to a CSV file
        return f"{self.id},{self.name},{self.email},{self.join_date},{self.role}"


class Members:
    def __init__(self):
        self.members=[]
        self.load_members_from_file()
    def add_member(self):
        while(1):
            name = input("Enter name: ")
            check = only_letters(name)
            if(check!=-1):
                break
        while(1):
            id = input("Enter member ID: ")
            check = only_numbers(id)
            for member in self.members:
                if member.id == id:
                    print("Error: Member ID already exists.")
                    check = -1
                    break
            if(check!=-1):
                break

        email = input("Enter email: ")
        while(1):
            join_date = input("Enter join date (YYYY-MM-DD): ")
            check = only_date(join_date)
            if(check!=-1):
                break

        member = Member(name,id,email,join_date)
        self.members.append(member)
        mail.send_member_notification(member)
        self.save_members_to_file()
        print(f"Member {member.name} has been added successfully!")

    
    def remove_member (self):
        id = input("Enter the member ID Please : ")
        for member in self.members:
            if(member.id == id):
                self.members.remove(member)
                print(f"Member with ID:{id} has been removed!")
                found = True
                break

        if not found:
            print("Member not found")


    def update_member(self):
        id = input("Enter the member ID to update: ")
        member_found = False
    
        for member in self.members:
            if member.id == id:
                print(f"Found member: {member.name}")
                new_name = input("Enter new name (or press Enter to keep the current): ")
                new_email = input("Enter new email (or press Enter to keep the current): ")
                new_join_date = input("Enter new join date (or press Enter to keep the current): ")
            
            # Update the member's information if provided
                if new_name:
                    member.name = new_name
                if new_email:
                    member.email = new_email
                if new_join_date:
                    member.join_date = new_join_date
            
                print("Member details updated successfully!")
                member_found = True
                break
    
        if not member_found:
            print("No member found with that ID.")




    def view_members(self):
        if not self.members:
            print("No members found.")
        else:
            print("\nList of Members:")
            for member in self.members:
                print(member)

    
    def save_members_to_file(self):
        filename="members.csv"
        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
            # Write the header
                writer.writerow(["Member ID", "Name", "Email", "Join Date", "Duty"])
            
            # Write each member's details
                for member in self.members:
                    writer.writerow([member.id, member.name, member.email, member.join_date, member.role])
            self.load_members_from_file()
            # print(f"Members have been saved to {filename}")
        except Exception as e:
            print(f"Error saving to file: {e}")

    def load_members_from_file(self):
        filename="members.csv"
        try:
            with open(filename, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row
                for row in reader:
                    member_id, name, email, join_date, duty = row
                    member = Member(name, member_id, email, join_date, duty)
                    self.members.append(member)
            # print(f"Members have been loaded from {filename}")
        except Exception as e:
            print(f"Error loading from file: {e}")

    def show_member_menu(self):
        while True:
            print("\nMember Management Menu:")
            print("1. Add Member")
            print("2. View Members")
            print("3. Update Member")
            print("4. Remove Member")
            print("5. Go Back")
        
            choice = input("Choose an option: ")
        
            if choice == '1':
                self.add_member()
            elif choice == '2':
                self.view_members()
            elif choice == '3':
                self.update_member()
            elif choice == '4':
                self.remove_member()
            elif choice == '5':
                break
            else:
                print("Invalid choice, please try again.")


def  finder(from_where,id):
    for i in from_where:
        if(i.id == id):
            return i
        else:
            return -1
    
class Event:
    def __init__(self, title,id,event_date):
        self.title = title
        self.id = id
        self.event_date = event_date
        self.attendees = []  # List of members attending this event
        self.roles = {}  # Dictionary to store roles for each member (key = member_id, value = role)
        self.attendance_record = {}  # Dictionary to track attendance status (key = member_id, value = boolean)
    
    def add_event_member(self,members):
        """Adds a member to the event and sets their role to 'attendee' by default."""
        while True:
            id = input("Enter the member ID to add: ")
            member = finder(members,id)
            if(member!=-1):
                    break
            print("Invalid Member ID")


        if member not in self.attendees:
            self.attendees.append(member)
            self.roles[member.id] = "attendee"  # Default role is 'attendee'
            self.attendance_record[member.id] = False  # Member is not yet marked as attended
            print(f"Member {member.name} added to event '{self.title}' as 'attendee'.")
            mail.send_event_notification(member,self)
        else:
            print(f"Member {member.name} is already attending this event.")

    def assign_role(self, id, role):
        """Assigns a new role to a member attending the event."""

        if id in self.roles:
            self.roles[id] = role
            print(f"Role '{role}' assigned to member with ID {id} for event '{self.title}'.")
        else:
            print(f"Member with ID {id} is not attending this event.")


    def mark_attendance(self, id):
        """Marks a member as having attended the event."""
        if id in self.attendance_record:
            self.attendance_record[id] = True
            print(f"Member with ID {id} marked as attended for event '{self.title}'.")
        else:
            print(f"Member with ID {id} is not in the attendance list.")

    def get_attendance(self):
        """Returns a list of members who attended the event."""
        # attended_members = member for self.member 
        return 

    def __str__(self):
        # String representation of the Event object (summary of event and attendees)
        return f"Event: {self.title}, Date: {self.event_date}, Attendees: {len(self.attendees)}"

class Events:
    def __init__(self):
        self.events = []
    
    def add_event(self):
        title = input("Enter Title: ")
        id = input("Enter event ID: ")
        event_date = input("Enter Event date (YYYY-MM-DD): ")
        event = Event(title,id,event_date)
        self.events.append(event)
        print(f"event {event.title} has been added successfully!")

    
    def remove_event (self):
        id = input("Enter the event ID Please : ")
        event = finder(self.events ,id)
        if (event==-1):
            print("event not found")
            return
        self.events.remove(event)
        print(f"event with ID:{id} has been removed!")
    



    def update_event(self):
        id = input("Enter the event ID to update: ")
        event = finder(self.events , id)
    
        if(event==-1):
                print("No event found with that ID.")
                return
                
        print(f"Found event: {event.name}")
        new_name = input("Enter new name (or press Enter to keep the current): ")
        new_email = input("Enter new email (or press Enter to keep the current): ")
        new_join_date = input("Enter new join date (or press Enter to keep the current): ")
            
        # Update the event's information if provided
        if new_name:
                    event.name = new_name
        if new_email:
                    event.email = new_email
        if new_join_date:
                    event.join_date = new_join_date
            
        print("event details updated successfully!")




    def view_events(self):
        if not self.events:
            print("No events found.")
        else:
            print("\nList of events:")
            for event in self.events:
                print(event)

    def show_single_event_management_menu(self,members):
        
        while(1):
            id = input("Enter the event ID to manage: ")
            event = finder(self.events, id)
            if event == -1:
                print("Event not found. Returning to previous menu.")
                continue
            break

        while True:
            print(f"\n========= Managing Event: {event.title} =========")
            print("1. Add Member to Event")
            print("2. Assign Role to Member")
            print("3. Mark Attendance")
            print("4. View Attendance")
            print("5. Go Back")

            choice = input("Choose an option: ")

            if choice == '1':
                event.add_event_member(members)
            elif choice == '2':
                id = input("Enter the member ID to assign a role: ")
                role = input("Enter the role: ")
                event.assign_role(id, role)
            elif choice == '3':
                id = input("Enter the member ID to mark attendance: ")
                event.mark_attendance(id)
            elif choice == '4':
                attendance = [member.name for member in event.attendees if event.attendance_record.get(member.id, False)]
                print("Attended Members:")
                for name in attendance:
                    print(name)
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")



    def show_event_menu(self):
        while True:
            print("\nevent Management Menu:")
            print("1. Add event")
            print("2. View events")
            print("3. Update event")
            print("4. Remove event")
            print("5. Go Back")
        
            choice = input("Choose an option: ")
        
            if choice == '1':
                self.add_event()
            elif choice == '2':
                self.view_events()
            elif choice == '3':
                self.update_event()
            elif choice == '4':
                self.remove_event()
            elif choice == '5':
                break
            else:
                print("Invalid choice, please try again.")

# Entry point for the program