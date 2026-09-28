# Grover Search Lab

Grover search, amplitude amplification and iteration count⚛️.

A three-qubit oracle marks 101 in an eight-state space. Compare analytical success probabilities, exact Qiskit simulation and finite samples. Three iterations overshoot the first peak reached at two; later peaks can be higher, so k=2 is not a global optimum. Baseline k=0–8 and 4,096 simulated samples per circuit.

## التشغيل

ثبت المكتبات وشغل التجربة من هذا المجلد⬅️

```bash
python -m pip install -r requirements.txt
python grover_search_lab.py --target 101 --max-iterations 8 --shots 4096
python -m unittest discover -s tests -v
```


يحتوي "experiment.ipynb" على الشرح والنتايج، افتحه في Jupyter او Colab لتشغيل الخلايا *ملاحظة مهمة : المحاكاة رح تصير معنا على Qiskit مو على جهاز كمي فعليا❗️

 References: [Qiskit Statevector](https://quantum.cloud.ibm.com/docs/en/api/qiskit/2.2/qiskit.quantum_info.Statevector), [Qiskit QuantumCircuit](https://quantum.cloud.ibm.com/docs/en/api/qiskit/2.2/qiskit.circuit.QuantumCircuit), [QWorld Bronze](https://qworld.net/workshop-bronze/), [QWorld Silver](https://qworld.net/qsilver/).
