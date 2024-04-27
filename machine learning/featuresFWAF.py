import os
import sys
import argparse
import array
import math
import pickle
import pefile
import hashlib
import pandas as pd
import numpy as np
# import yara
import re
import csv 
# from peframe import Peframe

class ExtractFeatures():
    
    def __init__(self, dataset_file):
        self.dataset_file = dataset_file

    def extract_payload_features(self):
        features_list = []
        with open(self.dataset_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                payload = row['payload']
                features = self.get_payload_features(payload)
                features_list.append(features)
        return features_list

    def get_payload_features(self, payload):
        features = []

        # Length of payload
        features.append(len(payload))

        # Presence of certain keywords or patterns
        keywords = ['select', 'union', 'where', '<script>']
        keyword_presence = [1 if re.search(keyword, payload, re.IGNORECASE) else 0 for keyword in keywords]
        features.extend(keyword_presence)

        # Other payload-related features can be added here...

        return features

# Example usage
dataset_file = 'payload_full.csv'  # Replace with the path to your dataset file
feature_extractor = ExtractFeatures(dataset_file)
payload_features = feature_extractor.extract_payload_features()

# Saving the extracted features
with open('payload_features.pickle', 'wb') as f:
    pickle.dump(payload_features, f)

# Example of loading and using the saved features
with open('payload_features.pickle', 'rb') as f:
    loaded_payload_features = pickle.load(f)

print("Loaded payload features:")
for idx, features in enumerate(loaded_payload_features):
    print(f"Payload {idx+1} features:", features)
