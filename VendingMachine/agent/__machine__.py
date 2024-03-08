

# Reglas: {"moneda": "pedir-codigo",
# 	"c1": "servir-refresco-1",
# 	"c2": "servir-refresco-2",
# 	"c3": "servir-refresco-3"}

class MachineAgent:

    def __init__(self, state, action):
        self.state = state
        self.action = action

        self.rules = {
            "sin-moneda": "pedir-moneda",
            "recibi-moneda": "pedir-codigo",
            "servido-c1": "servir-c1-esperar",
            "servido-c2": "servir-c2-esperar",
            "servido-c3": "servir-c3-esperar"
        }

        self.actions = {
            "pedir-moneda": "Pedir moneda",
            "pedir-codigo": "Pedir codigo",
            "servir-c1-esperar": "Sirviendo refresco 1 y esperar",
            "servir-c2-esperar": "Sirviendo refresco 2 y esperar",
            "servir-c3-esperar": "Sirviendo refresco 3 y esperar"
        }

        self.model = {
            ('sin-moneda', 'pedir-moneda'): "recibi-moneda",
            ('sin-moneda', 'pedir-moneda', "moneda"): "recibi-moneda",
            ('recibi-moneda', 'pedir-codigo', 'moneda'): "recibi-moneda",
            ('recibi-moneda', 'pedir-codigo', 'c1'): "servido-c1",
            ('recibi-moneda', 'pedir-codigo', 'c2'): "servido-c2",
            ('recibi-moneda', 'pedir-codigo', 'c3'): "servido-c3",
            ('servido-c1', 'servir-c1-esperar', 'servido'): "sin-moneda",
            ('servido-c2', 'servir-c2-esperar', 'servido'): "sin-moneda",
            ('servido-c3', 'servir-c3-esperar', 'servido'): "sin-moneda"
        }

    def update_state(self, state, action, perception):
        print("========================")
        print(F"({state}, {action}, {perception}) : {self.model.get((state, action, perception), None)}")
        print("========================")
        if self.model.get((state, action, perception), None):
            return self.model.get((state, action, perception), None)
        else:
            return "sin-moneda"

    def getRule(self, state):
        return self.rules[state]

    def rule_action(self, perception, state):
        if perception in self.rules:
            return self.rules[perception]
        else:
            return self.rules["moneda"]