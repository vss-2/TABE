from requests import get
from json import loads
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("pkg", help="Target package to be updated.", type=str)

def download(file_name: str, url: str, file_type: str) -> bool:
    # By default, it overwrites files with same name
    with open(file_name+'.'+file_type, 'wb') as file:
        try:
            file.write(get(url, allow_redirects=True).content)
            return True
        except:
            return False

def guide(file_name: str, file_type: str):
    text = ""
    if file_type == "deb":
        text = f"sudo dpkg -i {file_name}.{file_type} !"
    
    print("Make sure to run:\n"+text)
    return

def main():
    latest_release = get("https://api.github.com/repos/brave/brave-browser/releases/latest").json()["tag_name"]
    # Response: 'v1.00.000'
    
    args = {}
    pkg = ""
    try:
        args = parser.parse_args()
        pkg = args.pkg
        print("Downloading "+pkg+" now!")
    except:
        print("Unknown or unidentified arguments. Try a different one.")

    if pkg == "brave":
        download(pkg, f"https://github.com/brave/brave-browser/releases/download/{latest_release}/brave-browser_{latest_release[1:]}_amd64.deb", "deb")
        guide(pkg, "deb")
    else:
        print("The package "+pkg+"is currently not supported!")

main()

