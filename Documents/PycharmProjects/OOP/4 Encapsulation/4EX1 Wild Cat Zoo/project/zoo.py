from _collections import deque

class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity > len(self.animals):
            if self.__budget >= price:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {type(animal).__name__} added to the zoo"
            else:
                return "Not enough budget"
        else:
            return "Not enough space for animals"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        else:
            return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for wrker in self.workers:
            if wrker.name == worker_name:
                self.workers.remove(wrker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_of_salaries = 0
        for wrk in self.workers:
            sum_of_salaries += wrk.salary
        if self.__budget >= sum_of_salaries:
            self.__budget -= sum_of_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        care_for_animals = 0
        for anim in self.animals:
            care_for_animals += anim.money_for_care
        if self.__budget >= care_for_animals:
            self.__budget -= care_for_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = []
        cheetah = []
        tigers = []
        for anim in self.animals:
            if type(anim).__name__ == "Lion":
                lions.append(anim)
            elif type(anim).__name__ == "Tiger":
                tigers.append(anim)
            elif type(anim).__name__ == "Cheetah":
                cheetah.append(anim)
        lions_deq = deque(lions)
        tigers_deq = deque(tigers)
        cheetah_deq = deque(cheetah)
        result = ""
        result += f"You have {len(self.animals)} animals\n"
        result += f"----- {len(lions)} Lions:\n"
        for l in lions:
            if len(lions_deq) == 1 and len(tigers_deq) == 0 and len(cheetah_deq) == 0:
                result += f"{repr(l)}"
            else:
                result += f"{repr(l)}\n"
            lions_deq.popleft()
        result += f"----- {len(tigers)} Tigers:\n"
        for t in tigers:
            if len(tigers_deq) == 1 and len(lions_deq) == 0 and len(cheetah_deq) == 0:
                result += f"{repr(t)}"
            else:
                result += f"{repr(t)}\n"
            tigers_deq.popleft()
        result += f"----- {len(cheetah)} Cheetahs:\n"
        for ch in cheetah:
            if len(cheetah_deq) == 1 and len(lions_deq) == 0 and len(tigers_deq) == 0:
                result += f"{repr(ch)}"
            else:
                result += f"{repr(ch)}\n"
            cheetah_deq.popleft()
        return result

    def workers_status(self):
        keepers = []
        caretakers = []
        vets = []
        for wrker in self.workers:
            if type(wrker).__name__ == "Keeper":
                keepers.append(wrker)
            elif type(wrker).__name__ == "Caretaker":
                caretakers.append(wrker)
            elif type(wrker).__name__ == "Vet":
                vets.append(wrker)
        keepers_deq = deque(keepers)
        caretakers_deq = deque(caretakers)
        vets_deq = deque(vets)
        result = ""
        result += f"You have {len(self.workers)} workers\n"
        result += f"----- {len(keepers)} Keepers:\n"
        for k in keepers:
            if len(keepers_deq) == 1 and len(caretakers_deq) == 0 and len(vets_deq) == 0:
                result += f"{repr(k)}"
            else:
                result += f"{repr(k)}\n"
            keepers_deq.popleft()
        result += f"----- {len(caretakers)} Caretakers:\n"
        for care in caretakers:
            if len(caretakers_deq) == 1 and len(keepers_deq) == 0 and len(vets_deq) == 0:
                result += f"{repr(care)}"
            else:
                result += f"{repr(care)}\n"
            caretakers_deq.popleft()
        result += f"----- {len(vets)} Vets:\n"
        for vt in vets:
            if len(vets_deq) == 1 and len(caretakers_deq) == 0 and len(keepers_deq) == 0:
                result += f"{repr(vt)}"
            else:
                result += f"{repr(vt)}\n"
            vets_deq.popleft()
        return result


