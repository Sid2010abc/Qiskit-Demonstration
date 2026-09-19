# Qiskit Demo

This is an interactive command-line experience that teaches the three most fundamental quantum gates by framing them as pages from the notebook of David Deutsch, the physicist who wrote the first formal description of a quantum computer and co-developed the Deutsch-Jozsa algorithm, one of the earliest proofs that quantum computers can outperform classical ones on certain problems.

Rather than presenting gates as abstract matrices, the demo runs a real, if intentionally minimal, quantum circuit for each concept using Qiskit and executes it on Aer, IBM's local quantum circuit simulator. Each experiment builds a `QuantumCircuit`, applies a single gate, measures the result, transpiles it for the simulator's backend, and runs it for one shot, mirroring the actual workflow used to run circuits on real quantum hardware through Qiskit, just scaled down to a single measurement rather than a full shot distribution.

The three experiments map directly onto core quantum computing vocabulary. The Hadamard gate experiment demonstrates superposition, putting a single qubit into an equal combination of the |0> and |1> states before measurement collapses it to one classical outcome. The Pauli-X gate experiment demonstrates a basis flip, the quantum equivalent of a classical NOT gate. The final experiment scales up to three qubits, each put into superposition independently, illustrating how the state space of a multi-qubit system grows to represent many simultaneous possibilities.

As a framing device, each successful run reveals a fragment of a hidden word, and completing all three experiments spells out "DEUTSCH," followed by a short biographical passage about him. The reveal text itself is fixed rather than derived from the measured bitstring, so the narrative payoff is decoupled from the actual measurement outcome. If you want a version where the revealed content depends on what the simulator actually measures, that would be a natural next step to build on top of this.

Features:
- Three progressively introduced quantum circuits: Hadamard (superposition), Pauli-X (bit flip), and a three-qubit multi-Hadamard circuit
- Real circuit construction, transpilation, and execution via Qiskit and Qiskit Aer
- ASCII circuit diagrams printed directly from Qiskit's built-in circuit drawer
- A short biographical narrative about David Deutsch delivered as a typewriter-style terminal animation
- Simple menu-driven CLI loop, no external UI framework

Tech:
- Python 3
- `qiskit`
- `qiskit-aer`

Usage: install dependencies with `pip install qiskit qiskit-aer`, then run the file and follow the menu prompts to step through each experiment.
