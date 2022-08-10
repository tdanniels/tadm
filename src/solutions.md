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

```{.python include=python/src/q01_27.py snippet=check-tickets}
```

A function implementing a greedy heuristic algorithm to generate good winning
combinations of tickets follows.

```{.python include=python/src/q01_27.py snippet=gen-tickets}
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
See $\texttt{python/src/p01\_01.py}$.

### P1-3)
UVA Judge 10142.
See $\texttt{python/src/p01\_03.py}$.

## Chapter 2
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

See $\texttt{python/src/l02\_01.py}$.

### L2-3)
https://leetcode.com/problems/4sum/

See $\texttt{python/src/l02\_03.py}$.

## Chapter 3
### 3-1)
A stack is the appropriate data structure for this problem.
We give an algorithm in Python below.
```{.python include=python/src/q03_01.py snippet=balanced-parens}
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
Consider a similar underflow strategy, except that instead of shrinking the
array at $< 1/2$ capacity, we shrink it at $< 1/4$. Note that we still shrink
it down to half its capacity. This prevents this oscillatory behaviour we saw
with the previous strategy, since it takes $O(n)$ deletions (roughly $n/2$)
instead of $O(1)$ deletions to trigger a shrink operation. For this reason the
array has constant amortized cost per deletion.

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

### 3-7)
Allocate two memory locations to hold the minimum and maximum. Every time after
an item is inserted, check if the new item is less than the minimum or greater
than the maximum, and update if necessary. Whenever an item is deleted, if it's
the minimum or maximum element, update the minimum or maximum element with the
deleted item's successor.

### 3-9)
Since every key in $S_1$ is smaller than any key in $S_2$, we could just make
the root of $S_1$ the left child of the smallest item in $S_2$. However, this
would result in a poorly balanced tree. Better would be to make $S_1$ the left
subtree of a new tree, and $S_2$ the right subtree of the same new tree. But
how to choose the root of the new tree? We can take either the maximum element
of $S_1$ or the minimum element of $S_2$, detach it from its parent, and make
it the root of the new tree.

An implementation is given below.
```{.python include=python/src/q03_09.py snippet=concat-bsts}
```

### 3-11)
#### (a)
This can be accomplished with a 2D array indexed by $i$ and $j$ that stores the
minimum between $x_i$ and $x_j$. The array's entries are precomputed in $O(n^2)$
total time, which is required to initialize the array anyway.

#### (b)
Consider a complete binary tree that stores all $n$ values in its leaf nodes.
If $n = 2^k$, no modifications are required, otherwise we can pad out the tree
with infinite-valued nodes which have no effect on $\min$ queries. The tree's
internal nodes store the minimum values of all nodes beneath them. A tree of
this description would require $\Omega(n)$ space: $n$ leaf nodes and $n-1$
internal nodes.

Queries are answered recursively. Given a sequence $X = x_1, \dots, x_n$ and a tree
$T$ as described above, consider the query $\min_{i \dots j}{X}$. We answer the
query recursively as follows.

Starting at the root, we have $\min_{1 \dots n}X$. If $i = 1$ and $j = n$, we
are done. Otherwise, the interval $[i, j]$ can be classified as either (a)
being contained entirely within the left subtree of $T$, (b) contained entirely
within the right subtree of $T$, or (c) contained within the union of the left
and right subtrees. In the case of either (a) or (b), we recursive into either
the left or right subtree, respectively. In the case of (c), we recurse into
both. The goal is to find vertices which exactly cover $[i, j]$, and take the
minimum over their union in order to obtain $\min_{i \dots j}{X}$. It can be
shown that, for each level of the tree, we will only need to visit at most 4
nodes. Since the height of the tree is $O(\log{n})$, then the query complexity
is also $O(\log{n})$. Our proof proceeds by induction.

Base case: at the root node, we visit only one node (the root itself), which
is fewer than 4 nodes.

Assumptions: we visit at most 4 vertices at the $k$th level of the tree.

Inductive step: consider a recursive descent from the $k$th level of the tree.
Our goal is to find nodes that cover $[s, t]$. By assumption, we may visit at
most 4 nodes on this level. If we have only visited two nodes on this level,
then we can visit no more than 4 nodes on the next level, since each node
generates at most two recursive calls. Otherwise, suppose we have visted 3 or 4
nodes at this level. Consider the middle 1 or 2 vertices of the 3 or 4,
respectively. We know that the outer nodes of the 3 or 4 must cover the
endpoints $s$ and $t$, therefore the middle 1 or 2 vertices must cover the
entire contiguous range not covered by the outer vertices. Thus, we will not
need to recurse into the middle 1 or 2 nodes, and only the outer nodes will
potentially recurse into the $k+1$th level up to twice each, for a total of 4
nodes visited on level $k+1$ as well.
\begin{flushright} \rule{1.2ex}{1.2ex} \end{flushright}

### 3-13)
We use a similar tree structure to the one described in 3-11 (b). $A[1..n]$
stores the leaf nodes, and the auxiliary array $B[1..n]$ stores the internal
nodes, with the parent of $A[i]$ ($i \geq 0$) located at $B[\lfloor i/2 \rfloor]$, the
parent of $B[j]$ ($j < \lceil n/2 \rceil$) at $B[\lceil n/2 \rceil + \lfloor j/2
\rfloor]$, etc. Internal nodes store the sums of their children.

Then, $Add(i, y)$ requires us to add $y$ to $A[i]$ as well as all parents of
$A[i]$. This is $O(\log{n})$.

$Partial{\text -}sum(i)$ is computed recursively the same way as described in
3-11 (b), with the $\operatorname{min}$ operation replaced by summation.
This is also $O(\log{n})$.

### 3-15)
Note: this approach uses an approach inspired by the paper "An Efficient
Representation for Sparse Sets" by Briggs and Torczon. As suggested by
the title, their algorithm only works for sets, though it could
be modified to allow repetitions, but those modifications would exceed
the constraints of the problem. In order to support repeated integers,
I've taken the liberty of assuming that our memory locations are wide enough
to support the concatenation of two array indices.

This solution uses the suggested two arrays $A$ and $B$. We also use
one additional piece of memory, $t$, initialized to 0, that tracks the total
number of integers present in the table. The three required operations are
implemented as follows.

$\operatorname{search}(X)$: Read $A[X]$ to obtain an index $j$ into $B$.
If $j = 0$ or $j > t$, it is invalid, and $X$ is not present in the table.
Otherwise, read $B[j]$ to obtain the value $k||l$ ($||$ denotes concatenation).
If $k = X$, then $A[X]$ is 'vouched for,' and we may conclude that $X$ is present.
$l$ is unused here.

$\operatorname{insert}(X)$: If $t = n$, return an error. Otherwise, perform
$\operatorname{search}(X)$ to determine if $X$ is already present. If it is,
hold on to the value $j$. Otherwise set $j = 0$. Now increment $t$. Then write
$t$ into $A[X]$. Then, write $X||j$ into $B[t]$.

$\operatorname{delete}(X)$: First perform $\operatorname{search}(X)$ to
determine if $X$ is already present. If it isn't, return an error. Otherwise,
hold on to the values $j$ and $l$. Zero out $B[j]$. Then if $l \neq 0$, set
$A[X] := l$. Decrement $t$. We could also zero out $A[X]$ if $l = 0$, but it
isn't strictly necessary, since $B[j]$ no longer vouches for it.

### 3-17)
See $\texttt{python/src/q03\_17.py}$.

### 3-19)
Put the most frequently worn shirts in the most easily reached place. Kind of
like an LRU cache. (I refuse to suggest that anyone do a binary search over shirts...)

### 3-21)
Python affords a particularly nice implementation of this.
```{.python include=python/src/bst.py snippet=bst-def}
```
```{.python include=python/src/bst.py snippet=bst-eq}
```

### 3-23)
```{.python include=python/src/linkedlist.py snippet=reverse-ll dedent=4}
```

### 3-25)
Count the number of occurrences of each character in the search string.
Allocate a counter for each of the unique characters, and a counter for the
total number of characters required. Then iterate over each character in the
magazine and incremenent its counter if its target value has not been reached.
If a character's counter is incremented, increment the 'total' counter as well.
Halt and return true if the total reaches its target value. Otherwise, if all
characters have been checked and the target total count has still not been
reached, return false.

### 3-27)
The solution to this problem is the well known "Tortoise and Hare" algorithm.
An implementation is given below.
```{.python include=python/src/linkedlist.py snippet=tortoise-hare-ll dedent=4}
```

### 3-29)
We use two layers of hash tables in the algorithm below. It runs in $O(n)$ time
and uses $O(n)$ memory, where $n$ is the length of the corpus.
```{.python include=python/src/q03_29.py snippet=max-bigram}
```

### L3-1)
https://leetcode.com/problems/validate-binary-search-tree/

See $\texttt{python/src/l03\_01.py}$.

### L3-3)
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

See $\texttt{python/src/l03\_03.py}$.

## Chapter 4
### 4-1)
Sort the $2n$ players using any $O(n\log{n})$ sorting algorithm. Put the
first $n$ sorted players into team $A$, and the remaining $n$ into team $B$.
Since the sum of team $A$'s ratings is minimal and the sum of team $B$'s ratings
is maximal, the rating disparity between teams is maximized.

Note that this could also be achieved in $O(n)$ time using quickselect with
median of medians pivot selection (in order to guarantee linear time) to find
the median player, and then partitioning around that player.

### 4-3)
In order to minimize the maximum sum of any pair, we seek to pair the smallest
number with the largest number, the second smallest with the second largest,
etc. This can be achieved by sorting the $2n$ numbers with any $O(n\log{n})$
sorting algorithm and then iterating forwards from the beginning and backwards
from the end of the sorted sequence, pairing up the first and last numbers, the
second and second to last, etc.

### 4-5)
The mode of a multiset can be computed in $O(n)$ expected time and $O(n)$ space
with a hash table, by hashing each number and storing its multiplicity in the
table, then iterating over the table to find the number with the largest
multiplicity.

The mode can also be computed in $O(n\log{n}$) time and $O(1)$ space by sorting
the multiset and then iterating over the sorted sequence, counting the
multiplicity of each repeated number and storing the maximum count in a
register.

### 4-7)
#### (a)
Sort the telephone bills and checks by account number and place them in their
own stacks. (Merge sort would be a decent sorting algorithm to do by hand).
Then attempt to pair the bill on top of its stack with a check for the same
account number from the top of its corresponding stack. Accounts with unpaired
bills have unpaid bills, though if there can be multiple checks/bills from the
same account, the unpaid ones aren't necessarily the unpaired ones. This is
$O(n\log{n})$.

#### (b)
Use bucket sort on the books, bucketed by the 30 publishers, then count the size
of each bucket. This is $O(n)$.

#### (c)
Sort the checkout cards by name, and then scan the sorted pile for the count
of unique names. This is $O(n\log{n})$.

### 4-9)
Note that these can both be solved in $O(n)$ expected operations and $O(n)$
space with a hash table. We give sorting-based solutions below.

#### (a)
Sort $A$ and $B$ in ascending order, then iterate over them pair-wise,
inserting an item from the current pair $(a, b)$ into $C = A \cup B$ according
to the following rules:

- If $a = b$, insert $a$ into $C$ and advance the iterators for $A$ and $B$.
- If $a < b$, insert $a$ into $C$ and advance the iterator for $A$.
- If $a > b$, insert $b$ into $C$ and advance the iterator for $B$.
- If either of the queues has emptied out, insert the remaining elements of the
non-empty set into $C$.

#### (b)
Repeat the second half of the algorithm in (a), after $A$ and $B$ have been sorted.

### 4-11)
Note that this can be accomplished with a hash table that maps from elements to
element counts by hashing all elements and then scanning for keys with
counts greater than $n/2$ or $n/4$.

Since this is the sorting chapter, we give a sorting-based solution below.

Apply a quickselect-like procedure where we recursively partition the list
about a random pivot, recursing only into sublists of size $> n/2$ (or $n/4$).
Modify the $\operatorname{partition}$ function to track whether all elements in
a sublist are identical. If we partition a sublist of sufficient size with all
identical elements, append that element to the output list and move on to the
next sublist of sufficient size. When we run out of sublists of sufficient
size, return the output list, which may be empty. The expected number of
operations performed is $O(n + n/2 (+ n/4)) \in O(n)$.

### 4-13)
#### (a)
Doesn't matter. The maximum element can be retrieved in $O(1)$ from both a
max-heap and sorted array.

#### (b)
The heap is better. Deletion can be achieved in $O(\log{n})$, while deletion
from a sorted array is $O(n)$.

#### (c)
The heap is better, since it can be constructed in $O(n)$. Sorting the array is
$O(n\log{n})$.

#### (d)
The array is better, since the minimum element can be found in $O(1)$. The
max-heap requires $O(n)$, since each leaf must be visited in the worst case.

### 4-15)
#### (a)
We can construct a \textit{max tournament tree}, a binary tree in which each
parent node contains the greater of its children, with the $n$ keys as leaves,
in at most $n-2$ comparisons: $n/2$ comparisons at height 0 (the leaves) to
determine the next round of the tournament, $n/4$ at height 1, etc., for a
total of

$$ \sum_{i=1}^{\lceil \lg{n} \rceil} \frac{n}{2^i} \leq n $$

comparisons in the worst case of a complete tree. Label the finalists $a$ and
$b$ from largest to smallest. Then the second-largest element is one of $a$ or
$b$, or a descendant of $a$. We must thus traverse back down the path of $a$,
comparing elements to $b$, costing us $\lceil \lg{n}\rceil - 1$ more
comparisons, for a total of $n - 1 + \lceil \lg{n} \rceil$ comparisons in the
worst case.

#### (b)
The same data structure as in (a) can be used. Construct the tournament at the
cost of at most $n$ comparisons. We then identify the third largest
semifinalist at the cost of 1 comparison. Label the three largest semifinalists
$a, b, c$ from largest to smallest. Then the third largest element of the input
will either be a descendant of $a$ or $b$, or it will be $c$. We then must
traverse down the paths of $a$ and $b$, comparing elements to $c$ (or a
greater-valued element if we find one), at a cost of $2\lceil \lg{n} \rceil -
4$ additional comparisons, for a total of $n - 3 + 2\lceil \lg{n} \rceil$
comparisons in the worst case.

Note that this algorithm \textit{does} (and must) identify the two largest keys
$a$ and $b$ in the process as well.

### 4-17)
#### (a)
Quicksort would make $$\sum_{i=0}^{\lg{n} - 1} n = n\lg{n}$$ comparisons.

#### (b)
Quicksort would make $$\sum_{i=0}^{\log_{3/2}{n} - 1} n = n \log_{3/2}{n} \approx 1.71\lg{n}$$ comparisons.

### 4-19)
#### (a)
Consider a permutation of the integers $1, 2, \dots, n$. Assume that we're
using the total order defined by the "less than" relation. Clearly, the
permutation with the maximal number of inversions is $n, n-1, \dots, 1$. How
many inversions exactly? The $n-1$ numbers that follow $n$ are all inversions,
the $n-2$ numbers that follow $n-1$ are all inversions, etc. Thus we may count
the total number of inversions as $$\sum_{i=1}^{n-1}i = n(n-1)/2$$ Thus it is
clear that the permutation of $n$ items that has $n(n-1)/2$ inversions is one
in which all $n$ (unique) items are sorted in reverse order.

#### (b)
Consider a permutation $P$ on $n$ unique items and its reversal $P^r$. Suppose
$P$ has $k$ inversions. Then the remaining pairs in $P$, of which there must be
$\binom{n}{2} - k = n(n-1) - k$, are not inverted. Since $P$'s reversal $P^r$
turns inverted pairs into non-inverted pairs and vice-versa, we then have a total
of $k + n(n-1) - k = n(n-1)$ inversions between them.

#### (c)
Consider the set $P$ of all permutations on $n$ distinct items. The cardinality
of $P$ is $n!$. The expected number of inversions in a random permutation is
given by

\begin{align*}
\sum_{p \in P} \frac{\operatorname{inversions}{(p)}}{n!} &=
\frac{1}{n!}\sum_{p \in P} \operatorname{inversions}{(p)}
\end{align*}

We can partition $P$ into two sets $Q$ and $R$ of equal size $n!/2$, where $R$
contains the reversals of all permutations in $Q$. We may then express the
previous sum as

\begin{align*}
\frac{1}{n!}\sum_{p \in P} \operatorname{inversions}{(p)}
&= \frac{1}{n!} \left( \sum_{q \in Q} \operatorname{inversions}{(q)} +
   \sum_{r \in R} \operatorname{inversions}{(r)} \right) \\
&= \frac{1}{n!} \left( \frac{n!}{2} \frac{n(n-1)}{2} \right) \\
&= \frac{n(n-1)}{4}
\end{align*}

### 4-21)
In order to be stable, mergesort needs to ensure that during the merge
operation, items from the "left" (lower indexed) merge queue are inserted
before items from the "right" (higher indexed) merge queue when the items are
considered equal.

### 4-23)
This can be achieved with a hash-based counter in $O(n) \in O(n\log\log{n})$
operations and $O(\log{n})$ additional space. A dynamic perfect hash function
may be used in order to obtain guranteed worst-case performance.

Iterate over the input sequence, hashing each integer and incrementing its
associated counter. This can be done in $O(n)$ operations. Afterwards, the
number of keys in the table will be $O(\log{n})$. Then sort the keys with any
$O(n\log{n})$ sorting algorithm and decompress the keys for a worst-case total runtime of
$O(n + \log{n}\log\log{n}) \in O(n\log\log{n})$.

### 4-25)
Our algorithm must take at least $O(n)$ time, since we must examine every number in
the input. An $O(n)$ sorting algorithm can be implemented for this input
distribution as follows.

Construct a perfect hash table keyed on the elements of $A$ with values equal
to the counts of the elements of $A$ at the cost of $O(n)$ operations and
$O(\log\log{n})$ space. Then sort the items at the cost of
$(\log\log{n}\log\log\log{n})$ operations. Then decompress the items at the
cost of $O(n)$ operations for an overall worst-case runtime of $O(n)$.

### 4-27)
For each edge $e_i$ in $P$, compute the pair of angles $(\alpha_i, \beta_i)$
that corresponds to the vector from $q$ to either endpoint of $e_i$. Sort the
pair so that $\alpha_i \leq \beta_i$. This can all be done in $\Theta(n)$, where $n$ is
the number of edges in $P$.

We wish to find the angle $\hat{\theta}$ which lies between the maximum number
of $(\alpha_i, \beta_i$) pairs. Split apart the angle pairs and sort them
individually, maintaining a tag on each angle for whether it's an $\alpha_i$ or
$\beta_i$ angle, at a cost of $O(n\log{n})$ operations. Then scan through them,
incrementing a counter whenever an $\alpha_i$ angle (line segment beginning) is
encountered, and decrementing the same counter whenever a $\beta_i$ angle (line
segment end) is encountered. The $\alpha_i$ angle at which the counter reaches
its maximum value is $\hat{\theta}$.

### 4-29)
If such a priority queue existed, $O(n)$ comparison-based sorting could be
implemented by inserting all elements in a sequence into the queue at a cost of
$O(n)$ ($n times $O(1)$), and then extracting them all into an array, also at a
cost of $O(n)$. This contradicts the $\Omega(n\log{n})$ lower bound on
comparison-based sorting, and so such a queue cannot exist.

### 4-31)
- Given $A$ and $k$, $\operatorname{max}(A)$ can be found at $A[(n - 1 + k) \bmod n)]$
(using 0-based indexing).
- We can use one-sided binary search to find $k$, and then obtain
$\operatorname{max}(A)$ using the method described above. More specifically,
we compare $A[0]$ against $A[1]$, $A[2]$, $A[4]$, $A[8]$, etc., until we
encounter a value smaller than $A[0]$, or we reach the end of $A$. Then we can
repeat the process between the previous index and the one at which we found the
smaller value (or reached the end of $A$). Note that this only works for arrays $A$
without any duplicated values. An implementation in Python is given below.

```{.python include=python/src/q04_31.py snippet=find-k}
```

### 4-33)
We can use a binary search-like algorithm in which we begin our search in the
middle of the sequence at $a_{\lfloor n/2 \rfloor}$, recurse into the left half of
the sequence if $a_{\lfloor n/2 \rfloor} > \lfloor n/2 \rfloor$, and recurse
into the right half of the sequence if $a_{\lfloor n/2 \rfloor} < \lfloor n/2
\rfloor$. If we visit an index $i$ such that $a_i = i$ we return true,
otherwise if we arrive at a search window of size 1 without finding such an
$i$, we return false.

### 4-35)
We can attempt "2-D binary search" in which our search windows are rectangles.
An implementation in Python is given below.

```{.python include=python/src/q04_35.py snippet=binary-search-2d}
```

Unfortunately, the algorithm performs poorly in comparison to the
somewhat well known "saddleback" search given below.

```{.python include=python/src/q04_35.py snippet=saddleback}
```

The saddleback algorithm makes at most $n + m - 1$ comparisons. I haven't
analyzed the complexity of "2-D binary search," though is most likely superlinear.

### 4-37)
See $\texttt{python/src/sorting.py}$ for the implementation.

Output:

```
$ python python/src/q04_37.py
len(tokens) = 4400
Sample output: ['a', 'able', 'about', 'above', 'access', 'accomplished', 'according',
'account', 'accounts', 'achieved']
Sort function 'sort' took 0.0005221809988142923 seconds: 1.000x baseline.
Sort function 'selection_sort' took 0.4750563739980862 seconds: 909.754x baseline.
Sort function 'insertion_sort' took 0.808971163998649 seconds: 1549.216x baseline.
Sort function 'heapsort' took 0.02820608500041999 seconds: 54.016x baseline.
Sort function 'mergesort' took 0.012172155998996459 seconds: 23.310x baseline.
Sort function 'quicksort' took 0.014101160002610413 seconds: 27.004x baseline.
```

Some comments:

- Heapsort is noticeably slower than the other fast sorting algorithms.
This isn't too surprising given its reputation for being the slowest of the
fast sorting algorithms. I also didn't use the $O(n)$ heapify. This is perhaps
also exacerbated by function call overhead, given that CPython doesn't do any
inlining.
- Mergesort is marginally faster than quicksort. This can perhaps be explained by
repeated list appends being cheaper than repeated swaps in CPython.

### 4-39)
See $\texttt{rust/parmergesort/src/main.rs}$ for an implementation of parallel
merge sort. Results from a 4 core, 8 hyperthread machine:
```
$ ./target/release/parmergesort
n = 20000000
baseline_elapsed = 1.073 s
threads = 1, elapsed = 1.905 s (1.776x baseline)
threads = 2, elapsed = 1.015 s (0.946x baseline)
threads = 4, elapsed = 0.581 s (0.542x baseline)
threads = 8, elapsed = 0.592 s (0.552x baseline)
```
The baseline sort algorithm is the optimized mergesort implementation from
Rust's standard library. We achieve approximately linear speedup up to 4
threads, but are in fact slightly slower on 8. This can likely be attributed to
resource contention and cache thrashing between hyperthreads sharing cores.

### 4-41)
- Insertion sort
  - Good: simple to implement, low code size, efficient for small inputs due to
  small constants
  - Bad: $O(n^2)$ complexity means it's unusable for larger inputs
- Selection sort
  - Good: simple to implement, low code size, efficient for small inputs due to
  small constants
  - Bad: $O(n^2)$ complexity means it's unusable for larger inputs
- Heapsort
  - Good: in-place, relatively fast when one is already maintaining a sequence
  in a heap
  - Bad: not stable, worst constants out of the "big three" sorting algorithms
- Mergesort
  - Good: stable, amenable to external sorting, amenable
  to parallelization, often the fastest of the big 3 sorting algorithms due to
  good cache behaviour and \texttt{memcpy} being highly optimized
  - Bad: requires $\Theta(n)$ additional space
- Quicksort
  - Good: in-place, competitive for the title of the fastest sorting algorithm
  in the average case
  - Bad: $O(n^2)$ worst-case complexity if care isn't taken to handle pathological
  inputs

### 4-43)
Break the file into chunks of size $k < 2 \ \text{Mb}$ and sort them
individually, writing the sorted chunks as separate files to disk. Then perform
an $n$-way merge of the sorted chunks, using a heap to speed up the process.
Initialize $i$ to $0$ and build a min-heap from the smallest element of each of
the chunks, augmented with the index of the chunk it came from. Then pop the
smallest item from the heap and write it to position $i$ of the original file.
Then insert the next smallest item from the chunk that contained the popped
item into the heap. This maintains the invariant that the smallest item in the
heap is the smallest item across all of the chunks. Increment $i$ and repeat
this pop, insert, increment process until all values have been written.

### 4-45)
Collect the indices along with their associated word into a priority queue in
$O(n\lg{3}) \in O(n)$ time, where $n$ is the largest of the three index lists.
We can then iterate over the indices and maintain a minimal pair of indices
that contains all three words, if such a pair exists. See the full $O(n)$
implementation below.

```{.python include=python/src/q04_45.py snippet=closest3}
```

### L4-1)
https://leetcode.com/problems/sort-list/

See $\texttt{python/src/l04\_01.py}$.

### L4-3)
https://leetcode.com/problems/merge-k-sorted-lists/

See $\texttt{python/src/l04\_03.py}$.