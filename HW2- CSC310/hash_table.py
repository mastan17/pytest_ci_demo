class HashTable:
    """
    Custom hash table using open addressing and linear probing.
    Backed by dynamic array.
    """

    # Entry object stores a key/value pair inside the table
    class Entry:
        def __init__(self, key, value):
            self.key = key            # key used for lookup
            self.value = value        # stored value
            self.is_deleted = False   # marks slot as removed

    # constructor initializes table
    def __init__(self):
        self.capacity = 10           # starting size of array
        self.size = 0                # number of stored elements
        self.load_factor = 0.75      # resize threshold
        self.table = [None] * self.capacity

    # first hash function maps key to index
    def _hash1(self, key):
        return hash(key) % self.capacity

    # second hash function (step size)
    # returning 1 guarantees no infinite loops
    def _hash2(self, key):
        return 1

    # resize the array when load factor is exceeded
    # doubles the capacity and rehashes all entries
    def _resize(self):
        old_table = self.table
        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0

        # reinsert old entries into new table
        for entry in old_table:
            if entry is not None and not entry.is_deleted:
                self.insert(entry.key, entry.value)

    #insert a key/value pair into the table
    def insert(self, key, value):

        # resize if table is too full
        if self.size / self.capacity >= self.load_factor:
            self._resize()

        index = self._hash1(key)
        step = self._hash2(key)

        # probe until an empty slot is found
        while self.table[index] is not None and not self.table[index].is_deleted:

            # update value if key already exists
            if self.table[index].key == key:
                self.table[index].value = value
                return

            index = (index + step) % self.capacity

        # place new entry in open slot
        self.table[index] = HashTable.Entry(key, value)
        self.size += 1

    #retrieve value using a key
    def get(self, key):
        index = self._hash1(key)
        step = self._hash2(key)
        start_index = index

        # search until empty slot or full loop
        while self.table[index] is not None:

            entry = self.table[index]

            if not entry.is_deleted and entry.key == key:
                return entry.value

            index = (index + step) % self.capacity

            # stop if we loop back to start
            if index == start_index:
                break

        return None

    # remove a key/value pair
    def remove(self, key):
        index = self._hash1(key)
        step = self._hash2(key)
        start_index = index

        # search for the key
        while self.table[index] is not None:

            entry = self.table[index]

            if not entry.is_deleted and entry.key == key:
                entry.is_deleted = True
                self.size -= 1
                return True

            index = (index + step) % self.capacity

            if index == start_index:
                break

        return False

    # print underlying array
    def print_table(self):
        for entry in self.table:
            if entry is None or entry.is_deleted:
                print("-")
            else:
                print(str(entry.key) + " : " + str(entry.value))