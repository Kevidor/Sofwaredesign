class Singleton:
    
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.path = "test_file.txt"

        return cls.__instance
    
    def print_id(self):
        print(id(self))

if __name__ == "__main__":

    s1 = Singleton()
    s2 = Singleton()
    s3 = Singleton()

    s1.print_id()
    s2.print_id()
    s3.print_id()
