---
header-includes:
  - \usepackage{algorithm2e}
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
\ \text{m}^3/\text{h}$, or $1,200,000,000 \ \text{m}^3/\text{day}$. Converting
to freedom units, we arrive at about 2.87 cubic miles per day.

### 1-25)
#### (a)
We can frame this as $kn^2 = \text{run time}$. $k(1000)^2 = 1\ \text{s}
\Rightarrow k = 1 \ \mu\text{s}$. For $n = 10,000$, we obtain a run time of $1
\ \mu\text{s} \times (10,000)^2 = 100 \ \text{s}$.

#### (b)
This time our formula is $kn\log{n} = \text{run time}$. $k(1000)\log{1000} = 1
\ \text{s} \Rightarrow k \approx 100.3 \ \mu\text{s}$. So for $n = 10,000$, we
obtain a run time of about $13.33 \ \text{s}$.

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

### 1-29)
[For this problem we'll assume that no races can be tied. Also, that the
problem is asking for the minimum number of races \textit{across all problem
instances}, not for any specific cooked instance.]

Label each horse as $h_i$, $1 \leq i \leq 25$. Hold races between
$\{h_i,\dots,h_{i+4}\}$ for $i = 1, 6, \dots, 21$. After each race, eliminate
the slowest two horses, as they can't possibly be among the top three fastest.
After one round of this tournament, we have 15 horses remaining. Re-label these
horses from 1 to 15, where $h_1$ was the fastest from race 1, $h_2$ the second
fastest in race 1, $h_4$ the fastest in race 2, etc. Now race the top five
fastest horses $\{h_i\}_{i=1,4,7,10,13}$. Assume without loss of generality that
the horses finish in their labeled order. This allows us to eliminate all horses
known to be slower than horses 7, 10 and 13. Next, race horses $\{h_i\}_{2 \leq i
\leq 6}$. The fastest three horses are then, in order, $h_1$ and the two
fastest horses from the final race. This requires 7 races in total.


### 1-31)
Assumptions:

- There are 2 cars for every 3 Americans. This seems fairly reasonable given
that the United States has a high rate of car ownership, but many don't own
cars, and people also frequently share the ownership of cars.
- There is one gas station to every one thousand cars. This also seems
reasonable given the number of cars that a gas station should be able to
service per day (about 40 per hour, assuming the gas station is open 24/7).
- The United States has a population of 300 million.

Multiplying our assumptions out, we obtain
$$300,000,000 \ \text{people} \  \times \ 2/3 \ \text{cars}/\text{person} \times
\ 1/1,000 \ \text{gas stations}/\text{car} = 200,000 \ \text{gas stations}.$$

### 1-33)
Assumptions:

- The United States has an area of 10 million square kilometers.
- Roads criss cross the country in a grid pattern (obviously not true, but
useful for simplifying the proceeding calculation), with a spacing of 10
kilometers between them.
- The United States is shaped like a square (I know, I know...).

Then we obtain the edge length of the USA as $\sqrt{10^7} \ \text{km}^2
\approx 3163 \ \text{km}$. The number of roads going vertically is then $3163
\ \text{km} \ / \ 10 \ \text{km} \ = 316.3$,
each with a length of $3163 \ \text{km}$, for a total vertical road length
of $316.3 \times 3163 \ \text{km} \approx 1,000,457 \ \text{km}$. We have the
same amount of road in the horizontal direction, for a total of $2,000,914
\ \text{km} \ \approx 1,242,567 \ \text{miles}$ of road.

Looking it up, it seems I'm under by a factor of about 4.

### P1-1)
UVA Judge 100.
See $\texttt{src/p1-1.py}$.

### P1-3)
UVA Judge 10142.
See $\texttt{src/p1-3.py}$.

## Chapter 1
### 2-1)
We may derive a closed form for $\operatorname{mystery}(n)$ as follows.
Begin by expressing the function as a summation,
\begin{align*}
\operatorname{mystery}(n) &= \sum_{i=1}^{n-1} \sum_{j=i+1}^n \sum_{k=1}^j 1 \\
&= \sum_{i=1}^{n-1} \sum_{j=i+1}^n j
\end{align*}
In the following derivation we make use of the formulas $\sum_{i=1}^n i =
\frac{n(n+1)}{2}$ and $\sum_{i=1}^{n}i^2 = \frac{n(n+1)(2n+1)}{6}$.
\begin{align*}
\sum_{i=1}^{n-1} \sum_{j=i+1}^n j &= \sum_{i=1}^{n-1} \left( \sum_{j=1}^n j -
\sum_{k=1}^i k \right) \\
&= \sum_{i=1}^{n-1} \left( \frac{n(n+1)}{2} - \frac{i(i+1)}{2} \right) \\
&= \frac{1}{2} \left( n(n+1)(n-1) - \sum_{i=1}^{n-1}i(i+1) \right) \\
&= \frac{1}{2} \left( n(n+1)(n-1) - \left( \sum_{i=1}^{n-1}i^2 +
\sum_{i=1}^{n-1}i \right) \right) \\
&= \frac{1}{2} \left ( n(n+1)(n-1) - \left( \frac{n(n-1)(2n - 1)}{6} +
\frac{n(n-1)}{2} \right) \right) \\
&= \frac{1}{2} \left ( n(n+1)(n-1) - \left( \frac{2n^3 - 3n^2 + n}{6} +
\frac{3n^2 - 3n)}{6} \right) \right) \\
&= \frac{1}{2} \left ( \frac{6n^3-6n - 2n^3 + 2n}{6} \right) \\
&= \frac{n^3-n}{3} \\
\end{align*}
The worst-case running time of $\operatorname{mystery}(n)$ is $O(n^3)$, since
the number of operations it performs per increment of $r$ is independent of $n$,
and $r$ is incremented $\frac{n^3-n}{3} \in O(n^3)$ times.

### 2-3)
We may derive a closed form for $\operatorname{prestiferous}(n)$ as follows.
Begin by expressing the function as a summation,
\begin{align*}
\operatorname{prestiferous}(n) &= \sum_{i=1}^n \sum_{j=1}^i \sum_{k=j}^{i+j}
\sum_{l=1}^{i+j-k} 1 \\
&= \sum_{i=1}^n \sum_{j=1}^i \sum_{k=j}^{i+j} i+j-k \\
&= \sum_{i=1}^n \sum_{j=1}^i (i+j-j) + (i+j-j-1) + \dots + (i+j-i-j) \\
&= \sum_{i=1}^n \sum_{j=1}^i i + (i-1) + \dots + 1 \\
&= \sum_{i=1}^n \sum_{j=1}^i \frac{i(i+1)}{2} \\
&= \sum_{i=1}^n \frac{i^2(i+1)}{2} \\
&= \frac{1}{2} \left( \sum_{i=1}^n i^3 + \sum_{i=1}^n i^2 \right) \\
&= \frac{1}{2} \left( \frac{n^2(n+1)^2}{4} + \frac{n(n+1)(2n+1)}{6} \right) \\
&= \frac{3n^4+10n^3+9n^2+2n}{24}
\end{align*}
The worst-case running time of $\operatorname{prestiferous}(n)$ is $O(n^4)$,
since the number of operations it performs per increment of $r$ is independent
of $n$, and $r$ is incremented $\frac{3n^4+10n^3+9n^2+2n}{24} \in O(n^4)$ times.

### 2-5)
#### (a)
$2n$ multiplications are done in the worst case. Ignoring loop variable increments,
$n$ additions are done in the worst case.

#### (b)
$2n$ multiplications are done on the average.

#### (c)
We may improve this algorithm by using Horner's method. Rewrite the algorithm as

\begin{algorithm}[H]
\SetAlgoNoLine
\DontPrintSemicolon
$p \leftarrow a_n$\;
\For{$i \leftarrow n-1$ \KwTo $0$}{
    $p \leftarrow p * x + a_i$
}
\Return{$p$}\;
\end{algorithm}

This version uses only $n$ multiplications and $n$ additions.

### 2-7)
#### (a)
True. $2^{n+1} = 2(2^n) \in O(2^n)$, since we can take $c$ from the
definition of Big-Oh to be 2.

#### (b)
False. We proceed by contradiction. Suppose there exists a constant $c$ such
that $c2^n \geq 2^{2n} = (2^n)^2$ for $n \geq n_0$. Then $c \geq 2^n$, which is
impossible since $c$ is a constant.

### 2-9)
#### (a)
$g(n) \in O(f(n))$ since the $n^2$ term dominates.

#### (b)
$f(n) \in O(g(n))$ since the $n^2$ term dominates.

#### (c)
$f(n) \in O(g(n))$ since $\sqrt{n}$ dominates $\log{n}$.

#### (d)
$g(n) \in O(f(n))$ since $n$ dominates $\sqrt{n}$.

#### (e)
$g(n) \in O(f(n))$ since $\log^2{n}$ dominates $\log{n}$.

#### (f)
$f(n) \in O(g(n))$ since $n^2$ dominates $n \log{n}$.

### 2-11)
To prove $n^2 \in O(2^n)$, it suffices to show that $2^n$ dominates $n^2$.
Consider
$$\lim_{n \to \infty} \frac{n^2}{2^n}$$
We prove that this limit equals $0$ by applying L'Hôpital's rule twice:
\begin{align*}
\lim_{n \to \infty} \frac{n^2}{2^n} &= \lim_{n \to \infty}
\frac{\frac{d}{dn}n^2}{\frac{d}{dn}2^n} \\
&= \lim_{n \to \infty} \frac{2n}{2^n \ln{2}} \\
&= \lim_{n \to \infty} \frac{\frac{d}{dn}2n}{ \ln{2}\frac{d}{dn}2^n} \\
&= \lim_{n \to \infty} \frac{2}{ \ln^2{2} \cdot 2^n} \\
&= \frac{2}{\ln^2{2}}\lim_{n \to \infty} \frac{1}{2^n} \\
&= 0
\end{align*}
\begin{flushright} \rule{1.2ex}{1.2ex} \end{flushright}

### 2-13)
Let $f_1(n) \in O(g_1(n))$ and $f_2(n) \in O(g_2(n))$. Then by definition
$\exists\; c_1, c_2, n_1, n_2$ such that $$c_1g_1(n) \geq f_1(n) \;\forall\; n \geq n_1$$
and $$c_2g_2(n) \geq f_2(n) \;\forall\; n \geq n_2$$
Now consider $f_1(n) + f_2(n)$. Combining inequalities gives us
$$ c_1g_1(n) + c_2g_2(n) \geq f_1(n) + f_2(n) \;\forall\; n \geq
\operatorname{max}(n_1, n_2)$$
Finally, taking $c_3 = \operatorname{max}(c_1, c_2)$ and $n_3 = \operatorname{max}(n_1,n_2)$
yields
\begin{align*}
& c_3(g_1(n) + g_2(n)) \geq f_1(n) + f_2(n) \;\forall\; n \geq n_3 \\
& \Rightarrow f_1(n) + f_2(n) \in O(g_1(n) + g_2(n))
\end{align*}
\begin{flushright} \rule{1.2ex}{1.2ex} \end{flushright}

### 2-15)
Let $f_1(n) \in O(g_1(n))$ and $f_2(n) \in O(g_2(n))$. Then by definition
$\exists\; c_1, c_2, n_1, n_2$ such that $$c_1g_1(n) \geq f_1(n) \;\forall\; n \geq n_1$$
and $$c_2g_2(n) \geq f_2(n) \;\forall\; n \geq n_2$$
Now consider $f_1(n) \cdot f_2(n)$. Combining inequalities gives us
$$ c_1g_1(n) \cdot c_2g_2(n) \geq f_1(n) \cdot f_2(n) \;\forall\; n \geq
\operatorname{max}(n_1, n_2)$$
Finally, taking $c_3 = \operatorname{max}(c_1, c_2)$ and $n_3 = \operatorname{max}(n_1,n_2)$
yields
\begin{align*}
& c_3(g_1(n) \cdot g_2(n)) \geq f_1(n) \cdot f_2(n) \;\forall\; n \geq n_3 \\
& \Rightarrow f_1(n) \cdot f_2(n) \in O(g_1(n) \cdot g_2(n))
\end{align*}
\begin{flushright} \rule{1.2ex}{1.2ex} \end{flushright}

### 2-17)
We need to show that $\exists\; c_1, c_2, n0$ such that
$$(n+a)^b \leq c_1n^b \quad \forall\; n \geq n_0$$
and
$$(n+a)^b \geq c_2n^b \quad \forall\; n \geq n_0$$

Let $c_1 = 2^b$. Then for all $n \geq 2|a| = n_0$,
\begin{align*}
& n+a \leq 2n \\
\Rightarrow\quad& (n+a)^b \leq 2^bn^b
\end{align*}

Since we've fixed $n_0 = |a|$, we need to find $c_2$ such that
$$(n+a)^b \geq c_2n^b \qquad\forall\; n \geq |a|$$

Let $c_2 = 2^{-b}$. Then for all $n \geq 2|a| = n_0$,
\begin{align*}
& n+a \geq 2^{-1}n \\
\Rightarrow\quad& (n+a)^b \geq 2^{-b}n^b
\end{align*}

\begin{flushright} \rule{1.2ex}{1.2ex} \end{flushright}

### 2-19)

- $(1/3)^n$
- $6$
- $\log\log{n}$
- $\ln{n}$ same
- $\log{n}$ same
- $(\log{n})^2$
- $n^{\frac{1}{3}} + \log{n}$
- $\sqrt{n}$
- $\frac{n}{\log{n}}$
- $n$
- $n \log{n}$
- $n^2$
- $n^2 + \log{n}$
- $n^3$
- $n - n^3 + 7n^5$
- $(3/2)^n$
- $2^n$
- $n!$

### 2-21)
#### (a)
True

#### (b)
False

#### (c)
True

#### (d)
False

#### (e)
True

#### (f)
True

#### (g)
False

### 2-23)
#### (a)
Yes, worst-case analysis says nothing about how long the algorithm might take
on non-worst-case inputs.

#### (b)
Yes, $O(n^2)$ is only an upper bound. It is not necessarily tight.

#### (c)
Yes, the $\Theta(n^2)$ only indicates a tight bound for worst-case inputs.

#### (d)
No, the algorithm must take $\Theta(n^2)$ time on at least one input.

#### (e)
Yes, because $n^2$ dominates $n \log_2{n}$ in the odd $n$ case and thus both cases
are $\Theta(n^2)$.

### 2-25)
#### (a)
$g(n) = \log{n}$, since partial sums of the harmonic series can be expressed as
a function whose dominant term is $\ln{n}$.

#### (b)
$g(n) = n$

#### (c)
$n\log{n}$

#### (d)
$g(n) = n\log{n}$, since Stirling's approximation states that $log_2{n!} =
n\log{n} - n\log{e} + \Theta(\log{n})$, and $l\log{n}$ is the dominant term.

### 2-27)
1. $f_2(n) \in O(\sqrt{n} \log{n})$
2. $f_1(n) \in O(n)$
3. $f_3(n) \in O(n \sqrt{\log{n}})$
4. $f_4(n) \in O(n^\frac{3}{2})$

### 2-29)
\begin{align*}
\sum_{i=1}^n 3^i
&= \frac{3^{n+1} - 1}{2} - 1 \quad \\
&= \frac{1}{2} \left( 3^{n+1} - 3 \right) \in \Theta(3^{n+1}) \\
&= 3\left(\frac{1}{6} \left( 3^{n} - 3 \right)\right) \in \Theta(3^{n}) \\
&= 3^2\left(\frac{1}{18} \left( 3^{n-1} - 3 \right)\right) \in \Theta(3^{n-1}) \\
\end{align*}

So all of \textbf{(a)}, \textbf{(b)}, and \textbf{(c)} are true.

### 2-31)
#### (a)
$A \in O(B), o(B)$ since $2^n$ dominates all polynomial functions of $n$.

#### (b)
$A \in O(B), o(B)$ since $\sqrt{n}$ dominates all polylogarithmic functions of
$n$.

#### (c)
None of the relations hold since $B$ oscillates between $n$ and $1/n$.

#### (d)
$A \in O(B), o(B)$ since $100^n = (10^2)^n = (10^n)^2$ which dominates $10^n$.

#### (e)
$$\lim_{n \to \infty} \frac{n^{\lg{n}}}{(\lg{n})^n} = 0 \Rightarrow A \in O(B),
o(B)$$

#### (f)
Stirling's approximation gives $$\ln{n!} = n\ln{n} - n + \Theta(\ln{n})$$
so $A \in O(B), \Omega(B), \Theta(B)$.

### 2-33)
Each number $T_{ij}$ in column $j$ of row $i$ has three children. It contributes
its value to each of them. Thus $T_{ij}$ is counted three times in the sum of
$T_{i+1,j}$. Summing over $j$, we obtain
\begin{align*}
&S(i) = \sum_{j}T_{ij} \\
&= 3 \sum_{j}T_{i-1,j} \\
&= 3 \cdot S(i-1) \\
&= 3 \cdot 3 \cdot S(i-2) \\
&= 3 \cdot 3 \cdot \dots S(0) \\
&= 3^i
\end{align*}
for $i \geq 0$.

### 2-35)
#### (a)
$$T(n) = \sum_{i=1}^n\sum_{j=i}^{2i}1$$

#### (b)
\begin{align*}
&T(n) = \sum_{i=1}^n\sum_{j=1}^{i+1}1 \\
&= \sum_{i=1}^n i+1 \\
&= n + \sum_{i=1}^n i \\
&= n + \frac{n(n+1)}{2}
\end{align*}

### 2-37)
Multiplication in this fashion has worst-case time complexity $O(nb^n)$, since a
base-$b$, $n$-digit number can represent values up to $b^n - 1$. The product
$(b^n - 1)^2$ would require adding two $n$-bit values $b^n - 1$ times, for a
total of $n(b^n - 1) \in O(nb^n)$ addition operations. Note that this ignores
carries, which would only contribute up to an additional factor of $b$,
something which may be ignored in the Big-Oh representation due to it already
being exponential in $n$.

### 2-39)
#### (a)
\begin{align*}
a^{\log_a{x} + \log_{a}y} &= a^{\log_a{x}}a^{\log_a{y}} \\
&= xy \\
\Rightarrow \log_a{(xy)} &= \log_a{a^{(\log_a{x} + \log_{a}y)}} \\
&= \log_a{x} + \log_a{y}
\end{align*}

#### (b)
\begin{align*}
\log_a{x^y} &= \log_a{\left(\prod_{1}^y x\right)} \\
&= \sum_{1}^y \log_a{x} \\
&= y\log_a{x}
\end{align*}

#### (c)
\begin{align*}
a^{\log_a{x}} &= b^{\log_b{x}} \\
\Rightarrow \log_b{a^{\log_a{x}}} &= \log_a{x} \cdot \log_b{a} \\
&= \log_b{b^{\log_b{x}}} \\
&= \log_b{x} \\
\Rightarrow \log_a{x} &= \frac{\log_b{x}}{\log_b{a}}
\end{align*}

#### (d)
\begin{align*}
\log_b{y} &= \frac{\log_x{y}}{\log_x{b}} \\
\Rightarrow x^{\log_b{y}} &= x^{\frac{\log_x{y}}{\log_x{b}}} \\
&= y^\frac{1}{\log_x{b}} \\
&= y^{\log_b{x}}
\end{align*}
since $\log_{b}x = \frac{1}{\log_x{b}}$ is a special case of the usual
log base swap formula.

### 2-41)
$k$ bits can represent $2^k$ different values, or integers $0 \leq n \leq
2^k-1$. We need to show that $k = \lfloor \lg_2{n} \rfloor + 1$.

For the case $k=1$ it is easily verified that the above holds.

Now considering only the largest possible value of $n$, $n=2^k-1$,
representable by $k > 1$ bits and taking logs, we obtain $\lg_2{n} =
\lg_2{(2^k-1)}$. But $\lg_2{2^k} = k$, and $\lg_2{2^{k-1}} = k-1$, so
\begin{align*}
& k-1 < \lg_2{(2^k-1)} < k \\
&\Rightarrow \lfloor \lg_2{(2^k-1)} \rfloor = k-1 \\
&\Rightarrow \lfloor \lg_2{(2^k-1)} \rfloor + 1 = k \\
&\Rightarrow \lfloor \lg_2{n} \rfloor + 1 = k
\end{align*}
\begin{flushright} \rule{1.2ex}{1.2ex} \end{flushright}

### 2-43)
Assumptions: we don't get to choose $k$ (otherwise we could trivally select an
empty subset), $0 \leq k \leq n$, we have access to random numbers, and we
don't need to make our choices until we've made our pass over the entire
subset.

For each number $s$ in $S$ we may generate a random number $r$ and store $(r,
s)$ in a heap keyed on $r$. Once we've seen all of $S$, pop the top $k$
values from the heap.

### 2-45)
Let's ignore the assignment performed at the beginning. Assume a uniform
random distribution on $A[i]$ and on the location of $\min{A[i]}$.

The probability that a swap is made at position $i$, $p_i$, is the probability
that $A[i]$ is the minimum amongst $A[0 \dots i]$. Given our uniform
distribution, $p_i = 1/(i+1)$. The expected value of the number of swaps made
over all of $A$ is then
\begin{align*}
\sum_{i=1}^n p_i &= \sum_{i=1}^n \frac{1}{i+1} \\
&= \left(\sum_{i=2}^{n+1} \frac{1}{i} \right) \\
&\sim \ln{n}
\end{align*}

### 2-47)
Take 1 coin from bag 1, 2 coins from bag 2, \dots, 10 coins from bag 10, and
place the chosen coins all in one bag. Weigh that bag. The scale will report a
weight of $550-i$, where $i$ is the bag with the false coins.

### 2-49)
Assume companies merge as pairs. Then the number of ways for them to merge
is the same as the number of binary trees with $n$ leaves.

We have $\binom{n}{2}$ choices for the first merge, $\binom{n-1}{2}$ for the
second, etc. This results in a total number of ways to merge $T(n)$ given by
\begin{align*}
T(n) &= \prod_{i=0}^{n-2} \binom{n-i}{2} \\
&= \prod_{i=0}^{n-2} \frac{(n-i)!}{2(n-i-2)!} \\
&= \frac{n!(n-1)!}{2^{n-1}} \\
\end{align*}

### 2-51)
Label each pirate $p_i, 1 \leq i \leq 6$ in order of increasing seniority.

Consider the terminal state where only two pirates remain, and the more senior
of them, $p_5$, proposes that he receive all $300, and then secures 50% of the
vote with just his own. Now step backward to the state where three pirates
remain. Knowing that $p_6$ will receive $0 if the voting goes another round,
$p_4$ can offer $p_6$ $1 for his vote, securing himself $299. Now step backward
again, and repeat the process. Here $p_3$ can offer $p_5$ $1. Back another
step, and $p_2$ can offer $p_4$ and $p_6$ $1 each. Back one last time, and
$p_1$ can offer $p_3$ and $p_5$ $1 each. The final division is then $p_1:
\$298$, $p_3: \$1$, $p_5: \$1$, and $0 for the rest.

### L2-1)
https://leetcode.com/problems/remove-k-digits/

See $\texttt{src/l2-1.py}$.

### L2-3)
https://leetcode.com/problems/4sum/

See $\texttt{src/l2-3.py}$.

### 3-1)
A stack is the appropriate data structure for this problem.
We give an algorithm in Python below.
```{.python include=src/3-1.py snippet=balanced-parens}
```

### 3-3)
#### (a)
Consider the following sequence of insertions and deletions:

1. Insert 1025 elements (length = 1025, capacity = 2048)
2. Delete two elements (length = 1023, capacity = 1024)
3. Insert two elements (reallocate and copy; length = 1025, capacity = 2048)
4. Delete two elements (length = 1023, capacity = 1024)
5. Insert two elements (reallocate and copy; length = 1025, capacity = 2048)

etc.

With this access pattern, we must copy $\Theta(n)$ elements for every two deletions and
insertions.

#### (b)
Consider a similar underflow strategy, except that instead of shrinking the array
at $< 1/2$ capacity, we shrink it at $< 1/4$. This prevents this oscillatory
behaviour we saw with the previous strategy, since it takes $O(n)$ deletions
(roughly $n/2$) instead of $O(1)$ deletions to trigger a shrink operation. For this
reason the array has constant amortized cost per deletion.

### 3-5)
#### (a)
The overhead fraction is $4 / (2 * 4 + 4 + 4) = 1/4$.

#### (b)
The overhead fraction depends on how full the tree is.

For a degenerate binary tree (linked list) with $n$ nodes, the fraction would
be $4/(4 + 4(n-1)) = 1/n$.

For a full binary tree (with $n = 2^k - 1$ nodes), the fraction would be
$$4(\lfloor n/2 \rfloor + 1) / (4n) \approx 1/2$$
Thus the overhead fraction $f(n)$ is bounded as $$1/n \leq f(n) \lessapprox 1/2$$
