contactes = {'Roger':678232311, 'Oriol':566879326}

def elimina(contactes=dict, user=str):
    if user in contactes.keys():
        contacte = contactes.pop(user)
        return contacte

print(elimina(contactes, 'Roger'))
