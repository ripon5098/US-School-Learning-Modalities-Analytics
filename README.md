# US-School-Learning-Modalities-Project

## Problem Statement

The School Learning Modalities dataset provides estimates of school learning modality (including in-person, remote, or hybrid learning) for U.S. charter school districts for the 2021-2022 school year. The goal of this project is to gather information that how people interects with different learning modalities as well as the operating schools and students of different States of USA from [this website](https://healthdata.gov/National/School-Learning-Modalities-2021-2022/aitj-yx37).<br/>
Later I utilized the scraped data to understand some demographics and correlations using Tableau Dashboard.
The public dashboard is also attached [here](https://public.tableau.com/app/profile/minhaj.uddin4733/viz/USASchoolLearningModalitiesDataVisualization/PrimaryVisualizations).

## Tableau Dashboards

1. This dashboard represents total students, total operational schools and learning modalities applied by the students of each states of USA.<br/>
<img src = "dashboard_images\primary_viz.jpg" width="700" height="350">

2. This dashboard
<img src = "dashboard_images\selective_viz.jpg" width="700" height="350">
<img src = "dashboard_images\calculative_viz.jpg" width="700" height="350">
<img src = "dashboard_images\calculative_viz2.jpg" width="700" height="350">
<img src = "dashboard_images\overview.jpg" width="700" height="350">

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
4. You will get a file named `School_Learning_Modalities.csv` containing all the required fields.
Alternatively, check my scraped data here: <https://github.com/ripon5098/US-School-Learning-Modalities-Project/blob/main/School_Learning_Modalities.csv>
