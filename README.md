# SinSandhi

Word joining and splitting tool based on Sinhalese (සිංහල) Sandhi (සන්ධි) rules.

## Installation
* Dependencies
    * nltk - To process text files
    * tqdm
```bash
git clone https://github.com/yohanjk/sinsandhi.git
cd sinsandhi
python setup.py install
```

## Usage

* Word Joining
    ```python
    from sinsandhi import SandhiTool
    
    freq_dic_path = 'word_freq_dic.txt'
    sandhitool = SandhiTool(freq_dic_path) # or SandhiTool()
    
    sandhitool.join('ගුරු', 'උපදේශ')
    ```
* Word Splitting
    ```python
    from sinsandhi import SandhiTool
    
    freq_dic_path = 'word_freq_dic.txt'
    sandhitool = SandhiTool(freq_dic_path) # or SandhiTool()
    
    sandhitool.split('ගුරූපදේශ')
    ```
* Word Frequency Dictionary
    * Tool uses a word frequency dictionary to select the most probable outcome. 
    * When tool is initializing, the path of the word frequency dictionary can be specified, which is a text file with the following format. 
    ```text
      <word> <frequency as int>
      <word> <frequency as int>
      <word> <frequency as int>
    ```
    * Additionally, tool has a utility function to create a word frequency dictionary from a large text file as follows.
    ```python
      from sinsandhi import create_word_freq_dic
  
      text_file = 'data/sample.txt'
      freq_dic_file = 'data/sample_freq_dic.txt'
      create_word_freq_dic(text_file, freq_dic_file)  
    ``` 
* Output
    * Tool outputs a dictionary with `best` and `output` keys. Here, `best` and `output` keys contain the best and all possible results respectively.
    * Example
    ```python
      {'best': 'ගුරූපදේශ', 'output': {'ගුරූපදේශ': 13, 'ගුරුපදේශ': 2}}
    ```

## Notes
   * Tested on Python 3.7.3
