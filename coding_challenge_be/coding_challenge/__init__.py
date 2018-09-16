from coding_challenge.core.coding_challenge import CodingChallenge

container = None


def bootstrap(env):
    _challenge = CodingChallenge(env)
    globals()['container'] = _challenge
    return container
