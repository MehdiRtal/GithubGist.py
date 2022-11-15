import requests

class GitHubGist:
    def __init__(self, token):
        self.token = token

    def get_gists(self):
        r = requests.get("https://api.github.com/gists", headers={"auth": self.token})
        if r.status_code != 200:
            raise Exception(r.text)
        return r.json()

    def get_gist(self, id):
        r = requests.get(f"https://api.github.com/gists/{id}", headers={"auth": self.token})
        if r.status_code != 200:
            raise Exception(r.text)
        return r.json()

    def update_gist(self, id, filename, content):
        r = requests.patch(f"https://api.github.com/gists/{id}", headers={"auth": self.token}, json={"files": {filename: {"content": content}}})
        if r.status_code != 200:
            raise Exception(r.text)
    
    def get_files(self, gist: get_gist):
        return gist["files"]

    def get_file(self, gist: get_gist, filename):
        return gist["files"][filename]