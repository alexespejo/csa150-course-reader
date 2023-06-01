import os

files = ["A.astro", "B.astro", "C.astro", "D.astro", "E.astro"]
html_code = '''
---
import Layout from "../../../layouts/Layout.astro";
import Header from "../../../components/Header.astro";
const { no_layout } = Astro.props;
---

<Layout title="Week 1" dir="w01/B" prev="" next="" uselayout={no_layout}>
    <Header id="w01/B"></Header>
</Layout>'''

for file_name in files:
    with open(file_name, "w") as file:
        file.write(html_code)

print("Files created successfully!")
