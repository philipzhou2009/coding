const { MinPriorityQueue, MaxPriorityQueue } = require('@datastructures-js/priority-queue');
let logger = true ? console.log : () => { };

const patientsQueue = new MinPriorityQueue();

let array = [5, 3, 1, 7];

for (const element of array) {

    patientsQueue.enqueue(element, element);

}

patientsQueue.enqueue(7, 7);

logger(patientsQueue.toArray());