# Web-Scraping Project 1

I just need to scrap data from a few websites:
- https://medicament.ma/listing-des-medicaments/
CSV file with each product, and the following columns:
URL (https://medicament.ma/medicament/abilify-15-mg-comprime-2/)
Name
Présentation
Dosage
Princeps
Distributeur ou fabriquant
Composition
Classe thérapeutique
Statut
Code ATC
PPV
Prix hospitalier
PPH
Tableau
Indication(s)
Substance (s) psychoactive (s)

List of Pharmacies from the following website:
http://www.guidedumaroc.com/service-pharmacies-du-maroc.html
For each pharmacie in every city get the following fields:
URL (http://www.guidedumaroc.com/service-pharmacie-1-grande-pharmacie-centre.html)
Name
Adresse
Code postal
Ville
Téléphone

List of pharmacies from the following website:
https://www.med.ma/pharmacie/1
For each pharmacy get the following info in a csv file:
https://www.med.ma/pharmacie/rabat
URL
Name
Address
Téléphone

List of clinics from the following website:
https://www.med.ma/clinique
CSV file with the following columns
URL (https://www.med.ma/clinique/beni-mellal/clinique-assalam--361)
Name
Type (Clinique Pluridisciplinaire)
telephone
address
google pin


List of doctors:
https://www.med.ma/prendre-rdv
Name
Telephone
Address
Ville (city)
google pin
Spécialités
Qualification professionnelle
Actes et soins (| separated)

List of Labs from the following website:
https://www.med.ma/medecin/laboratoire-danalyses-de-biologie-medicale
CSV file with the following columns:
URL (https://www.med.ma/medecin/laboratoire-danalyses-de-biologie-medicale/casablanca/dr-machmachi-hanae-laboratoire-anfa-lab-208488)
Name
Type (Laboratoire d'analyses de biologie médicale)
Spécialités
telephone
addresse
ville
google pin
Qualification professionnelle
Actes et soins (| separated)

Ideally end result would be:
- CSV files with the data from the all the websites listed
- Code used to scrap and a small explanation of how to rerun it in the future
