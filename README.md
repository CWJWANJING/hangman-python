# hangman-python

This is the hangman game written in python. You will be given a random frequently used word and the length of the word. You need to guess what the word is by guessing a letter or a word each term. You have 11 chances, each time you guessed a wrong one the girl will be drew with one more stroke and until her entire body be drawn. After 11 chances you will lose and the girl will look like this:

<pre>
|------------  
|        |  
|        |  
|      //O\\   
|       /|\    
|      / | \   
|       / \    
|      /   \   
|                 
|------------  
</pre>

Your goal is to successfully guess the word before the girl dies. 

## Usage

After downloading all the files, you can start the game by simply using this command under the same directory:

```python
python hangman.py
```

The file *1-1000.txt* stores the most commonly used 1000 words, and the file *hanging_stages.txt* stores the different stages of what the hanging girl would look like.

Have fun!
