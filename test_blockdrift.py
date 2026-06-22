# test_blockdrift.py
"""
Tests for BlockDrift module.
"""

import unittest
from blockdrift import BlockDrift

class TestBlockDrift(unittest.TestCase):
    """Test cases for BlockDrift class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockDrift()
        self.assertIsInstance(instance, BlockDrift)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockDrift()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
