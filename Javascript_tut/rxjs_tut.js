// RxJs (Reactive Extensions for Javascript) - A library for working with async and event-based data streams
// Stream --> A stream is a sequence of ongoing events over time that you can process as they occur.
// RxJS provides tools for creating, transforming and subscribing to these streams
// import {Observable} from 'rxjs';

const { Observable, filter, map } = require('rxjs');
const { of } = require('rxjs');

// Observable --> represents a stream of data that can be observed 

// const dataStream = new Observable((observer) => {
//     let count = 0;

//     const intervalId = setInterval(() => {
//         count +=1;
//         observer.next(`Data Emitted: ${count}`);

//         if(count == 5){
//             observer.complete();
//         }
//     },1000);

//     return () => {
//         clearInterval(intervalId);
//         console.log("Stream stopped");
//     }
// })
// // 1 - 1s
// // 2 - 2s

// // Step 2: Subscribe to the Observable

// const subscription = dataStream.subscribe({
//     next: (data) => console.log(data), // called when data is emitted
//     error: (err) => console.error('Error:',err),
//     complete: () => console.log("Stream Completed!")
// });

// // Unsubscribe after 7 seconds (cleanup)

// setTimeout(() => {
//     subscription.unsubscribe();
//     console.log("Unsubscribed");
// },7000);

// Common Operator

// Observable "Simple"
const numbers = of(1,2,3,4,5)

numbers.pipe(
    filter((num) => num % 2 == 0),
    map((num) => num * 10)
).subscribe((result) => console.log(result))

