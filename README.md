console.log("Все числа от 1 до 20:");
for (let i = 1; i <=20; i++) {
    console.log(i);
}

console.log("Четные числа от 1 до 20:");
for(let i = 1; i<= 20; i++) {
    if(i % 2 === 0) {
        console.log(i);
    }
}

let sumOdd = 0;
for (let i = 1; i <= 20; i++) {
    if (i % 2 !== 0) {
       sumOdd += i; 
       console.log("Сумма нечетных чисел от1 до 20:", sumOdd);
         
    }
}
