init -1 python:
    register_language(name="日本語", id="japanese", subtitle_text="japanese", uifont_path="tl/japanese/fonts/MPLUS1-Medium.ttf",
                      dialoguefont_path="tl/japanese/fonts/851tegaki.ttf", breaking_method="japanese-loose", locale="ja", script=None,
                      region=None, version="1.0")

init python:
    TooltipComment("japanese_2A", "初心者が経験や知識がないにもかかわらず、偶然の幸運で良い結果を出す現象")
    TooltipComment("japanese_2B","韓国語発音はアジッカジヌン")
    TooltipComment("japanese_2C","いわゆる\"含み\"")
    TooltipComment("japanese_TRANSLATE","ここまでは人による翻訳が完了していますが、以降は機械翻訳です。")