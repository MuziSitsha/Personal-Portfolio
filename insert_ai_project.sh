#!/bin/bash
# Insert AI Health Predictor at line 259
head -258 index.html > temp1.html

cat > temp2.html << 'AIHTML'
            <div class="column" data-aos="fade-up">
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
            </div> <!-- end column -->
AIHTML

tail -n +259 index.html > temp3.html

cat temp1.html temp2.html temp3.html > index.html

rm temp1.html temp2.html temp3.html
echo "Inserted AI Health Predictor project"
