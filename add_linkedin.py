with open('index.html', 'r') as f:
    content = f.read()

# Add LinkedIn to social links
# Look for existing social links pattern
linkedin_html = '''                <li>
                    <a href="https://www.linkedin.com/in/muziwakhe-sitsha-31478b375/" target="_blank" title="LinkedIn">
                        <i class="fab fa-linkedin" aria-hidden="true"></i>
                        <span class="screen-reader-text">LinkedIn</span>
                    </a>
                </li>'''

# Try to insert after other social links
if 'fab fa-github' in content:
    # Insert LinkedIn before GitHub or after another social link
    content = content.replace('fab fa-github', 'fab fa-linkedin-in"></i><span class="screen-reader-text">LinkedIn</span></a></li>\n' + '                <li>\n                    <a href="https://github.com/MuziSitsha" target="_blank" title="GitHub">\n                        <i class="fab fa-github', 1)
elif 'class="s-header__social"' in content:
    # Insert LinkedIn inside social list
    content = content.replace('class="s-header__social"', 'class="s-header__social"')
    # Find the ul and add LinkedIn as first item
    import re
    content = re.sub(r'(<ul[^>]*class="[^"]*s-header__social[^"]*"[^>]*>\s*)', r'\1' + linkedin_html + '\n', content)

with open('index.html', 'w') as f:
    f.write(content)

print("Added LinkedIn link")
