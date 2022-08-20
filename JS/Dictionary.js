


class Dictionary {
  constructor(wordsArray, useWordMap) { 
    if (!useWordMap) {
      this.dict = new Set(wordsArray);
    } else {
      //Achieving O(1) lookup:
      //initialize dict as map of keyVal:keyVal using reducer 
      //(https://www.digitalocean.com/community/tutorials/js-finally-understand-reduce)
      const wordMap = wordsArray.reduce((acc, word)=> {
        acc[word] = word;
        return acc;
      }, {}); //acc initialized to {}
      this.dict = wordMap;
    }
  }

  isInDict(word) {
    //wordMap
    if (this.dict[word] !== undefined) return true;

    if (!word.includes("*")){
      return this.dict.has(word); //false
    }
    //some -> https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some
    return this.dict.some((dictWord) => {
      const regexTemplate = word.replaceAll('*', '.');
      const regex = new RegExp(`^${regexTemplate}$`);
      return regex.test(dictWord)
    });
  }

  getAll() {
    let result = []
    this.dict.forEach (function(value) {
      result.push(value);
    })
    return result;
  }

  filter(substr) {
    //convert set to list by spreading, then filter!
    const values = [...this.dict].filter((word) => word.includes(substr)); // [2, 4]
  }
}

const test = new Dictionary(['cat', 'bat'], false);
console.log(test.isInDict('cat'));