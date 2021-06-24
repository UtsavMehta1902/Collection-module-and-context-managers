

class contextManager(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):

        if type:
            ##Exception handling code
            print("Exception had occurred, but has been handled")

        self.file_obj.close()
        return True



###############################^^^^^^^^^^^^^^^^^^^^^^CONTEXT MANAGER^^^^^^^^^^^^^^^^^^^^^^^^###################################



from collections import Counter
import json

data = []
with contextManager('KOSS/sample_array.py', 'r') as opened_file:
    
    line = opened_file.readline()

    while True:
        line = opened_file.readline()

        if not line:
            data.pop()
            break

        data.append(line.strip('\', \n\''))

formatted_data = Counter(data)
# print(formatted_data)

with contextManager('KOSS/toBeDictionary.txt', 'w') as empty_file:
    empty_file.write(json.dumps(formatted_data))



#########################^^^^^^^^^^^^^^^^^^^^DATA READ AND WRITTEN TO AN EMPTY FILE^^^^^^^^^^^^^^^^^############################



data_as_dict = {}

with contextManager('KOSS/toBeDictionary.txt', 'r') as dictionary:
    data_as_string = dictionary.read()

    data_as_dict = json.loads(data_as_string)

    word = input("\n\nInput the word for which word count is required: ")
    if word not in data_as_dict:
        print("Not Present\n")
    else:
        print(data_as_dict[word])
        print("\n")



#####################^^^^^^^^^^^^^^^^^READING THE WORD COUNT FROM THE DICTIONARY^^^^^^^^^^^^^^^^^^#############################