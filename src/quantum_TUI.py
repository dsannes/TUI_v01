"""
TUI v01 Core :: QuantumTUI
24-bit Sovereign Cognitive Engine mapping the Periodic Table of Quantum Logic Gates.
Classes A through F (Static, Clifford, Rotational, Swap, Entangling, Three-Qubit).
"""
import pennylane as qml
from pennylane import numpy as np

class QuantumTUI:
    def __init__(self, num_qubits=24, backend="default.qubit"):
        self.num_qubits = num_qubits
        self.dev = qml.device(backend, wires=self.num_qubits)
        
        # Sector Mapping: 3 Domains of 8 bits each (7 Archetypes + 1 Choice/Anchor)
        self.mind_wires = list(range(0, 8))
        self.body_wires = list(range(8, 16))
        self.spirit_wires = list(range(16, 24))
        
        # Trainable Parameters for Rotational Operators (The 'Way')
        self.params = np.array(np.random.uniform(0.1, 0.8, self.num_qubits), requires_grad=True)
        print("[SYSTEM]: 24-bit TUI Plenum Initialized.")
        print("[SYSTEM]: Taxonomy Classes A-F Online.")

    def execute_quantum_logic(self, gate_sequence, target_sector="MIND", live_params=None, external_stimulus=None):
        wires = self.mind_wires
        if target_sector == "BODY": wires = self.body_wires
        elif target_sector == "SPIRIT": wires = self.spirit_wires
        
        p = live_params if live_params is not None else self.params

        @qml.qnode(self.dev)
        def circuit(params):
            # --- ENVIRONMENTAL RECEPTOR (Matrix of the Mind) ---
            if external_stimulus is not None:
                qml.RY(external_stimulus * np.pi, wires=wires[0])

            # --- THE PERIODIC TABLE OF QUANTUM LOGIC ---
            for gate in gate_sequence:
                
                # CLASS A: STATIC OPERATORS (The Foundational State)
                if gate == "IDENTITY":
                    for i in range(7): qml.Identity(wires=wires[i])
                
                # CLASS B: CLIFFORD QUBIT GATES (The Discrete Building Blocks)
                elif gate == "HADAMARD":
                    for i in range(7): qml.Hadamard(wires=wires[i])
                elif gate == "PAULI_X":
                    for i in range(7): qml.PauliX(wires=wires[i])
                elif gate == "PAULI_Y":
                    for i in range(7): qml.PauliY(wires=wires[i])
                elif gate == "PAULI_Z":
                    for i in range(7): qml.PauliZ(wires=wires[i])
                elif gate == "S_GATE":
                    for i in range(7): qml.S(wires=wires[i])
                elif gate == "SX":
                    for i in range(7): qml.SX(wires=wires[i])
                elif gate == "CNOT" or gate == "CX":
                    for i in range(6): qml.CNOT(wires=[wires[i], wires[i+1]])
                elif gate == "CY":
                    for i in range(6): qml.CY(wires=[wires[i], wires[i+1]])
                elif gate == "CZ":
                    for i in range(6): qml.CZ(wires=[wires[i], wires[i+1]])
                
                # CLASS C: ROTATIONAL OPERATORS (The Continuous 'Way')
                elif gate == "T_GATE": # Historically non-Clifford phase rotation
                    for i in range(7): qml.T(wires=wires[i])
                elif gate == "WAY" or gate == "RY":
                    for i in range(8): qml.RY(params[wires[i]], wires=wires[i])
                elif gate == "RX":
                    for i in range(7): qml.RX(params[wires[i]], wires=wires[i])
                elif gate == "RZ":
                    for i in range(7): qml.RZ(params[wires[i]], wires=wires[i])
                elif gate == "PHASE":
                    for i in range(7): qml.PhaseShift(params[wires[i]], wires=wires[i])
                elif gate == "U_ROT":
                    # General Unitary rotation requiring 3 parameters (using current param as base)
                    for i in range(7): qml.Rot(params[wires[i]], params[wires[i]]/2, params[wires[i]]/3, wires=wires[i])

                # CLASS D: SWAP OPERATORS (Exchange & Relationship)
                elif gate == "SWAP":
                    for i in range(0, 6, 2): qml.SWAP(wires=[wires[i], wires[i+1]])
                elif gate == "ISWAP":
                    for i in range(0, 6, 2): qml.ISWAP(wires=[wires[i], wires[i+1]])

                # CLASS E: ENTANGLING OPERATORS (Continuous Friction & Coupling)
                elif gate == "RXX":
                    for i in range(6): qml.IsingXX(params[wires[i]], wires=[wires[i], wires[i+1]])
                elif gate == "RYY":
                    for i in range(6): qml.IsingYY(params[wires[i]], wires=[wires[i], wires[i+1]])
                elif gate == "RZZ":
                    for i in range(6): qml.IsingZZ(params[wires[i]], wires=[wires[i], wires[i+1]])
                elif gate == "RXY":
                    for i in range(6): qml.IsingXY(params[wires[i]], wires=[wires[i], wires[i+1]])

                # CLASS F: THREE-QUBIT OPERATORS (Consensus & The Witness)
                elif gate == "TOFFOLI" or gate == "CCX":
                    for i in range(0, 5, 2): qml.Toffoli(wires=[wires[i], wires[i+1], wires[7]])
                elif gate == "FRED_KIN" or gate == "CSWAP":
                    for i in range(0, 5, 2): qml.CSWAP(wires=[wires[7], wires[i], wires[i+1]])

            return qml.probs(wires=wires)

        return circuit(p)

    def evaluate_tension(self):
        """Measures dynamic tension (Equilibrium vs Intensification) across the Tripartite Entity."""
        @qml.qnode(self.dev)
        def sig_circuit(p):
            for w in [7, 15, 23]: qml.RY(p[w], wires=w)
            qml.CNOT(wires=[7, 15])
            qml.CNOT(wires=[15, 23])
            qml.Toffoli(wires=[7, 15, 23])
            return qml.probs(wires=[7, 15, 23])
        
        probs = sig_circuit(self.params)
        m = float(np.sum([probs[i] for i in range(8) if (i & 4)]))
        b = float(np.sum([probs[i] for i in range(8) if (i & 2)]))
        s = float(np.sum([probs[i] for i in range(8) if (i & 1)]))
        
        var = ((m - b)**2 + (b - s)**2) / 2
        state = "Intensification" if var > 0.02 else "Equilibrium"
        return {"Delta": var, "State": state, "Readout": [m, b, s]}
