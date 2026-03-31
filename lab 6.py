class Map:

    LOAD_FACTOR = .75

    def __init__(self):
        self._buckets = []
        for bucket in range(11):
            self._buckets.append([])
        self._number_of_items = 0

    def _resize(self):
        new_buckets = []
        for bucket in range(len(self._buckets) * 2):
            new_buckets.append([])

        old_buckets = self._buckets

        self._buckets = new_buckets

        for bucket_index in range(len(old_buckets)):
            for pair in old_buckets[bucket_index]:
                self._buckets[self._get_bucket_index(pair[0])].append(pair)



    def _get_bucket_index(self, key):
        return hash(key) % len(self._buckets)

    def __setitem__(self, key, value):
        if self._number_of_items / len(self._buckets) >= self.LOAD_FACTOR:
            self._resize()

        bucket_index = self._get_bucket_index(key)
        for pairs in self._buckets[bucket_index]:
            if pairs[0] == key:
                pairs[1] = value
                return
        self._buckets[bucket_index].append([key, value])
        self._number_of_items += 1

    def __getitem__(self, key):
        bucket_index = self._get_bucket_index(key)
        for pairs in self._buckets[bucket_index]:
            if pairs[0] == key:
                return pairs[1]
        raise KeyError("not found")
import time

def test_map(load_factor):
    Map.LOAD_FACTOR = load_factor
    m = Map()

    start = time.time()

    for i in range(1_000_000):
        m[i] = i

    end = time.time()

    return end - start

small = test_map(0.25)
default = test_map(0.75)
large = test_map(2.0)

print("Load Factor 0.25:", small)
print("Load Factor 0.75:", default)
print("Load Factor 2.0:", large)