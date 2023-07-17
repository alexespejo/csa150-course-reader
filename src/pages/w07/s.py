import os

folders = ['A', 'B', 'C', 'D', 'E']
files = [
    "A.astro", "B.astro", "C.astro", "D.astro", "E.astro", "F.astro",
    "G.astro", "H.astro", "I.astro"
]

index_code = '''
---
import Layout from "../../../layouts/Layout.astro";
import A from "./A.astro";
import B from "./B.astro";
import C from "./C.astro";
import D from "./D.astro";
import E from "./E.astro";
import F from "./F.astro";
---
<Layout
 title="CSA150 Course Reader"
 dir=""
 displayLayout={true}
 chapterSubSections={[]}
>
 <A displayLayout={false} />
 <B displayLayout={false} />
 <C displayLayout={false} />
 <D displayLayout={false} />
 <E displayLayout={false} />
 <F displayLayout={false} />
</Layout>'''


def getCode(fn):
    return '''---
import Layout from "../../../layouts/Layout.astro";
import Header from "../../../components/Header.astro";
const { useLayout } = Astro.props;
---
<Layout
title="Week 7"
dir="w07/"
displayLayout={useLayout}
chapterSubSections={[]}
>''' + f'<Header id="{fn[0]}">text</Header></Layout>'


# Get the directory of the Python script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create folders
for folder in folders:
    os.makedirs(os.path.join(script_dir, folder))

# Create files in each folder
for folder in folders:
    index_file = os.path.join(script_dir, folder, 'index.astro')
    with open(index_file, 'w') as f:
        f.write(index_code)

    for file in files:
        file_path = os.path.join(script_dir, folder, file)
        with open(file_path, 'w') as f:
            f.write(getCode(file))
