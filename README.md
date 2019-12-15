# SinSandhi

Word joining and splitting tool based on Sinhalese (සිංහල) Sandhi (සන්ධි) rules.

## Installation

```bash
git clone https://github.com/yohanjk/sinsandhi.git
cd sinsandhi
python setup.py install
```

## Usage

* Word Joining
    ```python
    from sinsandhi import SandhiTool
    
    freq_dic_path = 'word_freq_dic.pickle'
    sandhitool = SandhiTool(freq_dic_path)
    
    sandhitool.join('ගුරු', 'උපදේශ')
    ```
* Word Splitting
    ```python
    from sinsandhi import SandhiTool
    
    freq_dic_path = 'word_freq_dic.pickle'
    sandhitool = SandhiTool(freq_dic_path)
    
    sandhitool.split('ගුරූපදේශ')
    ```
* Word Frequency Dictionary
    * Tool uses a word frequency dictionary to select the most probable outcome. 
    * When tool is initializing, the path of a Python dictionary saved as a `pickle file` can be specified, which has format of `{'word':'frequency in int'}`
* Output
    * Tool outputs a dictionary with `best` and `output` keys. Here, `best` and `output` keys contain the best and all possible results respectively.

## Notes
    * Tested on Python 3.7.3