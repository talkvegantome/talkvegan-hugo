# TalkVeganToMe - Content [![Build Status](https://travis-ci.org/talkvegantome/talkvegan-hugo.svg?branch=master)](https://travis-ci.org/talkvegantome/talkvegan-hugo)

# Our Mission

1. Make the day-to-day lives of vegans easier by making information easily accessible
2. Make vegan advocacy in all its forms easier to learn about, understand, and do
3. Ensure we do not promote messaging which harm any other justice movements
4. Embody the compassion that veganism typifies in all our material and interactions
5. Ensure the accuracy of our information and provide _full disclosure_ of mitigating information even if it undermines the argument being presented
6. Not to engage in the gatekeeping of veganism (no-one can take away your V card)
7. Not to use the platform to further the personal agenda or profit of the individual contributors
8. Use the platform to promote inclusion and intersectional messaging wherever possible
9. Remind ourselves and everyone else that veganism is about the animals, not the vegans.

# Contributing

## High level steps

1. Fork the repository
2. Create the new page using `hugo new category-name/page-name.md` 
3. Write your content in Markdown (don't forget to swap `draft` to false!)
4. Preview the website by running `hugo server` and navigating to `http://localhost:1313`
5. Commit and push your update
6. Raise a Pull Request against this repo with your changes.

For more details on these steps see our [CONTRIBUTING.md](CONTRIBUTING.md) page.

## Writing Good content

1. Don't boil the ocean. Submit contributions frequently and often to ensure no-one gets overwhelmed.
2. Opinionated is good, but ensure it doesn't contravene the mission statement.
3. Science wins, cite your _original_ sources.
4. Make key information easily available. Link to other people's long form articles, don't write your own.
5. Be charitable in interpreting other people's arguments, even if you don't like them.
6. If an argument (charitably interpreted) is flawed, bigoted, or misleading, it is _not_ your responsibility to represent it as equally valid.
7. Veganism is about the animals. When writing persuasions (rebuttals, reasons to go vegan, etc.) try to ensure your response keeps animal welfare at the centre of your argument.

# Deployment

Deployment is performed automatically by Travis CI to the Github Pages site. As this is also the source for the app's refresh url, it will also ensure the app's content gets updated as soon as a refresh occurs.
