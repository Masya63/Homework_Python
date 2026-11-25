from address import Address
from mailing import Mailing

to_address = Address(482169, "Барнаул", "Ленина", 28, 7)
from_address = Address(698741, "Тверь", "Пушкинская", 11, 88)

mail = Mailing(to_address = to_address, from_address = from_address, cost = 928, track = "JHGYU982FPL2")

print(f"Отправление {mail.track} из {mail.to_address.formatted()} в {mail.from_address.formatted()}. Стоимость {mail.cost} рублей.")