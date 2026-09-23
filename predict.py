import joblib
import pandas as pd

# Load the model
loaded_model = joblib.load("phishing_url_detector.pkl")


def check_phishing(url):
    # Prepare feature in the exact trained order
    features = pd.DataFrame(
        [
            {
                "num_dots": url.count("."),
                "num_hyphens": url.count("-"),
                "num_at": url.count("@"),
                "num_digits": sum(c.isdigit() for c in url),
                "url_length": len(url),
            }
        ]
    )

    # Get prediction
    prediction = loaded_model.predict(features)
    return "Phishing" if prediction[0] == 1 else "Legitimate"


# Test one or multiple url
test_url = "http://login.youtube.com-verify8832.account-update.info/login@user"

# print result
print(f"Prediction: {check_phishing(test_url)}")
