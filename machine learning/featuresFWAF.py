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


# import yara

# class PayloadAnalyzer:
#     def __init__(self):
#         self.rules = yara.compile(source=self.get_yara_rule())
    
#     def get_yara_rule(self):
#         # Define YARA rule for detecting malicious payloads
#         rule = """
#         rule MaliciousPayload {
#             strings:
#                 $malicious_string = "malicious_string"
#             condition:
#                 $malicious_string
#         }
#         """
#         return rule

#     def analyze_payload(self, payload):
#         features = []

#         # Extract length of the payload
#         length = len(payload)
#         features.append(length)

#         # Check if payload matches any malicious pattern
#         if self.rules.match(data=payload):
#             features.append("malicious")
#             label = 1
#         else:
#             features.append("normal")
#             label = 0

#         return features, label

#     def process_dataset(self, dataset):
#         processed_data = []

#         for payload in dataset:
#             features, label = self.analyze_payload(payload)
#             processed_data.append((payload, features[0], features[1], label))

#         return processed_data

# # Example usage:
# payload_analyzer = PayloadAnalyzer()
# dataset = ["normal_payload1", "malicious_payload1", "normal_payload2"]
# processed_dataset = payload_analyzer.process_dataset(dataset)
# for data in processed_dataset:
#     print(data)


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
