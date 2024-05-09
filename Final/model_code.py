import pandas as pd
import numpy as np
from urllib.parse import urlparse
import re
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, accuracy_score, recall_score, f1_score, roc_auc_score, mean_absolute_error
import pickle


def load_data(file_path):
    """Load the dataset from a CSV file."""
    csic_data = pd.read_csv(file_path)
    return csic_data


def preprocess_data(csic_data):
    """Preprocess the dataset, perform feature engineering, and encode categorical variables."""
    # Rename and select relevant columns
    csic_data = csic_data.rename(columns={'Unnamed: 0': 'Class', 'lenght': 'content_length'})
    feature_names = ['Class', 'Method', 'host', 'cookie', 'Accept', 'content_length', 'content', 'classification', 'URL']
    X = csic_data[feature_names]
    
    # Handle missing and numeric conversion issues
    X['content_length'] = X['content_length'].astype(str).str.extract(r'(\d+)').fillna(0).astype(int)

    # Define URL-based preprocessing functions
    def count_dot(url): return url.count('.')
    def no_of_dir(url): return urlparse(url).path.count('/')
    def no_of_embed(url): return urlparse(url).path.count('//')
    def shortening_service(url): return 1 if re.search(r'bit\.ly|goo\.gl', url) else 0
    def count_http(url): return url.count('http')
    def count_per(url): return url.count('%')
    def count_ques(url): return url.count('?')
    def count_hyphen(url): return url.count('-')
    def count_equal(url): return url.count('=')
    def url_length(url): return len(url)
    def hostname_length(url): return len(urlparse(url).netloc)
    def suspicious_words(url):
        return sum(word in url.lower() for word in ['error', 'select', 'password'])
    def digit_count(url): return sum(char.isdigit() for char in url)
    def letter_count(url): return sum(char.isalpha() for char in url)
    def count_special_characters(url): return len(re.sub(r'[a-zA-Z0-9\s]', '', url))

    # Apply these functions to the URL column
    X['count_dot_url'] = X['URL'].apply(count_dot)
    X['count_dir_url'] = X['URL'].apply(no_of_dir)
    X['count_embed_domain_url'] = X['URL'].apply(no_of_embed)
    X['short_url'] = X['URL'].apply(shortening_service)
    X['count-http'] = X['URL'].apply(count_http)
    X['count%_url'] = X['URL'].apply(count_per)
    X['count?_url'] = X['URL'].apply(count_ques)
    X['count-_url'] = X['URL'].apply(count_hyphen)
    X['count=_url'] = X['URL'].apply(count_equal)
    X['url_length'] = X['URL'].apply(url_length)
    X['hostname_length_url'] = X['URL'].apply(hostname_length)
    X['sus_url'] = X['URL'].apply(suspicious_words)
    X['count-digits_url'] = X['URL'].apply(digit_count)
    X['count-letters_url'] = X['URL'].apply(letter_count)
    X['special_count_url'] = X['URL'].apply(count_special_characters)

    # Encode categorical variables
    lb_make = LabelEncoder()
    X["Method_enc"] = lb_make.fit_transform(X["Method"])
    X["host_enc"] = lb_make.fit_transform(X["host"])
    X["Accept_enc"] = lb_make.fit_transform(X["Accept"])

    # Select features and target
    labels = [
        'count_dot_url', 'count_dir_url', 'count_embed_domain_url', 'count-http',
        'count%_url', 'count?_url', 'count-_url', 'count=_url', 'url_length', 'hostname_length_url',
        'sus_url', 'count-digits_url', 'count-letters_url', 'Method_enc'
    ]
    X = X[labels]
    y = csic_data['classification']

    return X, y


def train_model(X, y):
    """Train a machine learning model using a random forest classifier."""
    x_tr, x_ts, y_tr, y_ts = train_test_split(X, y, test_size=0.3, random_state=0)

    random_forest_model = RandomForestClassifier(random_state=1000)
    random_forest_model.fit(x_tr, y_tr)
    predictions = random_forest_model.predict(x_ts)

    # Calculate metrics
    metrics = {
        "MAE": mean_absolute_error(y_ts, predictions),
        "Accuracy": accuracy_score(y_ts, predictions),
        "Precision": precision_score(y_ts, predictions, average='weighted', labels=np.unique(predictions)),
        "Recall": recall_score(y_ts, predictions, average='weighted', labels=np.unique(predictions)),
        "F1": f1_score(y_ts, predictions, average='weighted', labels=np.unique(predictions)),
        "ROC AUC": roc_auc_score(y_ts, predictions, average='weighted', labels=np.unique(predictions)),
        "Error Rate": (predictions != y_ts).mean()
    }

    return random_forest_model, metrics


def save_model(model, file_path='model.pkl'):
    """Save the trained model to a file."""
    with open(file_path, 'wb') as file:
        pickle.dump(model, file)


def main():
    """Main function to execute preprocessing and model training."""
    # Load and preprocess data
    csic_data = load_data('csic_database.csv')
    X, y = preprocess_data(csic_data)

    # Train the model
    model, metrics = train_model(X, y)
    print("Training metrics:", metrics)

    # Save the model
    save_model(model, 'model.pkl')
    print('Model saved successfully!')


if __name__ == "__main__":
    main()



import pandas as pd
import pickle

class URLChecker:
    def __init__(self, data_path='combined_balanced_urls.csv'):
        """Initialize the URL checker with a specific dataset path."""
        self.data_path = data_path
        self.data = pd.read_csv(self.data_path)

    def check_url(self, url: str) -> int:
        """Check the status of a given URL in the dataset.

        Args:
            url (str): The URL to check.

        Returns:
            int: 0 if the URL is found and benign, otherwise 1.
        """
        found = self.data[self.data['url'] == url]
        if not found.empty and found.iloc[0]['label'] == 'benign':
            return 0
        else:
            return 1

# Create an instance and specify the path to the CSV file
checker = URLChecker('combined_balanced_urls.csv')  # Update with actual path

# Save the instance to a pickle file
with open('url_checker.pkl', 'wb') as f:
    pickle.dump(checker, f)

# Load the instance from the pickle file
with open('url_checker.pkl', 'rb') as f:
    loaded_checker = pickle.load(f)

# Example usage of the loaded checker
test_url = "mp3raid.com/music/krizz_kaliko.html"
result = loaded_checker.check_url(test_url)
print(f"URL check result for {test_url}: {result}")
