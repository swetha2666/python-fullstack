var x
x=[1,2,3,4,5]
y=x.length // for array length o/p is 5
console.log(y)
 
z=x.push(6)
console.log(x) //push 6 into end of the array

z=x.pop(6)
console.log(x) //pop 6 at end of the array

z=x.shift(1)
console.log(x) // remove first element


z=x.unshift(2,1) // add element at starting index
console.log(x)


s=x.indexOf(3)
console.log(s) //find index