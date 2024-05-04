<div align="center">
      <h1><br/>2024MCM_B_Deep-Sea_Rescue</h1>
     </div>


# Update in 3th May 2024
This paper was awarded with **Honorable Mention** in 2024 Mathematical Contest in Modeling

[Certificate](https://media.licdn.com/dms/image/D562DAQHkL9iMe0Nsiw/profile-treasury-image-shrink_800_800/0/1714711838322?e=1715432400&v=beta&t=G13kF18D3_6LS-VVvQxHU0Y9DEHbbNEj1IB3tiyyZXY)

---

# Description
2024 MCM Question B titled "Deep-Sea Rescue: Localization and Search Strategies in Challenging Oceanic Environments"

# Features
The Greek Maritime Cruise Mini-Submersible Company (MCMS) aims to develop a safety program to predict the location of the submersible in case of failure. The research involves the establishment of a localization model that considers the changes in the physical environment of the submersible in the situation of communication loss or propulsion loss, including factors such as fluid resistance, ocean currents and water density. We propose an integrated model based on physical analysis, probability theory and random walk to predict the location of the submersible and provide guidance for rescue operations.

For Task 1, predict the location of the submersible, which is influenced by several factors. The study begins by analyzing the locational changes of the submersible in the event of a shipwreck, including changes in acceleration due to fluid friction. A decay model is constructed to simulate the decay of the initial velocity, and a Random Walk model is leveraged to predict the drift path of the submersible in conjunction with real-time ocean current velocity. The uncertainty of the predicted path is reduced by a Savitsky-Golay Filter, and the validity of the model is verified based on the Monte Carlo method.

For Task 2, combine the Analytic Hierarchy Process and a Large Language Model to propose an evaluation framework for selecting optimal equipment for the host ship and the rescue ship. The framework considers equipment costs of the availability, the maintenance, the readiness, the usage, and the utilization efficiency. By adding the ability to employ the GoogleWebSearch API for the Open AI GPT-4 model, we perform the online fact-checking and scoring of the candidate equipment to ensure the objectivity of the scores. Finally, we choose ROV Hydroid Remus 6000 and LR7 as
the probing equipment and the rescue equipment, respectively.

For Task 3, we propose a search model based on the Long Baseline Communication
System and the Bayesian Search for searching within the range determined by the location prediction model. These models are constructed and implemented with a combination of Model Predictive Control strategies to optimize search paths and reduce search time. In simulations, the probability of being able to search in about 12 hours can be
more than 90%.

For Task 4, we consider the scalability of the model and find that it can be easily extended to other oceans. Moreover, the flexibility of the model is demonstrated by the argument that when there are multiple submersibles in the vicinity of the same ocean area, the remaining submersibles can be used as ROVs for exploration.

Finally, a sensitivity analysis on the proposed model is performed to test the robustness under different parameters. The strength of the model lies in its high scalability to adapt to search and rescue missions in different ocean areas.

Keywords: analytic hierarchy process; Bayesian search; GPT-4 as reviewers; model
predictive control; random walk; Savitsky-Golay filter

# Tech Used
 ![LaTeX](https://img.shields.io/badge/latex-%23008080.svg?style=for-the-badge&logo=latex&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
      
---

![图片](https://github.com/jxTse/)
    
