import re

# Read the file
with open('index.html', 'r') as f:
    content = f.read()

# The AI Health Predictor HTML
ai_health_predictor_html = '''<div class="project-card">
    <img src="https://raw.githubusercontent.com/MuziSitsha/ai-health-predictor/main/images/ai-health-predictor.png" alt="AI Health Predictor" class="project-image">
    <div class="project-content">
        <h3>AI Health Predictor</h3>
        <p>A machine learning web application that predicts potential health risks using patient data. Built with Random Forest Classifier and Streamlit for deployment.</p>
        <div class="tech-stack">
            <span class="tech-tag">Python</span>
            <span class="tech-tag">Scikit-learn</span>
            <span class="tech-tag">Streamlit</span>
            <span class="tech-tag">Pandas</span>
            <span class="tech-tag">NumPy</span>
        </div>
        <div class="project-links">
            <a href="https://ai-health-predictor-kaknzejwgvtneyqpxzsm5b.streamlit.app/" target="_blank" class="project-link">Live Demo</a>
            <a href="https://github.com/MuziSitsha/ai-health-predictor" target="_blank" class="project-link">GitHub</a>
        </div>
    </div>
</div>'''

# Try to find and replace Lula Power App section
# This pattern looks for a div containing "Lula Power App"
pattern = r'<div class="project-card">[\s\S]*?Lula Power App[\s\S]*?</div>\s*</div>\s*</div>'

# Try replacement
new_content = re.sub(pattern, ai_health_predictor_html, content, flags=re.DOTALL)

# If pattern not found, try simpler pattern
if new_content == content:
    print("Pattern 1 not found, trying simpler pattern...")
    # Try a simpler pattern
    pattern2 = r'Lula Power App[\s\S]*?</div>\s*</div>\s*</div>'
    new_content = re.sub(pattern2, ai_health_predictor_html, content, flags=re.DOTALL)

# Write back
with open('index.html', 'w') as f:
    f.write(new_content)

print("Replacement attempted. Check index.html for changes.")
