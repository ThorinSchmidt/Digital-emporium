# Readit
# Thorin Schmidt

'''figure out how to put the text file into a LIST OF LISTS'''

def fill_list():
    '''open the files and put the contents into a list of lists'''
    local_list = []
    text_file = open("core.txt", "r")

    for line in text_file:
        entry = line.split('|')
        # strip whitespace, convert cost and weight to float
        entry[0] = entry[0].strip()
        entry[1] = entry[1].strip()
        entry[2] = float(entry[2])
        entry[3] = float(entry[3])

        local_list.append(entry)
 
    text_file.close()
    
    return local_list


inventory = fill_list()

for entry in inventory:
    print(entry[0])
    
print("Done...")
