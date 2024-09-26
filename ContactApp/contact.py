from datetime import datetime

class Contact:
    def __init__(self, last_name, first_name, phone, birth_date, email, vk_id):
        self.last_name = last_name.title()  # Преобразуем первую букву в верхний регистр
        self.first_name = first_name.title()  # Преобразуем первую букву в верхний регистр
        self.phone = self.validate_phone(phone)
        self.birth_date = self.validate_birth_date(birth_date)
        self.email = self.validate_email(email)
        self.vk_id = vk_id

    def validate_phone(self, phone):
        if not phone.isdigit() or len(phone) != 11 or phone[0] != '7':
            raise ValueError("Phone number must start with '7' and contain exactly 11 digits.")
        return phone

    def validate_birth_date(self, birth_date):
        date = datetime.strptime(birth_date, '%Y-%m-%d')
        if date.year < 1900 or date > datetime.now():
            raise ValueError("Birth date must be between 1900 and today.")
        return birth_date

    def validate_email(self, email):
        if len(email) > 50:
            raise ValueError("Email must be less than 50 characters.")
        return email
