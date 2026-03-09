# Table of Quantum Logic Gates — Archetypal Taxonomy
## A Semantic Framework Using the Seven Prime Archetypes

---

> **Methodological Note:** The Seven Prime Archetypes — Matrix, Potentiator, Catalyst, Experience,
> Significator, Transformation, and Way — function throughout this document as a *semantic descriptive
> layer* applied to quantum logic gates. They are not redefinitions of quantum mechanical concepts but
> a structured interpretive framework through which the operational character of each gate is rendered
> in relatable, philosophically coherent language. Each archetype illuminates a distinct dimension of
> a gate's identity: its foundational substrate, its latent potential, its mechanism of action, its
> observable signature, its formal representation, its transformational character, and its governing
> operational principle.

---

## Taxonomy Structure

**Total Entities:** 39 gate entities across 6 classes and 8 subgroups

| Class | Name | Entities |
|-------|------|----------|
| Foundational | Quantum Logic & Quantum Logic Gates | 1–2 |
| Class A | Static Operators | 3–4 |
| Class B | Clifford Qubit Gates | 5–14 |
| Class C | Rotational Operators | 15–23 |
| Class D | Swap Operators | 24–28 |
| Class E | Entangling Operators | 29–34 |
| Class F | Three-Qubit Operators | 35–39 |

**Excluded Gates (hardware-specific / implementation-dependent):**
Sycamore, Echoed Cross Resonance, Dagwood Bumstead, Fermionic-Fredkin, Fermionic Simulation

**Note:** The Feynman gate is incorporated into Entity 12 (CNOT) as a notation variant.

---

## The Seven Prime Archetypes

| Archetype | Dimension |
|-----------|-----------|
| **Matrix** | The foundational substrate — the state space, reference frame, or structural ground within which the gate operates |
| **Potentiator** | The latent potential — the complete range of operational possibilities held within the gate |
| **Catalyst** | The mechanism of action — the role the gate plays in enabling or triggering quantum computational processes |
| **Experience** | The observable signature — the measurable effects and phenomenological character of the gate's action |
| **Significator** | The formal representation — the mathematical object that most completely identifies the gate |
| **Transformation** | The transformational character — the specific change the gate enacts upon the quantum state |
| **Way** | The governing principle — the operational discipline or structural law that defines the gate's deepest identity |

---

---

# FOUNDATIONAL ENTITIES

---

## Entity 1: Quantum Logic

**The Matrix of Quantum Logic**
The Hilbert space — the complex vector space equipped with an inner product that forms the mathematical substrate of all quantum mechanical states. Every qubit exists as a vector in this space; every gate operates as a transformation within it.

**The Potentiator of Quantum Logic**
The superposition principle — the capacity of quantum systems to exist in linear combinations of basis states simultaneously, enabling the exponential parallelism that distinguishes quantum from classical computation.

**The Catalyst of Quantum Logic**
Quantum gates as unitary operators — the discrete transformations that drive state evolution, generate entanglement, and produce the interference patterns through which quantum algorithms achieve computational advantage.

**The Experience of Quantum Logic**
Measurement — the irreversible collapse of quantum superposition into a definite classical outcome, the singular moment at which the quantum computation yields an observable result.

**The Significator of Quantum Logic**
Entanglement — the non-classical correlation between qubits that has no classical analog, the resource that enables quantum computational tasks provably impossible for classical systems.

**The Transformation of Quantum Logic**
Unitary state evolution — the reversible, norm-preserving transformation of quantum states through the sequential application of quantum gate operations in a quantum circuit.

**The Way of Quantum Logic**
Reversibility and unitarity — the structural requirement that all quantum gate operations preserve the total probability of the quantum state, distinguishing quantum logic from classical Boolean logic through the conservation of quantum information.

### Narrative

Quantum logic is the formal framework governing the processing of quantum information — a framework that is structurally distinct from classical Boolean logic in every fundamental respect. Where classical Boolean logic operates on definite binary values and irreversible logical operations, quantum logic operates on quantum states existing in superpositions of basis values and reversible unitary transformations that preserve all information throughout the computation. The mathematical substrate of quantum logic is the Hilbert space — a complex vector space equipped with an inner product — within which quantum states are represented as unit vectors and quantum gate operations are represented as unitary matrices. The defining computational resource of quantum logic is superposition — the capacity of quantum systems to exist in linear combinations of basis states simultaneously — combined with entanglement — the non-classical correlations between quantum systems that have no classical analog — and interference — the constructive and destructive combination of quantum probability amplitudes that enables quantum algorithms to suppress incorrect answers and amplify correct ones. Quantum logic is not a replacement for classical Boolean logic but its most complete generalization: classical logic is recoverable as the special case of quantum logic restricted to computational basis states and measurement outcomes, while the full quantum logical framework encompasses an exponentially richer operational space that forms the foundation of quantum computational advantage.

---

## Entity 2: Quantum Logic Gates

**The Matrix of Quantum Logic Gates**
The complete space of unitary transformations on the n-qubit Hilbert space — the full operational space within which all possible quantum gate operations are defined and within which every quantum circuit is constructed.

**The Potentiator of Quantum Logic Gates**
The amplitude alteration capacity of each gate — the specific range of quantum state transformations accessible through a single gate application, from the null transformation of the identity to the complete state space rotations of maximally entangling multi-qubit gates.

**The Catalyst of Quantum Logic Gates**
Gate application — the physical operation that applies a specific unitary transformation to one or more qubits, advancing the quantum computation from one state to the next and building up the complex quantum state transformations required by quantum algorithms through sequential gate applications.

**The Experience of Quantum Logic Gates**
Statistical measurement outcomes — the probability distributions over computational basis measurement results that constitute the observable output of quantum gate operations on quantum states.

**The Significator of Quantum Logic Gates**
The unitary matrix representation — the complete mathematical descriptor of each gate's action, a square complex matrix satisfying U†U = I that encodes the complete transformation of every quantum state under the gate's application.

**The Transformation of Quantum Logic Gates**
Sequential circuit operations — the ordered application of quantum gates in a quantum circuit that progressively transforms an initial quantum state through a designed sequence of unitary operations to produce a final state whose measurement outcomes encode the result of the quantum computation.

**The Way of Quantum Logic Gates**
The unitarity requirement — the structural constraint that every quantum gate must be represented by a unitary matrix, ensuring the reversibility of quantum computation and the conservation of total quantum state probability throughout every stage of the quantum circuit.

### Narrative

Quantum logic gates are the primitive vocabulary of quantum circuits — the discrete unitary transformations that act on individual qubits or groups of qubits to progressively transform an initial quantum state into a final state whose measurement outcomes encode the result of a quantum computation. Each gate is characterized by a unitary matrix — a square complex matrix satisfying U†U = I — that completely describes the gate's action on the quantum state space of its target qubits. This unitarity condition is the structural foundation of the quantum gate framework: it ensures that quantum gate operations are reversible — every quantum gate has a unique inverse obtained by taking the conjugate transpose of its matrix — and that the total probability of the quantum state is conserved through every gate operation in the circuit. Quantum logic gates are distinguished from their classical Boolean counterparts by three structural properties that have no classical analog: they operate on quantum superpositions rather than definite bit values, they must be reversible rather than potentially irreversible, and they can generate entanglement between multiple qubits through non-local gate operations. These three properties collectively define the quantum gate framework as a strictly more powerful computational model than classical Boolean circuits and establish quantum gates as the operational primitives through which the computational advantages of quantum mechanics are accessed and exploited.

---

---

# CLASS A: STATIC OPERATORS (State & Boundary)

**Class Annotation:** Static Operators are the gates that preserve or fix the logical and phase state of the qubit without rotation, entanglement, or relative phase differentiation. The Identity and Global Phase gates define the operational baseline and boundary conditions of the single-qubit gate framework — the null transformation and the phase equivalence class boundary that together establish the reference frame within which all other gates are defined.

**Prime Archetypal Analysis — Class A**

**Matrix:** The unaltered single-qubit state space organized around computational basis fixed points — |0⟩ and |1⟩ as the invariant reference states of the static operator class.

**Potentiator:** The preserved full superposition potential — every quantum state that enters a Static Operator exits with its complete superposition structure intact, with no reduction of any operational potential.

**Catalyst:** Structural roles in circuit architecture — timing alignment, benchmarking placeholders, and the enabling of controlled gate constructions through global phase promotion to relative phase.

**Experience:** Statistical invariance — no Static Operator changes any measurement outcome probability for any input state, making the entire class experientially invisible in single-qubit computational basis measurements.

**Significator:** Identity matrix and U(1) phase manifold — the 2×2 identity matrix for the Identity gate and the complex scalar e^(iφ) for the Global Phase gate.

**Transformation:** Null transformation with formal acknowledgment — the Identity gate enacts no transformation and the Global Phase gate enacts a transformation that is physically unobservable in isolation.

**Way:** Algebraic closure requirement — the complete single-qubit gate group U(2) requires both the identity element and the global phase manifold for its formal completeness, establishing Static Operators as structurally necessary even where operationally trivial.

---

## Entity 3: Identity Gate

**Gate Annotation:** I (also denoted **Id**, **I gate**) — The single-qubit gate that returns the qubit state exactly unchanged. Represented by the 2×2 identity matrix. Eigenstate of every state. Zero transformation. The multiplicative identity of the unitary group U(2).

$$I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$$

$$I|\psi\rangle = |\psi\rangle \quad \text{for all } |\psi\rangle$$

### Prime Archetypal Analysis

**Matrix:** The unaltered state space — every qubit state is an eigenstate of the identity gate with eigenvalue 1.

**Potentiator:** The fully preserved superposition — the identity gate does not reduce or alter any latent operational potential of the qubit state.

**Catalyst:** Structural placeholder — used in quantum circuits for timing alignment, idle qubit representation, benchmarking reference, and as the formal starting point for gate decomposition algorithms.

**Experience:** Complete statistical invariance — the identity gate produces no change in any measurement outcome probability for any input state.

**Significator:** The 2×2 identity matrix — the multiplicative identity of U(2), the unique matrix satisfying IA = AI = A for all A ∈ U(2).

**Transformation:** Null transformation — the identity gate formally acknowledges the qubit state without enacting any change upon it.

**Way:** Algebraic closure requirement — every complete group requires an identity element, and the identity gate is the required identity element of the single-qubit unitary group U(2).

### Narrative

The Identity gate is the single-qubit gate that returns the qubit state exactly unchanged — the null operation that formally acknowledges the qubit's existence without altering any property of its quantum state. Represented by the 2×2 identity matrix with unit diagonal entries and zero off-diagonal entries, it is the multiplicative identity of the single-qubit unitary group U(2): every other gate composed with the identity gate — in either order — returns that gate unchanged. Every quantum state is an eigenstate of the identity gate with eigenvalue 1, confirming that no state is distinguished or affected by its action. In quantum circuit design the identity gate serves as the formal representation of idle qubit time — the placeholder operation used to indicate that a qubit undergoes no transformation during a given circuit layer — and as the benchmarking reference from which gate error is measured through randomized benchmarking protocols. Its algebraic necessity as the identity element of U(2) establishes the identity gate as structurally fundamental even where operationally trivial.

---

## Entity 4: Global Phase Gate

**Gate Annotation:** e^(iφ) (also denoted **global phase**, **phase factor**) — The single-qubit gate that applies a uniform scalar phase factor e^(iφ) to the entire qubit state vector. Physically unobservable in isolation. Formally required for the completeness of U(2). Becomes a physically significant relative phase in controlled gate constructions.

$$e^{i\phi}I = \begin{pmatrix} e^{i\phi} & 0 \\ 0 & e^{i\phi} \end{pmatrix}$$

$$e^{i\phi}|\psi\rangle = e^{i\phi}|\psi\rangle \quad \text{(physically equivalent to } |\psi\rangle \text{ in isolation)}$$

### Prime Archetypal Analysis

**Matrix:** The projective Hilbert space equivalence class — the set of all state vectors differing only by a global phase factor that are physically identical in all single-qubit measurement contexts.

**Potentiator:** The full phase angle range [0, 2π) — the complete continuous family of global phase factors accessible through this gate, spanning the full U(1) manifold.

**Catalyst:** The enabler of controlled gate constructions — when the global phase gate appears as the target of a controlled operation, the global phase becomes a relative phase between control qubit branches and is physically significant.

**Experience:** Complete measurement invariance — the global phase gate produces no change in any measurement outcome probability for any input state in any measurement basis.

**Significator:** The complex scalar e^(iφ) on the U(1) manifold — the group of unit-modulus complex numbers that forms the global phase degree of freedom of the single-qubit unitary group.

**Transformation:** Uniform complex plane rotation — the global phase gate rotates the entire state vector uniformly in the complex plane without altering any relative phase between basis components.

**Way:** Formal completeness over operational minimalism — the global phase gate is required for the formal completeness of U(2) over SU(2) and for the correct treatment of controlled gate constructions in multi-qubit circuits.

### Narrative

The Global Phase gate applies a uniform scalar phase factor e^(iφ) to the entire qubit state vector — a transformation that is physically unobservable in single-qubit measurement contexts but formally indispensable for the completeness of the single-qubit unitary group and for the correct treatment of controlled gate operations in multi-qubit circuits. The physical unobservability of the global phase in isolation follows from the fact that all measurement outcome probabilities depend on the modulus squared of the state vector amplitudes — |e^(iφ)α|² = |α|² — making the global phase factor e^(iφ) invisible to all single-qubit measurements in all bases. The formal indispensability of the global phase follows from the structure of the single-qubit unitary group U(2): U(2) is the product of SU(2) — the group of 2×2 unitary matrices with determinant 1, parameterized by three real angles — and U(1) — the group of global phase factors e^(iφ) parameterized by one real angle. The global phase gate is the representation of the U(1) factor in this decomposition, and its inclusion is required for the formal completeness of the full unitary group U(2) over the special unitary group SU(2). In multi-qubit circuits, the global phase of a single-qubit gate becomes a relative phase between the branches of a control qubit superposition when the gate is controlled — the controlled-global-phase gate introduces a physically significant phase difference between the |0⟩ and |1⟩ control branches — transforming the physically unobservable global phase of the single-qubit context into a physically significant and measurable relative phase in the two-qubit controlled gate context.

---

---

# CLASS B: CLIFFORD QUBIT GATES

**Class Annotation:** Clifford gates map the Pauli group to itself under conjugation. They are efficiently classically simulable on stabilizer states (Gottesman-Knill theorem). The complete n-qubit Clifford group is generated by the set {H, S, CNOT}. Clifford gates form the foundation of quantum error correction, quantum teleportation, and stabilizer-based quantum computing architectures.

**Prime Archetypal Analysis — Class B**

**Matrix:** The Pauli group and its stabilizer states — the group generated by {I, X, Y, Z} under multiplication, together with the stabilizer states preserved by Clifford group conjugation.

**Potentiator:** Generative completeness — the set {H, S, CNOT} generates the complete n-qubit Clifford group, providing the full operational potential of the Clifford framework from three primitive gates.

**Catalyst:** Error correction and classical simulability — Clifford gates implement the logical operations of stabilizer quantum error correcting codes and define the classical simulability boundary established by the Gottesman-Knill theorem.

**Experience:** Stabilizer state evolution — Clifford gates map stabilizer states to stabilizer states, preserving the classical simulability of the quantum state throughout the computation.

**Significator:** Symplectic representation — every Clifford gate has an exact representation as a symplectic matrix over the two-element field F₂, encoding its action on the Pauli group through binary linear algebra.

**Transformation:** Stabilizer state transformation — the Clifford group acts transitively on the set of stabilizer states, mapping any stabilizer state to any other stabilizer state through an appropriate Clifford circuit.

**Way:** The threshold of quantum advantage — the Clifford group defines the boundary between classically simulable quantum computation and potentially quantum-advantaged computation, with the addition of any non-Clifford gate crossing this boundary.

---

## Subgroup B.1 — Pauli Operators

**Subgroup Annotation:** The three non-identity Pauli operators — X, Y, Z — represent π radian rotations about the three axes of the Bloch sphere and form the non-identity elements of the single-qubit Pauli group. Each Pauli operator is simultaneously unitary, Hermitian, and self-inverse, forming the canonical single-qubit error basis and the generative elements of the Pauli group under multiplication.

---

## Entity 6: Pauli X (NOT, bit flip)

**Gate Annotation:** X (also denoted **σₓ**, **NOT**, **bit flip**) — The single-qubit gate that enacts a π radian rotation about the X-axis of the Bloch sphere. The quantum NOT gate. Maps |0⟩↔|1⟩. Self-inverse: X² = I. Eigenstates: |±⟩.

$$X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$$

$$X|0\rangle = |1\rangle \qquad X|1\rangle = |0\rangle$$

### Prime Archetypal Analysis

**Matrix:** The X-axis of the Bloch sphere as the rotation axis — |±⟩ = (|0⟩ ± |1⟩)/√2 are the eigenstates, the fixed points of X-axis rotation.

**Potentiator:** The complete binary inversion potential — the Pauli X gate can flip any computational basis state to its logical complement.

**Catalyst:** Bit flip error operator and quantum NOT — the primary mechanism of computational basis state inversion and the canonical model of bit flip errors in quantum error correction.

**Experience:** Deterministic outcome inversion — the Pauli X gate always swaps the measurement outcome probabilities of |0⟩ and |1⟩ for any input state.

**Significator:** The anti-diagonal matrix with off-diagonal ones — the 2×2 matrix with entries X₀₁ = X₁₀ = 1 and X₀₀ = X₁₁ = 0.

**Transformation:** π rotation about the X-axis — the Bloch sphere state vector is rotated through π radians about the X-axis, exchanging the north and south poles.

**Way:** The quantum extension of classical NOT — the Pauli X gate restores reversibility to binary logical inversion within the quantum gate framework, implementing the NOT function as a reversible unitary operation.

### Narrative

The Pauli X gate is the quantum NOT gate — the single-qubit gate that maps the computational basis state |0⟩ to |1⟩ and |1⟩ to |0⟩, implementing the binary NOT function as a reversible unitary operation. Represented by the anti-diagonal 2×2 matrix with off-diagonal unit entries, it is simultaneously unitary, Hermitian, and self-inverse — X² = I exactly — reflecting the self-inverse character of the NOT operation and the reversibility of the quantum gate framework. The Pauli X gate is the π radian rotation of the Bloch sphere about the X-axis — a rotation that exchanges the north and south poles while leaving the X-axis poles |+⟩ and |−⟩ fixed — and its eigenstates |+⟩ = (|0⟩ + |1⟩)/√2 and |−⟩ = (|0⟩ − |1⟩)/√2 are the states that accumulate only a global phase factor under its action. In quantum error correction, the Pauli X gate is the canonical bit flip error operator — the single-qubit Pauli error that most directly threatens the integrity of quantum information encoded in the computational basis — and its detection and correction are the primary functions of bit flip quantum error correcting codes.

---

## Entity 7: Pauli Y

**Gate Annotation:** Y (also denoted **σᵧ**) — The single-qubit gate that enacts a π radian rotation about the Y-axis of the Bloch sphere. Combined bit-phase flip. Maps |0⟩→i|1⟩, |1⟩→−i|0⟩. Self-inverse: Y² = I. Eigenstates: |±i⟩. Algebraically: Y = iXZ.

$$Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}$$

$$Y|0\rangle = i|1\rangle \qquad Y|1\rangle = -i|0\rangle$$

### Prime Archetypal Analysis

**Matrix:** The Y-axis of the Bloch sphere — |+i⟩ = (|0⟩ + i|1⟩)/√2 and |−i⟩ = (|0⟩ − i|1⟩)/√2 are the eigenstates.

**Potentiator:** The combined bit-phase flip potential — the Pauli Y gate simultaneously inverts the computational basis state and introduces imaginary phase factors.

**Catalyst:** Completion of the single-qubit error basis — together with X and Z, the Pauli Y gate completes the single-qubit Pauli error basis {I, X, Y, Z} required for universal single-qubit error characterization.

**Experience:** Simultaneous amplitude and phase modification — the Pauli Y gate changes both measurement outcome labels and introduces imaginary phase factors into the output state amplitudes.

**Significator:** The anti-diagonal matrix with imaginary entries — entries Y₀₁ = −i, Y₁₀ = i.

**Transformation:** π rotation about the Y-axis — the combined action of the X and Z rotations, algebraically expressed as Y = iXZ.

**Way:** The most operationally complex Pauli operator — the Pauli Y gate engages the full complex structure of the single-qubit Hilbert space through its imaginary matrix entries, providing the bridge between the real-amplitude X rotation and the phase-only Z rotation.

### Narrative

The Pauli Y gate is the single-qubit gate that enacts a π radian rotation about the Y-axis of the Bloch sphere — the combined bit-phase flip that simultaneously inverts the computational basis state and introduces imaginary phase factors into the output state amplitudes. Represented by the anti-diagonal 2×2 matrix with entries −i and i, it is simultaneously unitary, Hermitian, and self-inverse — Y² = I exactly — and is algebraically expressible as Y = iXZ, establishing it as the product of the Pauli X and Z gates up to a global phase factor of i. The Pauli Y gate maps |0⟩ to i|1⟩ and |1⟩ to −i|0⟩ — a combined amplitude inversion and imaginary phase advance that engages the full complex structure of the single-qubit Hilbert space through both its amplitude-mixing and phase-shifting actions simultaneously. Its eigenstates are the Y-basis states |+i⟩ = (|0⟩ + i|1⟩)/√2 and |−i⟩ = (|0⟩ − i|1⟩)/√2 — the poles of the Bloch sphere along the Y-axis — which accumulate only global phase factors under its action.

---

## Entity 8: Pauli Z (phase flip)

**Gate Annotation:** Z (also denoted **σ_z**, **phase flip**) — The single-qubit gate that enacts a π radian rotation about the Z-axis of the Bloch sphere. Applies phase factor −1 to |1⟩ component. Maps |0⟩→|0⟩, |1⟩→−|1⟩. Self-inverse: Z² = I. Eigenstates: |0⟩, |1⟩ (computational basis).

$$Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

$$Z|0\rangle = |0\rangle \qquad Z|1\rangle = -|1\rangle$$

### Prime Archetypal Analysis

**Matrix:** The Z-axis of the Bloch sphere — the computational basis states |0⟩ and |1⟩ are the eigenstates of the Pauli Z gate with eigenvalues +1 and −1 respectively.

**Potentiator:** The phase flip potential — the capacity to apply a −1 phase factor to the |1⟩ component of any qubit state without affecting its amplitude.

**Catalyst:** Phase flip error operator — the canonical model of phase flip errors in quantum error correction, and the basis of phase-sensitive quantum protocols.

**Experience:** Amplitude-invariant phase modification — the Pauli Z gate changes no measurement outcome probability in the computational basis but fully reverses the phase of the |1⟩ component, producing observable effects in X-basis measurements.

**Significator:** The diagonal matrix with entries +1, −1 — the unique Pauli operator that is diagonal in the computational basis.

**Transformation:** π rotation about the Z-axis — the Bloch sphere equatorial states are rotated through π radians about the Z-axis, mapping |+⟩↔|−⟩.

**Way:** Phase as an independent logical operation — the Pauli Z gate establishes that quantum phase is an independent and irreducible logical variable, not reducible to amplitude operations.

### Narrative

The Pauli Z gate is the single-qubit gate that applies a phase factor of −1 to the |1⟩ computational basis component of the qubit state while leaving the |0⟩ component unchanged — the canonical phase flip operation that enacts a π radian rotation of the Bloch sphere about the Z-axis. Represented by the diagonal 2×2 matrix with entries +1 and −1, it is simultaneously unitary, Hermitian, and self-inverse — Z² = I exactly — and its eigenstates are the computational basis states |0⟩ and |1⟩ themselves, with eigenvalues +1 and −1 respectively. The Pauli Z gate is completely invisible in the computational basis — it produces no change in the measurement outcome probability for |0⟩ or |1⟩ measurements — but is fully observable in the X-basis, where it exchanges the |+⟩ and |−⟩ measurement outcomes. The Hadamard conjugation relation HXH = Z and HZH = X establishes the precise duality between the Pauli X and Z gates: they enact identical operations in their respective eigenbases — bit flip in the computational basis for X, phase flip in the X-basis for Z — and are interconverted by the Hadamard basis transformation.

---

## Subgroup B.2 — Single-Qubit Clifford Derivatives

**Subgroup Annotation:** Three gates — Phase gate S, Square root of X (√X), and Hadamard (H) — that extend the Pauli π rotations to π/2 rotations and the XZ diagonal axis rotation. S and H together generate the complete single-qubit Clifford group. Hadamard is the foundational superposition generator of the quantum circuit framework.

---

## Entity 9: Phase Gate S (square root of Z)

**Gate Annotation:** S (also denoted **√Z**, **P**, **phase gate**) — The single-qubit Clifford gate that applies a phase factor of i to the |1⟩ computational basis component. Diagonal matrix with entries 1, i. Square root of Z: S² = Z. One of two generators of the single-qubit Clifford group (with H). Maps |+⟩→|+i⟩.

$$S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}$$

$$S|0\rangle = |0\rangle \qquad S|1\rangle = i|1\rangle \qquad S^2 = Z$$

### Prime Archetypal Analysis

**Matrix:** The Z-axis phase rotation at π/2 — the computational basis organized as a phase reference system in which |0⟩ is the phase anchor and |1⟩ carries an i phase advance.

**Potentiator:** The π/2 Z-axis phase rotation family — the bridge between the Pauli identity at 0 and the Pauli Z gate at π through the specific half-angle rotation S² = Z.

**Catalyst:** Clifford group generator — together with the Hadamard gate, the Phase gate S generates the complete single-qubit Clifford group.

**Experience:** Phase advance of the |1⟩ component by π/2 — interconverting the X-basis and Y-basis: S|+⟩ = |+i⟩.

**Significator:** Diagonal matrix with entries 1, i — the specific complex unit entry i at the |1⟩ position distinguishes S from all other single-qubit phase gates.

**Transformation:** π/2 rotation about the Z-axis — the Bloch sphere equatorial state |+⟩ is advanced to the Y-axis pole |+i⟩.

**Way:** Bridge between the Pauli subgroup and the full Clifford group — the Phase gate S is the minimal extension of the Pauli group generators that completes the single-qubit Clifford group generating set.

### Narrative

The Phase gate S is the single-qubit Clifford gate that applies a phase factor of i to the |1⟩ computational basis component of the qubit state while leaving the |0⟩ component unchanged — the π/2 radian rotation of the Bloch sphere about the Z-axis that bridges the Pauli Z gate at π and the identity at 0. Represented by the diagonal 2×2 matrix with entries 1 and i, it satisfies S² = Z — two Phase gate applications reproduce the Pauli Z gate — and S† = S³ — the inverse Phase gate is the three-fold application of S. The Phase gate S is one of two generators of the complete single-qubit Clifford group — together with the Hadamard gate, every single-qubit Clifford operation is expressible as a finite composition of S and H gates. In quantum hardware implementation, the Phase gate is often realized as a virtual gate — a software-level phase advance of the reference frame for all subsequent gate pulses — making it implementable with effectively zero error in superconducting qubit and trapped ion platforms, and establishing it as the most efficiently implementable Clifford phase gate in practical quantum circuit execution.

---

## Entity 10: Square Root of X

**Gate Annotation:** √X (also denoted **SX**, **√NOT**, **V**) — The single-qubit Clifford gate that enacts a π/2 radian rotation about the X-axis. Two applications yield X: (√X)² = X. Matrix with complex entries (1±i)/2. Hardware-native gate in superconducting qubit architectures. Generates complex superposition states from computational basis inputs.

$$\sqrt{X} = \frac{1}{2}\begin{pmatrix} 1+i & 1-i \\ 1-i & 1+i \end{pmatrix}$$

$$(\sqrt{X})^2 = X \qquad \sqrt{X}|0\rangle = \frac{(1+i)|0\rangle + (1-i)|1\rangle}{2}$$

### Prime Archetypal Analysis

**Matrix:** The X-axis of the Bloch sphere — |±⟩ are the fixed points of X-axis rotation, and the √X gate rotates all other states through π/2 radians about this axis.

**Potentiator:** The π/2 X-axis rotation family — the half-step toward the Pauli X gate through the square root relationship (√X)² = X.

**Catalyst:** Hardware-native Clifford primitive — the direct quantum gate representation of a resonant π/2 microwave pulse in superconducting qubit architectures.

**Experience:** Complex superposition generation — √X maps computational basis states to complex equal-weight superpositions with (1±i)/2 amplitude factors.

**Significator:** Complex matrix with entries (1±i)/2 — the specific complex amplitude structure distinguishes √X from the real-amplitude Hadamard gate.

**Transformation:** π/2 rotation about the X-axis — halfway between the identity and the Pauli X gate along the X-axis rotation family.

**Way:** X-axis analog of the Phase gate S — the independent Clifford group generator through the X-axis rotation pathway.

### Narrative

The Square root of X gate is the single-qubit Clifford gate that enacts a π/2 radian rotation about the X-axis of the Bloch sphere — the halfway point between the identity and the Pauli X gate along the X-axis rotation family. Defined by the property (√X)² = X — two applications reproduce the Pauli X gate — it is represented by the 2×2 complex matrix with diagonal entries (1+i)/2 and off-diagonal entries (1−i)/2. Applied to the computational basis state |0⟩, it produces the complex superposition ((1+i)|0⟩ + (1−i)|1⟩)/2 — an equal-weight superposition with complex phase factors that distinguish it from the real-amplitude equal superposition |+⟩ produced by the Hadamard gate. The Square root of X gate is the primary hardware-native single-qubit gate in superconducting qubit platforms — physically realized as a resonant microwave pulse of half the duration required to implement the full Pauli X rotation — making it one of the most experimentally immediate Clifford gates in leading quantum computing hardware architectures.

---

## Entity 11: Hadamard

**Gate Annotation:** H (also denoted **Hadamard gate**) — The single-qubit Clifford gate that enacts a π radian rotation about the diagonal XZ axis of the Bloch sphere. Maps |0⟩↔|+⟩, |1⟩↔|−⟩. Self-inverse: H² = I. Real symmetric matrix with entries ±1/√2. One of two generators of the single-qubit Clifford group (with S). The foundational superposition generator of quantum computing.

$$H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$$

$$H|0\rangle = |+\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}} \qquad H|1\rangle = |-\rangle = \frac{|0\rangle - |1\rangle}{\sqrt{2}}$$

$$H^2 = I \qquad HXH = Z \qquad HZH = X \qquad HYH = -Y$$

### Prime Archetypal Analysis

**Matrix:** The diagonal XZ axis of the Bloch sphere — the unique axis equidistant between the X-axis and Z-axis about which the Hadamard rotation interconverts the two most operationally significant measurement bases.

**Potentiator:** The complete single-qubit basis transformation potential — H interconverts the Z-basis and X-basis, providing access to all states in both bases from either basis.

**Catalyst:** Foundational superposition generator — the Hadamard gate initializes quantum parallelism by creating equal superpositions from computational basis inputs, enabling quantum algorithms to process exponentially many classical inputs simultaneously.

**Experience:** Deterministic superposition creation — H maps computational basis states to equal superposition states and vice versa with certainty, the most directly observable superposition generation operation in the single-qubit gate framework.

**Significator:** Real symmetric matrix with entries ±1/√2 — simultaneously unitary, Hermitian, and self-inverse, the unique combination that enables the basis interconversion property.

**Transformation:** π rotation about the XZ diagonal — a rotation that exchanges the X and Z axes of the Bloch sphere, interconverting the computational basis and the equal superposition basis.

**Way:** The quantum parallelism enabler — the Hadamard gate is the operational primitive through which the classical sequential information of a computational basis state is transformed into the parallel quantum information of an equal superposition, initiating the quantum computational advantage of parallel state processing.

### Narrative

The Hadamard gate is the single-qubit Clifford gate that enacts a π radian rotation about the diagonal XZ axis of the Bloch sphere — the most operationally central single-qubit gate in the complete quantum computing landscape. Represented by the real symmetric matrix H = (1/√2)[[1,1],[1,−1]], it is simultaneously unitary, Hermitian, and exactly self-inverse — H² = I — a unique combination of properties that enables its role as the canonical basis interconversion gate between the Z-basis (computational basis) and the X-basis (equal superposition basis). Applied to the computational basis state |0⟩, the Hadamard gate produces the equal superposition state |+⟩ = (|0⟩ + |1⟩)/√2 — the state with equal and in-phase amplitudes for both basis states — and applied to |1⟩ it produces |−⟩ = (|0⟩ − |1⟩)/√2 — the state with equal but phase-opposite amplitudes. The conjugation relations HXH = Z and HZH = X are the formal expressions of the Hadamard gate's basis interconversion property: they establish that the Pauli X gate in the computational basis is equivalent to the Pauli Z gate in the X-basis, and vice versa — a duality that is fundamental to the structure of the single-qubit Clifford group. Together with the Phase gate S, the Hadamard gate generates the complete single-qubit Clifford group, establishing the pair {H, S} as the minimal generating set of single-qubit Clifford operations.

---

## Subgroup B.3 — Two-Qubit Clifford Operators

**Subgroup Annotation:** Clifford gates acting on two-qubit Hilbert space (4D). The minimal gate class capable of generating entanglement. Conditional logical structure: target transformation depends on control state. Contains three gates: CNOT, Anticontrolled-NOT, and Controlled-Z.

---

## Entity 12: Controlled-NOT (CNOT) [includes Feynman notation]

**Gate Annotation:** CNOT (also denoted **CX**, **controlled-X**, **Feynman gate**) — The two-qubit Clifford gate that applies Pauli X to the target qubit if and only if the control qubit is in |1⟩. Block diagonal 4×4 matrix. Self-inverse. Generates Bell states with Hadamard. Universal entangling primitive of the Clifford+T gate set. Feynman gate is an identical notation variant.

$$CNOT = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}$$

$$CNOT|00\rangle = |00\rangle \quad CNOT|01\rangle = |01\rangle \quad CNOT|10\rangle = |11\rangle \quad CNOT|11\rangle = |10\rangle$$

$$(H \otimes I) \cdot CNOT|00\rangle = |\Phi^+\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}$$

### Prime Archetypal Analysis

**Matrix:** The four-dimensional two-qubit Hilbert space partitioned into the control-zero subspace (identity action) and control-one subspace (Pauli X action).

**Potentiator:** The complete two-qubit entanglement generation potential accessible through conditional bit flip — all four Bell states are reachable from computational basis inputs through CNOT combined with single-qubit operations.

**Catalyst:** Universal entangling primitive — together with single-qubit rotations, the CNOT gate generates the complete multi-qubit Clifford group and forms a universal gate set for quantum computation.

**Experience:** Conditional bit flip — the target qubit measurement outcome is deterministically flipped when the control is measured as |1⟩, and unchanged when the control is measured as |0⟩.

**Significator:** Block diagonal 4×4 matrix — identity block for control-0, Pauli X block for control-1.

**Transformation:** Conditional π rotation of target qubit about X-axis, enacted only when the control qubit is in |1⟩.

**Way:** The quantum reversible XOR gate — the CNOT gate implements the classical XOR function reversibly, establishing the connection between classical reversible logic and quantum entangling operations.

### Narrative

The CNOT gate is the two-qubit Clifford gate that applies the Pauli X transformation to a designated target qubit conditioned upon a designated control qubit being in the |1⟩ state, and leaves the target qubit unchanged when the control is in |0⟩. Represented by the 4×4 block diagonal matrix with a 2×2 identity block in the control-zero subspace and a 2×2 Pauli X block in the control-one subspace, it is simultaneously unitary, Hermitian, and exactly self-inverse — CNOT² = I. The CNOT gate is the canonical entangling gate of the quantum circuit framework: applied after a Hadamard gate on the control qubit, it generates the Bell state |Φ+⟩ = (|00⟩ + |11⟩)/√2 from the separable input |00⟩ — the canonical maximally entangled two-qubit state. Together with the single-qubit Hadamard and Phase gates, the CNOT gate generates the complete n-qubit Clifford group, and combined with arbitrary single-qubit rotations it forms a universal gate set for quantum computation. The Feynman gate is a notation variant of the CNOT gate — the two gates are operationally identical and differ only in the circuit diagram symbol used to represent them.

---

## Entity 13: Anticontrolled-NOT

**Gate Annotation:** ACNOT (also denoted **zero-controlled NOT**, **controlled-NOT with zero control**) — The two-qubit Clifford gate that applies Pauli X to the target qubit if and only if the control qubit is in |0⟩. Logical complement of CNOT. Algebraically: ACNOT = (X⊗I)·CNOT·(X⊗I). Quantum analog of reversible exclusive NOR.

$$ACNOT = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

$$ACNOT|00\rangle = |01\rangle \quad ACNOT|01\rangle = |00\rangle \quad ACNOT|10\rangle = |10\rangle \quad ACNOT|11\rangle = |11\rangle$$

### Prime Archetypal Analysis

**Matrix:** The four-dimensional two-qubit Hilbert space partitioned into the control-zero subspace (Pauli X action) and control-one subspace (identity action) — the logical complement of the CNOT partitioning.

**Potentiator:** Zero-activated conditional bit flip potential — all circuit constructions requiring conditional operations activated by the |0⟩ control state rather than the |1⟩ control state.

**Catalyst:** Zero-activated conditional control primitive — enables quantum circuit designs that branch on the absence rather than the presence of a control signal.

**Experience:** Conditional bit flip on zero control — the target qubit is flipped when the control is in |0⟩ and unchanged when the control is in |1⟩.

**Significator:** Block diagonal 4×4 matrix — Pauli X block for control-0, identity block for control-1.

**Transformation:** Conditional π rotation of target qubit about X-axis, enacted only when the control qubit is in |0⟩.

**Way:** Complete conditional branching — together with CNOT, ACNOT enables conditional operations on both control values, completing the two-branch conditional operation framework for single-qubit control.

### Narrative

The Anticontrolled-NOT gate is the two-qubit Clifford gate that applies the Pauli X transformation to a designated target qubit conditioned upon a designated control qubit being in the |0⟩ state — the logical complement of the CNOT gate's activation condition. Algebraically expressible as ACNOT = (X⊗I)·CNOT·(X⊗I) — a CNOT gate with the control qubit inverted before and after — it maps |00⟩↔|01⟩ while leaving |10⟩ and |11⟩ unchanged. The ACNOT gate is the quantum analog of the classical reversible exclusive NOR gate and is used in quantum arithmetic circuits requiring zero-activated carry propagation, quantum oracle constructions requiring operations conditioned on zero-valued inputs, and algorithms requiring distinct conditional operations on both possible control qubit values.

---

## Entity 14: Controlled-Z

**Gate Annotation:** CZ (also denoted **controlled-phase**, **CZ gate**) — The two-qubit Clifford gate that applies a phase factor of −1 to the |11⟩ two-qubit computational basis state. Diagonal 4×4 matrix. Symmetric: control-target designation irrelevant. Self-inverse. Related to CNOT by Hadamard conjugation: CZ = (I⊗H)·CNOT·(I⊗H). Native gate in superconducting qubits.

$$CZ = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & -1 \end{pmatrix}$$

$$CZ|11\rangle = -|11\rangle \qquad CZ = (I \otimes H) \cdot CNOT \cdot (I \otimes H)$$

### Prime Archetypal Analysis

**Matrix:** The four-dimensional two-qubit Hilbert space with the |11⟩ state as the uniquely phase-differentiated element — the state in which both qubits are simultaneously activated.

**Potentiator:** Symmetric phase-encoded entanglement potential — because CZ is symmetric under qubit exchange, either qubit can serve as control or target without altering the gate's action.

**Catalyst:** Phase-encoding entanglement primitive — the CZ gate generates phase-encoded entanglement that is invisible in the computational basis but fully observable in the X-basis.

**Experience:** Phase flip of the |11⟩ state — the only computational basis state affected by the CZ gate acquires a phase factor of −1, invisible in computational basis measurements but observable through Hadamard-conjugated X-basis measurements.

**Significator:** Diagonal 4×4 matrix with entries +1, +1, +1, −1 — the phase flip exclusively at the |11⟩ position.

**Transformation:** Conditional phase flip — a −1 phase factor applied to the two-qubit state only when both qubits are simultaneously in |1⟩.

**Way:** Native phase entanglement — the CZ gate is the natural entangling primitive of quantum hardware platforms where phase interactions dominate over amplitude interactions.

### Narrative

The Controlled-Z gate is the two-qubit Clifford gate that applies a phase factor of −1 to the |11⟩ two-qubit computational basis state while leaving all other computational basis states unchanged. Represented by the diagonal 4×4 matrix with entries +1, +1, +1, −1 corresponding to |00⟩, |01⟩, |10⟩, |11⟩ respectively, it is simultaneously unitary, Hermitian, and exactly self-inverse — CZ² = I — and is related to the CNOT gate by Hadamard conjugation on the target qubit: CZ = (I⊗H)·CNOT·(I⊗H). The CZ gate is symmetric under the exchange of its two qubit labels — the control-target designation is irrelevant because the gate's only non-trivial action is the phase flip at |11⟩, which treats both qubits identically. This symmetry is the primary operational advantage of the CZ gate over the CNOT gate in many quantum circuit contexts and is the source of its native gate status in superconducting qubit architectures where capacitive coupling between qubits generates symmetric ZZ interactions. The CZ gate is a core primitive of the quantum phase estimation algorithm and the quantum Fourier transform.

---

---

# CLASS C: ROTATIONAL OPERATORS

**Class Annotation:** Gates with continuously parameterized rotation angles. Generalize Clifford fixed-angle rotations to the continuous parameter space. Enable arbitrary single-qubit unitary construction. Cross the boundary from Clifford (classically simulable) to universal quantum computation.

---

## Subgroup C.1 — Principal Axis Rotation Gates

**Subgroup Annotation:** Three gates (Rx, Ry, Rz) enacting parameterized rotations about the X, Y, and Z axes of the Bloch sphere. Single parameter θ ∈ [0, 4π). Matrix exponentials of Pauli operators: Rn(θ) = e^(−iθσn/2). Any SU(2) element is expressible as at most three principal axis rotations through the Euler angle decomposition U = Rz(α)Ry(β)Rz(γ).

---

## Entity 15: Rx (X-axis rotation)

**Gate Annotation:** Rx(θ) — The single-qubit rotational gate enacting a continuously parameterized rotation about the X-axis by angle θ. Defined by Rx(θ) = e^(−iθX/2). Real diagonal entries cos(θ/2), purely imaginary off-diagonal entries −i·sin(θ/2). Reduces to Pauli X up to global phase at θ = π. Direct representation of the physical Rabi rotation in superconducting and trapped ion hardware.

$$R_x(\theta) = \begin{pmatrix} \cos(\theta/2) & -i\sin(\theta/2) \\ -i\sin(\theta/2) & \cos(\theta/2) \end{pmatrix}$$

$$R_x(\theta)|0\rangle = \cos(\theta/2)|0\rangle - i\sin(\theta/2)|1\rangle$$

$$R_x(0) = I \qquad R_x(\pi) = -iX \qquad R_x(2\pi) = -I \qquad R_x(4\pi) = I$$

### Prime Archetypal Analysis

**Matrix:** The X-axis of the Bloch sphere as the continuous rotation axis — eigenstates |±⟩ are the fixed points of all X-axis rotations.

**Potentiator:** The one-parameter subgroup {Rx(θ) : θ ∈ [0, 4π)} — the complete continuous interpolation between identity and Pauli X.

**Catalyst:** Physical Rabi rotation representation — the direct gate representation of resonant microwave or laser pulse driving in superconducting qubit and trapped ion hardware.

**Experience:** Continuous sinusoidal redistribution of measurement probabilities — cos²(θ/2) for |0⟩, sin²(θ/2) for |1⟩.

**Significator:** 2×2 matrix with real diagonal cos(θ/2) and purely imaginary off-diagonal −i·sin(θ/2) — SU(2) element with 4π periodicity.

**Transformation:** Continuous rotation of the Bloch sphere about the X-axis through angle θ — great circle arc in the YZ plane.

**Way:** Amplitude control — precise and continuously tunable redistribution of quantum probability amplitude between computational basis states.

### Narrative

The Rx gate is the single-qubit rotational gate that enacts a continuously parameterized rotation of the qubit state about the X-axis of the Bloch sphere by angle θ. Defined as Rx(θ) = e^(−iθX/2), it is represented by a 2×2 unitary matrix with real diagonal entries cos(θ/2) and purely imaginary off-diagonal entries −i·sin(θ/2). Applied to |0⟩, it produces cos(θ/2)|0⟩ − i·sin(θ/2)|1⟩ — a superposition whose measurement probabilities vary continuously as cos²(θ/2) and sin²(θ/2). The Rx gate reduces to the identity at θ = 0, to Pauli X up to global phase at θ = π, to −I at θ = 2π, and returns exactly to the identity at θ = 4π — completing the full 4π spinor cycle. In quantum hardware, the Rx gate is the direct mathematical representation of the Rabi rotation — the physical process through which a resonant electromagnetic field drives population transfer between qubit energy eigenstates — making it one of the most physically immediate gates in the complete taxonomy. Its purely imaginary off-diagonal entries distinguish it from the Ry gate, reflecting the distinct complex phase structure introduced by X-axis versus Y-axis rotation.

---

## Entity 16: Ry (Y-axis rotation)

**Gate Annotation:** Ry(θ) — The single-qubit rotational gate enacting a continuously parameterized rotation about the Y-axis by angle θ. Defined by Ry(θ) = e^(−iθY/2). The unique principal axis rotation gate with exclusively real matrix entries. Generates real-amplitude superpositions from computational basis inputs. Standard rotation primitive in the ZYZ Euler angle decomposition.

$$R_y(\theta) = \begin{pmatrix} \cos(\theta/2) & -\sin(\theta/2) \\ \sin(\theta/2) & \cos(\theta/2) \end{pmatrix}$$

$$R_y(\theta)|0\rangle = \cos(\theta/2)|0\rangle + \sin(\theta/2)|1\rangle$$

$$R_y(0) = I \qquad R_y(\pi) = -iY \qquad R_y(\pi/2)|0\rangle = |+\rangle$$

### Prime Archetypal Analysis

**Matrix:** The Y-axis of the Bloch sphere as the continuous rotation axis — eigenstates |±i⟩ are the fixed points of all Y-axis rotations.

**Potentiator:** The complete family of real-amplitude superposition states — {cos(θ/2)|0⟩ + sin(θ/2)|1⟩ : θ ∈ [0, 4π)} spanning the XZ great circle of the Bloch sphere.

**Catalyst:** Real-amplitude state preparation primitive — the natural rotation for quantum chemistry and variational algorithms operating in real-amplitude subspaces.

**Experience:** Continuous redistribution of real probability amplitude — cos²(θ/2) for |0⟩, sin²(θ/2) for |1⟩, without any imaginary phase factors in the output.

**Significator:** 2×2 real orthogonal matrix — member of both U(2) and O(2), the unique principal axis rotation with exclusively real entries.

**Transformation:** Continuous rotation of the Bloch sphere about the Y-axis through angle θ — great circle arc in the XZ plane through the real-amplitude superposition states.

**Way:** Real-amplitude completeness — the primary rotation primitive for the real-amplitude subspace of the single-qubit Hilbert space.

### Narrative

The Ry gate is the single-qubit rotational gate that enacts a continuously parameterized rotation of the qubit state about the Y-axis of the Bloch sphere by angle θ. Defined as Ry(θ) = e^(−iθY/2), it is represented by a 2×2 real orthogonal matrix with diagonal entries cos(θ/2) and off-diagonal entries ∓sin(θ/2) — the unique principal axis rotation gate whose matrix contains exclusively real entries for all values of θ. Applied to |0⟩, it produces the real superposition cos(θ/2)|0⟩ + sin(θ/2)|1⟩ — a state with real positive amplitudes whose measurement probabilities are cos²(θ/2) and sin²(θ/2), passing through |+⟩ at θ = π/2. The real matrix structure of the Ry gate is its most structurally significant distinguishing property: it acts entirely within the real subspace of the single-qubit Hilbert space, mapping any real-amplitude input to a real-amplitude output without introducing imaginary phase factors. This makes the Ry gate the preferred rotation primitive for variational quantum algorithms, quantum chemistry simulations, and all computations operating within the real-amplitude subspace. In the ZYZ Euler angle decomposition U = Rz(α)Ry(β)Rz(γ), the Ry gate provides the latitude rotation controlling the polar angle of the output state on the Bloch sphere.

---

## Entity 17: Rz (Z-axis rotation)

**Gate Annotation:** Rz(θ) (also denoted **phase rotation**) — The single-qubit rotational gate enacting a continuously parameterized rotation about the Z-axis by angle θ. Defined by Rz(θ) = e^(−iθZ/2). Diagonal matrix with entries e^(∓iθ/2). Leaves computational basis measurement probabilities unchanged. Special cases: Rz(π) = −iZ, Rz(π/2) = e^(−iπ/4)S, Rz(π/4) = e^(−iπ/8)T. Implementable as a virtual gate (zero error) in superconducting platforms.

$$R_z(\theta) = \begin{pmatrix} e^{-i\theta/2} & 0 \\ 0 & e^{i\theta/2} \end{pmatrix}$$

$$R_z(\theta)|0\rangle = e^{-i\theta/2}|0\rangle \qquad R_z(\theta)|1\rangle = e^{i\theta/2}|1\rangle$$

$$R_z(0) = I \qquad R_z(\pi) = -iZ \qquad R_z(\pi/2) = e^{-i\pi/4}S \qquad R_z(\pi/4) = e^{-i\pi/8}T$$

### Prime Archetypal Analysis

**Matrix:** The Z-axis of the Bloch sphere as the phase rotation axis — eigenstates |0⟩ and |1⟩ are the fixed points of all Z-axis rotations.

**Potentiator:** The complete continuous family of relative phase relationships — {e^(iθ) : θ ∈ [0, 4π)} spanning the full azimuthal rotational freedom of the Bloch sphere.

**Catalyst:** Phase control primitive — the primary gate for engineering precise quantum interference conditions in phase-sensitive quantum algorithms.

**Experience:** Complete invisibility in the computational basis — no change in measurement probabilities — full observability in equatorial measurement bases through phase-sensitive interference.

**Significator:** Diagonal 2×2 matrix with entries e^(∓iθ/2) — the formal signature of pure phase action on the computational basis.

**Transformation:** Continuous azimuthal rotation of the Bloch sphere equatorial plane through angle θ — circular arc of the equatorial states about the Z-axis.

**Way:** Phase completeness through virtual implementation — the most efficiently implementable single-qubit gate, realizable as a software-level reference frame adjustment with zero error contribution.

### Narrative

The Rz gate is the single-qubit rotational gate that enacts a continuously parameterized rotation of the qubit state about the Z-axis of the Bloch sphere by angle θ. Defined as Rz(θ) = e^(−iθZ/2), it is represented by a 2×2 diagonal unitary matrix with entries e^(−iθ/2) and e^(iθ/2) — the unique principal axis rotation gate whose matrix is diagonal for all values of θ. Applied to computational basis states, it produces e^(−iθ/2)|0⟩ and e^(iθ/2)|1⟩ — states physically identical to |0⟩ and |1⟩ under computational basis measurement but carrying differential phase factors encoding the rotation angle. The Rz gate's special cases reproduce the complete discrete Z-axis phase gate family: Rz(π) = −iZ, Rz(π/2) = e^(−iπ/4)S, and Rz(π/4) = e^(−iπ/8)T — establishing it as the continuous parameterized envelope unifying the Pauli Z, Phase gate S, and T gate within a single gate family. In superconducting qubit and trapped ion platforms, the Rz gate is implemented as a virtual gate — a software-level adjustment to the reference phase of all subsequent gate pulses — with zero additional error contribution, making it the most resource-efficient single-qubit gate in the complete taxonomy.

---

## Subgroup C.2 — Phase Rotation Gates

**Subgroup Annotation:** Single-qubit gates applying a defined phase factor to the |1⟩ computational basis component while leaving |0⟩ unchanged. Three members: R1(λ) — continuous phase rotation; T gate — discrete π/4 non-Clifford rotation; U(θ,φ,λ) — complete three-parameter SU(2) parameterization. Together they span the complete phase rotation family from continuous parameter control through the non-Clifford universality threshold to full single-qubit unitary completeness.

$$R_1(\lambda) = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\lambda} \end{pmatrix} \qquad T = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{pmatrix} \qquad U(\theta,\phi,\lambda) = \begin{pmatrix} \cos(\theta/2) & -e^{i\lambda}\sin(\theta/2) \\ e^{i\phi}\sin(\theta/2) & e^{i(\phi+\lambda)}\cos(\theta/2) \end{pmatrix}$$

---

## Entity 18: Phase Shift Gate R1

**Gate Annotation:** R1(λ) (also denoted **P(λ)**, **Rφ**, **phase gate**) — The continuously parameterized single-qubit phase rotation gate. Applies e^(iλ) to |1⟩, leaves |0⟩ unchanged. Related to Rz by global phase: R1(λ) = e^(iλ/2)Rz(λ). Special cases: R1(π) = Z, R1(π/2) = S, R1(π/4) = T. Unifies all Z-axis phase gates within a single continuous parameterized family.

$$R_1(\lambda) = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\lambda} \end{pmatrix}$$

$$R_1(\lambda)|0\rangle = |0\rangle \qquad R_1(\lambda)|1\rangle = e^{i\lambda}|1\rangle$$

$$R_1(\pi) = Z \qquad R_1\left(\frac{\pi}{2}\right) = S \qquad R_1\left(\frac{\pi}{4}\right) = T \qquad R_1\left(\frac{\pi}{8}\right) = \sqrt{T}$$

### Prime Archetypal Analysis

**Matrix:** The computational basis as a phase-asymmetric reference structure — |0⟩ is the invariant phase anchor, |1⟩ is the phase-variable component.

**Potentiator:** The complete continuous phase angle range {e^(iλ) : λ ∈ [0, 2π)} — every possible relative phase relationship between |0⟩ and |1⟩.

**Catalyst:** Universal phase marking primitive — the gate through which any desired relative phase is established in a single application.

**Experience:** Phase-basis-dependent observability — invisible in computational basis, fully observable in equatorial measurement bases through sinusoidal interference signatures.

**Significator:** Upper-triangular 2×2 matrix with entry 1 at |0⟩ and e^(iλ) at |1⟩ — the explicit phase reference structure encoded in the matrix.

**Transformation:** Asymmetric azimuthal rotation — advancing the |1⟩ phase by λ while holding |0⟩ at zero phase.

**Way:** Unification of the discrete Z-axis phase gate family — Pauli Z, S gate, T gate, and all discrete phase gates as special cases at discrete λ values.

### Narrative

The Phase Shift gate R1(λ) is the single-qubit gate that applies a continuously parameterized phase factor e^(iλ) to the |1⟩ computational basis component while leaving |0⟩ unchanged in both amplitude and phase. Represented by the upper-triangular matrix with entries 1 and e^(iλ), it is the most directly interpretable phase rotation gate in the single-qubit framework — its unit entry at |0⟩ makes the phase reference role explicit, while the e^(iλ) entry directly encodes the phase advance applied to |1⟩. The R1 gate is related to Rz by a global phase: R1(λ) = e^(iλ/2)Rz(λ) — both produce identical relative phase advances between computational basis components. The distinction becomes physically significant in controlled gate contexts, where the global phase factor becomes a relative phase between control qubit branches. Its special case hierarchy — R1(π) = Z, R1(π/2) = S, R1(π/4) = T — establishes the R1 gate as the continuous parameterized envelope unifying the complete discrete Z-axis phase gate family within a single expression. In the quantum Fourier transform, controlled R1 gates at binary-fractional phase angles λ = 2π/2^k implement the Fourier phase relationships that underlie Shor's factoring algorithm.

---

## Entity 19: T Gate (π/8 gate, square root of S)

**Gate Annotation:** T (also denoted **π/8 gate**, **√S**) — The canonical non-Clifford single-qubit gate. Applies phase factor e^(iπ/4) to |1⟩. Special case of R1 at λ = π/4. Square root of S: T² = S. Non-Clifford gate enabling universal quantum computation via Solovay-Kitaev. Dominant resource cost in fault-tolerant quantum computing. T-count minimization is the primary circuit optimization objective in fault-tolerant contexts.

$$T = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & \frac{1+i}{\sqrt{2}} \end{pmatrix}$$

$$T^2 = S \qquad T^4 = Z \qquad T^8 = I$$

### Prime Archetypal Analysis

**Matrix:** The computational basis at the precise phase boundary between Clifford and non-Clifford operation — the π/4 phase advance at |1⟩ is the smallest binary-fractional phase not in the Clifford group.

**Potentiator:** Magic state generation — the capacity to produce the magic state |T⟩ = (|0⟩ + e^(iπ/4)|1⟩)/√2 from Clifford-preparable inputs, the consumable resource of fault-tolerant universal quantum computing.

**Catalyst:** Non-Clifford universality enabler — the specific gate whose inclusion breaks the Gottesman-Knill classical simulability and enables universal quantum computation via Solovay-Kitaev.

**Experience:** Generation of non-stabilizer states — T gate outputs from Clifford inputs are magic states that cannot be represented within the stabilizer formalism and require full quantum state description.

**Significator:** Eighth root of unity e^(iπ/4) = (1+i)/√2 at |1⟩ — the algebraic signature of non-Clifford operation and membership outside the Clifford group.

**Transformation:** Discrete π/4 radian phase advance of |1⟩ — positioning the Bloch sphere equatorial state at azimuthal angle π/4, midway between the nearest Clifford-accessible equatorial states.

**Way:** Resource theory of magic — T gate count (T-count) is the primary measure of non-Clifford resource cost; T-count minimization is the central optimization objective of fault-tolerant quantum circuit synthesis.

### Narrative

The T gate is the single-qubit non-Clifford gate that applies a fixed phase factor e^(iπ/4) to the |1⟩ computational basis component while leaving |0⟩ unchanged. Represented by the diagonal matrix with entries 1 and e^(iπ/4) = (1+i)/√2, it is the special case of R1 at λ = π/4 and the square root of the Phase gate S: T² = S. Its iterated powers generate the eight-element cyclic phase hierarchy T¹ = T, T² = S, T⁴ = Z, T⁸ = I — the T gate is the unique non-Clifford element in this sequence. The T gate's canonical status as the non-Clifford primitive of universal quantum computation follows from the Gottesman-Knill theorem — Clifford circuits are classically simulable — and the Solovay-Kitaev theorem — the Clifford+T gate set can approximate any single-qubit unitary to arbitrary precision with logarithmic gate count overhead. In fault-tolerant quantum computing architectures based on stabilizer error-correcting codes, the T gate cannot be implemented transversally and requires magic state distillation — a resource-intensive protocol consuming many physical qubits and gate operations per logical T gate application. T-count minimization is consequently the primary optimization objective of fault-tolerant quantum circuit synthesis, with the T gate representing the dominant resource cost of any fault-tolerant quantum algorithm.

---

## Entity 20: General Single-Qubit Rotation U

**Gate Annotation:** U(θ, φ, λ) (also denoted **U gate**, **U3 gate**, **universal single-qubit gate**) — The complete three-parameter parameterization of the full SU(2) group of single-qubit unitaries. Every single-qubit gate in the taxonomy is a special case at specific discrete parameter values. Standard compilation target of quantum circuit synthesis frameworks. Unifies the complete single-qubit gate framework within one parameterized family.

$$U(\theta, \phi, \lambda) = \begin{pmatrix} \cos(\theta/2) & -e^{i\lambda}\sin(\theta/2) \\ e^{i\phi}\sin(\theta/2) & e^{i(\phi+\lambda)}\cos(\theta/2) \end{pmatrix}$$

$$U(\pi, 0, \pi) = X \quad U(\pi, \pi/2, \pi/2) = Y \quad U(0, 0, \pi) = Z \quad U(\pi/2, 0, \pi) = H$$

### Prime Archetypal Analysis

**Matrix:** The complete SU(2) group manifold — topologically equivalent to the three-sphere S³, the three-dimensional compact connected manifold parameterized by (θ, φ, λ).

**Potentiator:** The complete three-parameter space {(θ, φ, λ)} — every point corresponds to a physically distinct single-qubit unitary, collectively filling the SU(2) manifold without gap.

**Catalyst:** Universal single-qubit compilation target — the intermediate representation into which any single-qubit unitary is translated during quantum circuit compilation before decomposition into hardware-native sequences.

**Experience:** Complete and independently controllable manipulation of all three observable properties — polar amplitude ratio (θ), azimuthal phase (φ), and input phase relationship (λ).

**Significator:** Most general 2×2 unitary matrix with three independent parameters — every single-qubit gate in the taxonomy appears as a special case at specific discrete parameter values.

**Transformation:** The most general single-qubit unitary transformation — simultaneously controlling polar angle, azimuthal phase, and input phase through three independent parameters.

**Way:** Unified operational completeness — all single-qubit operations are members of a single continuous three-parameter family; the U gate is the formal expression of this completeness.

### Narrative

The General single-qubit rotation U(θ, φ, λ) is the complete parameterization of the full SU(2) group of single-qubit unitary operations — the single gate expression that encompasses every possible single-qubit unitary transformation within a unified three-parameter matrix. Its three parameters independently control the three degrees of freedom of SU(2): θ determines the amplitude mixing ratio between |0⟩ and |1⟩ output components; φ determines the azimuthal phase of the |1⟩ output; and λ determines the phase advance applied to the |1⟩ input. Every single-qubit gate in the taxonomy is a special case: Pauli X is U(π, 0, π), Pauli Y is U(π, π/2, π/2), Hadamard is U(π/2, 0, π), Phase gate S is U(0, 0, π/2), T gate is U(0, 0, π/4), Rx(θ) is U(θ, −π/2, π/2), and Ry(θ) is U(θ, 0, 0). The KAK decomposition and Euler angle decomposition establish the U gate as the universal single-qubit compilation target — the standard format into which arbitrary single-qubit unitaries are translated during quantum circuit compilation before decomposition into hardware-native gate sequences. The Solovay-Kitaev theorem establishes that any U(θ, φ, λ) can be approximated to precision ε from any universal single-qubit gate set with O(log^c(1/ε)) gates.

---

## Subgroup C.3 — Two-Qubit Rotational Gates

**Subgroup Annotation:** Three parameterized two-qubit gates — Rxx, Ryy, Rzz — enacting continuously parameterized rotations of the two-qubit state space about the XX, YY, and ZZ tensor product interaction axes. Each defined as Rnn(θ) = e^(−iθ(σn⊗σn)/2). Native entangling gates of quantum hardware platforms with tensor product Pauli coupling Hamiltonians. Primary parameterized entangling primitives for Hamiltonian simulation and variational quantum algorithms.

$$R_{xx}(\theta) = e^{-i\theta X\otimes X/2} \qquad R_{yy}(\theta) = e^{-i\theta Y\otimes Y/2} \qquad R_{zz}(\theta) = e^{-i\theta Z\otimes Z/2}$$

---

## Entity 21: Rxx (XX interaction rotation)

**Gate Annotation:** Rxx(θ) — Two-qubit parameterized rotation about the XX interaction axis. Defined as e^(−iθX⊗X/2). 4×4 matrix with cos(θ/2) diagonal and −i·sin(θ/2) anti-diagonal corner entries. Native gate of trapped ion quantum computers via Mølmer-Sørensen interaction. Maximally entangling at θ = π/2.

$$R_{xx}(\theta) = \begin{pmatrix} \cos(\theta/2) & 0 & 0 & -i\sin(\theta/2) \\ 0 & \cos(\theta/2) & -i\sin(\theta/2) & 0 \\ 0 & -i\sin(\theta/2) & \cos(\theta/2) & 0 \\ -i\sin(\theta/2) & 0 & 0 & \cos(\theta/2) \end{pmatrix}$$

**Special cases:** Rxx(0) = I, Rxx(π/2) = maximally entangling, Rxx(π) = −i(X⊗X)

### Narrative

The Rxx gate enacts a continuously parameterized rotation of the two-qubit state space about the XX tensor product interaction axis. At θ = 0 it is the identity; at θ = π/2 it is maximally entangling; at θ = π it reproduces the XX tensor product operator up to global phase. It is the native two-qubit gate of trapped ion quantum computers implementing the Mølmer-Sørensen interaction — a physical XX coupling between ion qubits through shared motional modes, directly realizing Rxx as a physical operation whose rotation angle is controlled by laser pulse duration and intensity. The Rxx gate generates XX-type two-qubit correlations — correlated bit flip interactions between the two qubits — and is the principal axis XX interaction member of the Two-Qubit Rotational Gate family.

---

## Entity 22: Ryy (YY interaction rotation)

**Gate Annotation:** Ryy(θ) — Two-qubit parameterized rotation about the YY interaction axis. Defined as e^(−iθY⊗Y/2). 4×4 matrix with real and imaginary entries reflecting the complex structure of Y⊗Y. Generates YY-type correlated bit-phase flip interactions.

$$R_{yy}(\theta) = \begin{pmatrix} \cos(\theta/2) & 0 & 0 & i\sin(\theta/2) \\ 0 & \cos(\theta/2) & -i\sin(\theta/2) & 0 \\ 0 & -i\sin(\theta/2) & \cos(\theta/2) & 0 \\ i\sin(\theta/2) & 0 & 0 & \cos(\theta/2) \end{pmatrix}$$

### Narrative

The Ryy gate enacts a continuously parameterized rotation of the two-qubit state space about the YY tensor product interaction axis. It generates YY-type two-qubit correlations — correlated combined bit-phase flip interactions between the two qubits — and is the most algebraically complex of the three principal axis two-qubit rotation gates, reflecting the imaginary and combined bit-phase flip character of the Pauli Y operator in its tensor product structure. At θ = π/2 the Ryy gate is maximally entangling, generating maximal YY-correlated entanglement from separable computational basis inputs. The Ryy gate completes the three-gate principal axis family — alongside Rxx and Rzz — providing the YY interaction axis member of the Two-Qubit Rotational Gate subgroup.

---

## Entity 23: Rzz (ZZ interaction rotation)

**Gate Annotation:** Rzz(θ) — Two-qubit parameterized rotation about the ZZ interaction axis. Defined as e^(−iθZ⊗Z/2). Diagonal 4×4 matrix with entries e^(∓iθ/2) reflecting the diagonal character of Z⊗Z. Invisible in computational basis measurement probabilities. Native gate of superconducting qubit systems with ZZ coupling Hamiltonians.

$$R_{zz}(\theta) = \begin{pmatrix} e^{-i\theta/2} & 0 & 0 & 0 \\ 0 & e^{i\theta/2} & 0 & 0 \\ 0 & 0 & e^{i\theta/2} & 0 \\ 0 & 0 & 0 & e^{-i\theta/2} \end{pmatrix}$$

### Narrative

The Rzz gate enacts a continuously parameterized rotation of the two-qubit state space about the ZZ tensor product interaction axis. Its diagonal matrix structure reflects the phase-only action of the ZZ interaction — the Rzz gate acts exclusively through differential phase factors applied to the four computational basis states without redistributing amplitude between them. It is invisible in computational basis measurement probabilities but fully observable through phase-sensitive two-qubit correlation measurements. In superconducting qubit systems with direct inductive coupling between transmon qubits, the native ZZ coupling Hamiltonian directly realizes the Rzz gate as a physical operation whose rotation angle is controlled by coupling strength and interaction time. The Rzz gate generates ZZ-type two-qubit correlations — correlated phase flip interactions — and is the phase-dominant member of the Two-Qubit Rotational Gate subgroup.

---

---

# CLASS D: SWAP OPERATORS

**Class Annotation:** Two-qubit gates whose primary operational characteristic is the exchange of quantum information between qubit register positions — transferring the complete quantum state of one qubit to the other, with or without phase modification, partial exchange, or combined entangling operations. Essential for quantum circuit routing in hardware architectures with limited qubit connectivity.

---

## Entity 24: SWAP

**Gate Annotation:** SWAP — The canonical two-qubit state exchange gate. Exchanges complete quantum states of two qubits without phase modification. Self-inverse: SWAP² = I. Simultaneously unitary, Hermitian, self-inverse. Decomposable into three CNOT gates. Preserves entanglement structure through register position exchange.

$$SWAP = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

$$SWAP|01\rangle = |10\rangle \qquad SWAP|10\rangle = |01\rangle \qquad SWAP = CNOT_{12} \cdot CNOT_{21} \cdot CNOT_{12}$$

### Narrative

The SWAP gate exchanges the complete quantum states of two qubits — transferring every amplitude and phase property of each qubit to the other register position without modification. Simultaneously unitary, Hermitian, and exactly self-inverse, it treats both qubits symmetrically: neither is privileged as source or destination. Decomposable into three sequential CNOT gates in alternating control-target configurations, the SWAP gate is the foundational quantum information routing primitive — the gate through which quantum information is moved between non-adjacent register positions to satisfy the physical connectivity constraints of quantum hardware architectures. Its preservation of entanglement structure through register position exchange is central to quantum repeater architectures and entanglement swapping protocols in quantum networks.

---

## Entity 25: iSWAP

**Gate Annotation:** iSWAP — The phase-augmented state exchange gate. Exchanges |01⟩ and |10⟩ states while applying imaginary phase factor i to each exchanged component. Both a state exchange and a maximally entangling operation simultaneously. Native two-qubit gate of XY-coupled superconducting qubit architectures. Related to SWAP by XY interaction: iSWAP = e^(iπ(X⊗X + Y⊗Y)/4)·SWAP.

$$iSWAP = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & i & 0 \\ 0 & i & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

$$iSWAP|01\rangle = i|10\rangle \qquad iSWAP|10\rangle = i|01\rangle$$

### Narrative

The iSWAP gate exchanges the |01⟩ and |10⟩ computational basis states while introducing an imaginary phase factor i to each exchanged component, leaving |00⟩ and |11⟩ unchanged. It is simultaneously a state exchange operation and a maximally entangling operation — combining both information routing and entanglement generation within a single gate application. The iSWAP gate is the native two-qubit gate of superconducting qubit architectures based on XY-type qubit-qubit coupling, directly realizing the π/2 rotation of the XY interaction Hamiltonian H = g(X⊗X + Y⊗Y)/2. Its inverse is the iSWAP† gate with exchange entries −i, enacting the time-reversed phase-exchange operation. The dual routing-and-entanglement character of the iSWAP gate makes it the most operationally efficient two-qubit gate in hardware architectures requiring both operations simultaneously.

---

## Entity 26: Square Root of SWAP

**Gate Annotation:** √SWAP (also denoted **half-swap**) — The partial exchange gate. Enacts a partial exchange advancing exactly halfway between identity and full SWAP, generating maximal entanglement as a consequence of incomplete exchange. (√SWAP)² = SWAP. Maximally entangling gate. Together with single-qubit rotations forms a universal gate set. Exchange subspace block is structurally equivalent to √X.

$$\sqrt{SWAP} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & \frac{1+i}{2} & \frac{1-i}{2} & 0 \\ 0 & \frac{1-i}{2} & \frac{1+i}{2} & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

$$(\sqrt{SWAP})^2 = SWAP \qquad \sqrt{SWAP}|01\rangle = \frac{(1+i)|01\rangle + (1-i)|10\rangle}{2}$$

### Narrative

The Square root of SWAP gate enacts a partial exchange of quantum information between two qubits — halting the exchange at the halfway point and generating maximal entanglement as a direct consequence of the incomplete transfer. Defined by (√SWAP)² = SWAP, it acts trivially on {|00⟩, |11⟩} and enacts a partial complex rotation within the {|01⟩, |10⟩} exchange subspace whose 2×2 block is structurally equivalent to the single-qubit √X gate. The maximal entanglement generated from computational basis exchange subspace inputs follows precisely from the incompleteness of the transfer — the quantum information is equally distributed between both register positions simultaneously, the defining condition of maximal entanglement. Applied twice, the transfer completes and the system disentangles back to a separable state with exchanged registers. Together with single-qubit rotations, the Square root of SWAP forms a universal gate set for quantum computation.

---

## Entity 27: Fermionic SWAP

**Gate Annotation:** FSWAP (also denoted **fSWAP**) — The fermionic exchange gate. Performs standard SWAP for |00⟩, |01⟩, |10⟩ states while applying phase factor −1 to |11⟩. Encodes fermionic anticommutation relation: simultaneous occupation of both modes under exchange generates antisymmetric sign. Self-inverse: FSWAP² = I. Decomposable as FSWAP = SWAP·CZ. Eliminates Jordan-Wigner string overhead in fermionic quantum simulation circuits.

$$FSWAP = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & -1 \end{pmatrix}$$

$$FSWAP|11\rangle = -|11\rangle \qquad FSWAP = SWAP \cdot CZ$$

### Narrative

The Fermionic SWAP gate is the quantum gate representation of the exchange operation for fermionic modes — performing the standard SWAP exchange for |00⟩, |01⟩, and |10⟩ computational basis states while applying a phase factor of −1 to the |11⟩ state, directly encoding the fermionic anticommutation relation that arises when two simultaneously occupied modes are exchanged. Decomposable as FSWAP = SWAP·CZ, it is self-inverse — FSWAP² = I — with the two −1 phase applications at |11⟩ canceling under double application. In quantum chemistry simulation circuits using the Jordan-Wigner encoding, the Fermionic SWAP gate eliminates the need for separate Jordan-Wigner string correction sequences after each routing operation by incorporating the antisymmetry phase correction directly into the exchange primitive, reducing fermionic simulation circuit gate counts by a factor proportional to system size.

---

## Entity 28: CZ-SWAP

**Gate Annotation:** CZ-SWAP (also denoted **CZSWAP**) — Combined Controlled-Z phase and SWAP exchange gate. Applies −1 to |11⟩ state and exchanges |01⟩↔|10⟩ simultaneously. Matrix identical to Fermionic SWAP: CZ-SWAP = FSWAP. Commutativity identity: CZ·SWAP = SWAP·CZ = CZ-SWAP. Self-inverse. Achieves factor-of-two circuit depth reduction for combined phase-and-exchange operations.

$$CZ\text{-}SWAP = SWAP \cdot CZ = CZ \cdot SWAP = FSWAP$$

$$CZ\text{-}SWAP|11\rangle = -|11\rangle \qquad (CZ\text{-}SWAP)^2 = I$$

### Narrative

The CZ-SWAP gate combines the Controlled-Z phase operation and the SWAP exchange operation into a single unified gate — applying a conditional −1 phase to the |11⟩ state while simultaneously exchanging the |01⟩ and |10⟩ states and leaving |00⟩ unchanged. Its matrix is formally identical to the Fermionic SWAP — CZ-SWAP = FSWAP — establishing the two as the same physical operation described through complementary interpretive frameworks: the CZ-SWAP notation foregrounds the explicit circuit composition CZ·SWAP, while the FSWAP notation foregrounds the fermionic physics interpretation. The commutativity of CZ and SWAP — CZ·SWAP = SWAP·CZ = CZ-SWAP — reflects their non-overlapping actions on distinct degrees of freedom of the two-qubit state space, enabling their composition into a single gate that achieves a factor-of-two circuit depth reduction for operations requiring both phase control and state exchange on the same qubit pair.

---

---

# CLASS E: ENTANGLING OPERATORS

**Class Annotation:** Two-qubit gates generating entanglement through non-Clifford interaction structures — operations in the non-Clifford sector of SU(4). Analyzed through the KAK (Cartan) decomposition framework: U = (A₁⊗A₂)·e^(i(cₓX⊗X + cᵧY⊗Y + c_zZ⊗Z))·(B₁⊗B₂). Gate position in the Weyl chamber (cₓ, cᵧ, c_z) is the primary structural descriptor of non-local entangling character.

---

## Entity 29: Controlled-V (controlled square root NOT)

**Gate Annotation:** CV (also denoted **controlled-√X**) — Applies √X to target if control is |1⟩. Block diagonal with identity block (control-0) and √X block (control-1). CV² = CNOT. Partially entangling non-Clifford gate. Intermediate position in Weyl chamber between identity and CNOT. Used in Toffoli gate decompositions requiring fewer CNOT gates.

$$CV = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & \frac{1+i}{2} & \frac{1-i}{2} \\ 0 & 0 & \frac{1-i}{2} & \frac{1+i}{2} \end{pmatrix}$$

$$CV^2 = CNOT \qquad CV|10\rangle = \frac{(1+i)|10\rangle + (1-i)|11\rangle}{2}$$

### Narrative

The Controlled-V gate applies the Square root of X transformation to a target qubit conditioned on the control qubit being in |1⟩, leaving the target unchanged when the control is in |0⟩. Defined by the property CV² = CNOT, it is the two-qubit conditional extension of the single-qubit √X gate — the intermediate half-step in the two-application completion of the conditional bit flip. A partially entangling non-Clifford gate, it maps the activating input |10⟩ to the complex superposition ((1+i)|10⟩ + (1−i)|11⟩)/2 — a maximally entangled state within the control-one subspace — at an intermediate level of total two-qubit entanglement between zero and the CNOT maximum. The square root relationship CV² = CNOT establishes it as the conditional analog of the single-qubit √X gate and enables its use in Toffoli gate decompositions that achieve fewer two-qubit gate applications than the standard six-CNOT decomposition.

---

## Entity 30: Core Entangling / Canonical Decomposition Gate

**Gate Annotation:** U_d (also denoted **KAK gate**, **canonical gate**, **Ud(cₓ, cᵧ, c_z)**) — Three-parameter family defining the complete non-local entangling content of any two-qubit unitary via the KAK decomposition. Defined as e^(i(cₓX⊗X + cᵧY⊗Y + c_zZ⊗Z)). Every two-qubit gate expressed as U = (A₁⊗A₂)·Ud·(B₁⊗B₂). Special cases: Ud(π/4,0,0)=CNOT, Ud(π/4,π/4,0)=iSWAP, Ud(π/4,π/4,π/4)=SWAP.

$$U_d(c_x, c_y, c_z) = e^{i(c_x X\otimes X + c_y Y\otimes Y + c_z Z\otimes Z)}$$

$$U_d\left(\frac{\pi}{4}, 0, 0\right) = CNOT \quad U_d\left(\frac{\pi}{4}, \frac{\pi}{4}, 0\right) = iSWAP \quad U_d\left(\frac{\pi}{4}, \frac{\pi}{4}, \frac{\pi}{4}\right) = SWAP$$

### Narrative

The Core Entangling gate Ud(cₓ, cᵧ, c_z) is the three-parameter family that defines the complete non-local entangling content of the two-qubit unitary group through the KAK decomposition theorem — the mathematical result establishing that every U ∈ SU(4) is expressible as U = (A₁⊗A₂)·Ud(cₓ, cᵧ, c_z)·(B₁⊗B₂) with uniquely determined interaction coefficients. The parameter space of (cₓ, cᵧ, c_z) forms the Weyl chamber — the complete geometric classification of two-qubit entangling operations — containing the CNOT at (π/4,0,0), iSWAP at (π/4,π/4,0), and SWAP at (π/4,π/4,π/4) as special cases. This gate is not a single fixed gate but the complete three-parameter family spanning all two-qubit entangling operations. In quantum circuit compilation, the KAK decomposition extracts the interaction coefficients from any target two-qubit unitary, providing the universal two-qubit intermediate representation used by all major quantum computing software stacks — Qiskit, Cirq, PennyLane — for optimal two-qubit gate synthesis.

---

## Entity 31: Givens Rotation Gate

**Gate Annotation:** G(θ) (also denoted **Givens gate**, **partial fermionic exchange**) — Real-amplitude rotation within the {|01⟩, |10⟩} exchange subspace by angle θ. Leaves |00⟩ and |11⟩ unchanged. Real orthogonal matrix in exchange subspace — member of both U(4) and O(4). Two-qubit analog of the single-qubit Ry gate. Direct quantum realization of the classical Givens rotation of numerical linear algebra. Primary entangling primitive for particle-number-preserving quantum chemistry circuits.

$$G(\theta) = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & \cos\theta & -\sin\theta & 0 \\ 0 & \sin\theta & \cos\theta & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

$$G(\theta)|01\rangle = \cos(\theta)|01\rangle + \sin(\theta)|10\rangle \qquad G(\pi/2) = SWAP$$

### Narrative

The Givens gate enacts a continuously parameterized real orthogonal rotation within the {|01⟩, |10⟩} exchange subspace of the two-qubit Hilbert space, leaving the {|00⟩, |11⟩} invariant subspace unchanged. The exchange subspace block is precisely the classical Givens rotation matrix of numerical linear algebra — establishing a direct mathematical correspondence between the quantum gate and the elementary orthogonal transformation used in QR decomposition and singular value decomposition. The Givens gate is the two-qubit analog of the single-qubit Ry gate: both enact purely real orthogonal rotations within a two-dimensional real subspace, generating real-amplitude superposition states from basis inputs without introducing imaginary phase factors. It preserves particle number in the fermionic occupation number encoding — mapping states with equal fermion counts to equal-fermion-count superpositions — making it the natural entangling primitive for particle-number-preserving quantum chemistry simulation circuits and the elementary operation of Givens rotation network ansatz circuits for electronic structure calculation.

---

## Entity 32: Magic Gate

**Gate Annotation:** M (also denoted **M gate**) — Transforms the computational basis to the Bell basis: M|00⟩ = |Φ+⟩, M|01⟩ = |Ψ+⟩, M|10⟩ = |Ψ−⟩, M|11⟩ = |Φ−⟩. Maximally entangling gate — lies on the maximally entangling surface of the Weyl chamber. Canonical basis transformation between computational and Bell bases. Two-qubit analog of the Hadamard gate.

$$M = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 0 & 0 & i \\ 0 & i & 1 & 0 \\ 0 & i & -1 & 0 \\ 1 & 0 & 0 & -i \end{pmatrix}$$

$$M|00\rangle = |\Phi^+\rangle \quad M|01\rangle = |\Psi^+\rangle \quad M|10\rangle = |\Psi^-\rangle \quad M|11\rangle = |\Phi^-\rangle$$

### Narrative

The Magic gate is the two-qubit gate that transforms the computational basis into the Bell basis — the four maximally entangled two-qubit states — mapping each of the four computational basis states to a distinct Bell state in a single gate application. Where the CNOT gate generates maximally entangled Bell states from only specific superposition inputs, the Magic gate generates a distinct maximally entangled Bell state from every computational basis input without exception. It lies on the maximally entangling surface of the Weyl chamber — the set of two-qubit gates achieving maximum average entangling power. The Magic gate is the two-qubit analog of the single-qubit Hadamard gate: both convert the most local basis description into the most non-local basis description through a complete and systematic basis transformation. Through its inverse M†, it implements Bell basis measurement — the joint measurement primitive of quantum teleportation, superdense coding, and entanglement-based quantum key distribution protocols.

---

## Entity 33: Berkeley B Gate

**Gate Annotation:** B (also denoted **Berkeley gate**) — Maximally entangling gate with minimum CNOT decomposition complexity. KAK position: (cₓ, cᵧ, c_z) = (π/4, π/8, 0). Requires only one CNOT gate for exact implementation — the minimum CNOT count achievable by any maximally entangling gate. Unique intersection of maximum entangling power and minimum implementation complexity on the maximally entangling surface.

$$\text{KAK position: } (c_x, c_y, c_z) = \left(\frac{\pi}{4}, \frac{\pi}{8}, 0\right) \qquad B = U_d\left(\frac{\pi}{4}, \frac{\pi}{8}, 0\right)$$

$$\text{Entangling power: maximum} \qquad \text{CNOT decomposition cost: 1 (minimum among maximally entangling gates)}$$

### Narrative

The Berkeley B gate is the two-qubit maximally entangling gate identified at the University of California, Berkeley as the member of the maximally entangling surface of the Weyl chamber requiring the minimum CNOT decomposition cost. Defined by KAK interaction coefficients (cₓ, cᵧ, c_z) = (π/4, π/8, 0) — maximum-strength XX interaction combined with half-strength YY interaction and zero ZZ interaction — it achieves maximum average entangling power while requiring only a single CNOT gate plus single-qubit operations for its exact implementation. Most maximally entangling gates require two CNOT gates for their decomposition; the Berkeley B gate achieves the same maximum entanglement at half the CNOT cost, making it the most CNOT-efficient maximally entangling gate in the complete taxonomy. This dual optimality — maximum entanglement, minimum CNOT complexity — positions the Berkeley B gate at the precise optimal intersection of entanglement generation and implementation efficiency on the Weyl chamber's maximally entangling surface.

---

## Entity 34: Barenco Gate

**Gate Annotation:** A (also denoted **Barenco gate**) — Continuously parameterized controlled-rotation gate introduced by Barenco et al. as a universal two-qubit primitive. Applies a general single-qubit rotation to the target conditioned on the control qubit being in |1⟩. Parameterized by angles (α, φ, θ). Together with single-qubit gates forms a universal gate set for quantum computation. Historically significant as a primitive in early universal quantum gate set proofs.

$$A(\alpha, \phi, \theta) = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & e^{i\alpha}\cos\theta & -ie^{i(\alpha-\phi)}\sin\theta \\ 0 & 0 & -ie^{i(\alpha+\phi)}\sin\theta & e^{i\alpha}\cos\theta \end{pmatrix}$$

### Narrative

The Barenco gate is the continuously parameterized controlled-rotation two-qubit gate introduced by Adriano Barenco and colleagues in their foundational 1995 paper establishing universal gate sets for quantum computation. It applies a parameterized single-qubit rotation — controlled by angles α, φ, and θ — to the target qubit conditioned on the control qubit being in |1⟩, leaving both qubits unchanged when the control is in |0⟩. The Barenco gate is universal for quantum computation when combined with single-qubit gates — a single Barenco gate at appropriate parameter values can implement any two-qubit interaction through appropriate parameter choices. Its historical significance lies in its role as the primitive through which Barenco et al. proved that almost any two-qubit gate is universal for quantum computation — establishing the foundational result that universality is a generic property of two-qubit gates rather than a special property of specific constructions, and providing the theoretical underpinning for the practical quantum gate set design that followed.

---

---

# CLASS F: THREE-QUBIT OPERATORS

**Class Annotation:** Gates acting on three-qubit registers through 8×8 unitary matrices. The minimal gate class introducing doubly-conditional logical relationships. Classical reversible logic primitives of quantum computing: Toffoli gate alone is universal for reversible classical computation; Toffoli + Hadamard is universal for quantum computation. Five members: Toffoli, Margolus, Fredkin, Peres, Deutsch.

---

## Entity 35: Toffoli Gate (controlled-controlled NOT)

**Gate Annotation:** CCX (also denoted **Toffoli**, **CCNOT**) — Applies Pauli X to target if and only if both control qubits are simultaneously in |1⟩. 8×8 permutation matrix. Self-inverse: CCX² = I. Universal for reversible classical computation. Toffoli + Hadamard = universal for quantum computation. Standard decomposition: 6 CNOT gates + 7 T/T† gates. Quantum reversible analog of classical AND gate.

$$CCX|abc\rangle = |ab, c\oplus ab\rangle$$

$$CCX|110\rangle = |111\rangle \qquad CCX|111\rangle = |110\rangle$$

$$CCX^2 = I \qquad CCX \text{ universal for reversible classical computation}$$

### Narrative

The Toffoli gate applies the Pauli X transformation to a target qubit if and only if both of two control qubits are simultaneously in |1⟩, leaving the target unchanged in all six non-activating configurations. The quantum reversible analog of the classical AND gate, it implements the AND function of the two control qubit values in the target qubit through a reversible XOR operation — mapping |110⟩ to |111⟩ and |111⟩ to |110⟩ while leaving all other computational basis states unchanged. Self-inverse and simultaneously unitary and Hermitian, it is named after Tommaso Toffoli who introduced it in 1980 as the foundational primitive of reversible classical computation. Its classical universality — any Boolean circuit is implementable through Toffoli gates and initialized ancilla qubits — combined with the Hadamard gate's superposition generation produces the most economical known universal gate set for quantum computation: Toffoli + Hadamard. The standard decomposition requires 6 CNOT gates and 7 T/T† gates — the highest decomposition cost in the three-qubit operator class — making Toffoli count minimization a central circuit optimization objective in fault-tolerant quantum computing.

---

## Entity 36: Margolus Gate (simplified Toffoli)

**Gate Annotation:** RC (also denoted **Margolus gate**, **relative phase Toffoli**) — Implements doubly-controlled NOT on computational basis states while introducing −1 phase factors at |011⟩ and |101⟩. Identical to Toffoli in all computational basis measurements. Requires only 3 CNOT gates vs. 6 for Toffoli — factor-of-two reduction. Not self-inverse: RC² ≠ I. Applicable wherever Toffoli is used purely as a computational basis oracle.

$$RC|abc\rangle = CCX|abc\rangle \text{ (measurement outcomes)} \qquad RC|011\rangle = -|011\rangle \qquad RC|101\rangle = -|101\rangle$$

$$\text{CNOT cost: 3 (vs. 6 for Toffoli)} \qquad RC^2 \neq I$$

### Narrative

The Margolus gate implements the doubly-controlled NOT operation on all eight computational basis states — producing identical measurement outcomes to the Toffoli gate — while introducing phase factors of −1 at the |011⟩ and |101⟩ non-activating states. This phase relaxation condition — allowing specific non-activating states to acquire unobservable phase factors in computational basis measurements — enables a factor-of-two reduction in CNOT decomposition cost: 3 CNOT gates versus the 6 required by the standard Toffoli decomposition. The Margolus gate is applicable as a direct Toffoli replacement in all quantum circuit contexts where correctness is determined exclusively by computational basis measurement outcomes — including oracle-based quantum algorithms where the gate's output is measured rather than used as input to further quantum interference operations. Not self-inverse — RC² ≠ I — the Margolus gate is the canonical example of the relative phase Toffoli design principle: exploiting quantum phase freedom in non-activating subspaces as a circuit optimization resource.

---

## Entity 37: Fredkin Gate (controlled SWAP)

**Gate Annotation:** CSWAP (also denoted **Fredkin gate**, **CS**) — Applies SWAP to two target qubits if control is |1⟩; leaves both unchanged if control is |0⟩. 8×8 permutation matrix with identity block (control-0) and SWAP block (control-1). Self-inverse: CSWAP² = I. Universal for reversible classical computation. Quantum analog of classical controlled multiplexer. Enables quantum swap test protocols.

$$CSWAP|0ab\rangle = |0ab\rangle \quad CSWAP|101\rangle = |110\rangle \quad CSWAP|110\rangle = |101\rangle \quad CSWAP|100\rangle = |100\rangle \quad CSWAP|111\rangle = |111\rangle$$

$$CSWAP^2 = I \qquad \text{Minimum decomposition: 5 two-qubit gates}$$

### Narrative

The Fredkin gate applies the complete SWAP exchange operation to two designated target qubits conditioned on a control qubit being in |1⟩, leaving both target qubits unchanged when the control is in |0⟩. The quantum reversible analog of the classical controlled multiplexer, it implements conditional information routing — selectively exchanging qubit states between register positions based on a classical or quantum control signal. Self-inverse and simultaneously unitary and Hermitian, it is named after Edward Fredkin who introduced it in 1982 as an independently universal primitive for reversible classical computation — any Boolean function is implementable through Fredkin gate networks and initialized ancilla qubits. With the control in superposition, the Fredkin gate generates three-qubit entanglement between the control and the exchange configuration of the targets — the basis of quantum swap test protocols that estimate the overlap between two unknown quantum states through control qubit interference measurements, used in quantum machine learning and quantum state certification.

---

## Entity 38: Peres Gate

**Gate Annotation:** PG (also denoted **Peres gate**) — Combines Toffoli doubly-controlled NOT and CNOT singly-controlled NOT in a single three-qubit gate. Action: |a, b⊕a, c⊕ab⟩. Self-inverse: PG² = I. Requires 4 CNOT gates vs. 7 for separate Toffoli+CNOT. Computes AND and XOR simultaneously — the core operations of one-bit binary addition. Primary quantum full adder primitive.

$$PG|abc\rangle = |a, b\oplus a, c\oplus ab\rangle$$

$$PG^2 = I \qquad \text{CNOT cost: 4 (vs. 7 for Toffoli + CNOT separately)}$$

### Narrative

The Peres gate combines the doubly-controlled NOT of the Toffoli gate and the singly-controlled NOT of the CNOT gate into a single unified three-qubit operation — implementing the Boolean function |a, b⊕a, c⊕ab⟩ that simultaneously computes the XOR of the first and second qubits (b⊕a) in the second output and the AND of the first and second qubits XORed with the third (c⊕ab) in the third output. Self-inverse and requiring only 4 CNOT gates for its decomposition versus 7 for separate Toffoli+CNOT implementation, the Peres gate achieves simultaneous AND-XOR computation — the two elementary arithmetic operations constituting one-bit binary addition — in a single gate application. This direct correspondence to the sum-carry computation of quantum full adder circuits establishes the Peres gate as the primary quantum arithmetic primitive for binary addition and the canonical example of the combined gate operation principle: exploiting algebraic relationships between multiple Boolean functions to achieve lower quantum resource cost than separately implemented gate sequences.

---

## Entity 39: Deutsch Gate

**Gate Annotation:** D(θ) (also denoted **Deutsch gate**) — The unique continuously parameterized three-qubit gate. Enacts parameterized rotation within doubly-activated {|110⟩, |111⟩} subspace by angle θ, leaving all six non-activating states unchanged. D(π/2) = i·CCX (Toffoli up to global phase). The first explicitly identified universal quantum gate primitive (Deutsch, 1985). Universal for quantum computation combined with single-qubit rotations. Only non-permutation gate in the Three-Qubit Operator class.

$$D(\theta)|110\rangle = i\cos(\theta)|110\rangle + \sin(\theta)|111\rangle$$
$$D(\theta)|111\rangle = \sin(\theta)|110\rangle + i\cos(\theta)|111\rangle$$

$$D\left(\frac{\pi}{2}\right) = i \cdot CCX \qquad D(\theta)|abc\rangle = |abc\rangle \text{ for } (a,b) \neq (1,1)$$

### Narrative

The Deutsch gate is the three-qubit gate introduced by David Deutsch in 1985 as the first explicitly identified universal quantum gate primitive — enacting a continuously parameterized rotation within the doubly-activated {|110⟩, |111⟩} subspace by angle θ while leaving all six non-activating computational basis states unchanged. Its 2×2 activated subspace block has diagonal entries i·cos(θ) and off-diagonal entries sin(θ) — a general complex unitary rotation that reduces to the Toffoli gate up to global phase at θ = π/2: D(π/2) = i·CCX. The unique continuously parameterized member of the Three-Qubit Operator class and the only non-permutation gate in that class, the Deutsch gate's universality was established in the 1985 paper "Quantum theory, the Church-Turing principle and the universal quantum computer" — the foundational demonstration that any unitary transformation on any number of qubits is approximable by finite sequences of Deutsch gates and single-qubit operations, establishing the quantum circuit model as computationally complete. Its continuous rotation parameter θ provides the non-Clifford resource that, combined with doubly-conditional activation structure, enables the generation of arbitrary quantum interference patterns within the activated subspace.

---

---

## Key Technical Relationships

| Relationship | Expression |
|---|---|
| Pauli group closure | X² = Y² = Z² = I; XY = iZ, YZ = iX, ZX = iY |
| Clifford generators | {H, S, CNOT} generates n-qubit Clifford group |
| Gottesman-Knill theorem | Clifford circuits are classically simulable |
| Hadamard conjugation | HXH = Z, HZH = X, HYH = −Y |
| Square root hierarchy | T² = S, S² = Z, (√X)² = X, H² = I |
| Phase gate special cases | R1(π) = Z, R1(π/2) = S, R1(π/4) = T |
| CZ-CNOT equivalence | CZ = (I⊗H)·CNOT·(I⊗H) |
| SWAP decomposition | SWAP = CNOT₁₂·CNOT₂₁·CNOT₁₂ |
| FSWAP decomposition | FSWAP = SWAP·CZ |
| Bell state generation | (H⊗I)·CNOT|00⟩ = |Φ+⟩ |
| Euler decomposition | U = Rz(α)Ry(β)Rz(γ) for any SU(2) |
| KAK decomposition | U = (A₁⊗A₂)·Ud(cₓ,cᵧ,c_z)·(B₁⊗B₂) for any SU(4) |
| CV square root | CV² = CNOT |
| Toffoli universality | CCX + ancilla → any Boolean function |
| Deutsch reduces to Toffoli | D(π/2) = i·CCX |
| Solovay-Kitaev | Clifford+T approximates any SU(2) to ε in O(log^c(1/ε)) gates |

---

## Glossary of Mathematical Notation

| Symbol | Meaning |
|--------|---------|
| ⟩\|ψ⟩ | Quantum state (Dirac ket notation) |
| ⊗ | Tensor product |
| U† | Conjugate transpose (Hermitian adjoint) of U |
| σₓ, σᵧ, σ_z | Pauli matrices X, Y, Z |
| e^(iθ) | Complex phase factor: cos(θ) + i·sin(θ) |
| SU(2) | Special unitary group in 2 dimensions |
| SU(4) | Special unitary group in 4 dimensions |
| U(2) | Unitary group in 2 dimensions |
| |Φ+⟩, |Ψ±⟩, |Φ−⟩ | Bell states (maximally entangled two-qubit states) |
| ⊕ | XOR (exclusive OR) operation |
| F₂ | Two-element field {0, 1} |
| ebit | Unit of entanglement (one Bell pair) |

---

*Document compiled from the complete session record.*
*All 39 gate entities: Gate Annotation, Prime Archetypal Analysis (7 archetypes), and Narrative.*
*Formatted for GitHub Markdown rendering.*

---
**© 2026 Per David Sannes** This work, including the Archetypal Taxonomy and semantic frameworks, is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/). 

*The underlying software execution core (TUI v01) is licensed separately under the MIT License. See the `LICENSE` file in the repository root for full details.*
---
