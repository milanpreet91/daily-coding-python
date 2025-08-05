class MyHashMap:

    def __init__(self):
        self.data = [-1]*1000001

    def put(self, key: int, value: int) -> None:
        if key < len(self.data):
            self.data[key] = value
            return
        old = self.data
        self.data = [-1] * (key+1)
        for k, v in enumerate(old):
            self.data[k] = v
        print(f"Adding {key} : {value} with array len {len(self.data)}")
        self.data[key] = value

    def get(self, key: int) -> int:
        if key < len(self.data):
            return self.data[key]
        return -1

    def remove(self, key: int) -> None:
        if key < len(self.data):
            self.data[key] = -1
