# ~ from user import User
from admin import Admin

privileges = ['can read posts', "can delete users"]
admin = Admin('juan', 'pérez', privileges)
admin.privileges.show_privileges()
