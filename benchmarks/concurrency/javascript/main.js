const N_TASKS = 100000;
let counter = 0;

async function task() {
    counter++;
}

async function main() {
    const promises = [];
    for (let i = 0; i < N_TASKS; i++) {
        promises.push(task());
    }

    await Promise.all(promises);
    console.log(`Done. Counter: ${counter}`);
}

main();
