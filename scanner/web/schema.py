class Schema:
    def __init__(self, name: str, description: str, level: str, remediation: str):
        self.name = name
        self.description = description
        self.level = level
        self.remediation = remediation