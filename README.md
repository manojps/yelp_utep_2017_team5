Yelp Dataset (Round 9)

Data mining project repository

Folder structure
-----------------
<b>LCE_detection</b>: Contains script to calculate local category elite score

<b>aggregation</b>: Experimental scripts to analyze some trends related to reviews

<b>elite_user_classifier</b>: Scripts to classify elite users

<b>expert_detection/V1</b>: Scripts to calculate local experts based on initial deterministic model

<b>location_plot</b>: Scripts to plot geolocations on Google Maps

<b>notebook</b>: Contains Jupyter Notebook files that were used to test proof of concept before actual implementation. hence, these files can be interesting if you want to look at all things that were done.

<b>parser/postgres-parse</b>: Contains parsers to parse the dataset in a PostgreSQL database

<b>topical_authority_classifier</b>: Scripts to classify topical authority of users

<b>user_location</b>: Gaussian Mixture Model implementation and yelp website crawler (not based on an actual spider)
---------------------------
Scripts needed for calculating P(LocalCategoryElite)

You would need the following four scripts to calculate P(LCE):

<ul>
<li>user_location/gmm_parallel_v2.py for user location estimation</li>
<li>/topical_authority_classifier/topic_expert_classifier.py for topical authority calculation</li>
<li>elite_user_classifier/elite_user_classifier.py for classifying elite users</li>
<li>LCE_detection/lce_detection.py to combine the results of the above three and calculate the P(LCE) score</li>
</ul>



------------------------------------------------------

This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
