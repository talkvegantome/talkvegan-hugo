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

This figure is the average of two calculations, one partly based on an industry analysis and one wholly based on a statistical model. The former is as follows:

> Almond production + almond processing =  
> 0.20113 kgal + 1.068555 kgal = 1.269685 kgal water / 1L almond milk  
> [Almond Milk vs. Cow Milk Life Cycle Assessment - 2016 - p13](https://web.archive.org/web/20181003201254/https://www.ioes.ucla.edu/wp-content/uploads/cow-vs-almond-milk-1.pdf)

The first figure of 201 gallons per litre of almonond milk (consumed in the growing of the almonds) is derived from [Almond Eco­Efficiency Analysis (BASF Corporation, 2011)](http://www.nsfturkey.com/newsroom_pdf/Almond_EEA_Study_Verification_Final_August_2011.pdf). The second figure of 1,068 gallons per 1 litre of Almond milk (consumed in the processing of almonds into milk) is the vast majority of the total and is rather suspect. 

### Almond Processing Figure
Due to a lack of statistical data regarding almond processing, the almond processing figure (1,068 gallons of water to 1 litre of almond milk) is derived using the ratio of water usage in soybean production to soybean processing. [p11](https://web.archive.org/web/20181003201254/https://www.ioes.ucla.edu/wp-content/uploads/cow-vs-almond-milk-1.pdf).

The ratio of water usage in producing vs processing soybeans came out as 0.83x  [p11](https://web.archive.org/web/20181003201254/https://www.ioes.ucla.edu/wp-content/uploads/cow-vs-almond-milk-1.pdf) (i.e. producing the soybeans took 0.83x as much water as processing them). 

It seems very strange to use a ratio of water to grow vs water to process for this, as just because almonds take more water to grow, it does not follow that they take more to process.  It seems far more likely (without evidence to the contrary) that the amount of water to process soybeans is _broadly_ similar. The amount of water used to process soybeans they cite is 136 gallons [p12](https://web.archive.org/web/20181003201254/https://www.ioes.ucla.edu/wp-content/uploads/cow-vs-almond-milk-1.pdf). It seems staggering to believe that almonds use more than 8x as much water for processing as soybeans without any additional details on the process.

This ratio of 0.83x is then applied to 0.885 kgal for farming.  

> 0.82822086 = Tree nut farming / x  
> 0.82822086 = 0.885 kgal / x  
> x = 1.068555 kgal water used in processing almonds into almond milk  
> - [p13](https://web.archive.org/web/20181003201254/https://www.ioes.ucla.edu/wp-content/uploads/cow-vs-almond-milk-1.pdf) 

This gives us the 1,068 gallons of water used in the processing of almonds into milk to yield to 1 litre of milk.
But where does the 0.885 kgal come from?

The 0.885 kgal figure was calculated using the [EIOCLA US 2002 Benchmark Producer Price Model - Tree Nut Farming](http://www.eiolca.net/cgi-bin/dft/display.pl?hybrid=no&first_level_sector=-1&second_level_sector=111335&newmatrix=US430CIDOC2002&key=7216147368&value=0244216612&incdemand=0.0000017858&selectvect=water&select_button1=Run+Model) with an input of the average retail price of almond milk per litre (1.7858$/litre) [p12](https://web.archive.org/web/20181003201254/https://www.ioes.ucla.edu/wp-content/uploads/cow-vs-almond-milk-1.pdf). The EIOCLA is a rather clever statistical model that uses data from [a variety of public sources](http://www.eiolca.net/docs/full-document-2002-042310.pdf) to calculate the environmental impact of various industries per million dollars of the _producer_ price. 

To be clear, they are using data on the amount of water it takes to grow (produce) nuts to infer the amount of water it takes to process the (already grown) nuts into milk

The dollar value input for the EIOCLA model is naturally crucial, and the tutorial for the calculator warns:

> The dollar value entered represents producer price - the cost to make the output; it is not the consumer price - the cost to purchase the output. For an average automobile, the producer price is around $20,000. A consumer would purchase this average vehicle for $25,000 to $30,000.  
> - [EICLA Tutorial](https://web.archive.org/web/20190606115219/http://www.eiolca.net/tutorial-new/tut_3.html)

Unfortunately it seems that in this study, the retail price has been used, inflating the results significantly. The study justifies this by saying:  

> We are assuming that the cost of packaging is negligible thereby allowing us to use the retail price as the economic activity for EIOLCA.  
> -  [p12](https://web.archive.org/web/20181003201254/https://www.ioes.ucla.edu/wp-content/uploads/cow-vs-almond-milk-1.pdf)

But this ignores retail markup, distribution costs, not to mention the fact that the dataset we're working against is for the _Tree Nut Farming_ industry [p12](https://web.archive.org/web/20181003201254/https://www.ioes.ucla.edu/wp-content/uploads/cow-vs-almond-milk-1.pdf), not the almond _milk_ industry which skews the result due to the farming industry having a much lower 'producer price' (price the farmer/factory sells it at) by virtue of being further back in the value chain.

We therefore regard the numbers cited here for almond processing as _highly_ suspect due to:  

1. The conflation of retail and producer pricing
2. The conflation of nut milk producer pricing and nut farming producer pricing
3. The inference of processing water usage from farming water usage (two **completely** unrelated numbers)
4. The assumption that the ratio (0.83x) of production (farming) water usage to processing (almonds into milk) water usage from data regarding soybeans somehow applies to almonds.

Using the datasets and methodologies that the study provides it is impossible to come to a reliable conclusion regarding the total water usage per litre of almond milk.

#### Speculating further

Out of curiousity however, we can use the data the authors provided to make two still unsupportable, but arguably more accurate calculations for water usage per litre of almond milk. 

**Use soybeans' processing water usage per litre as a comparison**

> Almond Farming + Soybean Processing = Approximate Total gallons per litre of milk  
>   0.20113 kgal [p13](https://web.archive.org/web/20181003201254/https://www.ioes.ucla.edu/wp-content/uploads/cow-vs-almond-milk-1.pdf) + 0.136 kgals [p12](https://web.archive.org/web/20181003201254/https://www.ioes.ucla.edu/wp-content/uploads/cow-vs-almond-milk-1.pdf) = Approximate Total  
> Approximate Total = 0.33713 kgals  

So our total would be 337 gallons of water per litre of almond milk rather than their cited 1,611. This makes the assumption that almond processing takes exactly as much water as soybean processing, but that seems a more defensible assumption than the _wild_ speculation of the figures based on the model. (See the 4 bullet points above for why.)

**Use the [Almond Eco­Efficiency Analysis](http://www.nsfturkey.com/newsroom_pdf/Almond_EEA_Study_Verification_Final_August_2011.pdf) figure with the 0.83 ratio**

> Almond Farming Water Usage / Almond Processing Water Usage = 0.83 [p11](https://web.archive.org/web/20181003201254/https://www.ioes.ucla.edu/wp-content/uploads/cow-vs-almond-milk-1.pdf))  
>  0.2 kgals / x = 0.83  
>  x = 0.24 kgals  
> Almond Processing Water Usage = 240 gallons

Which would make our total (Almond Farming + Almond Processing): 0.44 kgallons, or 440 gallons of water to make 1 litre of almond milk rather than the cited 1,611 gallons.

**Important:** The calculation above is still completely spurious and is merely an extrapolation based on the article's own unfounded assumption of a universally applicable ratio between farming water usage and processing water usage.


# Sources

- [The Guardian - Ditch the almond milk: why everything you know about sustainable eating is probably wrong - 2018](https://www.theguardian.com/food/2018/sep/05/ditch-the-almond-milk-why-everything-you-know-about-sustainable-eating-is-probably-wrong)
- [Almond Milk vs. Cow Milk Life Cycle Assessment - 2016](https://web.archive.org/web/20181003201254/https://www.ioes.ucla.edu/wp-content/uploads/cow-vs-almond-milk-1.pdf)
- [EICLA Tutorial](https://web.archive.org/web/20190606115219/http://www.eiolca.net/tutorial-new/tut_3.html)
- [EIOCLA US 2002 Benchmark Producer Price Model - Tree Nut Farming](http://www.eiolca.net/cgi-bin/dft/display.pl?hybrid=no&first_level_sector=-1&second_level_sector=111335&newmatrix=US430CIDOC2002&key=7216147368&value=0244216612&incdemand=0.0000017858&selectvect=water&select_button1=Run+Model)