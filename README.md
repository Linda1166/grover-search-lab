# ✦ Grover Search Lab ✦

**Grover search, amplitude amplification and iteration count⚛️❗️**

A three-qubit oracle marks 101 in an eight-state space. Compare analytical success probabilities, exact Qiskit simulation and finite samples. Three iterations overshoot the first peak reached at two; later peaks can be higher, so k=2 is not a global optimum. Baseline  k=0–8 and 4,096 simulated samples per circuit.

## Run

 Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1`. Then run:

```bash
python -m pip install -r requirements.txt
python grover_search_lab.py --target 101 --max-iterations 8 --shots 4096
python -m unittest discover -s tests -v
```

References: [Qiskit Statevector](https://quantum.cloud.ibm.com/docs/en/api/qiskit/2.2/qiskit.quantum_info.Statevector), [Qiskit QuantumCircuit](https://quantum.cloud.ibm.com/docs/en/api/qiskit/2.2/qiskit.circuit.QuantumCircuit), [QWorld Bronze](https://qworld.net/workshop-bronze/), [QWorld Silver](https://qworld.net/qsilver/).
