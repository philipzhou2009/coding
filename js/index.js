const algo = require('./algorithms')
const regexp = require('./regexp')
let arr = [-5, 5, -4, 4, -3, 3, -2, 2, -1, 1, -6, 6]

// http://www.jianshu.com/p/ae620ad1c702
// http://www.bkjia.com/Javascript/1174199.html
// console.log(arr)

// const str = 'abcd1cba'
// console.log(algo.palindrome(str))

// console.log(algo.getMaxProfit(arr))

let template = '{{key1}}, {{key2}}? {{key1}}, {{key2}}!'
let data = {key1: 'hello', key2: 'world'}
console.log(regexp.regexpReplace(template, data))
