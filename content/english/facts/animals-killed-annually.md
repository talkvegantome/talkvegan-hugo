---
title: "Number of Animals Killed Annually"
date: 2019-05-16T21:35:14+01:00
lastmod: 2019-05-16T21:35:14+01:00
contributors:
    - 
        name: sam-martin
        role: author
draft: false
description: "Is it true that \"between 40 billion and 3 trillion animals are slaughtered anually\""
weight: 100
---

# Popular Fact

The numbers quoted in this statistic vary between 40 billion and 3 trillion.  
The smaller number pertains to land animals (sometimes only mammals) and the latter includes all sea life including shrimp and other small creatures.

# Reality

> According to the FAO database 74,857,206,136 land animals were slaughtered in 2017. Many more marine animals were slaughtered. 

See below for how this figure was calculated.


# Original Sources

The [Food and Agriculture Organization of the United Nations](http://www.fao.org/faostat/en/#data/QL) database is an incredible resource for information. To get the relevant stats from this site we need to do the following:

1. Visit [the database](http://www.fao.org/faostat/en/#data/QL)
2. Click "Livestock Primary" under "Production"
3. Select Regions > World (Total)
4. Select Producing Animals/Slaughtered
5. Select Items (Aggregated) > Meat, Poultry (list)
6. Select 2017 (latest data available.)
7. Download dataset
8. Normalise the poultry values by multiplying it by 1,000 (as they're provided per 1,000 head)
9. Sum the total normalised value

You can see these sums [in our excel spreadsheet](https://docs.google.com/spreadsheets/d/1ymkUc2hl0FS41veh3Mqp8JVsiinry8XC0aPKQUV48Us/).

This gives us:

>  Total number of land animals slaughtered in 2017: 74,857,206,136  
> - [Food and Agriculture Organization of the United Nations](http://www.fao.org/faostat/en/#data/QL) calculated as per [our excel spreadsheet](https://docs.google.com/spreadsheets/d/1ymkUc2hl0FS41veh3Mqp8JVsiinry8XC0aPKQUV48Us/).

The dataset's explanation for how their figures were arrived at is as follows: 

> The data on livestock numbers are intended to cover all domestic animals irrespective of their age and the place or purpose of their breeding. Estimates have been made for non-reporting countries as well as for countries reporting incomplete data. However, in certain countries, data for chickens, ducks and turkeys do not yet seem to represent the total number of these birds. Certain other countries give a single figure for all poultry; data for these countries are shown under “Chickens”. [...]  
>  Data relate to animals slaughtered within national boundaries, irrespective of their origin. All data shown relate to total meat production, that is, from both commercial and farm
slaughter. Data are given in terms of dressed carcass weight, excluding offal and slaughter fats.   
> The compilation of the data domain has been made possible by the cooperation of
governments, which have supplied most of the information in the form of replies to annual
FAO questionnaires.   
> - [FAO Methodology Document](http://fenixservices.fao.org/faostat/static/documents/QL/QL_methodology_e.pdf)

Two pieces of this are slightly confusing:  

>  The data on livestock numbers are intended to cover all domestic animals irrespective of their age and the place or purpose of their breeding.  

This appears to refer to a separate dataset than the one we're inspecting, i.e. 'Live animals'.  

> Data are given in terms of dressed carcass weight, excluding offal and slaughter fats.   

Again, this refers to a separate set of statistics within the same dataset which refer to tonnes of animal flesh, not our statistics which are 'per head'.



## Further Reading

- [BiteSizeVegan - Quantifying Suffering, Cruelty by the Numbers](http://www.bitesizevegan.org/bite-size-vegan-nuggets/qa/quantifying-suffering-cruelty-by-the-numbers/)


