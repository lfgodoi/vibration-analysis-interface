"""

Class: Processing

"""

# Importing packages and modules
from sources.classes.time_processing import TimeProcessing
from sources.classes.frequency_processing import FrequencyProcessing

# Signal processing class
class Processing:

    # Constructor
    def __init__(self, sampling_frequency):
        self.sampling_frequency = sampling_frequency

    # Time and frequency domain processing
    def run(self, samples):
        time_processing = TimeProcessing()
        time_processing.run(samples)
        frequency_processing = FrequencyProcessing(self.sampling_frequency)
        frequency_processing.run(samples)
        self.time_features = time_processing.features
        self.frequency_features = frequency_processing.features

