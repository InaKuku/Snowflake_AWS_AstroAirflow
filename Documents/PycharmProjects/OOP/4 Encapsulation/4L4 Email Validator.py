class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def validate(self, email):
        self.name = email[:email.index("@")]
        self.mail = email[email.index("@") + 1:email.index(".")]
        self.domain = email[email.index(".") + 1:]
        if self.__is_name_valid(self.name) and self.__is_mail_valid(self.mail) and self.__is_domain_valid(self.domain):
            return True
        return False

    def __is_name_valid(self, name):
        if len(name) >= self.min_length:
            return True
        return False

    def __is_mail_valid(self, mail):
        for ml in self.mails:
            if ml == mail:
                return True
        return False

    def __is_domain_valid(self, domain):
        for dm in self.domains:
            if dm == domain:
                return True
        return False



mails = ["gmail", "softuni"]
domains = ["com", "bg", "co.uk"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("georgios@gmail.co.uk"))
