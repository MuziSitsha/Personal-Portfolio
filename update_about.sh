#!/bin/bash
# Read the file
content=$(cat index.html)

# Replace the About paragraph
new_content=$(echo "$content" | sed 's/<p class="lead">[^<]*<\/p>/<p class="lead">I am an AI\/ML Engineer passionate about building intelligent systems and data-driven solutions. My expertise spans machine learning, deep learning, and data science, with a focus on creating predictive models and scalable AI applications. I specialize in developing end-to-end machine learning pipelines and believe in leveraging AI to solve real-world problems.<\/p>/')

echo "$new_content" > index.html
echo "Updated About section"
