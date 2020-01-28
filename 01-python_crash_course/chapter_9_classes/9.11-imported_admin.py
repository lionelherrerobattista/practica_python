import user

privileges = ['can read posts', "can delete users"]
admin = user.Admin('juan', 'pérez', privileges)
admin.privileges.show_privileges()
