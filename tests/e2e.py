from selenium import webdriver

def test_scores_service(url):
    try:
        driver = webdriver.Chrome()
        driver.get(url)
        score_element = driver.find_element_by_id('score')
        score = int(score_element.text)
        return 1 <= score <= 1000
    except Exception as e:
        print(f"Test failed: {e}")
        return False

def main():
    test_url = "http://localhost:8777/score"  # Adjust URL as needed
    if test_scores_service(test_url):
        print("Scores web service test passed")
        return 0
    else:
        print("Scores web service test failed")
        return -1

if __name__ == "__main__":
    exit(main())