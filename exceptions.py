class AmbroBotException(Exception):
    """All handled exceptions inherit from it"""
    pass


class InvalidMoneyCode(AmbroBotException):
    pass