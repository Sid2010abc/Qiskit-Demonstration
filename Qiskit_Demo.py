import time
import random
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer

def slow_print(message):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.05)

def run(qc):
    sim = Aer.get_backend('aer_simulator')
    compiled = transpile(qc, sim)
    result = sim.run(compiled, shots=1).result()
    return list(result.get_counts().keys())[0]

def reveal_letters(message):
    """Print a message letter by letter with delay"""
    for char in message:
        print(char, end="", flush=True)
    print("\n")

def intro():
    slow_print("\n🌌 You are opening the notebook of an extraordinary thinker...\n")
    time.sleep(1)
    slow_print("David Deutsch, a man whose mind glimpsed the shape of reality itself.\n")
    time.sleep(1)
    slow_print("He saw that the universe isn’t just a single path—but a multitude of possibilities, all coexisting.\n")
    time.sleep(1)
    slow_print("He imagined a machine, a quantum computer, that could explore them all at once.\n")
    time.sleep(1)
    slow_print("Brilliant, daring, and curious beyond measure, he changed the way we understand computation.\n")
    time.sleep(1)
    input("Press ENTER to see his first experiment...\n")

def explain_diagram():
    slow_print("\n📖 HOW TO READ THE CIRCUITS:\n")
    slow_print("""
q_0: ──[ H ]───M──
c_0: ════════════
""")
    slow_print("- q_0 → qubit (quantum coin)\n")
    slow_print("- [ H ] → operation (H gate = spin into both states)\n")
    slow_print("- M → measurement (look at it)\n")
    slow_print("- c_0 → classical bit to store the result\n")
    input("Press ENTER to continue...\n")

def experiment_h(letter):
    slow_print("\n📝 Dave’s Experiment: H gate (Superposition)\n")
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)
    slow_print("Circuit:\n")
    print(qc.draw())
    slow_print("\nDave writes: 'I put the qubit into BOTH 0 and 1. Now I look...'\n")
    input("Press ENTER to run the experiment...\n")
    run(qc)
    print("Secret letter revealed: ", end="")
    reveal_letters(letter)

def experiment_x(letter):
    slow_print("\n📝 Dave’s Experiment: X gate (Flip)")
    qc = QuantumCircuit(1, 1)
    qc.x(0)
    qc.measure(0, 0)
    slow_print("Circuit:\n")
    print(qc.draw())
    slow_print("\nDave writes: 'I flip the qubit. 0 becomes 1 or 1 becomes 0.'\n")
    input("Press ENTER to run the experiment...\n")
    run(qc)
    print("Secret letter revealed: ", end="")
    reveal_letters(letter)

def experiment_multi(letters):
    slow_print("\n📝 Dave’s Experiment: Multiple Qubits (Many possibilities)\n")
    qc = QuantumCircuit(3, 3)
    for i in range(3):
        qc.h(i)
    qc.measure([0,1,2], [0,1,2])
    slow_print("Circuit:\n")
    print(qc.draw())
    slow_print("\nDave writes: 'With multiple qubits, all outcomes exist at once.'\n")
    input("Press ENTER to run the experiment...\n")
    run(qc)
    print("Secret letters revealed: ", end="")
    reveal_letters(letters)

def main():
    intro()
    explain_diagram()

    while True:
        slow_print("\nChoose an experiment from Dave’s notebook:\n")
        slow_print("1. H gate (Superposition)\n")
        slow_print("2. X gate (Flip)\n")
        slow_print("3. Multiple Qubits (Many possibilities)\n")
        slow_print("4. Close notebook\n")

        choice = input("> ")

        if choice == "1":
            # H gate reveals letter D
            experiment_h("DE")
        elif choice == "2":
            # X gate reveals letter E
            experiment_x("UT")
        elif choice == "3":
            # Multi-qubit reveals full word UTS
            experiment_multi("SCH")
        elif choice == "4":
            slow_print("\n🌌 Closing the notebook...\n")
            slow_print("David Deutsch – pioneer of quantum computation.\n")
            print("The letters you uncovered spell his name: ", end="")
            reveal_letters("DEUTSCH")
            slow_print("David Deutsch is an amazing scientist who helped create quantum computers—the kind of super‑fast machines that could solve problems regular computers can’t handle. He grew up loving science, studied at some of the world’s top universities, and eventually became a leading researcher at Oxford. David came up with the first design for a quantum computer and helped invent important ideas like the Deutsch–Jozsa algorithm, which showed how powerful these computers could be. He also writes mind‑stretching books, like The Fabric of Reality and The Beginning of Infinity, where he explains big ideas about the universe in exciting ways. He’s won major science awards, and many people see him as a real‑life explorer of how reality works. He shows kids that curiosity, imagination, and big questions can change the world.")

            break
        else:
            slow_print("That page doesn't exist. Try again.")


if __name__ == "__main__":
    main()
