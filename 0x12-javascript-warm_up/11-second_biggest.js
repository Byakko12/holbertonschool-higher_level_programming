#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
} else {
  args.sort((i, j) => i - j);
  args.pop();
  console.log(args.pop());
}
