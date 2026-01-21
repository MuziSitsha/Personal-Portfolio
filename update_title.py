with open('index.html', 'r') as f:
    content = f.read()

# Update page title
content = content.replace('<title>Ethos</title>', '<title>Muziwakhe Sitsha - AI/ML Engineer</title>')

# Update meta description if it exists
if '<meta name="description" content="">' in content:
    content = content.replace(
        '<meta name="description" content="">',
        '<meta name="description" content="AI/ML Engineer specializing in machine learning, data science, and building intelligent systems. Portfolio showcasing AI projects and data science work.">'
    )

with open('index.html', 'w') as f:
    f.write(content)

print("Updated page title and description")
