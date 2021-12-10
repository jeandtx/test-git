

def Company_list(Company):

    print("The CEO is : \n", Company['CEO'],
          "\nThe Project Manager is : \n", Company['Project Manager'],
          "\nThe first programmer is :\n", Company['Programmer 1'],
          "\nThe second one is :\n", Company['Programmer 2'],
          "\nThe third one is :\n", Company['Programmer 3'],
          "\nThe last programmer is :\n", Company['Programmer 5'] )


Company = {
    'Programmer 1': 'Tristan',
    'Programmer 2': 'Amaury',
    'Programmer 3': 'Clement',
    'CEO': 'Jean',
    'Project Manager': 'Marc-Antoine',
    'Programmer 5': 'Tshiya'
}

Company_list(Company)