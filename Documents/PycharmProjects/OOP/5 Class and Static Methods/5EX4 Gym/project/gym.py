class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if not customer in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if not trainer in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if not equipment in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if not plan in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if not subscription in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        a=5
        result = ""
        subsc = [subs for subs in self.subscriptions if subs.id == subscription_id]
        if len(subsc) > 0:
            result += f"{subsc[0]}"
            cstmer = [cstmer for cstmer in self.customers if subsc[0].customer_id == cstmer.customer_id]
            if len(cstmer) > 0:
                result += f"\n{cstmer[0]}"
                trnr = [trnr for trnr in self.trainers if subsc[0].trainer_id == trnr.id]
                if len(trnr) > 0:
                    result += f"\n{trnr[0]}"
                    exc_plan = [exc_plan for exc_plan in self.plans if exc_plan.trainer_id == trnr[0].id]
                    if len(exc_plan) > 0:
                        equi = [equi for equi in self.equipment if equi.id == exc_plan[0].equipment_id]
                        if len(equi) >  0:
                            result += f"\n{equi[0]}"
                            result += f"\n{exc_plan[0]}"
        return result

