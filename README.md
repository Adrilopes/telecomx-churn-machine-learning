<h1 align="center">🤖 TelecomX - Machine Learning for Customer Churn Prediction</h1>

<p align="center">
  Machine Learning project focused on predicting customer churn in a telecommunications company.
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python">
  <img alt="Pandas" src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas">
  <img alt="Scikit-Learn" src="https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?style=for-the-badge&logo=scikitlearn">
  <img alt="Matplotlib" src="https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge">
  <img alt="Seaborn" src="https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge">
</p>

<hr>

<h2>📌 Project Overview</h2>

<p>
This project applies <strong>Machine Learning techniques</strong> to predict customer churn in a telecommunications company.
The objective is to identify customers who are more likely to cancel the service and transform descriptive insights into predictive solutions that support <strong>data-driven decision-making</strong>.
</p>

<p>
This project is a continuation of the previous ETL and exploratory analysis stage, where the dataset was cleaned, standardized, and prepared for modeling.
</p>

<p>
🔎 <strong>Previous Project – ETL and Data Preparation:</strong><br>
<a href="https://github.com/Adrilopes/telecomx-churn-analysis" target="_blank">TelecomX Churn ETL Repository</a>
</p>

<hr>

<h2>🎯 Objectives</h2>

<ul>
  <li>Analyze customer churn patterns</li>
  <li>Prepare the dataset for machine learning</li>
  <li>Train predictive models to classify churn risk</li>
  <li>Compare model performance using classification metrics</li>
  <li>Identify the most relevant variables influencing churn</li>
  <li>Generate strategic business recommendations for retention</li>
</ul>

<hr>

<h2>🧠 Models Used</h2>

<ul>
  <li><strong>Logistic Regression</strong> – baseline model for binary classification</li>
  <li><strong>Random Forest</strong> – tree-based ensemble model for non-linear relationships</li>
</ul>

<p>
To handle the class imbalance problem, <strong>SMOTE</strong> was applied during model training.
Logistic Regression was trained using scaled data, while Random Forest was trained on non-scaled features.
</p>

<hr>

<h2>📂 Project Structure</h2>

<pre>
ml_churn_telecomx/
│
├── data/
│   └── churn_tratado.csv
│
├── notebooks/
│   └── analysis.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── train_model.py
│   └── evaluate_model.py
│
└── README.md
</pre>

<hr>

<h2>⚙️ Technologies and Libraries</h2>

<ul>
  <li>Python</li>
  <li>Pandas</li>
  <li>NumPy</li>
  <li>Scikit-learn</li>
  <li>Imbalanced-learn (SMOTE)</li>
  <li>Matplotlib</li>
  <li>Seaborn</li>
  <li>Jupyter Notebook</li>
</ul>

<hr>

<h2>🔍 Workflow</h2>

<ol>
  <li>Load the treated dataset</li>
  <li>Perform exploratory and descriptive analysis</li>
  <li>Encode categorical variables</li>
  <li>Split data into training and testing sets</li>
  <li>Handle class imbalance with SMOTE</li>
  <li>Scale features for Logistic Regression</li>
  <li>Train Logistic Regression and Random Forest models</li>
  <li>Evaluate models with:
    <ul>
      <li>Accuracy</li>
      <li>Precision</li>
      <li>Recall</li>
      <li>F1-score</li>
      <li>Confusion Matrix</li>
      <li>ROC Curve / AUC</li>
    </ul>
  </li>
  <li>Analyze feature importance</li>
  <li>Extract business insights and retention strategies</li>
</ol>

<hr>

<h2>📈 Main Results</h2>

<p>
Both models demonstrated good predictive performance, with <strong>AUC values above 0.80</strong>.
</p>

<ul>
  <li><strong>Logistic Regression</strong> achieved slightly better performance in detecting churn cases</li>
  <li><strong>Random Forest</strong> produced comparable results, but with slightly lower recall for the churn class</li>
</ul>

<p>
The results suggest that churn behavior in this dataset follows relatively linear patterns, which are effectively captured by Logistic Regression.
</p>

<hr>

<h2>📊 Key Insights</h2>

<ul>
  <li><strong>Tenure</strong> was one of the strongest variables related to churn</li>
  <li>Customers with <strong>shorter tenure</strong> are more likely to leave</li>
  <li><strong>Total charges</strong> and <strong>monthly charges</strong> are highly relevant predictors</li>
  <li><strong>Contract type</strong> strongly influences churn behavior</li>
  <li>Long-term contracts significantly reduce churn probability</li>
</ul>

<hr>

<h2>🎯 Strategic Recommendations</h2>

<ul>
  <li>Focus retention efforts on customers in the early months of their contracts</li>
  <li>Encourage long-term contracts through incentives or loyalty benefits</li>
  <li>Monitor customers with higher monthly charges who may present greater churn risk</li>
  <li>Promote automatic payment methods to improve customer retention</li>
  <li>Integrate predictive models into decision-making processes to proactively identify customers at risk</li>
</ul>

<hr>

<h2>🚀 How to Run the Project</h2>

<h3>1. Clone the repository</h3>

<pre><code>git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
</code></pre>

<h3>2. Create and activate a virtual environment</h3>

<pre><code>python -m venv .venv
source .venv/bin/activate
</code></pre>

<h3>3. Install dependencies</h3>

<pre><code>pip install pandas numpy matplotlib seaborn scikit-learn imbalanced-learn notebook
</code></pre>

<h3>4. Run the notebook</h3>

<pre><code>jupyter notebook
</code></pre>

<p>
Then open:
</p>

<pre><code>notebooks/analysis.ipynb
</code></pre>

<hr>

<h2>📌 Conclusion</h2>

<p>
This project demonstrates how customer churn data can be transformed into actionable business insights through machine learning.
By combining exploratory analysis, predictive modeling, and feature importance interpretation, it is possible to identify churn drivers and support more effective retention strategies.
</p>

<hr>

<h2>👩‍💻 Author</h2>

<p>
<strong>Adriely Lopes</strong><br>
Data Science student and developer passionate about transforming data into strategic solutions.
</p>

<p>
<a href="https://github.com/Adrilopes" target="_blank">GitHub</a> |
<a href="https://www.linkedin.com/in/adriely-lopes/?locale=en" target="_blank">LinkedIn</a>
</p>