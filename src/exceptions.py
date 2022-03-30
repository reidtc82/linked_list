class NonExistentNodeError(Exception):
    def __init__(self, message="Node does not exist"):
        self.message = message
        super().__init__(self.message)
