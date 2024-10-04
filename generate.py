import os
import json

def process(glyph: dict):
    name = glyph.get("code-name", "")
    name = name.replace("-", "_")
    name = name.upper()
    code = glyph.get("codepoint", "")
    code = chr(code).encode("utf-8")
    formatted = "\\x".join([f"{b:02x}" for b in code])
    formatted = f"\\x{formatted}"
    return {
        "name": f"PF_{name}",
        "code": glyph.get("code", ""),
        "value": glyph.get("codepoint", ""),
        "formatted": formatted,
    }

metadata = os.path.join("promptfont", "glyphs.json")
with open(metadata, "r", encoding="utf-8") as f:
    glyphs = json.load(f)
    glyphs = [process(glyph) for glyph in glyphs]

source = os.path.join("include", "promptfont.h")
with open(source, "w") as f:
    print("#ifndef PROMPT_FONT_H", file=f)
    print("#define PROMPT_FONT_H", file=f)
    print(file=f)
    print('#define PF_ICON_FONT_FILE_NAME "promptfont.ttf"', file=f)
    print(file=f)
    print("// clang-format off", file=f)
    align = max([len(glyph["name"]) for glyph in glyphs])
    for glyph in glyphs:
        name = glyph["name"]
        code = glyph["code"]
        format = glyph["formatted"]
        padding = " " * (align - len(name) + 2)
        print(f'#define {name}{padding} \"{format}\" // {code}', file=f)
    print("// clang-format on", file=f)
    print(file=f)

    print("// clang-format off", file=f)
    for glyph in glyphs:
        name = glyph["name"]
        code = glyph["code"]
        value = glyph["value"]
        padding = " " * (align - len(name) + 2)
        print(f'#define {name}_HEX{padding} 0x{value:x} // {code}', file=f)
    print("// clang-format on", file=f)

    print(file=f)
    print("#endif // PROMPT_FONT_H", file=f)
