let matriculas = [1,3,5,7,8,9,10,15];
matriculas.push(20);
console.log(matriculas); // [1, 3, 5, 7, 8, 9, 10, 15, 20]
matriculas.pop();
console.log(matriculas); // [1, 3, 5, 7, 8, 9, 10, 15]
matriculas.unshift(2, 4, 6);
console.log(matriculas); // [2, 4, 6, 1, 3, 5, 7, 8, 9, 10, 15]
console.log(matriculas.includes(10)); // true
console.log(matriculas.includes(0)); // false
console.log(matriculas.indexOf(10)); // 8
console.log(matriculas.indexOf(30)); // -1
//matriculas =  [4, 6, 1, 3, 5, 7, 8, 9, 10, 15]
console.log(matriculas.slice(0, 4)); // [4, 6, 1, 3]
var myFish = ["angel", "clown", "mandarin", "surgeon"];

//remove 0 elementos a partir do índice 2, e insere "drum"
var removed = myFish.splice(2, 0, "drum");
//myFish é ["angel", "clown", "drum", "mandarin", "surgeon"]
//removed é [], nenhum elemento removido

//remove 1 elemento do índice 3
removed = myFish.splice(3, 1);
//myFish é ["angel", "clown", "drum", "surgeon"]
//removed é ["mandarim"]

//remove 1 elemento a partir do índice 2, e insere "trumpet"
removed = myFish.splice(2, 1, "trumpet");
//myFish é ["angel", "clown", "trumpet", "surgeon"]
//removed é ["drum"]

//remove 2 elementos a partir do índice 0, e insere "parrot", "anemone" e "blue"
removed = myFish.splice(0, 2, "parrot", "anemone", "blue");
//myFish é ["parrot", "anemone", "blue", "trumpet", "surgeon"]
//removed é ["angel", "clown"]

//remove 2 elementos a partir do indice 3
removed = myFish.splice(3, Number.MAX_VALUE);
//myFish é ["parrot", "anemone", "blue"]
//removed é ["trumpet", "surgeon"]