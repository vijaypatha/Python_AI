names = ["Boston_terrier_02259.jpg","German_shpeard_02999.jpg"]
new_names = []
for i in range(0, len(names), 1):
    new_names.extend(names[i].split("_"))
    #new_names = names[i].split("_") # this will only give the last item in the list
print(new_names)
pet_labels = ""
for x in new_names:
    if x.isalpha():
        pet_labels += x.lower() + " "
print(pet_labels)
print(type(pet_labels))