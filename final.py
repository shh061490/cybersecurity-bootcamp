import requests
import pandas as pd

def main():
    try:
        # Fetch comments from API
        response = requests.get("https://jsonplaceholder.typicode.com/comments")
        response.raise_for_status()

        # Load data into DataFrame
        data = response.json()
        df = pd.DataFrame(data)

        # Group by email and count comments
        result = df.groupby("email")["id"].count().reset_index(name="comment_count")

        # Save result to CSV
        result.to_csv("comments.csv", index=False)
        print("Data saved to comments.csv")
        print(result.head())

    except requests.RequestException as e:
        print(f"API error: {e}")
    except IOError as e:
        print(f"File error: {e}")

if __name__ == "__main__":
    main() 