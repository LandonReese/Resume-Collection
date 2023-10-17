import os
import random
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Inventory.settings")
django.setup()

from students.models import Student
from instruments.models import Instrument

def createStudent(student_first_name: str, student_last_name: str, student_address: str, 
                  student_city: str, student_state: str, student_zip: int, 
                  student_phone: int, student_notes: str) -> Student:
    
    student = Student(firstname=student_first_name, lastname = student_last_name, 
                address=student_address, city=student_city, state=student_state,
                zip=student_zip, phone=student_phone, notes=student_notes)
    return student

def createInstrument(instrument_type: str, instrument_serial_number: str, 
                     instrument_maker: str, notes: str) -> Instrument:
    # Create a new Instrument object with the provided data
    instrument = Instrument(type=instrument_type, serial_num=instrument_serial_number, 
                            maker=instrument_maker, notes=notes)
    return instrument

def addRandomStudent():
    """add a random student to the database"""
    firstnames = [
        "Adam", "Alice", "Amélie", "Antoine", "Aurélie", "Baptiste", "Camille", "Céline", "Charlène", "Charlotte",
        "Clara", "Damien", "Éléonore", "Élodie", "Emmanuel", "Eva", "Félix", "Florian", "Gabriel", "Hugo",
        "Inès", "Jade", "Jeanne", "Julie", "Julien", "Léa", "Léo", "Léonie", "Lola", "Lucas",
        "Lucie", "Manon", "Marie", "Mathieu", "Mathilde", "Maxime", "Mélissa", "Morgane", "Nathan", "Noémie",
        "Océane", "Paul", "Pauline", "Quentin", "Raphaël", "Romane", "Samuel", "Sarah", "Sophie", "Théo",
        "Tom", "Valentin", "Valérie", "Victor", "Vincent", "Yann", "Yasmine", "Yves", "Zoé", "Adèle",
        "Alexandre", "Anaïs", "Anthony", "Arthur", "Aurélien", "Benoît", "Camélia", "Caroline", "Cécile", "Cédric",
        "Chloé", "Christophe", "Coralie", "David", "Éric", "Estelle", "Étienne", "Eugénie", "Fabien", "Fanny",
        "Frédéric", "Gaël", "Géraldine", "Guillaume", "Isabelle", "Jérémie", "Jessica", "Jonathan", "Julia", "Laëtitia",
        "Laura", "Loïc", "Lorraine", "Louise", "Marianne", "Mélodie", "Nicolas", "Olivier", "Patricia", "Pierre",
        "Romain", "Sandrine", "Sébastien", "Sylvie", "Thomas", "Tristan", "Valentine", "Xavier"
    ]

    lastnames = [
        "Adam", "Alonso", "André", "Arnaud", "Aubert", "Barbier", "Beauvais", "Blanc", "Boucher", "Boulanger",
        "Bourgeois", "Brun", "Caron", "Chevalier", "Clement", "Colin", "David", "Denis", "Deschamps", "Dufour",
        "Dupont", "Dupuis", "Durand", "Fabre", "Faure", "Fernandez", "Fontaine", "Fournier", "Garcia", "Garnier",
        "Gauthier", "Girard", "Gonzalez", "Guerin", "Guillaume", "Henry", "Hubert", "Jacquet", "Jean", "Lambert",
        "Lefebvre", "Lefevre", "Lemaire", "Lemoine", "Leroy", "Lopez", "Marchand", "Martin", "Mercier", "Meyer",
        "Michel", "Moreau", "Morin", "Muller", "Nguyen", "Noel", "Perrot", "Perrin", "Petit", "Philippe",
        "Picard", "Pierre", "Renaud", "Rey", "Richard", "Robert", "Robin", "Roche", "Roger", "Rolland",
        "Roussel", "Rousseau", "Sanchez", "Simon", "Thomas", "Vidal", "Vincent", "Weber"
    ]


    cities = [
        "Austin", "Dallas", "Houston", "San Antonio", "Fort Worth", 
        "El Paso", "Arlington", "Plano", "Lubbock", "Irving", 
        "Corpus Christi", "Amarillo", "Laredo", "Garland", "McAllen", 
        "Killeen", "Frisco", "Brownsville", "McKinney", "Mesquite"
    ]

    states = [
        "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
        "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho",
        "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
        "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
        "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
        "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota",
        "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
        "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington",
        "West Virginia", "Wisconsin", "Wyoming"
    ]

    firstname = random.choice(firstnames)
    lastname = random.choice(lastnames)
    address = random.randint(0, 9999)
    city = random.choice(cities)
    state = random.choice(states)
    zipcode = random.randint(10000, 99999)
    phone = random.randint(1000000000, 9999999999)
    notes = ""

    student = createStudent(firstname, lastname, address, city, state, zipcode, phone, notes)
    student.save()

def addRandomInstrument():
    types = [
        "Piccolo", "Flute", "Clarinet", "Bass Clarinet", "Alto Saxophone", 
        "Tenor Saxophone", "Baritone Saxophone", "Oboe", "Bassoon", "Trumpet", 
        "Flugelhorn", "Horn", "Mellophone", "Euphonium", "Trombone", "Tuba", "Percussion"
    ]

    makers = [
        "AKAI", "Armstrong", "Audio-Technica", "Bach", "Buffet Crampon", 
        "Casio", "Cannonball", "Conn-Selmer", "Epiphone", "ESP", "Fender", 
        "Gemeinhardt", "Gibson", "Gon Bops", "Gretsch", "Gretsch Drums", 
        "Gretsch Guitars", "Getzen", "Holton", "Ibanez", "Jupiter", 
        "King", "Korg", "Kurzweil", "Latin Percussion (LP)", "Ludwig", 
        "Mapex", "Martin", "Meinl Cymbals", "Meinl Percussion", "Nord", 
        "Novation", "Pearl", "Remo", "Rickenbacker", "Roland", "Sabian", 
        "Schecter", "Sennheiser", "Selmer", "Shure", "Sonor", "Sonor Drums", 
        "Taylor", "Tama", "Vic Firth", "Vox", "Warwick", "Yamaha", "Yamaha Drums", 
        "Zildjian"
    ]

    type = random.choice(types)
    serial_num = random.randint(1000, 999999)
    maker = random.choice(makers)
    notes = ""
    instrument = createInstrument(type, serial_num, maker, notes)
    instrument.save()

def main():
    amount_of_students = 300
    amount_of_instruments = 450

    for _ in range(0, amount_of_students):
        addRandomStudent()

    print(f"Added {amount_of_students} students to the database")

    for _ in range(0, amount_of_instruments):
        addRandomInstrument()

    print(f"Added {amount_of_instruments} instruments to the database")

main()

# id = models.AutoField(primary_key=True)
# firstname = models.CharField(max_length=50)
# lastname = models.CharField(max_length=50)
# address = models.CharField(max_length=50)
# city = models.CharField(max_length=50)
# state = models.CharField(max_length=50)
# zip = models.IntegerField()
# phone = models.IntegerField()
# notes = models.CharField(max_length=200)

# id = models.AutoField(primary_key=True, blank=False)
# type = models.CharField(max_length=50, blank=False)
# serial_num = models.CharField(max_length=50, blank=True)
# maker = models.CharField(max_length=50, blank=False)
# notes = models.CharField(max_length=200, blank=True)