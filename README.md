# US-School-Learning-Modalities-Analytics

## Problem Statement

The School Learning Modalities dataset provides estimates of school learning modality (including in-person, remote, or hybrid learning) for U.S. charter school districts for the 2021-2022 school year. The goal of this project is to gather information that how people interects with different learning modalities as well as the operating schools and students of different States of USA from [this website](https://healthdata.gov/National/School-Learning-Modalities-2021-2022/aitj-yx37).<br/>
Later I utilized the scraped data to understand some demographics and correlations using Tableau Dashboard.
The public dashboard is also attached [here](https://public.tableau.com/app/profile/minhaj.uddin4733/viz/USASchoolLearningModalitiesDataVisualization/PrimaryVisualizations).

## Tableau [Dashboard](https://public.tableau.com/app/profile/minhaj.uddin4733/viz/USASchoolLearningModalitiesDataVisualization/PrimaryVisualizations)

1. This dashboard represents total students, total operational schools and learning modalities applied by the students of each states of USA.<br/>
<img src = "dashboard_images\primary_viz.jpg" width="700" height="350">

2. This dashboard represents students, average operational schools of particular states of USA.<br/>
<img src = "dashboard_images\selective_viz.jpg" width="700" height="350">

3. A box plot to detect student outliers and a pie plot to highlight percentage of operational schools are attached in this dashboard.<br/>
<img src = "dashboard_images\calculative_viz.jpg" width="700" height="350">

4. Total operational schools and standard deviation of operational schools are visualized in this dashboard.<br/>
<img src = "dashboard_images\calculative_viz2.jpg" width="700" height="350">

5. A overview of all the given information in the dataset are represented as different visualization in this dashboard.<br/>
<img src = "dashboard_images\overview.jpg" width="700" height="350">

## Findings and Observations from the [Dashboard](https://public.tableau.com/app/profile/minhaj.uddin4733/viz/USASchoolLearningModalitiesDataVisualization/PrimaryVisualizations)

1. California(CA) state has the highest number of operational schools and the most number of students.
2. In this era of globalization, people still extremely prefer In Person learning method over Remote or Hybrid lerning method.
3. Total Students in each state is (almost) proportionate to total operational schools in these states.
4. Alaska(AK) is the largest U.S. state by area, comprising more total area than the next three largest states of Texas(TX), California(CA), and Montana(MT) combined meanwhile it is the third-least populous and most sparsely populated U.S. state. That's why, it has only 956 operational schools and 301,416 students.
5. Los Angeles, the city of California(CA) topped with total number of students having 978,491 students.
6. Most number of students admitted on 20th november, 2022 in California(CA).

## Build from Sources

1. Clone the repo

```bash
 git clone https://github.com/ripon5098/US-School-Learning-Modalities-Project.git
 ```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Download chrome Webdriver from <https://chromedriver.chromium.org/downloads>
4. Run the scraper

```bash
python files/scraping_learning_modality.py --chromedriver_path <path_to_chromedriver>
```

5. You will get a file named `School_Learning_Modalities.csv` containing all the required fields.
Alternatively, check my scraped data here: <https://github.com/ripon5098/US-School-Learning-Modalities-Project/blob/main/School_Learning_Modalities.csv>
