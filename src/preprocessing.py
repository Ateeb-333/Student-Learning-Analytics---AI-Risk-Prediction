class DataPreprocessor:
    def __init__(self, features):
        self.features = features

    def normalize(self):
        """Apply min-max normalization for all features."""
        # Extract all values for each column
        keys = list(next(iter(self.features.values())).keys())
        mins = {k: float('inf') for k in keys}
        maxs = {k: float('-inf') for k in keys}

        for student, vals in self.features.items():
            for k, v in vals.items():
                mins[k] = min(mins[k], v)
                maxs[k] = max(maxs[k], v)

        # Scale values
        scaled_data = {}
        for student, vals in self.features.items():
            scaled_data[student] = {
                k: (v - mins[k]) / (maxs[k] - mins[k]) if maxs[k] != mins[k] else 0
                for k, v in vals.items()
            }
        return scaled_data
