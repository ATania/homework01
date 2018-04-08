import hello_world
from io import StringIO
import sys

def test_say_hello():
    assert hasattr(hello_world, 'say_hello'), "Your Script must have an 'say_hello'-function!"

    mystdout = StringIO()
    sys.stdout = mystdout
    hello_world.say_hello()

    assert mystdout.getvalue() == 'hello world\n'
