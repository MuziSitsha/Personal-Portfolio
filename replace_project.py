import re

with open('index.html', 'r') as f:
    content = f.read()

# Define the replacement HTML that matches your portfolio's structure
ai_health_html = '''            <div class="column" data-aos="fade-up">
                <div class="folio-item">
                    <div class="folio-item__thumb">
                        <a class="folio-item__thumb-link" href="https://raw.githubusercontent.com/MuziSitsha/ai-health-predictor/main/images/ai-health-predictor.png" Title="AI Health Predictor" data-size="1050x700">
                            <img src="https://raw.githubusercontent.com/MuziSitsha/ai-health-predictor/main/images/ai-health-predictor.png"
                                 srcset="https://raw.githubusercontent.com/MuziSitsha/ai-health-predictor/main/images/ai-health-predictor.png 1x" alt="AI Health Predictor">
                        </a>
                    </div>
                    <div class="folio-item__info">
                        <div class="folio-item__cat">AI Health Predictor</div>
                        <h4 class="folio-item__title">Machine Learning Web Application</h4>
                    </div>
                    <a href="https://ai-health-predictor-kaknzejwgvtneyqpxzsm5b.streamlit.app/" title="Launch App" class="folio-item__project-link" target="_blank">Live Demo</a>
                    <a href="https://github.com/MuziSitsha/ai-health-predictor" title="View Code" class="folio-item__project-link" target="_blank" style="margin-left: 10px;">GitHub</a>
                    <div class="folio-item__caption">
                        <p>A machine learning web application that predicts potential health risks using patient data. Built with Random Forest Classifier, Scikit-learn, and deployed with Streamlit.</p>
                        <p><strong>Technologies:</strong> Python, Scikit-learn, Streamlit, Pandas, NumPy, Matplotlib</p>
                    </div>
                </div>
            </div> <!-- end column -->'''

# Find the exact Lula Power App section (lines 259-282 based on your output)
# We need to replace from line 259 to line 282
lines = content.split('\n')
new_lines = []
i = 0
while i < len(lines):
    if 'Lula Power App' in lines[i] and i > 250 and i < 290:
        # We found the Lula Power App section
        # Skip the entire section (we'll replace it)
        # Find where this column ends
        j = i
        column_start = None
        while j >= 0:
            if 'class="column" data-aos="fade-up"' in lines[j]:
                column_start = j
                break
            j -= 1
        
        if column_start is not None:
            # Find where this column ends
            k = column_start
            column_count = 0
            while k < len(lines):
                if '<!-- end column -->' in lines[k]:
                    column_count += 1
                    if column_count == 1:  # Found the end of this column
                        # Add the new AI Health Predictor HTML
                        new_lines.append(ai_health_html)
                        i = k + 1  # Skip to after the end column comment
                        break
                k += 1
            else:
                # If we didn't find end column, just skip this line
                i += 1
        else:
            # If we didn't find column start, just skip this line
            i += 1
    else:
        new_lines.append(lines[i])
        i += 1

# Join back
new_content = '\n'.join(new_lines)

# Write back
with open('index.html', 'w') as f:
    f.write(new_content)

print("Replaced Lula Power App with AI Health Predictor")
