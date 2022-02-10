from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from os import system

# Intialize the webdriver
driver = webdriver.Chrome()

# Intialize the data we are going to extract
doctor_names = []
doctor_telephone = []
doctor_address = []
doctor_city = []
doctor_google_pin = []
doctor_speciality = []
doctor_qualification = []
doctor_acts = []
doctor_links = []

# Open the webpage
driver.get('https://www.med.ma/prendre-rdv')

# Clear the terminal
system('cls')

# Accept Cookies
input("Please accept the cookies and press anykey to continue.....")


# Get the result container
results_container = driver.find_element(By.XPATH,'/html/body/div[4]/div/div/section/div/div[1]/div[2]/div')

# Get each container for each doctor
doctors_container = results_container.find_elements(By.CLASS_NAME,'card-doctor-block')

# Get the link for each doctor page
for doctor in doctors_container:
    doctor_links.append(doctor.find_element(By.TAG_NAME,'a').get_attribute('href'))

# Clear the Terminal
system('cls')

# Loop Over each doctor link
for link in doctor_links:

    # Go to the doctor link
    driver.get(link)

    # Get the header container that includes [Name,Speciality,City]
    header_container = driver.find_element(By.CSS_SELECTOR,'#pfmaincontent > div.profile__header > div.col-resp.col-lg-9.col-md-9.col-sm-12.col-xs-12 > div > div.profile__label')
    
    # Get the Doctor Name by getting the text of the H1 Tag inside the header Container
    doctor_names.append(header_container.find_element(By.TAG_NAME,'h1').text)

    # We get the container that has the info of the Doctor [Speciality,City]
    doctor_info = header_container.find_elements(By.TAG_NAME,'div')

    # We will observe that following
    # The First Div will include the city
    doctor_city.append(doctor_info[1].text)

    # The Second Div will include the speciality
    doctor_speciality.append(doctor_info[0].text)

    # Get the doctor address using the class name
    doctor_address.append(driver.find_element(By.CLASS_NAME,'profile__adr').text)
    
    # Google pin and adress will be the same
    doctor_google_pin.append(driver.find_element(By.CLASS_NAME,'profile__adr').text)
    
    # Get the container that has the the phone number button
    phone_container = driver.find_element(By.CLASS_NAME,'profile__btn')

    # If we take a look on the element we will find that the container id is sharedoc and the numbers 
    # are stored in element called meta in the attribute content
    # So we used the xpath to find the element meta inside the button 
    phone_numbers = phone_container.find_element(By.XPATH,'//*[@id="sharedoc"]/div[1]/div[2]/meta').get_attribute('content')
    
    # We check if the length is larger than 25 so there will be more than 1 telephone 
    # and by observing the code we will observe that they are separated by /
    # if there is only one number we will create a list that includes this number only
    # Why list? to keep on the data type of the whole list
    if len(phone_numbers) > 25:
        numbers = phone_numbers.split('/')
    else:
        numbers = [phone_numbers]
    doctor_telephone.append(numbers)
    

    # We check the qualifications and if there isn't any we add NA
    try:

        doctor_qualification.append(driver.find_element(By.XPATH,'/html/body/div[4]/div[2]/div[2]/div/div/div[1]/div[3]/div[2]/p[2]').text)
    except:
        doctor_qualification.append("NA")
    
    # We check the acts and cares section and if there isn't any we add NA
    try:

        acts_container = driver.find_element(By.XPATH,'/html/body/div[4]/div[2]/div[2]/div/div/div[1]/div[3]/div[2]/span')
        acts = [ac.text for ac in acts_container.find_elements(By.TAG_NAME,'a')]
        doctor_acts.append(acts)
    except:
        doctor_acts.append(["NA"])
    
    sleep(2)

# Close the Driver
driver.close()

# Clear the terminal to be ready for the output
system('cls')

# Output the results 
for i in range(len(doctor_names)):
    print(f"Doctor Name: {doctor_names[i]}")
    print(f'Doctor Speciality: {doctor_speciality[i]}')
    print(f'Doctor City: {doctor_city[i]}')
    print("Doctor Telephone:")
    for number in doctor_telephone[i]:
        print(f'- {number}')
    print(f"Doctor Qualifications: {doctor_qualification[i]}")
    print("Doctor Acts and Care: ")
    print("|".join(doctor_acts[i]))
    print("\n\n")
    print("-" * 50)