import pandas as pd
from sklearn.ensemble import AdaBoostClassifier
import re
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
import pickle
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier

# List of common SQL injection keywords and patterns
SQL_INJECTION_PATTERNS = [
    "select", "union", "insert", "update", "delete", "drop", "table", "information_schema",
    "--", ";", "/", "/", "@@", "char", "concat", "xp_", "sp_", "exec", "' OR '1'='1"
]

def contains_sql_injection(text):
    """
    Check if the input text contains any potential SQL injection keywords/patterns.
    """
    text_lower = text.lower()
    for pattern in SQL_INJECTION_PATTERNS:
        if pattern in text_lower:
            return True
    return False

# Feature Extraction Function
def extract_features_from_url(url):
    """
    Extracts HTTP request features from a given URL.

    Args:
    - url (str): The URL to extract features from.

    Returns:
    - pd.DataFrame: A DataFrame containing the extracted features.
    """
    http_request = {
        'Unnamed':'0',
        'Method': 'GET',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8',
        'Accept-encoding': 'gzip, deflate, br',
        'Accept-charset': 'UTF-8',
        'language': 'en-US,en;q=0.5',
        'host': '',
        'cookie': 'JSESSIONID=ABCDE12345',
        'content-type': 'application/x-www-form-urlencoded',
        'connection': 'keep-alive',
        'lenght': 'Content-Length: 123',
        'content': 'param1=value1&param2=value2',
        'URL': url
    }

    # Extract host and path from the URL
    url_parts = re.match(r"(http[s]?://)?([^/]+)(/.*)", url)
    if url_parts:
        http_request['host'] = url_parts.group(2)

    # Convert length to numeric
    http_request['lenght'] = re.findall(r'\d+', http_request['lenght'])
    http_request['lenght'] = int(http_request['lenght'][0]) if http_request['lenght'] else 0

    # Create a DataFrame from the HTTP request dictionary
    extracted_features_df = pd.DataFrame([http_request])

    return extracted_features_df

# Load and preprocess dataset (assumes a CSV file named 'csic_database.csv')
file_path = 'csic_database.csv'
data = pd.read_csv(file_path)

# Drop unnecessary columns and isolate features and labels
data_clean = data.drop(['Unnamed: 0'], axis=1)
features = data_clean.drop(['classification'], axis=1)
labels = data_clean['classification']

# Convert 'lenght' to numeric, replacing invalid values with NaN
features['lenght'] = pd.to_numeric(features['lenght'].str.extract('(\d+)')[0], errors='coerce')
features['lenght'].fillna(features['lenght'].median(), inplace=True)

# Define columns to preprocess
numeric_features = ['lenght']
categorical_features = ['Method', 'Pragma', 'Cache-Control', 'Accept', 'Accept-encoding', 'Accept-charset', 'language', 'host', 'cookie', 'content-type', 'connection']

# Create preprocessor and model pipelines
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ])

# Replace the classifier with an AdaBoost model
classifier = AdaBoostClassifier(DecisionTreeClassifier(max_depth=4, min_samples_leaf=50,random_state=1),
                           n_estimators=500,
                           learning_rate=0.05,
                           random_state=1
)

model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', classifier)
])

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.25, random_state=42)

# Train the model
model_pipeline.fit(X_train, y_train)

# Evaluate the model
accuracy = model_pipeline.score(X_test, y_test)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save the trained model
model_path = 'ml_model.pkl'
with open(model_path, 'wb') as model_file:
    pickle.dump(model_pipeline, model_file)

print(f"Model saved to: {model_path}")

# Function to classify URLs
def classify_url(url):
    # Extract features from the URL
    new_features = extract_features_from_url(url)
    
    # Load the trained model
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
    
    # Predict
    prediction = model.predict(new_features)
    return prediction[0]

# Main function to check for SQL injection and classify URL
def analyze_url(url):
    # Check if the URL contains SQL injection patterns
    if contains_sql_injection(url):
        return "Potential SQL Injection detected!"
    else:
        # Classify the URL if it's clean
        return classify_url(url)

# Example usage
new_url = "https://miuegypt.edu.eg/"
result = analyze_url(new_url)
print(f"The analysis result for {new_url} is: {result}")