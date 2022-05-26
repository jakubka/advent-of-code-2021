class Point {
  private connections: Point[] = [];
  public flashed = false;
  constructor(public n: number) {}

  public addConnections(p: Iterable<Point>) {
    this.connections.push(...p);
  }

  public getConnections() {
    return this.connections;
  }

  public increment() {
    if (this.n != 10) {
      this.n++;
    }
  }

  public flash() {
    if (this.n == 10 && !this.flashed) {
      this.flashed = true;
      for (const p of this.connections) {
        p.increment();
      }
      for (const p of this.connections) {
        p.flash();
      }
    }
  }

  public resetIfFlashed() {
    if (this.n == 10) {
      this.n = 0;
      this.flashed = false;
    }
  }

  public toString(): string {
    if (this.flashed) {
      return "_";
    }
    return this.n.toString();
  }
}

const p = (n: number) => new Point(n);

const grid = [
  [p(3), p(2), p(6), p(5), p(2), p(5), p(5), p(2), p(7), p(6)],
  [p(1), p(5), p(3), p(7), p(4), p(1), p(2), p(6), p(6), p(5)],
  [p(7), p(3), p(3), p(5), p(7), p(4), p(6), p(4), p(2), p(2)],
  [p(6), p(4), p(2), p(6), p(3), p(2), p(5), p(6), p(5), p(8)],
  [p(3), p(8), p(5), p(4), p(4), p(3), p(4), p(3), p(6), p(4)],
  [p(8), p(7), p(1), p(7), p(3), p(7), p(7), p(4), p(8), p(6)],
  [p(4), p(5), p(2), p(2), p(2), p(8), p(6), p(3), p(2), p(6)],
  [p(6), p(3), p(3), p(7), p(7), p(7), p(2), p(8), p(4), p(5)],
  [p(8), p(8), p(2), p(4), p(3), p(8), p(7), p(6), p(6), p(5)],
  [p(6), p(3), p(5), p(1), p(5), p(8), p(6), p(4), p(8), p(4)],
];

// const grid = [
//   [p(5), p(4), p(8), p(3), p(1), p(4), p(3), p(2), p(2), p(3)],
//   [p(2), p(7), p(4), p(5), p(8), p(5), p(4), p(7), p(1), p(1)],
//   [p(5), p(2), p(6), p(4), p(5), p(5), p(6), p(1), p(7), p(3)],
//   [p(6), p(1), p(4), p(1), p(3), p(3), p(6), p(1), p(4), p(6)],
//   [p(6), p(3), p(5), p(7), p(3), p(8), p(5), p(4), p(7), p(8)],
//   [p(4), p(1), p(6), p(7), p(5), p(2), p(4), p(6), p(4), p(5)],
//   [p(2), p(1), p(7), p(6), p(8), p(4), p(1), p(7), p(2), p(1)],
//   [p(6), p(8), p(8), p(2), p(8), p(8), p(1), p(1), p(3), p(4)],
//   [p(4), p(8), p(4), p(6), p(8), p(4), p(8), p(5), p(5), p(4)],
//   [p(5), p(2), p(8), p(3), p(7), p(5), p(1), p(5), p(2), p(6)],
// ];

function* getNeighbours(row_i: number, col_i: number) {
  function* inner() {
    yield row_i > 0 && col_i > 0 && grid[row_i - 1][col_i - 1];
    yield row_i > 0 && grid[row_i - 1][col_i];
    yield row_i > 0 && col_i < 9 && grid[row_i - 1][col_i + 1];
    yield col_i > 0 && grid[row_i][col_i - 1];
    yield col_i < 9 && grid[row_i][col_i + 1];
    yield row_i < 9 && col_i > 0 && grid[row_i + 1][col_i - 1];
    yield row_i < 9 && grid[row_i + 1][col_i];
    yield row_i < 9 && col_i < 9 && grid[row_i + 1][col_i + 1];
  }
  for (const p of inner()) {
    if (p) {
      yield p;
    }
  }
}

for (const [row_i, row] of grid.entries()) {
  for (const [col_i, p] of row.entries()) {
    p.addConnections(getNeighbours(row_i, col_i));
  }
}

function* iterPoints() {
  for (const row of grid) {
    for (const p of row) {
      yield p;
    }
  }
}

function* filter<T>(a: Iterator<T>, p: (a: T) => boolean) {
  let current = a.next();
  while (current.done == false) {
    if (p(current.value)) {
      yield current.value;
    }
    current = a.next();
  }
}

function count<T>(a: Iterator<T>): number {
  let c = 0;
  let current = a.next();
  while (current.done == false) {
    c++;
    current = a.next();
  }
  return c;
}

function print() {
  for (const row of grid) {
    for (const p of row) {
      Deno.writeAllSync(
        Deno.stdout,
        new TextEncoder().encode(`${p.toString()} `)
      );
    }
    console.log();
  }
  console.log();
}

console.log(`Before any steps:`)
print()

for (let i = 0; i < 1000; i++) {
  for (const p of iterPoints()) {
    p.increment();
  }
  for (const p of iterPoints()) {
    p.flash();
  }
  console.log(`After step: ${i + 1}:`)
  print()
  const flashedThisRound = count(filter(iterPoints(), (p) => p.flashed));
  if (flashedThisRound == 100) {
    console.log(i + 1);
    break;
  }
  for (const p of iterPoints()) {
    p.resetIfFlashed();
  }
}

