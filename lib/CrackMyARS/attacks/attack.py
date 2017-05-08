class Attack(object):
    def __init__(self):
        self.params = None
        self.func = None
        self.name = None

    def should_work(self, args):
        for param in self.params:
            if not (param in args and type(args[param]) == type(self.params[param])):
                return False
        return True
