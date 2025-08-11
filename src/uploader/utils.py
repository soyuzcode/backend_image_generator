import requests

def upload_temp_image(image_file):
    res = requests.post("https://file.io", files={'file': ('temp.png', image_file)})
    if res.status_code != 200:
        return None
    return res.json().get("link")

def call_p_api(temp_link, TOKEN:str|None, prompt:str|None=None, seed:int=0):

    if prompt is not None:
        prompt = ""

    res = requests.get(f"http://image.pollinations.ai/prompt/{prompt}?model=kontext&image={temp_link}&token={TOKEN}&seed={seed}&nologo=true")
    if res.status_code != 200:
        return None
    return res.content
