# 2 Lab
# Classes and Objects

# Create a class called Smartphone. Upon initialization it should receive a memory (number). It should also have 2 other instance attributes: apps (empty list by default) and is_on (False by default). Create 3 methods:
# ⦁	power() - sets is_on on True if the phone is off, otherwise sets it to False
# ⦁	install(app, app_memory)
# ⦁	If there is enough memory on the phone and it is on, install the app (add it to apps and decrease the memory of the phone) and return "Installing {app}"
# ⦁	If there is enough memory, but the phone is off, return "Turn on your phone to install {app}"
# ⦁	Otherwise return "Not enough memory to install {app}"
# ⦁	status() - returns "Total apps: {total_apps_count}. Memory left: {memory_left}"

class Smartphone:
    def __init__(self, memory: int):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        if self.is_on:
            self.is_on = False
        else:
            self.is_on = True

    def install(self, app, app_memory):
        if self.memory >= app_memory:
            if self.is_on == True:
                self.apps.append(app)
                self.memory -= app_memory
                return f"Installing {app}"
            else:
                return f"Turn on your phone to install {app}"
        else:
            return f"Not enough memory to install {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())