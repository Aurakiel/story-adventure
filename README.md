# **Story Adventure**

## Project Notes: 02/28/2025 ##

> Cleaned up the comments so they were more consistent in style. Added a Chapter Two file and fully scripted the
> "Go Forward" options.  Realized a text base game is going to have lots of code lines. I'm debating creating a second
> file for the "Go West" options just to keep everything in its place. As of now, I've got 3 different beginnings for 
> Chapter 3...on one path.  That's pretty tame all things considered. In order to keep it that way I had to make more 
> choices than I wanted result in the player death. There's only one path out with the Crimson Orb and it's not direct.
> First round of tests looked good. More story to be added - Next up are the "Go West" options for Chapter 2.

## Project Notes: 02/25/2025 ##

> Not a big update today. Just went back and cleaned up the display/narration in the pre-game chapters.
> Everything looks more consistent. In doing this though, I did catch an area of code that needed some error catching.
> I solved my problem with the player submitting an empty name, but I didn't account for it if the player
> decided to change their name.  Shoved the while loop fix in to that section of code to prevent it from happening
> there. I still need to create some dialogue during the game over screen, but it can wait until after the final two 
> chapters are coded. 

## Project Notes: 02/24/2025 ##

> Mainly worked on Chapter One today. I deleted and altered so much code it became headache inducing
> but I'm finally happy with how everything is working so far. <br><br>
> 
> Currently working on going back and cleaning up the narration in the naming/stats sections so it looks as polished 
> as Chapter One. Also adding some explanation regarding random encounters. I've got them mostly happening after a 
> selection and made it so the hero's hp is reset to max if they survive. The victory display does show how much hp
> they had left over at the end just so they can see how close they came to death. <br><br>
>
> As much as I would like to have written the story myself, I just didn't have the time so AI got fed prompts and I made
> alterations as needed. Chapter One is solid though...for now.  Holding out it stays that way. Two more chapters to go 
> before wrapping things up.

## Project Notes: 02/23/2025 ##

> Dear reader, if you knew what life was slinging at me right now, you'd be proud of your
> girl for sticking with it. Enough of that talk though...<br><br>
> Got the console display cleaned up enough to start progressing the story.  After realizing these
> chapters were going to require a ton of code, I figured it best to shove it all in their own files.
> I've started Chapter One - everything is looking good so far. Lots of different match cases and if statements
> to follow - testing area is holding chapter one for now so the hero stats are carried over from the function
> file. I've boosted those defaults. Still really pumped the random encounters didn't take as long as expected.

## Project Notes: 02/22/2025 ##

> Update 2: Spent most of the day working on enemies and random encounters. Alot
> of code has been added to the functions file. I just went back and added the comments
> and caught a couple errors in the process.  It explained why it was working fine sometimes
> and weirdly at random - finalized testing for now.  Everything appears to be working the 
> way it should be. It's really only getting iffy when I'm pulling a function to test above
> where it should be in the program. Running everything in order is as intended. <br> <br>
> ***Next Step:*** More writing. The random encounters were the hard part. Next update
> should progress the game along. I may need to play with enemy hp/atk more though - not going
> to have a problem making sure it's playable in one sitting with the hero dying more often than
> I'd like  👀 oops!
> 
> Update 1: It's been a wild couple days preventing me from working on the project
> however, I've made up for lost time tonight. <br> <br>
> I've finished all the pre-game set up. Player naming and initial stats are 
> done for now unless changes are made later. In doing this I've added classes
> for armor and weapon bonuses. <br> <br>
> I've added a function to display hero stats and another for a generic loading
> bar just to give the player time to fully read the screen before a clear happens. 
> I updated the intro screen/narration in the process. I'm a lot happier with the
> opening. <br> <br>
> ***Next Step:*** Begin working on chapter one.  This is going to involve creating
> classes for mobs. I'm shooting for 3 chapters just so the game stays playable in
> one sitting. Overall really happy with today's work. Hold on to that energy.

## Project Notes: 02/18/2025 ##

> Update 2: So, I figured out the direction. We're going with a
> narration driven story adventure you can play in one sitting. 
> That avoids the save state issue and heavy coding I don't have
> time for in a side project. 

***General Ideas***
- Randomize the story OR Randomize the encounters
- Randomize the story AND Randomize the encounters
- Just start coding and see where it goes (leaning into
- this one hard)
>
> Update 1: Shelved previous project (Random Adventure) to start
> fresh - realized before I started going nuts I needed to work on
> how to code save states so the game did not need to be completed
> in one sitting. First push is probably going to be a hot mess of
> ideas with zero direction.  I've yet to code anything yet. 