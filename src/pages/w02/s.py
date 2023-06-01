import os

folders = ['A', 'B', 'C', 'D', 'E']
file_content = '''
---
import Layout from "../../../layouts/Layout.astro";
import Header from "../../../components/Header.astro";
const { no_layout } = Astro.props;
---
<Layout title="Week 1" dir="w01/{folder}" prev="" next="" uselayout={no_layout}>
    <Header id="w02/{folder}"></Header>
</Layout>'''

# Get the directory of the Python file
current_directory = os.path.dirname(os.path.abspath(__file__))

for folder in folders:
    folder_path = os.path.join(current_directory, folder)
    os.makedirs(folder_path, exist_ok=True)

    for i in range(1, 6):
        file_name = f'{folders[i-1]}.astro'
        file_path = os.path.join(folder_path, file_name)

        with open(file_path, 'w') as file:
            file.write(file_content.replace('{folder}', folder))