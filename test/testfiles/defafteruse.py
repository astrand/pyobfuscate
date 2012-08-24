
import sys

class Server:
    def fun(self):
        agenthost = "arne"
        return get_fortytwo(agenthost,kwarg=42)

def get_fortytwo(agenthost, kwarg=3):
    foo = agenthost
    return kwarg

s = Server()

sys.exit(s.fun())
