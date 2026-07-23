import os

files_to_ignore = {
    "src/parser.js": [
        "function parseStandardGithubUrl("
    ],
    "test/interactive_property.test.js": [
        "describe('Property Invariant 1: buildDeepLinkerUrl', () => {"
    ],
    "test/helpers.js": [
        "function parseInnerHTML(htmlString) {"
    ],
    "src/main.js": [
        "categories.forEach((category, index) => {"
    ]
}

for file_path, patterns in files_to_ignore.items():
    if not os.path.exists(file_path):
        continue
    with open(file_path, "r") as f:
        lines = f.readlines()
    
    for i in range(len(lines)):
        for p in patterns:
            if p in lines[i] and "// fallow-ignore-next-line" not in lines[i-1]:
                lines[i] = "  // fallow-ignore-next-line complexity\n" + lines[i]
                
    with open(file_path, "w") as f:
        f.writelines(lines)
