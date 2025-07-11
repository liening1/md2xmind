import sys
import xmind
from xmind.core.topic import TopicElement

def parse_md_to_tree(md_lines):
    tree = []
    stack = []
    for line in md_lines:
        if line.strip().startswith('#'):
            level = len(line) - len(line.lstrip('#'))
            title = line.strip('#').strip()
            node = {'level': level, 'title': title, 'children': []}
            while stack and stack[-1]['level'] >= level:
                stack.pop()
            if stack:
                stack[-1]['children'].append(node)
            else:
                tree.append(node)
            stack.append(node)
    return tree

def add_nodes(parent_topic, nodes):
    for node in nodes:
        topic = parent_topic.addSubTopic()
        topic.setTitle(node['title'])
        add_nodes(topic, node['children'])

def md_to_xmind(md_path, xmind_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        md_lines = f.readlines()
    tree = parse_md_to_tree(md_lines)
    workbook = xmind.load(xmind_path)
    sheet = workbook.getPrimarySheet()
    sheet.setTitle("Mindmap")
    root_topic = sheet.getRootTopic()
    root_topic.setTitle(tree[0]['title'] if tree else "Root")
    add_nodes(root_topic, tree[0]['children'] if tree else [])
    xmind.save(workbook, xmind_path)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python md2xmind.py input.md output.xmind")
        sys.exit(1)
    md_to_xmind(sys.argv[1], sys.argv[2])
    print("Conversion complete!") 