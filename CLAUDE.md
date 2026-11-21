# 맘편한 허리 웹페이지

- 웹페이지 본체: `맘편한허리_시네마틱/index.html` (파일 하나에 디자인·기능·이미지가 모두 들어 있음)
- 공개 사이트: Netlify (https://silly-baklava-aca9a4.netlify.app). 사용자가 `index.html`을 Netlify 배포 화면에 직접 끌어다 놓아 반영한다.
- 사용자는 한국어로, 휴대폰에서 주로 작업한다. 쉬운 말로 짧게 설명한다.

## 운동 사진 추가 순서

사용자가 운동 사진을 보내면 매번 이렇게 한다.

1. 사진을 가로 800px WebP(품질 80)로 줄여 `맘편한허리_시네마틱/media/ex/<번호>_<이름>.webp`로 저장한다.
   번호·이름은 운동 이미지 프롬프트 목록(1–27번)을 따른다. 예: `13_버드독.webp`
2. `index.html`의 `EX_IMG`에서 해당 운동 이름의 값을 `'media/ex/<파일명>.webp'`로 채운다.
3. `맘편한허리_시네마틱` 폴더에서 `python3 tools/embed_images.py`를 실행해 사진을 `index.html` 안에 넣는다.
4. 결과 화면과 시기별 운동 페이지에서 사진이 나오는지 확인한다. 이미지 칸은 4:3, `object-fit: contain`이라 사진이 잘리지 않는다.
5. 커밋·푸시하고, 새 `index.html`을 사용자에게 보내며, 미리보기 아티팩트(https://claude.ai/artifact/GRGxkK9jxap8EVgvh2wBGr)도 같은 내용으로 업데이트한다.

사진의 자세가 웹페이지의 운동 설명과 다르면 넣기 전에 사용자에게 알린다.
