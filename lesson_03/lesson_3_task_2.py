from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy S300", "+79654824931"),
    Smartphone("Apple", "iPhone 10", "+79648135201"),
    Smartphone("Infinix", "Not 40", "+79246348955"),
    Smartphone("OPPO", "A 20", "+79945471151"),
    Smartphone("POCCO", "F 16", "+79145889771")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")