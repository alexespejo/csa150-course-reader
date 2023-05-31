import os

files = ["A.astro", "B.astro", "C.astro", "D.astro", "E.astro"]
html_code = '''
---
import Layout from "../../../layouts/Layout.astro";
import Header from "../../../components/Header.astro";
---

<Layout title="Week 1" dir="w01/E" prev="" next="">

</Layout>'''

for file_name in files:
    with open(file_name, "w") as file:
        file.write(html_code)

print("Files created successfully!")
