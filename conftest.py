# Import ALL fixtures from 'examples.py'
from tests.test_trans import data_bridge, setup_bridge, expected_probs
from tests.test_inference import setup_sys_rbd
from tests.test_cpm import setup_condition, setup_hybrid
from tests.test_brc import main_sys, setup_brs, setup_inference

#, setup_bridge_alt
# Import fixture_a and fixture_b from 'examples.py'
#from root.module.tests.fixtures.examples import fixture_a, fixture_b  
# Import all fixtures from list of plugins
#pytest_plugins = [
#            "root.module.tests.fixtures.examples",
#                "root.module.tests.fixtures.other_examples",
#                ]
