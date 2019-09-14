---
title: "Blog"
description: "All about the making of TalkVeganToMe!"
date: 2019-07-18T21:21:51+01:00
displayInApp: false
draft: false
---

# TalkVeganToMe - #11 - 14/09/19

Wow, your app gets released and then you naff off for two weeks? What's that about!
Lots of updates, that's what that's about!

First let's start with what we aimed to achieve from the last newsletter:  

1. ✅ Add an expanded category section rather than forcing people to scroll through categories (currently the articles towards the end of the scroll list just don't get seen!)
1. ✅ Add favourites to allow you to easily access pages
1. ✅ Fix bug that causes you to scroll back to the top of the page
1. ✅ Improve search so that it's faster
1. ✅ Improve search so that it will match pages that don't contain 100% of the words.
1. ✅ Highlight new articles on the main page
1. ✅ Add a Random Article button (Kinda, I just randomised the display on the front page!)
1. ✅Next/Previous articles on the bottom of each article page

100% Success rate! Love it.  
In addition to that I've:

1. Added alert notifications of new articles
1. Added prompt to rate the app (will help app store rankings massively)
1. Added iPad Support
1. Added iOS 10.3 support (previously 12.2+ was required!)
1. Made the prompt to enable analytics prettier
1. Fixed a bug where swapping between apps would scroll you back to the top of the page
1. Fixed a memory leak (improved performance)
1. Improved handling of settings updates (stopped it erasing your back button/location unnecessarily

And I've also added automated functional testing which you can see in action here: [https://imgur.com/a/LXPD4Qo](https://imgur.com/a/LXPD4Qo)

At the time of writing notifications and prompt-to-rate are not available in the Apple App Store, only on Google Play as I finished the submission on Friday evening so it will be Monday before it's available on iOS!
What's Next
Marketing and Content!
The main features I wanted for the app are now done so barring any bugfixes that need to happen I can focus on getting people to use the app by cross-posting it across the internet.

As for content, the articles I'm going to start with are:
Tofu contains Estrogen 
Plants feel pain

If you've got any other articles you'd like to see, just let me know. You can see what I'm working on here: [https://trello.com/b/7ecEPfjW/talkvegantome-content]( https://trello.com/b/7ecEPfjW/talkvegantome-content)

Have a great week everyone!

# TalkVeganToMe - #10 - 25/08/19

This week has been an absolute rollercoaster!
On Sunday I had the app cleaned up enough to be ready to submit it again for approval, just to test the waters and see if it would be possible to release as a content only app (i.e. without additional functionality). 
On Tuesday, I got another rejection, which annoyed me somewhat due to there being multiple similar apps out there and an entire reference section of the app store, but ultimately it was what I was expecting.
I started to get quite excited about building a ingredients scanning feature into the app using AWS's text recognition API, and then having those snapshots and ingredients missing in the database appear in a "vegan or not" section of the app where people could swipe through photos of packaging and swipe left/right tinder style on whether they were vegan or not.

THE NEXT DAY THE APP GOT APPROVED

I was in shock, I'd replied to the rejection asking for some feedback on what needed changing given it was similar to other apps that were already on the app store, but given that I waited 3 weeks for a response to my appeal last time it got rejected, I was genuinely not expecting any response at all. Let alone for it to be approved within 24hrs. BUT IT IS FINALLY LIVE!

**Apple App Store:** [https://apps.apple.com/gb/app/talkvegantome/id1463279026](https://apps.apple.com/gb/app/talkvegantome/id1463279026)  
**Android Play Store:** [https://play.google.com/store/apps/details?id=com.talkvegantome](https://play.google.com/store/apps/details?id=com.talkvegantome)

The UK Vegans discord people were the first to find out and gave a bunch of five star reviews on both app stores which is unbelievably helpful and I'm so grateful for their positive feedback the last few days.

I also happened to notice a post on Reddit distributing an infographic that was based on the ancient land-usage data that I chimed in on to provide a better citation for, and which caused the first bit of social media exposure for the app!

There are a few more things I want to tidy up before I give it a proper social media push though:

1. Add an expanded category section rather than forcing people to scroll through categories (currently the articles towards the end of the scroll list just don't get seen!)
1. Add favourites to allow you to easily access pages
1. Fix bug that causes you to scroll back to the top of the page
1. Improve search so that it's faster
1. Improve search so that it will match pages that don't contain 100% of the words.
1. Highlight new articles on the main page
1. Add a Random Article button
1. Next/Previous articles on the bottom of each article page

I think you get the theme here, navigation is a problem right now and content discovery is an even bigger one. Fortunately I don't think any of these are particularly hard work, I'm just going to struggle to find the time to spend on them for the next few weeks!

Thank you all so much for your support and ideas for the app until its release, I couldn't have done it without you.

But this is just the beginning. After this first push to clean up the app I want to focus back on content again and create more new articles that I'm as excited about as the ones I've written so far! And at some point I want to add the ingredients scanning too but... I mustn't get ahead of myself. I want the app to stand on its own legs with regards to content first.

I'm SO FUCKING EXCITED everyone! I will still keep you all up to date every week just so I don't burst with excitement!

# TalkVeganToMe - #9 - 18/08/19

So this week has been pretty productive.
As you've probably seen if you've opened the app recently there has been a complete overhaul of the interface including search!

[Image 1](https://gallery.mailchimp.com/7efbe101e4e479517a32c8738/images/02c2705f-2c96-4dd9-9d19-fab61dfa14ac.png)  
[Image 2](https://gallery.mailchimp.com/7efbe101e4e479517a32c8738/images/99f6959c-5069-4fc3-a94f-07b31dc91dd6.png)

If any of you have downloaded some of the beta updates for the Android app you will have noticed some pretty abysmal performance, particularly in search. Thankfully this has now been resolved, and the latest beta update (which is still working its way through the playstore release process) will be reflect these fixes and should be available soon.

As for next week, my availability is pretty limited but I'm going to be working mainly on tidying up the code and trying to get a release approved on the Apple App Store!

Wish me luck! And send feedback!!!

# TalkVeganToMe - #8 - 10/08/19

Erm... Not going to lie there has not been a lot of progress in the weeks since my last email.  
If you recall, last time I wrote, the app had just been rejected from the app store and I was awaiting a response to my appeal.  
That was on the 20th of July, and here we are three weeks later and there has been no response at all from apple. Not even a confirmation email. I would have started to doubt that I'd even successfully sent the appeal apart from the fact that I printed the confirmation page to a pdf which explicitly states:   
Please note that if you self- reject or resubmit your binary in App Store Connect, your appeal will not be reviewed and this request will be canceled.

Which basically means there's no recourse or follow up, or ability to find out if they've just chucked it in the bin. I'm pretty annoyed about this because with my lack of experience with app development I don't actually know what will meet the threshold for them to allow the app on the app store. I could put another 3 months work into it and still get rejected because there's no communication about what exactly their rules are beyond some vague description of "meaningfully different from a mobile browsing experience". 

In any case, I've been buoyed by the response from some of you suggesting new app designs to make it easier to use, and today finally got out of my rut with a flash of motiviation and frantically sketched out a new design for the app.

You can see that here: [New App Design Sketch](https://imgur.com/a/RsW63YR)
 
(As you can tell I'm no artist.)

So I'm going to start working on that over the next few weeks, and will keep you all posted on how it goes.

The main new features will be:

* Complete redesign
* Left/right scrolling between articles
* Search
* Flashcards

All in all this should improve the usability of the app pretty significantly, and also add some nice features like the search and flash cards which I've been wanting to add anyway.

Hopefully that'll be enough to get it through to the app store! Failing that I'll have to do something more drastic!

# TalkVeganToMe - #7 - 13/07/18

This week has been extremely productive!

## Content
 - Anti Vegan Arguments - WIthout farming there would be no animals
 - Updated the almond milk water usage article to include recent sources
 - Added a linter to flag gendered pronouns to be replaced with ze/zir pronouns (when unsure of persons preferred pronouns)
 - Created a Media Pack page of logos and blurb
 - Added these newsletters to a Blog page

## App changes
 - Added table of contents to the bottom of the page
 - Allowed pages to be displayed only on website (e.g. the media pack)
 - Reskinned the app to look a bit more like the website
 - Submitted the app for review for inclusion on the app store

That last one is a doozy as... *drumroll* the app got rejected!
 
> Guideline 4.2.2 - Design - Minimum Functionality  
>
> We noticed that your app only includes links, images, or content aggregated from the Internet with limited or no native iOS functionality. Although this content may be curated from the web specifically for your users, since it does not sufficiently differ from a mobile web browsing experience, it is not appropriate for the App Store.

Which... I can't argue with in a way because it is at its heart, a reference app, and definitely does contain all the content from the website with no additional functionality except the offline mode!  
That offline functionality and immediate feedback of the app is utterly critical to the whole concept of TalkVeganToMe. If you're in a pub, talking with your omni friends and mention a stat and get rebutted with "Where's your source?" you need to be able to come up with that quickly, easily, and reliably. If you have no internet, you're done. If you have to try and remember the name of the site, type it in, load it, you're done.
It's a huge difference between having this content on a website and in the app. The app came first, the website is just secondary so people can link to the content without having to download the app. 

Anyway, I've appealed the decision with the above reasons, so it may still get in, but we shall see!

Worst case scenario I'll have to add some additional functionality to the app to make it 'differ sufficiently from a mobile browsing experience'. A few ideas spring to mind  

 - Fact flash cards, e.g. Shows an e-number on-screen and you hit vegan/not vegan and get a score based on success.  
- Debate dialogue trees, an expansion on how the anti-vegan argument pages work right now, except you are presented with an anti-vegan argument, and then given options to choose from to respond with, and then get different responses depending on what you choose (a lot of work).

Some-one also suggested adding in a product barcode scanning feature (to determine whether the product was vegan or not) but gathering the data for that would be a huge amount of work to make it useful for even a small percentage of the globe.

I'm open to ideas! Let me know if you have anything you'd like to see in the app!

# 2019-07-13

## Progress this week
This week has actually been extremely productive! I carved out 2 days to focus on the app and do nothing else, which helped immensely. 

The biggest thing is we have a newly skinned website!

http://talkveganto.me

The website was always there, but it looked rather like a corporate intranet so I was hesitant to distribute the address too much. I'd love to say that the design was all my work, but it was thanks to the skill of some-one I hired on Fiverr that we have the design. I just took the design and applied it as a Hugo template.

Additionally, we also have a number of promotional screenshots designed! Again from some-one on Fiverr. These will go in the App Store page to make it a bit more attractive to people who are just browsing through randomly. You can see these here: https://imgur.com/a/T3mLLAC

As for articles we have:

- Anti Vegan - It's too weird/counter cultural
- Anti-Vegan - Animals are slaughtered humanely
- Anti-Vegan - Animals aren't Sentient/Sapient
- Facts - Animals slaughtered annually (improved to provide an explanation of how to generate figures from the UN's FAO statistics)

In fact there's only one article left in the pre-release pool!
## Roadmap to Release
Prior to the release I need to do the following

- Write 'Anti Vegan - Without farming there would be no animals'
- Update Almond Milk Water Usage article with latest stats
- Proofread all articles!
- Add tutorial to app to indicate workflow
- Put a Table of Contents at the bottom of the page in app to make navigation easier
- Make the app scroll back to the top of the page on navigate to new page
- Setup talkvegantome.com in addition to .me
- Create a media pack for the site (logos, blurb, etc.)
And then it's ready to release!

Honestly I'm getting quite excited, the end is in sight after a couple of month's worth of work.
The biggest gap currently is the marketing strategy. I think it's going to be quite hard to get the word out as I've had very limited responses to my attempts to reach out to vegan news outlets and influencers. This means I'm going to be relying on word of mouth a lot which... Is unpredictable but probably has a better chance in the vegan community as it's quite well engaged!

We'll see how it goes. I'm setting my launch expectations low so I won't be sad if it just gets 10 downloads in the first week!

Fingers crossed!

# 2019-07-07

## The Saga of 1/6th of an Acre
I have finally found the original source for the Cowspiracy fact that 1/6th of an acre is required to feed a vegan and 3.5 acres required to feed a meat eater.
Cowspiracy (2014) cites an Earthsave article (2006) which cites a book called Diet for a new America (1987) which cites an article called Proteins (1965) which cites another article called Land Use and Food Production (1961) which cites a book Our Developing World (1960) which cites the 1948-1952 UN FAO statistics on food production to compare a JAPANESE diet (which takes 1/6th of an acre to feed one person) and an American diet (which takes 2.5 acres and got rounded up somewhere along the way).

So it's not even a vegan diet at all! The much better stat is: Beef consumed in the United States requires around 160x as much land as potatoes, wheat, or rice for the same number of calories, and nearly 100x as much land for the same amount of protein. Which is sourced from a 2014 article on comparative land usage.
Other Progress this Week

I spent quite a lot of time researching the above last week as it required 2-3 trips to the British Library to fetch the ancient articles and books which weren't available anywhere else. I only managed to finish:

- Anti-Vegan Arguments - One Person Can't Make a Difference
- And made some progress but didn't release
- Anti-Vegan Arguments - It's Okay to Kill Animals Because They Aren't Sentient/Sapient

Which is not an argument you see very often I don't think but it one that holds special value to me because it's what I believed before going vegan! 

## Contributions this Week

I had two people reach out to me this week with suggestions for content and the app, one in particular being a very detailed set of feedback for app design which was extremely helpful!
I can't overstate how much it means to hear from people using the app, so please keep reaching out by replying to this email, even if it's just a tiny suggestion or piece of feedback it means a great deal!
As always, you can see the pipeline for content on the [Trello board](https://trello.com/b/7ecEPfjW/talkvegantome-content)!

# 2019-06-29

## The Past Two Weeks
The past two weeks have been quiet as expected due to a week's holiday! 
I had secretly hoped to spend some time writing even on holiday, but I think for mental health's sake it's a good thing I didn't.

This week I've been figuring out how to tackle one of the biggest remaining challenges for content which is the "Anti Vegan Arguments" section.
My first attempt at this section ended up being merged into the "Vegan Facts" section, primarily because the format warranted a clear differentiation between "analysis of facts" and "rebuttal of arguments" and it didn't make sense to keep them under the same section.

In creating the new "rebuttal of arguments" vision for anti-vegan-arguments I was heavily inspired by Earthling Ed's 30 Non Vegan Excuses. In fact the original scope for this section was to reach out to Ed and ask for permission to redistribute some of the chapters. Since then however I've become more accepting of writing content for the app, and wanted to produce something unique rather than simply reword it. Especially because as the app is community based and editable by anyone, we would either have to lock Ed's chapters as immutable, or allow people to edit them, neither of which seemed good options. 

In writing these pages I wanted to bring as much of the analytic rigor from the fact check pages as I could, and in my first attempt this sent me spiralling down a rabbit hole of analytic philosophy akin to my degree coursework. What the app needed though was not some 10,000 word dense philosophical analysis with a vocabulary only academics could understand, so I settled on a much simpler format that only used citations where absolutely necessary (e.g. for the facts!).

The ones I've finished so far are:

- No Food is Truly Vegan
- Personal Choice
- Animals Eat other Animals

I'm reasonably happy with what I've got so far, continuing with the summary sections at the top and splitting out the detailed analysis further down into Analytic and Emotive arguments, with no judgement intended as to the validity of either section. The purpose of these sections is purely to allow you to tailor your response to the person you're debating.

Prior to release I've committed to finishing rebuttals to the following as well:

- Animals are Slaughtered Humanely
- Animals aren't 'sentient'
- Without Farming there would be no animals
- It's too extreme/weird

In addition, I still need to take the design from last week and apply it to the website, and get a complete marketing strategy in place. On this aspect I had some positive feedback earlier today from a vegan podcast who said they'd be interested in seeing the app when complete and would mention it as part of the podcast if they liked it, which is great news as so far I've had naff all response from other vegan news sites and influencers.

Anyway, this has run extremely long, hope you've all had a wonderful few weeks and as ever, let me know if you have any ideas for the app, or any comments about the content!

As always, you can see the pipeline for content on the [Trello board](https://trello.com/b/7ecEPfjW/talkvegantome-content)!

# 2019-06-15

This week has been much less productive for a couple of reasons. Firstly I took it as a bit of a self-care week, as I've been spending every waking moment on the app for 2-3 months now!
Secondly, I was a bit stuck on how to get from where I am to "released". I've been enjoying writing articles on facts and their sources, but we have enough for the moment and writing more wouldn't actually get me any closer to released. My vision for TalkVeganToMe was not just a "vegan snopes" but a one-stop-shop for quick reference of:

1. Rebuttals to vegan arguments
2. Ethical purchasing advice
3. 'Further information". Books, films, organisations, podcasts, youtube channels
4. Fact's sources

The first three are broadly the killer features from an app perspective. My original use case was someone in a shop (me) looking up e-numbers quickly. 
The fourth however is probably most often going to be used in debates on social media, and not the app at all. The fourth is also probably the most compelling unique selling point. 
That's when I realised that most likely people's first experiences with TalkVeganToMe is going to be the website, irrespective of much I am in love with the app and want them to use it.

So I came up with the following path-to-released.

1. Make the website something I'm proud of.
2. Write rebuttals to vegan arguments
3. Polish up ethical purchasing advice
4. Final review of all content's accuracy and legibility

I'm debating adding a fifth:

5. Add a search function to the app and website.

I very much want this to be a feature at some point, but I don't know if it's necessary for release (i.e. if people will take one look at the app and think: unusable). Let me know what you think!

As an aside, next week is not going to be a super productive one either as I'm on holiday!


As always, you can see the pipeline for content on the [Trello board](https://trello.com/b/7ecEPfjW/talkvegantome-content)!

# 2019-06-08

This week has been super productive, focussing pretty much entirely on content and investigating some really interesting stats!

This week I managed to add 

- Facts - Ocean Plastic is mostly nets
- Facts - Most soy is fed to cattle
- Facts - WHO, FDA, BDA endorsements for vegan diets
- Facts - Almond Milk Water Usage
- Facts - Land Usage
- Facts - Tofu Causes Deforestation
- Vegan Lifestyle & Culture - Defined Documentaries template
- Vegan Lifestyle & Culture - Defined and fleshed out Organisations

You can see the pipeline for content on the Trello board.

Some of these, particularly the Land Usage and Almond Milk Water Usage stats were really fascinating to explore the original sources, and uncovered some pretty egregious misrepresentations of data.

# 2019-06-01

Thanks for signing up to the beta and downloading the app. Hopefully you've had a chance to browse around and make sure it works for you.
Probably the first thing you'll notice is that it is light on content. I'm working hard to rectify this, but as I'm just one person this is subject to my own schedule and may end up being a touch sporadic in updates!

This week I managed to add:

- Anti-Vegan Arguments - Protein
- Vegan Statistics - Animal Life Expectancy
- Vegan Statistics - Animal Slaughter Methods
- How to contribute

You can see the pipeline for content on the Trello board.
I'm always looking for new ideas, especially for stats to add, so just reply to this email with any ideas you've got and I'll add them to the board!
