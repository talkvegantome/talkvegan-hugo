# Contributing

In order to contribute you'll  need to have the following pre-requisites:

## Pre-requisites

1. A Github account [Sign up here](https://github.com/join)
2. GitHub Desktop installed [Install it from here](https://desktop.github.com/)
3. Hugo installed [Mac - Brew](https://gohugo.io/getting-started/installing/#install-hugo-with-brew), [Windows](https://gohugo.io/getting-started/installing/#windows)
4. A Markdown or text editor installed like [Macdown](https://macdown.uranusjr.com/) or [Typora](https://typora.io/)


## Quick Start

**Objective:** Contribute content to both the TalkVeganToMe app and website.
**Tip:** Make sure you've fulfilled the pre-requisites before trying the quick start!


### Making changes

1. Fork the [TalkVeganToMe Hugo Github Repo](https://github.com/talkvegantome/talkvegan-hugo) by pressing the button on the top right hand corner. (This makes a copy of it in your Github account.)
2. Open GitHub Desktop, sign in, and click on the TalkVeganToMe Hugo repo under "Your Repositories" and click "clone". **Important:** Make a note of the "Local Path" it's cloning it to so you can find it again!
3. Open up the command line (**Mac:** press Command+Spacebar and search for 'terminal', **Windows:** press Win+R and type 'cmd'.)
4. In the terminal window type `cd <path>` (where `<path>` is the "Local Path" you made a note of earlier, if you can't find it it's probably in Documents) and hit enter.
5. Type `hugo server`, hit enter and then copy the link from the line that says `Web Server is available at http://localhost:1313/` and paste it into your browser
6. Tada! You should see the TalkVeganToMeApp running on your computer!
7. Open up your Markdown editor (e.g. Macdown or Typora) and open the file inside the "Local Path" from earlier that's under `content/english/splash.md`, make any changes you like, and save the file.
8. Refresh the front page in your browser (making sure you're on `http://localhost:1313`) and you should see your new text!

### Making a new page

**Important:** You must have followed the first 5 steps in Making Changes prior to making a new page.

1. Open your terminal and browse to the Local Path (see Making Changes) 
2. Type `hugo new ../<language>/<category-name>/<new-page-name>.md` (e.g. `hugo new ../english/vegan-statistics/numnber-of-vegans.md`)
3. Open the new file in your Markdown editor

### Formatting text

The TalkVeganToMe use a formatting syntax called Markdown, which uses simple symbols to format the text.  
Check out this [cheat sheet](https://www.markdownguide.org/cheat-sheet/) for a quick start


### Saving changes
1. Open Github Desktop
2. You should see the files you've changed in the bar on the left. Hit the button at the bottom saying "Commit to Master".
3. On the right hit "Push Origin"
4. Done! Your file is now saved in GitHub so even if your laptop dies you can get it back.

### Submitting Changes

**Important:** You must have saved your changes first, see Saving Changes above.

1. Navigate to your fork of the TalkVeganToMe Hugo repo by going to [Github.com](https://github.com) and clicking on the `<your-username>/talkvegan-hugo`
2. In the little grey bar below the green 'Clone or download' button, click the button labelled "Pull request".
3. In the next screen click the "Create Pull Request" button
4. In the title and description enter a summary of what you've changed or added, and why.
5. Click "Create pull request".
6. Done! The TalkVeganToMe team will receive a notification that you've add a contribution and will get back to you with an approval or feedback as soon as possible.


## Links

- [TalkVeganToMe Hugo Github Repo](https://github.com/talkvegantome/talkvegan-hugo)
- [Github Desktop](https://desktop.github.com/)
- Hugo - [Mac - Brew](https://gohugo.io/getting-started/installing/#install-hugo-with-brew), [Windows](https://gohugo.io/getting-started/installing/#windows)
- Markdown Editors - [Macdown](https://macdown.uranusjr.com/) or [Typora](https://typora.io/)
- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
