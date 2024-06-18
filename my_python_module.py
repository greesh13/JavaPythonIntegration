from py4j.java_gateway import JavaGateway

class PythonClass:
    def __init__(self):
        self.gateway = JavaGateway()
        self.my_java_class = self.gateway.entry_point.getMyJavaClass()

    def add(self, a, b):
        return self.my_java_class.add(a, b)

    def subtract(self, a, b):
        return self.my_java_class.subtract(a, b)

# Create an instance of PythonClass
python_class = PythonClass()

# Call the Java methods
result_add = python_class.add(10, 5)
result_subtract = python_class.subtract(10, 5)

print(f"Addition Result: {result_add}")        # Output: 15
print(f"Subtraction Result: {result_subtract}") # Output: 5
