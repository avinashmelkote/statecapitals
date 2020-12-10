#Find the capital cities of each state within the USA
statecapitals={}

statecapitals['ALABAMA']='Montgomery'
statecapitals['ALASKA']='Juneau'
statecapitals['ARIZONA']='Phoenix'
statecapitals['ARKANSAS']='Little Rock'
statecapitals['CALIFORNIA']='Sacramento'
statecapitals['COLORADO']='Denver'
statecapitals['CONNECTICUT']='Hartford'
statecapitals['DELAWARE']='Dover'
statecapitals['FLORIDA']='Tallahassee'
statecapitals['GEORGIA']='Atlanta'
statecapitals['HAWAII']='Honolulu'
statecapitals['IDAHO']='Boise'
statecapitals['ILLINOIS']='Springfield'
statecapitals['INDIANA']='Indianapolis'
statecapitals['IOWA']='Des Moines'
statecapitals['KANSAS']='Topeka'
statecapitals['KENTUCKY']='Frankfort'
statecapitals['LOUISIANA']='Baton Rouge'
statecapitals['MAINE']='Augusta'
statecapitals['MARYLAND']='Annapolis'
statecapitals['MASSACHUSETTS']='Boston'
statecapitals['MICHIGAN']='Lansing'
statecapitals['MINNESOTA']='Saint Paul'
statecapitals['MISSISSIPPI']='Jackson'
statecapitals['MISSOURI']='Jefferson City'
statecapitals['MONTANA']='Helena'
statecapitals['NEBRASKA']='Lincoln'
statecapitals['NEVADA']='Carson City'
statecapitals['NEW HAMPSHIRE']='Concord'
statecapitals['NEW JERSEY']='Trenton'
statecapitals['NEW MEXICO']='Santa Fe'
statecapitals['NEW YORK']='Albany'
statecapitals['NORTH CAROLINA']='Raleigh'
statecapitals['NORTH DAKOTA']='Bismarck'
statecapitals['OHIO']='Columbus'
statecapitals['OKLAHOMA']='Oklahoma City'
statecapitals['OREGON']='Salem'
statecapitals['PENNSYLVANIA']='Harrisburg'
statecapitals['RHODE ISLAND']='Providence'
statecapitals['SOUTH CAROLINA']='Columbia'
statecapitals['SOUTH DAKOTA']='Pierre'
statecapitals['TENNESSEE']='Nashville'
statecapitals['TEXAS']='Austin'
statecapitals['UTAH']='Salt Lake City'
statecapitals['VERMONT']='Montpelier'
statecapitals['VIRGINIA']='Richmond'
statecapitals['WASHINGTON']='Olympia'
statecapitals['WEST VIRGINIA']='Charleston'
statecapitals['WISCONSIN']='Madison'
statecapitals['WYOMING']='Cheyenne'

while True:
    mystate = input("Enter the name of any state in the USA\nWhen you are finished, enter 'done':").upper()
    if mystate=='DONE':
        print('All done!')
        break
    else:
        try:
            if mystate in statecapitals:
                print('Capital:',statecapitals[mystate])
            else:
                print('State not found:',mystate)
            continue
        except:
            print('Invalid data, try again.')
            continue
