# Readit
# Thorin Schmidt

'''figure out how to put the text file into a dictionary of item entries'''

def fill_list():
    '''open the files and put the contents into a dictonary'''
    local_dict = {}
    key = 0
    text_file = open("core.txt", "r")

    for line in text_file:
        str_name = line[:-1]
        str_cost = text_file.readline()[:-1]
        str_weight = text_file.readline()[:-1]

        # Parse the cost into "gold pieces"
        flt_cost = 0
        number, units = str_cost.split()
        number = int(number)
        if units.upper() == 'PP':
            flt_cost = number * 8


        elif units.upper() == 'GP':
            flt_cost = number

        elif units.upper() == 'EP':
            flt_cost = number * .5

        elif units.upper() == 'SP':
            flt_cost = number * .1

        else:
            flt_cost = number * .01

        # Parse the weight into units
        try:
            flt_weight = float(str_weight)

        except:
            if str_weight == '*':
                flt_weight = .1
                
            else:
                flt_weight = 0
                
        entry = [str_name, str_cost, str_weight, flt_cost, flt_weight, 0]
        if '' not in entry:
            local_dict[key] = entry

        else:
            break

        key += 1

    text_file.close()
    
    return local_dict


inventory = fill_list()

for key in inventory.keys():
    print( key, ":", inventory[key])
    
print("Done...")
