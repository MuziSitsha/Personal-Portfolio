with open('index.html', 'r') as f:
    content = f.read()

# Update the name and add AI/ML Engineer title
# Based on typical portfolio structure, we'll update the h1
content = content.replace('Muziwakhe Sitsha', 'Muziwakhe Sitsha<br><span class="ai-ml-title">AI/ML Engineer</span>')

# Look for intro text and update it
# Find section with typical intro text pattern
import re

# Try to find and update intro paragraph
intro_pattern = r'(<p[^>]*class="[^"]*intro[^"]*"[^>]*>)[^<]*(</p>)'
if re.search(intro_pattern, content):
    content = re.sub(intro_pattern, r'\1AI/ML Engineer specializing in machine learning, data science, and building intelligent systems\2', content)
else:
    # Try another common pattern
    intro_pattern2 = r'(<p[^>]*class="[^"]*lead[^"]*"[^>]*>)[^<]*(</p>)'
    if re.search(intro_pattern2, content):
        content = re.sub(intro_pattern2, r'\1Passionate about creating data-driven solutions and intelligent systems. Experienced in end-to-end ML pipelines from data preprocessing to deployment.\2', content)

with open('index.html', 'w') as f:
    f.write(content)

print("Updated hero section")
