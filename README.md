# Skincare-Keywords-Mining
Project for summer internship at Elemen.

## Objectives:
* Text Mining: develope web scrapers to extract texts from skincare blog webpages on skin problems, skincare products and ingredients
* Analyze the correlations between skincare keywords (skin types, problems, seasons, ingredients) to get insights about our customers’ most concerned skin issues and form marketing strategies

## Data:
The texts are extracted from articles which posted between 2015 and 2019 on five popular skincare blogs in the US: [Into The Gloss](https://intothegloss.com/sections/skincare/), [Dermstore](https://www.dermstore.com/blog/category/skin-care/), [SkinStore](https://www.skinstore.com/blog/skincare/), [b-glowing](https://www.b-glowing.com/blog/category/skincare/), and [Askderm](https://askderm.com/blogs/askderm-blog/). All the results are combined to one single csv file containing four columns (URL, Title, Author & Date, Content). You can find the raw dataset [here](https://github.com/yding-nyu/Skincare-Keywords-Mining/tree/master/data).

## Jupyter Notebooks
* [crawler_Intothegloss.ipynb](https://github.com/yding-nyu/Skincare-Keywords-Mining/blob/master/crawler_Intothegloss.ipynb), [crawler_askderm.ipynb](https://github.com/yding-nyu/Skincare-Keywords-Mining/blob/master/crawler_askderm.ipynb), [crawler_bglowing.ipynb](https://github.com/yding-nyu/Skincare-Keywords-Mining/blob/master/crawler_bglowing.ipynb), [crawler_dermstore.ipynb](https://github.com/yding-nyu/Skincare-Keywords-Mining/blob/master/crawler_dermstore.ipynb) and [crawler_skinstore.ipynb](https://github.com/yding-nyu/Skincare-Keywords-Mining/blob/master/crawler_skinstore.ipynb): Develop web scrapers to extract texts from the skincare blogs
* [scrapyspider folder](https://github.com/yding-nyu/Skincare-Keywords-Mining/tree/master/scrapyspider/scrapyspider): I also tried Scrapy web-crawling framework for the project
* [Final_correlation analysis.ipynb](https://github.com/yding-nyu/Skincare-Keywords-Mining/blob/master/Final_correlation_analysis.ipynb): For the correlation anaysis of FOUR kinds of skincare keywords including skin types, skin problems, seasons and ingredients

## Team Presentation
* Final team presentation slides: [Presentation_Correlation_Analysis.pdf](https://github.com/yding-nyu/Skincare-Keywords-Mining/blob/master/Presentation_Correlation_Analysis.pdf)
