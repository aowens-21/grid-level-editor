# grid-level-editor
This grid based level editor is a very simple level editor that consists of a 2D array of Block objects. This is saved to a file and represented as a 2D array of 1s and 0s. 

## Important Controls
Left-Click: Add a block (means there is something in that grid space)
Right-Click: Remove a block (means the grid space is empty)
Resize: You can resize the window at any point, but not the level
Exit: Upon exit it saves the file as an .txt file full of 1s or 0s

## Small Tutorial
When you first run the program, a prompt will appear in the console window asking for the level's width, this will be in
16px grid spaces, so for example if you enter 32, the level size will be 32x16 pixels: 512. The same thing applies for height, which is asked next.

After you have entered the size, you will be asked for the name of the level. This name does not need to include a file extension, as a .txt is appended upon inputting the name.

Use the controls defined above to change your level however you want, and then hit X to close the application and save your level. The file will be saved into the working directory under the name you specified.

### Potential Improvements/Features:
- Ability to load in a .txt file and edit a pre-existing level
- Some kind of GUI as opposed to console input
- Resizing the level while editing (keeping the populated blocks)
- Make the main loop run on a consistent framerate (probably unnecessary for this application though)
