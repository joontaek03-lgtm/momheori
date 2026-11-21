"""운동 이미지를 index.html 안에 넣어 주는 도구.

index.html의 EX_IMG에 적힌 경로(예: 'media/ex/13_버드독.webp')를 읽어,
그 파일들을 data URI로 바꿔 <script id="ex-img-data"> 블록에 넣습니다.
이렇게 하면 index.html 파일 하나만 Netlify에 올려도 이미지가 보입니다.

사용법 (맘편한허리_시네마틱 폴더에서):  python3 tools/embed_images.py
"""
import base64
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / "index.html"
START = '<script id="ex-img-data">'
END = "</script>"
MIME = {".webp": "image/webp", ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg"}

html = PAGE.read_text(encoding="utf-8")
block = re.search(r"const EX_IMG = \{(.*?)\n\};", html, re.S).group(1)
paths = [p for p in re.findall(r":'([^']*)'", block) if p]

data = {}
for p in paths:
    f = ROOT / p
    if not f.exists():
        raise SystemExit(f"이미지 파일이 없어요: {p}")
    b64 = base64.b64encode(f.read_bytes()).decode()
    data[p] = f"data:{MIME[f.suffix.lower()]};base64,{b64}"

new = START + "window.EX_IMG_DATA=" + json.dumps(data, ensure_ascii=False) + ";" + END
i = html.find(START)
if i >= 0:
    j = html.index(END, i) + len(END)
    html = html[:i] + new + html[j:]
else:
    html = html.replace("<script>\nconst ARROW", new + "\n<script>\nconst ARROW", 1)
PAGE.write_text(html, encoding="utf-8")
print(f"이미지 {len(data)}개를 넣었어요 ({len(new) // 1024}KB)")
