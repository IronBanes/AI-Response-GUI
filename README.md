# AI-Response-GUI
This tkinter GUI takes three prompts from the user's supplied instruction files. These files populate the dropdown box within the GUI allowing the user to change what prompt before inputting the information they need to process.

# Info
The GUI has two tabs at the moment
Tab 1: Generate
  The Generate tab handles the openAI integration part of the GUI. This is the tab where you are processing your prompts with user-supplied information. 
 
  ![image](https://github.com/IronBanes/AI-Response-GUI/assets/19214784/77a76104-e689-4997-97c3-973ad5b47875)

Tab 2: Image
  The Image tab gathers the width and length of a collection of images and creates an Excel sheet listing the image name and respective sizes. 
  
  ![image](https://github.com/IronBanes/AI-Response-GUI/assets/19214784/ba569f32-9ff9-4528-a273-0c8d2ae12415)

# Instructions
To use the Tkinter GUI you need to change a few of the files. 
The first file to change is the .env file

The next files to change are the instructions files with the apps\tabs\modules\memory to match the prompts you want to use

Once both files are updated for your use case you should be ready to use the generate tab portion of the GUI to your needs. 

![image](https://github.com/IronBanes/AI-Response-GUI/assets/19214784/b5f1901d-e410-4b84-947b-690825ab473a)

The image processing portion of the GUI only needs a folder of images to be located after pressing the select folder button

![image](https://github.com/IronBanes/AI-Response-GUI/assets/19214784/9371017e-8b4c-41d4-be28-ca0bc55fd8c6)

After selecting the folder you press start and it will generate an Excel sheet with the image information. 
