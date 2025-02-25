list = []

def bill(name, height, age, wants_photos):
    if int(height) <= 120:
        print(f"Applicant {name} with age {age} and height {height} cannot ride.")
        return -1
    else:
        applicant_bill = 0

        match age:
            case age if age < 12:
                applicant_bill += 5
            case age if age < 18:
                applicant_bill += 7
            case age if age >= 18:
                if age in range(45,56):
                    applicant_bill += 0
                else:
                    applicant_bill += 12

        if wants_photos.lower() == 'y':
            applicant_bill += 3

        return applicant_bill

while True:
    print('Enter your details')
    name = input("Name: ")
    height = input("Height: ")
    age = int(input("Age: "))
    wants_photos = input("Wants photos (Y/N): ")

    total_bill = bill(name, height, age, wants_photos)

    if total_bill>=0:
       identity = {'name': name, 'height': height, 'age': age, 'wants_photos': wants_photos, 'total_bill': total_bill}
       list.append(identity)

    o = input("Do you want to continue (Y/N): ")

    if o == 'N' or o == 'n':
        break

print("User Details:", list)
