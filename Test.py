import unittest
from get_cost_per_server import get_Cost_2 ,get_Cost_3,get_Cost_1
from InstanceAvail import instanceAvail
class TestAllocation(unittest.TestCase):
    """
    Our basic test class
    """
    def test_Cost1(self):
        res = get_Cost_1(instanceAvail,5,100)
        self.assertEqual(res[0].get('total_cost'), '$44.25')

    def test_Cost2(self):

        res = get_Cost_2(instanceAvail,5,10)
        self.assertEqual(res[0].get('total_cost'), '$7.68')
if __name__ == '__main__':
    unittest.main()

