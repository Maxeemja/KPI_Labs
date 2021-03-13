
//відсортувати слова за зростанням кількості голосних у них
const str = "Ознайомлення з рядками та використання основних методів їх обробки в мові програмування Джава";
const golosni = ["а", "е", "є", "и", "і", "ї", "о", "у", "ю", "я", "А", "Е", "Є", "И", "І", "Ї", "О", "У", "Ю", "Я"];

let arr = str.replace(/[0-9]|[...]|[.,\/#!$%?\^&\*;:{}=\-_`~()@]/g, ' ').trim().split(' ');

    
let dict = {};

for (let word of arr){
    //let w = word.toLowerCase();
    let w = word.split('');
    let counter = 0;
    for (w of word){
        if(golosni.includes(w)){
            counter++;
        }
    }
    dict[word] = counter;
}
let sortable = [];
for (let i in dict) {
    sortable.push([i, dict[i]]);
}

sortable.sort(function(a, b) {
    return a[1] - b[1];
});
for(let i in sortable){
    sortable[i].pop();
}

console.log(sortable.join(' '));