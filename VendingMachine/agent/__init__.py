import time
import threading

from agent.__machine__ import MachineAgent


def run_agent():
    thread1 = threading.Thread(target=main())
    thread1.start()
    thread1.join()


def main():
    # global perception
    state = 'sin-moneda'
    action = 'pedir-moneda'
    perception = None
    machine = MachineAgent(state, action)
    while True:
        try:
            print("Ingrese percepcion")
            perception = input()

            state = machine.update_state(state,action,perception)
            rule = machine.getRule(state)
            action = rule
            txtAction = machine.actions.get(action)
            print(txtAction)
            print("")
            time.sleep(2)
        except KeyboardInterrupt:
            print("")


def showRules():
    print("\n")
    print("+--------------------+")
    print("| Percepciones       |")
    print("+--------------------+")
    print("| moneda:            |")
    print("| c1:                |")
    print("| c2:                |")
    print("| c3:                |")
    print("| servido:           |")
    print("+--------------------+\n")


run_agent()
