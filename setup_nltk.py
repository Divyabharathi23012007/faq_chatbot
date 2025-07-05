import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

def download_nltk_data():
    """Download required NLTK data files"""
    print("Downloading NLTK data files...")
    
    required_packages = [
        'punkt',
        'punkt_tab',
        'wordnet',
        'stopwords',
        'averaged_perceptron_tagger',
        'omw-1.4'
    ]
    
    for package in required_packages:
        try:
            print(f"Downloading {package}...")
            nltk.download(package, quiet=True)
            print(f"✓ {package} downloaded successfully")
        except Exception as e:
            print(f"✗ Error downloading {package}: {e}")
    
    print("\nNLTK setup complete!")

if __name__ == "__main__":
    download_nltk_data() 