class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating new instance")
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# 1. Basic Logger Singleton
# Implement a logger that stores log messages in memory.

# 🔧 Requirements:
# Create a Logger class using the Singleton pattern.

# Add a method log(message) to store logs.

# Add a method get_logs() to return all logs.

class Logger:

    _instance = None
    _logs = []

    def __new__(cls):
        if cls._instance is None:
            print("Creating new instance")
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
    
    def logs(self, message):
        self._logs.append(message)
    
    def get_logs(self):
        return self._logs
    
# 2. App Configuration Manager
# Build a Singleton that stores app settings.

# 🔧 Requirements:
# Create Config class using Singleton.

# Method: set(key, value) and get(key)

# Store all key-value pairs in a dictionary.

class Logger:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating new instance")
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance._data = {}
        return cls._instance
    
    def set(self, key, value):
        self._data[key] = value

    def get(self,key):
        return self._data.get(key, None)