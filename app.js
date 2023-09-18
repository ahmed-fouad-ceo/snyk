const regex = /^(\d+)+$/; // Vulnerable regular expression

const input = '11111111111111111111111111111111111111111111111111111111!'; // Input that can trigger ReDoS

if (regex.test(input)) {
  console.log('Valid input');
} else {
  console.log('Invalid input');
}
