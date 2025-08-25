# Analysis of U.S. Steel Tariffs: A Partial Equilibrium Model

This project analyzes the economic effects of the Section 232 steel tariffs implemented by the Trump administration. Using a partial equilibrium model and data from the U.S. International Trade Commission, this repository visualizes the impact on consumer surplus, producer surplus, and the resulting deadweight loss in the U.S. steel market.

## Abstract

The implementation of import tariffs under the Trump administration marked a significant shift in U.S. trade policy and continues to be a subject of intense debate. To analyze the tariffs' effects on the American economy and welfare, this project utilizes microeconomic theory to examine the consequences of trade barriers. This theoretical framework is then connected to empirical data and observations to understand the full incentives and outcomes of the import tariffs.

## Economic Model: Partial Equilibrium

To analyze the effects of an import tariff, the standard tool in microeconomic theory is the partial equilibrium model. This model illustrates how a tariff raises the domestic price from the world price (Pw) to a new, higher price (Pw + Tariff). This leads to the following theoretical consequences:

* **Decreased Consumption:** The total quantity demanded in the country falls (from Q2 to Q4) due to the higher price.
* **Increased Domestic Production:** The higher price makes it more profitable for domestic producers, who increase their output (from Q1 to Q3).
* **Reduced Imports:** The gap between domestic consumption and production (Q4 - Q3) narrows, resulting in a lower import volume.
* **Welfare Effects:** The tariff causes a redistribution of surplus. Consumer surplus decreases, while producer surplus and government tariff revenue increase. Crucially, a net loss in total welfare, known as **Deadweight Loss (DWL)**, occurs due to inefficiencies in production and consumption.

## Data & Analysis

The visualization in this project is based on empirical data from the report "Economic Impact of Section 232 and 301 Tariffs on U.S. Industries" by the U.S. International Trade Commission. The analysis uses 2017 as the pre-tariff baseline year.

**Key Data Points for the Model:**
* [cite_start]**World Price (Pw, 2017):** $530.42 / metric ton. [cite: 110, 111]
* [cite_start]**Domestic Production (Q1, 2017):** 81,600 thousand metric tons. [cite: 114]
* [cite_start]**Domestic Consumption (Q2, 2017):** 106,324.8 thousand metric tons. [cite: 117, 118]
* [cite_start]**Price with Tariff (Pt, 2018-2021 avg.):** $543.15 / metric ton, a 2.4% increase. [cite: 121, 123]
* [cite_start]**Domestic Production (Q3, 2018-2021 avg.):** 83,150.4 thousand metric tons, a 1.9% increase. [cite: 125, 126]
* [cite_start]**Domestic Consumption (Q4, 2018-2021 avg.):** 102,562.5 thousand metric tons. [cite: 131, 132]

## Interactive Visualization

An interactive graph, generated with Python and Plotly, visualizes this data. The graph clearly shows the different economic areas and illustrates the deadweight loss created by the tariffs.

**[>> Click here to view the interactive graph <<](https://09stochastic.github.io/steel_tariff_model.py/interactive_steel_tariff_graph.html)**

*(Note: Replace the link above with the one you get from GitHub Pages after activating it!)*

## Discussion and Conclusion

The analysis confirms that the partial equilibrium model aligns well with the observed primary effects on the steel market. [cite_start]The data shows that the tariffs led to reduced imports of targeted steel products (-24.0%), higher domestic prices (+2.4%), and a slight increase in domestic production (+1.9%) during the 2018-2021 period. [cite: 102, 103]

However, the empirical observations reveal a more complex reality. [cite_start]The model does not capture secondary effects, such as retaliatory tariffs from trade partners like China, which harmed U.S. export industries, particularly agriculture. [cite: 92, 93, 94, 95] [cite_start]Furthermore, downstream U.S. manufacturers who rely on steel faced higher input costs, which in some cases reduced their competitiveness and led to job losses. [cite: 89, 90]

In summary, while the model is an effective tool for understanding the core principles, a complete picture requires consideration of global supply chains and political retaliations.

## How to Run the Code Locally

1.  Clone this repository to your local machine.
2.  Install the necessary libraries: `pip install plotly numpy`
3.  Run the script from your terminal: `python steel_tariff_model.py`
4.  This will generate the file `interactive_steel_tariff_graph.html` in the project directory.

## Sources

* **Primary Data Source:** U.S. International Trade Commission (2023). [cite_start]*Economic Impact of Section 232 and 301 Tariffs on U.S. Industries*. [cite: 100]
* **Full Academic Report:** The complete paper this analysis is based on is also available in this repository. **Please note: the report is written in Swedish.**
    * **[View the Full Report (PDF)](Full_Report_Swedish.pdf)**
