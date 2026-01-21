with open('index.html', 'r') as f:
    content = f.read()

# Update About section text
import re

# Find About section and update the text
# Look for paragraphs after About heading
about_section = re.search(r'(<h3[^>]*>About</h3>[\s\S]*?)(<p[^>]*>)[^<]*(</p>)', content)
if about_section:
    # Get the full match and positions
    full_match = about_section.group(0)
    before = about_section.group(1)
    p_tag = about_section.group(2)
    after = about_section.group(3)
    
    new_about_text = '''I am an AI/ML Engineer passionate about building intelligent systems and data-driven solutions. My expertise spans machine learning, deep learning, and data science, with a focus on creating predictive models and scalable AI applications.

I specialize in developing end-to-end machine learning pipelines - from data preprocessing and feature engineering to model development, deployment, and monitoring. My recent work includes healthcare prediction systems and various AI applications.

I believe in leveraging AI to solve real-world problems and create positive impact through technology.'''
    
    new_full = before + p_tag + new_about_text + after
    content = content.replace(full_match, new_full)

with open('index.html', 'w') as f:
    f.write(content)

print("Updated About section")
