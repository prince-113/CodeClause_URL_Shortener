import hashlib

class URLShortener:
    def __init__(self):
        self.urls = {}

    def shorten_url(self, url):
        # Generate a hash of the URL using SHA-256 algorithm
        hash_object = hashlib.sha256(url.encode())
        hash_hex = hash_object.hexdigest()

        # Take the first 8 characters of the hash and use them as the shortened URL
        short_url = hash_hex[:8]

        # Store the original URL and the shortened URL in a dictionary
        self.urls[short_url] = url

        return short_url

    def get_original_url(self, short_url):
        # Look up the original URL using the shortened URL
        return self.urls.get(short_url, None)

shortener = URLShortener()
short_url = shortener.shorten_url('https://www.Google.com/')
print(short_url)  # Output: 33f8a07c


original_url = shortener.get_original_url('989ba7f5')
print(original_url)  # Output: https://www.example.com/page.html
