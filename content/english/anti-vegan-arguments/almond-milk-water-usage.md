---
title: "Almond Milk Water Usage"
date: 2019-06-06T11:43:43+01:00
draft: false
---

# Popular Fact

>  “But what people don’t know is the environmental damage almond plantations are doing in California, and the water cost. It takes a bonkers 1,611 US gallons (6,098 litres) to produce 1 litre of almond milk,” says the Sustainable Restaurant Association’s Pete Hemingway.  
> - [The Guardian - Ditch the almond milk: why everything you know about sustainable eating is probably wrong - 2018](https://www.theguardian.com/food/2018/sep/05/ditch-the-almond-milk-why-everything-you-know-about-sustainable-eating-is-probably-wrong)

This cites [Almond Milk vs. Cow Milk Life Cycle Assessment - Jacqueline Ho, Ingrid Maradiaga, et al. - 2016](https://web.archive.org/web/20181003201254/https://www.ioes.ucla.edu/wp-content/uploads/cow-vs-almond-milk-1.pdf), which has figures that are _highly_ suspect due to methodological concerns (see below).

# Reality

A reliable source has not yet been found for this statistic.

# Original Sources

## Almond Milk vs. Cow Milk Life Cycle Assessment - Jacqueline Ho, Ingrid Maradiaga, et al. - 2016

This figure is the average of two calculations, the lower of which is:

> Almond production + almond processing =  
> 0.20113 kgal + 1.068555 kgal = 1.269685 kgal water / 1L almond milk  
> [Almond Milk vs. Cow Milk Life Cycle Assessment - 2016 - p13](https://web.archive.org/web/20181003201254/https://www.ioes.ucla.edu/wp-content/uploads/cow-vs-almond-milk-1.pdf)

The first figure (for production) is derived from [Almond Eco­Efficiency Analysis (BASF Corporation, 2011)](http://www.nsfturkey.com/newsroom_pdf/Almond_EEA_Study_Verification_Final_August_2011.pdf). The second figure is the vast majority of the total and is rather suspect. 

### Almond Processing Figure
Due to a lack of statistical data regarding almond processing, the figure is derived using the ratio of water usage in soybean production to soybean processing. [p11](https://web.archive.org/web/20181003201254/https://www.ioes.ucla.edu/wp-content/uploads/cow-vs-almond-milk-1.pdf).

The ratio of water usage in producing vs processing soybeans came out as 0.83x (i.e. producing the soybeans took 0.83x as much water as processing them). 

It seems very strange to use a ratio of water to grow vs water to process for this, as just because almonds take more water to grow, it does not follow that they take more to process.  It seems far more likely (without evidence to the contrary) that the amount of water to process soybeans is _broadly_ similar. The amount of water used to process soybeans they use is 136 gallons [p11](https://web.archive.org/web/20181003201254/https://www.ioes.ucla.edu/wp-content/uploads/cow-vs-almond-milk-1.pdf). It seems staggering to believe that almonds use more than 8x as much water for processing as soybeans without any additional details on the process.

This is then multiplied by 0.885 kgal to get a total of 1.07kgal used for processing almonds. But where does the 0.885 kgal come from?

The 0.885 kgal figure was calculated using the [EIOCLA US 2002 Benchmark Producer Price Model - Tree Nut Farming](http://www.eiolca.net/cgi-bin/dft/display.pl?hybrid=no&first_level_sector=-1&second_level_sector=111335&newmatrix=US430CIDOC2002&key=7216147368&value=0244216612&incdemand=0.0000017858&selectvect=water&select_button1=Run+Model) with an input of the average retail price of almond milk per litre (1.7858$/litre) [p12](https://web.archive.org/web/20181003201254/https://www.ioes.ucla.edu/wp-content/uploads/cow-vs-almond-milk-1.pdf).  
The EIOCLA is a rather clever statistical model that uses data from [a variety of public sources](http://www.eiolca.net/docs/full-document-2002-042310.pdf) to calculate the environmental impact of various industries per million dollars of the _producer_ price. 

To be clear, they are using data on the amount of water it takes to grow (produce) nuts and using it as the basis to infer the amount of water it takes to turn the (already grown) nuts into milk

The dollar value input for this is naturally crucial, and the tutorial for the calculator warns:

> The dollar value entered represents producer price - the cost to make the output; it is not the consumer price - the cost to purchase the output. For an average automobile, the producer price is around $20,000. A consumer would purchase this average vehicle for $25,000 to $30,000.  
> - [EICLA Tutorial](https://web.archive.org/web/20190606115219/http://www.eiolca.net/tutorial-new/tut_3.html)

Unfortunately it seems that in this study, the retail price has been used, inflating the results significantly. The study justifies this by saying:  

> We are assuming that the cost of packaging is negligible thereby allowing us to use the retail price as the economic activity for EIOLCA.  
> -  [p12](https://web.archive.org/web/20181003201254/https://www.ioes.ucla.edu/wp-content/uploads/cow-vs-almond-milk-1.pdf)

But this ignores retail markup, distribution costs, not to mention the fact that the dataset we're working against is for the _Tree Nut Farming_ industry [p12](https://web.archive.org/web/20181003201254/https://www.ioes.ucla.edu/wp-content/uploads/cow-vs-almond-milk-1.pdf), not the almond _milk_ industry which skews the result due to the farming industry having a much lower 'producer price' (price the farmer/factory sells it at) by virtue of being further back in the value chain.

We regard the numbers cited here for almond processing as _highly_ suspect due to:  

1. The conflation of retail and producer pricing
2. The inference of processing water usage from farming water usage
3. The conflation of nut milk producer pricing and nut farming producer pricing
4. The assumption that the average ratio of production water usage to processing water usage (two **completely** unrelated numbers) from data regarding soybeans applies to almonds.

It is unfortunately not possible to calculate even an approximate figure for processing using the datasets from the study as we do not have a cost per litre of almond milk at producer price, nor a dataset from the plant milk industry.  
For sheer curiosities sake, however, we can  run their assumption that the ratio (0.83x [p11](https://web.archive.org/web/20181003201254/https://www.ioes.ucla.edu/wp-content/uploads/cow-vs-almond-milk-1.pdf)) of water consumption in production and processing soybeans applies to almonds and infer the processing water usage from their 0.2 kgal almond production figure [p13](https://web.archive.org/web/20181003201254/https://www.ioes.ucla.edu/wp-content/uploads/cow-vs-almond-milk-1.pdf).  
That calculation would be: 

> Almond Farming Water Usage / Almond Processing Water Usage = 0.83  
>  0.2 kgals / x = 0.83  
>  x = 0.24 kgals  
> Almond Processing Water Usage = 240 gallons

Which would make our total (Almond Farming + Almond Processing): 0.44 kgallons, or 440 gallons of water to make 1 litre of almond milk rather than the cited 1,270 to 1,611 gallons.

**Important:** The calculation above is still completely spurious and is merely an extrapolation based on the article's own unfounded assumption of a consistent ratio between farming water usage and processing water usage.


# Sources

- [The Guardian - Ditch the almond milk: why everything you know about sustainable eating is probably wrong - 2018](https://www.theguardian.com/food/2018/sep/05/ditch-the-almond-milk-why-everything-you-know-about-sustainable-eating-is-probably-wrong)
- [Almond Milk vs. Cow Milk Life Cycle Assessment - 2016](https://web.archive.org/web/20181003201254/https://www.ioes.ucla.edu/wp-content/uploads/cow-vs-almond-milk-1.pdf)
- [EICLA Tutorial](https://web.archive.org/web/20190606115219/http://www.eiolca.net/tutorial-new/tut_3.html)
- [EIOCLA US 2002 Benchmark Producer Price Model - Tree Nut Farming](http://www.eiolca.net/cgi-bin/dft/display.pl?hybrid=no&first_level_sector=-1&second_level_sector=111335&newmatrix=US430CIDOC2002&key=7216147368&value=0244216612&incdemand=0.0000017858&selectvect=water&select_button1=Run+Model)