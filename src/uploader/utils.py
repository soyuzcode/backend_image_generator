import requests

def upload_temp_image(image_file):
    res = requests.post("https://file.io", files={'file': ('temp.png', image_file)})

    try:
        data = res.json()
    except ValueError:
        print("Error parsing JSON response")
        return None

    if res.status_code != 200:
        return None
    
    return data.get("link")

def call_p_api(temp_link, TOKEN:str|None, prompt:str|None=None, seed:int=0):

    if prompt is None:
        prompt = ""

    res = requests.get(f"http://image.pollinations.ai/prompt/{prompt}?model=kontext&image=https://i.postimg.cc/g2Cg4SvW/image.png&token={TOKEN}&seed={seed}&nologo=true")
    if res.status_code != 200:
        return None
    return res.content
