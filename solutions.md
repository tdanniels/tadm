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
&y \cdot (n+1)\\
\end{align*}
\begin{flushright} \rule{1.2ex}{1.2ex} \end{flushright}


