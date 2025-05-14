class IdGenerator:

    # словник що зберігає лічильникт об'єктів
    _counters = {}

    @classmethod
    def get_next_id(cls, prefix):
        if prefix not in cls._counters:
            cls._counters[prefix] = 1

        next_id = f"{prefix}_{cls._counters[prefix]}"
        cls._counters[prefix] += 1

        return next_id