let array = [];
let array2 = [];
let count = 10000;

for (let i = 1; i <= count; i++) {
    array.push(i);
}

for (let k = 0; k < array.length; k++) {
    const index = array.indexOf((d(array[k])));   
    if (index !== -1 ) array2.push(index + 1);
}

array = array.filter(x => {
    return array2.indexOf(x) === -1
})

console.log(array.join('\n'))

function d(n) {
    let sum = n;
    const temp = n.toString().split('');
    for (let j = 0; j < temp.length; j++) {
        const num = Number(temp[j]);
        sum += num;
    }
    return sum;
}