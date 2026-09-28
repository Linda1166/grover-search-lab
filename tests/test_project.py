import unittest
import numpy as np
from qiskit.quantum_info import Operator,Statevector
from grover_search_lab import phase_oracle,diffuser,grover_circuit,theoretical_success,first_peak_iterations

class Tests(unittest.TestCase):
 def test_oracle_targets(self):
  for i in range(8):
   expected=np.eye(8,dtype=complex); expected[i,i]=-1
   np.testing.assert_allclose(Operator(phase_oracle(format(i,'03b'))).data,expected,atol=1e-12)
 def test_diffuser_matrix(self):
  for n in [2,3,4]:
   size=2**n; expected=2*np.ones((size,size))/size-np.eye(size)
   np.testing.assert_allclose(Operator(diffuser(n)).data,expected,atol=1e-12)
 def test_probabilities_and_first_peak(self):
  self.assertEqual(first_peak_iterations(3),2)
  np.testing.assert_allclose(theoretical_success(3,np.arange(4)),[.125,.78125,.9453125,.330078125],atol=1e-12)
  for i in range(8):
   target=format(i,'03b')
   for k in range(9):
    p=Statevector.from_instruction(grover_circuit(target,k)).probabilities()
    self.assertAlmostEqual(p[i],theoretical_success(3,k),places=11)
if __name__=='__main__': unittest.main()
