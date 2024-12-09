import pytest
from brute import Brute
from unittest.mock import Mock
import random

todo = pytest.mark.skip(reason='todo: pending spec')

def describe_Brute():


    def test_describe_bruteOnce():
       crack = Brute("awesomesauce")
       assert crack.bruteOnce("awesomesauce") == True

    def test_describe_brute_init_string():
       hash = Mock()
       Brute.hash = hash
       crack = Brute("awesomesauce")
       assert hash.call_count == 1
    
    def test_describe_brute_init_int():
       hash = Mock()
       Brute.hash = hash
       crack = Brute("1234567890")
       assert hash.call_count == 1

    def test_describe_brute_once():
        crack = Brute("awesomesauce")
        testing = crack.bruteOnce("awesomesauce")
        assert testing == True
    
    def test_bruteOnce_manytimes():
        for i in range(10):
            alfabet = ("abcdefghijklmnopqrstuvwxyz")
            random_number1 = random.randint(1, 25)
            random_number2 = random.randint(1, 25)
            random_number3 = random.randint(1, 25)
            string = (alfabet[random_number1], alfabet[random_number2], alfabet[random_number3])
            string = string[0] + string[1] + string[2]
            crack = Brute(string)
            assert crack.bruteOnce(string) == True
    
    def test_describe_bruteMany_random():
        crack = Brute("awesomesauce")
        random = Mock()
        crack.randomGuess = random
        crack.bruteMany(1)
        assert random.call_count == 1
    
    def bruteMany():
        crack = Brute("awesomesauce")
        random = Mock()
        crack.randomGuess = random
        crack.bruteMany()
        assert random.call_count == 1
    
    
    def test_describe_bruteMany_hash():
        crack = Brute("awesomesauce")
        random = Mock()
        crack.hash = random
        crack.bruteMany(1)
        assert random.call_count == 1
    
    def test_describe_bruteOnce_hash():
       crack = Brute("awesomesauce")
       hash = Mock()
       crack.hash = hash
       crack.bruteOnce("awesomesauce")
       assert hash.call_count == 1

    def test_describe_brute_init_string_fail():
       crack = Brute("awesomesauce")
       hash = Mock()
       crack.hash = hash
       crack.bruteOnce("awesomesauce")
       assert crack.bruteOnce("fail") == False

      
