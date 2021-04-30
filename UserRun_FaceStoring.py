import utilities
import face_storing

admin_number = "+918074716450"
def admin():
    global admin_number
    print("ADMIN FACE STORING")
    admin_number = input("Enter your Mobile Number with country code\n")
    face_storing.face_storing()

def user_info():

    print("SAVE NUMBER {} AS 'Admin' TO SEND REQUEST OR ENTER THE NAME OF PERSON WITH THIS NUMBER "
          "(NOTE : CHARACTERS ARE CASE SENSITIVE)".format(admin_number))
    i = input("Press Enter to continue")
    name = input("Enter your Full Name\n")
    emp_id = input("Enter your Employee ID\n")
    admin = input("Enter name of Admin({}) as stored in your phone\n(NOTE : CHARACTERS ARE CASE SENSITIVE)\n".format(admin_number))
    return name,emp_id,admin

def user():

    name,emp_id,admin = user_info()
    utilities.whatsApp_user_details(name,emp_id,admin)
    print("Your Message has been sent to Admin\n")
    otp_sent = utilities.otp_generator(admin_number)
    print("OTP has been sent to user")
    print(otp_sent)
#    if (input("To Resend OTP press 'r' else Press Enter") == 'r'):
#        otp_sent = utilities.otp_generator(admin_number)
#    else:
    otp_received = int(input("ENTER THE OTP SENT BY THE ADMIN\n"))
    if(otp_sent == otp_received):
        face_storing.face_storing(emp_id)

if __name__ == '__main__':
    flag = input("Enter 'a' for Admin or 'u' for New User")
    if flag == 'a':
        admin()
        print("Admin Face Storing completed.")
    elif flag == 'u':
        user()


