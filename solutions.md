---
header-includes:
  - \hypersetup{colorlinks=false,
            allbordercolors={0 0 0},
            pdfborderstyle={/S/U/W 1}}
---

## Chapter 1
### 1-1)

Let $a = -1$ and $b = -1$. Then,
\begin{align*}
a+b &= -2\\
&< \min(a,b) = -1
\end{align*}

### 1-3)
```
          30 km/h
   ___________________
  /                  /
 /      1 km/h      /
a ---------------- b
```

### 1-5)

#### (a)
\begin{align*}
S &= \{1,2\}\\
T &= 2
\end{align*}

#### (b)
\begin{align*}
S &= \{1,2\}\\
T &= 2
\end{align*}

#### (c)
\begin{align*}
S &= \{2,3,4\}\\
T &= 5
\end{align*}

### 1-7)
Base case: $z = 0$.

If $z = 0$, $\operatorname{multiply}(y,z) = 0 = y \times z$. Thus the base case is proven.

Assumptions: the recursive algorithm is correct for $z \leq n$, $y \ge 0$, and $c \ge 2$.

Inductive step: consider $z = n+1$.

Then,
\begin{align*}
& \operatorname{multiply}(y, n+1)\\
&= \operatorname{multiply}(cy, \lfloor (n+1)/c \rfloor) + y \cdot ((n+1) \bmod c)
\end{align*}

Since $c \ge 2$, we know that $\lfloor (n+1) / c \rfloor \leq n$ and thus
that the recursive part of the above equation is assumed correct. That is,
\begin{align*}
\operatorname{multiply}(cy, \lfloor (n+1)/c \rfloor) = cy \cdot \lfloor (n+1) / c \rfloor
\end{align*}

From this we obtain
\begin{align}
&\operatorname{multiply}(cy, \lfloor (n+1)/c \rfloor) + y \cdot ((n+1) \bmod c) \nonumber\\
&= cy \cdot \lfloor (n+1) / c \rfloor + y \cdot ((n+1) \bmod c) \nonumber \\
&= y \cdot (c \lfloor (n+1)/c \rfloor + (n+1) \bmod c)
\label{1_7_1}
\end{align}

To complete the proof we must show that
\begin{align*}
c \lfloor x/c \rfloor + x \bmod c = x
\end{align*}
for $x \in \mathbb{N}$, $c \geq 2$.

Let $x \bmod c \equiv a$. Then, $(x - a) / c = \lfloor x / c \rfloor$.
Substituting, we then obtain

\begin{align*}
(x - a) / c &= (x - x \bmod c) / c \\
&= \lfloor x / c \rfloor \\
&\Rightarrow x = x \bmod c + c \lfloor x / c \rfloor
\end{align*}

which is what we set out to show.

Finally, applying the above identity to \eqref{1_7_1} yields
\begin{align*}
& \operatorname{multiply}(cy, \lfloor (n+1)/c \rfloor) + y \cdot ((n+1) \bmod c) \nonumber\\
&= y \cdot (n+1)\\
\end{align*}
\begin{flushright} \rule{1.2ex}{1.2ex} \end{flushright}

### 1-9)
Base case: $n = 1$.

A list of a single element is already sorted. In this case, the algorithm does
nothing. Thus the base case is proven.

Assumptions: that $\operatorname{bubblesort}$ correctly sorts lists of length $n-1$.
That is, after having run the algorithm on a list $A$, $A[i] \leq A[i+1]$ for
$1 \leq i < n-1$.

Inductive step: consider lists of length $n$.

Note that in the algorithm, $i$ begins at $n$. Once this outer iteration
completes, $i$ will be set to $n-1$, and the remainder of the iterations are
assumed correct since they constitute an execution of
$\operatorname{bubblesort}$ on a list of length $n-1$. Thus we only need to
show that the largest element in the list is moved to position $n$ in the first
outer iteration, since the remainder of the list will be sorted correctly by
assumption.

Furthermore, it is clear that in the first outer iteration, the largest element
in the list is guaranteed to make its way to the end, since all elements are
compared and swapped if necessary.
\begin{flushright} \rule{1.2ex}{1.2ex} \end{flushright}

### 1-11)
**Base case:** $n = 0$. In this case we have an empty sum, which equates to zero.
This matches the closed form's value at $n = 0$ and thus the base case is proven.

Assumptions: the given summation is equal to $n(n+1)(2n+1)/6$ for $n = k-1$.

Inductive step: Consider $n = k$.

First, note that $n(n+1)(2n+1)/6 = (2n^3 + 3n^2 + n)/6$.

Pulling out the largest term of the summation reveals our assumption. Then,
\begin{align*}
    k^2 + \sum_{i=1}^{k-1}i^2
    &= k^2 + (k-1)((k-1)+1)(2(k-1)+1)/6 \\
    &= k^2 + (k-1)(k)(2k-1)/6 \\
    &= 6k^2/6 + (2k^3-3k^2+k)/6 \\
    &= (2k^3 + 3k^2 + k)/6 \\
    &= k(k+1)(2k+1)/6
\end{align*}
\begin{flushright} \rule{1.2ex}{1.2ex} \end{flushright}

### 1-13)
Base case: $n = 0$. In this case we have an empty sum, which equates to zero.
This matches the closed form's value at $n = 0$ and thus the base case is proven.

Assumptions: the given summation is equal to $n(n+1)(n+2)(n+3)/4$ for $n = k-1$.

Inductive step: Consider $n = k$.

First, note that $n(n+1)(n+2)(n+3)/4 = (n^4 + 6n^3 + 11n^2 + 6n)/4$.

Pulling out the largest term of the summation reveals our assumption. Then,
\begin{align*}
    & k(k+1)(k+2) + \sum_{i=1}^{k-1}i(i+1)(i+2) \\
    &= k(k+1)(k+2) + (k-1)((k-1)+1)((k-1)+2)((k-1)+3)/4 \\
    &= k(k+1)(k+2) + (k-1)(k)(k+1)(k+2)/4 \\
    &= (4k^3 + 12k^2 + 8k)/4 + (k^2-k)(k+1)(k+2)/4 \\
    &= (4k^3 + 12k^2 + 8k)/4 + (k^3 -k)(k+2)/4 \\
    &= (4k^3 + 12k^2 + 8k)/4 + (k^4 + 2k^3 -k^2 -2k)/4 \\
    &= (k^4 + 6k^3 + 11k^2 + 6k)/4 \\
    &= k(k+1)(k+2)(k+3)/4
\end{align*}
\begin{flushright} \rule{1.2ex}{1.2ex} \end{flushright}

### 1-15)
Base case: $n = 1$. Here the left and right hand sides both equal $1/2$ and
thus the base case is proven.

Assumptions: the given summation is equal to $\frac{n}{n+1}$ for $n = k-1$.

Inductive step: Consider $n = k$.

Pulling out the largest term of the summation reveals our assumption. Then,
\begin{align*}
    \frac{1}{k(k+1)} + \sum_{i=1}^{k-1}\frac{1}{i(i+1)} &= \frac{1}{k(k+1)} +
    \frac{(k-1)}{(k-1)+1}\\
    &= \frac{1}{k(k+1)} + \frac{k-1}{k} \\
    &= \frac{1}{k(k+1)} + \frac{k-1}{k} \cdot \frac{k+1}{k+1}\\
    &= \frac{1+(k-1)(k+1)}{k(k+1)} \\
    &= \frac{k^2}{k(k+1)} \\
    &= \frac{k}{k+1} \\
\end{align*}
\begin{flushright} \rule{1.2ex}{1.2ex} \end{flushright}


### 1-17)
Base case: $n=1$. A tree with a single vertex has no edges, and thus the base
case is proven.

Assumptions: a tree with $n$ vertices has exactly $n-1$ edges.

Inductive step: Consider a tree with $n$ vertices. By assumption, it has $n-1$
edges. Now let's add another node to the tree. If the node we add is a leaf
node, it will introduce one new edge to its parent. If the node is an
interior node, it will introduce one edge to its parent, and one edge to its
child, but we must also delete an edge to introduce the new interior node. This
covers all cases, both of which result in a tree of $n+1$ vertices and $n$
edges.
\begin{flushright} \rule{1.2ex}{1.2ex} \end{flushright}

### 1-19)
- No. If we make the generous estimate that an average book in my collection
has 1000 pages, I would need to own 1000 books to reach a million pages. I
don't have that many books.
- My school library has four floors. Each floor has an area of about 10,000 square feet.
Suppose the library has 10% of its area devoted to book storage. One book shelf
holds about 100 books. Suppose an average library book has 500 pages. Multiplying it out,
we get $4 \times 10,000 \times 0.1 \times 100 \times 500 = 200,000,000$.

### 1-21)
- $1,000,000 / 60 / 60 = 1,000,000 / 3,600 \approx 300$
- $300 / 24 \approx 12$

### 1-23)
I have no idea how wide the mouth of the Mississippi is, though I know it's a
very large river. Let's assume 1,000 metres wide and 5 metres deep. Then let's
assume it flows at a rate of 10 km/h. This gives us a flow rate of $50,000,000
\:\text{m}^3/\text{h}$, or $1,200,000,000 \:\text{m}^3/\text{day}$. Converting
to freedom units, we arrive at about 2.87 cubic miles per day.

### 1-25)
#### (a)
We can frame this as $kn^2 = \text{run time}$. $k(1000)^2 = 1\:\text{s}
\Rightarrow k = 1 \:\mu\text{s}$. For $n = 10,000$, we obtain a run time of $1
\:\mu\text{s} \times (10,000)^2 = 100 \:\text{s}$.

#### (b)
This time our formula is $kn\log{n} = \text{run time}$. $k(1000)\log{1000} = 1
\:\text{s} \Rightarrow k \approx 100.3 \:\mu\text{s}$. So for $n = 10,000$, we
obtain a run time of about $13.33 \:\text{s}$.

### 1-27)
[Note: the Psychic Modeling war story and this associated problem seem to be
somewhat misphrased in that the parameter $j$ appears to have no relevance to
the problem as stated. I did some incredulous googling and found that [I wasn't
the only one who was confused by
this](https://mikkqu.com/notes/psychic-modeling/). For this reason, I'm
choosing to ignore $j$ entirely.]

Given a candidate set $S$ (with $\lvert S \rvert = n$), slot count $k$, and
number of matching numbers necessary to win a prize $l$, we may identify
whether a given set of tickets establishes sufficient coverage to guarantee a
prize as follows.

Essentially, a set of tickets must cover the set of all $\binom{n}{l}$
combinations of numbers. However, the tickets don't actually need to cover all
of those combinations explicitly: they only need to cover the combinations for
which it is the case that for each $l$-subset that is not explicitly covered,
the addition of any $k-l$ numbers from $S$ not already in the $l$-subset to the
$l$-subset results in a winning ticket. We formalize this in the function
below.

```{.python include=src/1-27.py snippet=check-tickets}
```

A function implementing a greedy heuristic algorithm to generate good winning
combinations of tickets follows.

```{.python include=src/1-27.py snippet=gen-tickets}
```
