class Contact:
 """
 Class that generates new instances of contacts
 """
contact_list = []
    #Init method up here
def save_contact(self):
    '''
    save_contact method saves contact objects into contact_list
    '''

    Contact.contact_list.append(self)

def __init__(self,first_name, last_name, phone_number, email):

    '''
    __init__method that helps define properties
    '''

    self.first_name = first_name
    self.last_name = last_name
    self.phone_number = phone_number
    self.email = email
