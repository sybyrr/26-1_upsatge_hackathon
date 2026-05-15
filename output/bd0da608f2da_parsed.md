# Parsed dump — job bd0da608f2da

- Source: `bd0da608f2da_dela_4-1.pdf`
- Elements: 225


## Page 1

`[   0 · paragraph]`

> Chapter 4

`[   1 · paragraph]`

> Linear Equations and Inverse
> Matrices

`[   2 · paragraph]`

> 4. 1 Two Pictures of Linear Equations

`[   3 · paragraph]`

> The central problem of linear algebra is to solve a system of equations. Those equations
> are linear, which means that the unknowns are only multiplied by numbers-we never see
> x2 or x times y. Our first linear system is deceptively small, only "2 by 2." But you will
> see how far it leads :

`[   4 · table]` *(base64 11144 chars attached)*

> | Two equations | x - 2y 1 |
> | --- | --- |
> | Two unknowns | 2x + 7 |

`[   5 · caption]`

> (1)

`[   6 · paragraph]`

> We begin a row at a time. The first equation x - 2y = 1 produces a straight line in the
> xy plane. The point x = 1, y = 0 is on the line because it solves that equation. The
> point x = 3, y = 1 is also on the line because 3 - 2 = 1. For x = 101 we find y = 50.

`[   7 · paragraph]`

> The slope of this line in Figure 4.1 is 1/2, because y increases by 1 when x changes
> by 2. But slopes are important in calculus and this is linear algebra !

`[   8 · chart]` *(base64 17608 chars attached)*

> ![image](/image/placeholder)
> - Chart Type: line
> |  | x - 2y | x - 3 | x + 4 |
> | --- | --- | --- | --- |
> | item_01 | 1 | 3.1 | 7 |

`[   9 · paragraph]`

> Figure 4.1: Row picture : The point (3, 1) where the two lines meet is the solution.


## Page 2

`[  10 · header]`

> 198

`[  11 · paragraph]`

> Chapter 4. Linear Equations and Inverse Matrices

`[  12 · heading1]`

> The second line in this "row picture" comes from the second equation 2x+y = 7. You
> can't miss the intersection point where the two lines meet. The point x = 3,y = 1 lies on
> both lines. It solves both equations at once. This is the solution to our two equations.

`[  13 · paragraph]`

> ROWS The row picture shows two lines meeting at a single point (the solution).

`[  14 · paragraph]`

> Turn now to the column picture. I want to recognize the same linear system as a
> "vector equation." Instead of numbers we need to see vectors. If you separate the original
> system into its columns instead of its rows, you get a vector equation:

`[  15 · paragraph]`

> -2 ]=[1 = b.
> x 1~2 | +y
> 1

`[  16 · heading1]`

> Combination equals b

`[  17 · equation]` *(base64 5184 chars attached)*

`[  18 · paragraph]`

> (2)

`[  19 · paragraph]`

> This has two column vectors on the left side. The problem is to find the combination of
> those vectors that equals the vector on the right. We are multiplying the first column by
> x and the second column by y, and adding vectors. With the right choices x = 3 and
> y = 1 (the same numbers as before), this produces 3(column 1) + 1(column 2) = b.

`[  20 · paragraph]`

> COLUMNS The column picture combines the column vectors on the left side
> of the equations to produce the vector b on the right side.

`[  21 · paragraph]`

> 6 3 (column 1)
> 36
> 4
> multiply by 3
> column 2
> 2 1
> column 1
> 2
> -2 -1 0 1 2 3

`[  22 · chart]` *(base64 28696 chars attached)*

> ![image](/image/placeholder)
> - Chart Type: line
> |  | -2 | -1 | 0 | 1 | 2 | 3 |
> | --- | --- | --- | --- | --- | --- | --- |
> | item_01 | 1 | -1 | 0 | 1 | 2 | 3 |

`[  23 · chart]` *(base64 35280 chars attached)*

> ![image](/image/placeholder)
> - Chart Type: line
> |  | -2 | -1 | 0 | 1 | 2 | 3 |
> | --- | --- | --- | --- | --- | --- | --- |
> | item_01 | 1 | 2 | 6 | 7 | 7 | 3 |

`[  24 · caption]`

> Figure 4.2: Column picture : A combination 3 (column 1 ) + 1 (column 2) gives the vector b.

`[  25 · paragraph]`

> Figure 4.2 is the "column picture" of two equations in two unknowns. The left side
> shows the two separate columns, and column 1 is multiplied by 3. This multiplication by a
> scalar (a number) is one of the two basic operations in linear algebra :

`[  26 · paragraph]`

> Scalar multiplication 3 □ 12 | =[ 36 ]


## Page 3

`[  27 · header]`

> 4.1. Two Pictures of Linear Equations

`[  28 · header]`

> 199

`[  29 · paragraph]`

> If the components of a vector v are V1 and v2, then cv has components CU1 and CV2.
> The other basic operation is vector addition. We add the first components and the
> second components separately. 3 - 2 and 6 + 1 give the vector sum (1, 7) as desired :

`[  30 · paragraph]`

> Vector addition

`[  31 · paragraph]`

> | 6 1 川魑 | 17 |
> 3 -2
> +

`[  32 · paragraph]`

> The right side of Figure 4.2 shows this addition. The sum along the diagonal is the vector
> b = (1, 7) on the right side of the linear equations.

`[  33 · paragraph]`

> To repeat : The left side of the vector equation is a linear combination of the columns.
> The problem is to find the right coefficients x = 3 and y = 1. We are combining scalar
> multiplication and vector addition into one step. That combination step is crucially impor-
> tant, because it contains both of the basic operations on vectors : multiply and add.

`[  34 · paragraph]`

> Linear combination 1 -2 1.7 |
> 3  2 1  
> +
> of the 2 columns

`[  35 · paragraph]`

> Of course the solution x = 3,y = 1 is the same as in the row picture. I don't know
> which picture you prefer ! Two intersecting lines are more familiar at first. You may like the
> row picture better, but only for a day. My own preference is to combine column vectors.
> It is a lot easier to see a combination of four vectors in four-dimensional space, than to
> visualize how four "planes" might possibly meet at a point. (Even one three-dimensional
> plane in four-dimensional space is hard enough. · )

`[  36 · paragraph]`

> The coefficient matrix on the left side of equation (1) is the 2 by 2 matrix A :

`[  37 · heading1]`

> 1 -2
> Coefficient matrix A = 1 ·
> 2 1

`[  38 · paragraph]`

> This is very typical of linear algebra, to look at a matrix by rows and also by columns.
> Its rows give the row picture and its columns give the column picture. Same numbers,
> different pictures, same equations. We write those equations as a matrix problem Av = b :

`[  39 · table]` *(base64 14068 chars attached)*

> | Matrix multiplies vector | 1 -2 x | 17 | | 2 1 y = |
> | --- | --- |

`[  40 · paragraph]`

> The row picture deals with the two rows of A. The column picture combines the columns.
> The numbers x = 3 and y = 1 go into the solution vector v. Here is matrix-vector
> multiplication, matrix A times vector v. Please look at this multiplication Av !

`[  41 · paragraph]`

> Dot products with rows | 2 1 | 1 = | 7 | (3)
> 1 -2
> 3
> 1
> Av = b is
> Combination of columns


## Page 4

`[  42 · paragraph]`

> 200

`[  43 · header]`

> Chapter 4. Linear Equations and Inverse Matrices

`[  44 · paragraph]`

> Linear Combinations of Vectors

`[  45 · paragraph]`

> Before I go to three dimensions, let me show you the most important operation on vectors.
> We can see a vector like v = (3, 1 ) as a pair of numbers, or as a point in the plane, or
> as an arrow that starts from (0, 0). The arrow ends at the point (3, 1) in Figure 4.3.

`[  46 · paragraph]`

> 1 v
> 3
> v =
> 1
> 1 2 3 (0, 0
> column vector point (3, 1) arrow to (3, 1)

`[  47 · chart]` *(base64 22208 chars attached)*

> ![image](/image/placeholder)
> - Chart Type: line
> |  | 0 | 1 | 2 | 3 | 4 | 5 |
> | --- | --- | --- | --- | --- | --- | --- |
> | item_01 | 3 | 1 | 1 | 3 | 0 | 1 |

`[  48 · figure]` *(base64 22208 chars attached)*

> ![image](/image/placeholder)

`[  49 · paragraph]`

> Figure 4.3: The vector v is given by two numbers or a point or an arrow from (0, 0).

`[  50 · paragraph]`

> A first step is to multiply that vector by any number c. If c = 2 then the vector is
> doubled to 2v. If c = -1 then it changes direction to -v. Always the "scalar" c multiplies
> each separate component (here 3 and 1) of the vector v. The arrow doubles the length to
> show 2v and it reverses direction to show -0 :

`[  51 · paragraph]`

> 2v
> v
> -3
> 6 | - v =
> 2v =
> 2
> -1
> -v
> column vectors arrows to (6,2) and (-3, -1)

`[  52 · figure]` *(base64 26484 chars attached)*

> ![image](/image/placeholder)

`[  53 · paragraph]`

> Figure 4.4: Multiply the vector v = (3,1) by scalars c = 2 and - 1 to get cv = (3c,c).

`[  54 · paragraph]`

> If we have another vector w = (-1, 1), we can add it to v. Vector addition v + w
> can use numbers (the normal way) or it can use the arrows (to visualize v + w). The
> arrows in Figure 4.5 go head to tail : At the end of v, place the start of w.

`[  55 · figure]` *(base64 18824 chars attached)*

> ![image](/image/placeholder)
> v + w
> 3 - 1 | 22  w v
> v + w = + =
> 1 1
> -1 1 2 3

`[  56 · chart]` *(base64 18824 chars attached)*

> ![image](/image/placeholder)
> - Chart Type: line
> |  | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 |
> | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
> | item_01 | 0 | 1 | 1 | 1 | 2 | 1 | 1 | 0 | 1 | 0 |

`[  57 · paragraph]`

> Figure 4.5: The sum of v = (3, 1) and w = (-1, 1) is v + w = (2,2). This is also w + v.

`[  58 · paragraph]`

> Allow me to say, adding v + w and multiplying cv will soon be second nature. In
> themselves they are not impressive. What really counts is when you do both at once.

`[  59 · equation]` *(base64 16924 chars attached)*

`[  60 · equation]` *(base64 11944 chars attached)*


## Page 5

`[  61 · header]`

> 4.1. Two Pictures of Linear Equations

`[  62 · header]`

> 201

`[  63 · paragraph]`

> Multiply cv and also dw, then add to get the linear combination cv + dw.

`[  64 · table]` *(base64 16368 chars attached)*

> | Linear combination 2v + 3w | 3 - 1 3 2 + 3 = 1 1 5 |
> | --- | --- |

`[  65 · paragraph]`

> This is the basic operation of linear algebra ! If you have two 5-dimensional vectors like
> v = (1, 1, 1, 1, 2) and w = (3, 0, 0, 1, 0), you can multiply v by 2 and w by 1. You
> can combine to get 2v + w = (5, 2,2, 3, 4). Every combination cv + dw is a vector in
> the big 5-dimensional space R5.

`[  66 · paragraph]`

> I admit that there is no picture to show these vectors in R5. Somehow I imagine arrows
> going to v and w. If you think of all the vectors cv, they form a line in R5 The line
> goes in both directions from (0, 0, 0, 0, 0) because c can be positive or negative or zero.

`[  67 · paragraph]`

> Similarly there is a line of all vectors d w. The hard but all-important part is to imagine
> all the combinations cv + dw. Add all vectors on one line to all vectors on the other line,
> and what do you get ? It is a "2-dimensional plane" inside the big 5-dimensional space.
> I don't lose sleep trying to visualize that plane. (There is no problem in working with the
> five numbers.) For linear combinations in high dimensions, algebra wins.

`[  68 · paragraph]`

> Dot Product of v and w

`[  69 · paragraph]`

> The other important operation on vectors is a kind of multiplication. This is not ordinary
> multiplication and we don't write vw. The output from v and w will be one number and it
> is called the dot product v · w.

`[  70 · paragraph]`

> DEFINITION The dot product of v = (v1, v2) and w = (w1, w2) is the number v · w :

`[  71 · equation]` *(base64 3668 chars attached)*

> v · w = v1w1 + v2w2.

`[  72 · paragraph]`

> (4)

`[  73 · paragraph]`

> The dot product of v = (3, 1) and w = (-1,1) is v · w = (3)(-1) + (1)(1) =-2.

`[  74 · equation]` *(base64 10096 chars attached)*

`[  75 · paragraph]`

> Example 1 The column vectors (1, 2) and (-2, 1) have a zero dot product:

`[  76 · paragraph]`

> Dot product is zero
> Perpendicular vectors

`[  77 · paragraph]`

> 1 | □ -2
> | 2
> = -2 + 2= 0.
> 1

`[  78 · paragraph]`

> In mathematics, zero is always a special number. For dot products, it means that these two
> vectors are perpendicular. The angle between them is 90°.

`[  79 · paragraph]`

> The clearest example of two perpendicular vectors is i = (1, 0) along the x axis and
> j = (0, 1) up the y axis. Again the dot product is i ·j = 0+0 = 0. Those vectors i and j
> form a right angle. They are the columns of the 2by 2 identity matrix I.

`[  80 · paragraph]`

> The dot product of v = (3, 1) and w = (1,2) is 5. Soon v * w will reveal the angle
> between v and w (not 90°). Please check that w * v is also 5.


## Page 6

`[  81 · header]`

> 202

`[  82 · paragraph]`

> Chapter 4. Linear Equations and Inverse Matrices

`[  83 · heading1]`

> Multiplying a Matrix A and a Vector v

`[  84 · paragraph]`

> Linear equations have the form Av = b. The right side b is a column vector. On the
> left side, the coefficient matrix A multiplies the unknown column vector v (we don't use
> a "dot" for Av). The all-important fact is that Av is computed by dot products in the
> row picture, and Av is a combination of the columns in the column picture.

`[  85 · paragraph]`

> I put those words "combination of the columns" in boldface, because this is an essential
> idea that is sometimes missed. One definition is usually enough in linear algebra, but Av
> has two definitions-the rows and the columns produce the same output vector Av.

`[  86 · paragraph]`

> The rules stay the same if A has n columns a1, · · · , an. Then v has n components.
> The vector Av is still a combination of the columns, Av = v1a1 + v2a2 + · · · + vnan.
> The numbers in v multiply the columns in A. Let me start with n = 2.

`[  87 · table]` *(base64 18588 chars attached)*

> | By rows Av = | (row 1) · v (row 2) · v | By columns Av = V1 (column 1)+v2(column 2). |
> | --- | --- | --- |

`[  88 · paragraph]`

> Example 2 In equation (3) I wrote "dot products with rows" and "combination of
> columns." Now you know what those mean. They are the two ways to look at Av :

`[  89 · table]` *(base64 25704 chars attached)*

> | Dot products with rows Combination of columns | a V1 + b v2 a | b | (5) = V1 + V2 c V1 + d V2 c d |
> | --- | --- |

`[  90 · paragraph]`

> You might naturally ask, which way to find Av ? My own answer is this : I compute
> by rows and I visualize (and understand) by columns. Combinations of columns are truly
> fundamental. But to calculate the answer Av, I have to find one component at a time.
> Those components of Av are the dot products with the rows of A.

`[  91 · equation]` *(base64 9200 chars attached)*

> 201 + 302 | = V1 | 4 | 5 |
>  2 3 | | V1 | = | 4v1 + 5v2
>  2
>  3
>  + V2
>  4 5
>  V2

`[  92 · heading1]`

> Singular Matrices and Parallel Lines

`[  93 · paragraph]`

> The row picture and column picture can fail-and they will fail together. For a 2 by 2
> matrix, the row picture fails when the lines from row 1 and row 2 are parallel. The lines
> don't meet and Av = b has no solution :

`[  94 · paragraph]`

> 2 3 | 201 - 302 = 6
> A =
> 4v1 - 6v2 = 0
> 4 6

`[  95 · equation]` *(base64 7056 chars attached)*

`[  96 · chart]` *(base64 11524 chars attached)*

> ![image](/image/placeholder)
> - Chart Title: Parallel lines no solution
> - Chart Type: pie
> |  | Purple | Green | Blue |
> | --- | --- | --- | --- |
> | item_01 | 90% | 5% | 5% |

`[  97 · paragraph]`

> The row picture shows the problem and so does the algebra : 2 times equation 1 produces
> 4v1 - 6v2 = 12. But equation 2 requires 4v1 - 6v2 = 0. Notice that this line goes
> through the center point (0, 0) because the right side is zero.


## Page 7

`[  98 · header]`

> 4.1. Two Pictures of Linear Equations

`[  99 · header]`

> 203

`[ 100 · paragraph]`

> How does the column picture fail ? Columns 1 and 2 point in the same direction.
> When the rows are "dependent", the columns are also dependent. All combinations of
> the columns (2, 4) and (3, 6) lie in the same direction. Since the right side b = (6, 0) is
> not on that line, b is not a combination of those two column vectors of A. Figure 4.6 (a)
> shows that there is no solution to the equation.

`[ 101 · chart]` *(base64 51608 chars attached)*

> ![image](/image/placeholder)
> - Chart Type: line
> |  | 1 | 2 | 3 | 4 | 5 | 6 |
> | --- | --- | --- | --- | --- | --- | --- |
> | item_01 | 1 | 4 | 2 | 6 | 6 | 12 |

`[ 102 · caption]`

> Figure 4.6: Column pictures (a) No solution (b) Infinity of solutions

`[ 103 · heading1]`

> Example 3 Same matrix A, now b = (6, 12), infinitely many solutions to Av = b

`[ 104 · paragraph]`

> 2 3 201 - 302 = 6
> A =
> 4 6 4v1 - 6v2 = 12

`[ 105 · equation]` *(base64 7540 chars attached)*

`[ 106 · chart]` *(base64 6928 chars attached)*

> ![image](/image/placeholder)
> - Chart Type: line
> |  | Dark Gray | Gray | Light Gray |
> | --- | --- | --- | --- |
> | item_01 | 50Not specified | 25Not specified | 25Not specified |

`[ 107 · paragraph]`

> In the row picture, the two lines are the same. All points on that line solve both equations.
> Two times equation 1 gives equation 2. Those close lines are one line.

`[ 108 · paragraph]`

> In the column picture above, the right side b = (6, 12) falls right onto the line of the
> columns. Later we will say : b is in the column space of A. There are infinitely many ways
> to produce (6, 12) as a combination of the columns. They come from infinitely many ways
> to produce b = (0, 0) (choose any c). Add one way to produce b = (6, 12) = 3(2, 4).

`[ 109 · equation]` *(base64 11752 chars attached)*

> -3
>  0 2 -3 6 2 1 +이 -6
>  | 0 | 4 -6 12 4
>  + 2c = 3
>  = 3c

`[ 110 · paragraph]`

> (6)

`[ 111 · paragraph]`

> The vector Un = (3c, 2c) is a null solution and vp = (3, 0) is a particular solution.
> Avn equals zero and Avp equals b. Then A(vp + vn) = b. Together, vp and Un
> give the complete solution, all the ways to produce b = (6, 12) from the columns of A :

`[ 112 · equation]` *(base64 12808 chars attached)*

> 3 3c
>  Complete solution to Av = b Ucomplete = vp + Un = + 1
>  0 2c

`[ 113 · caption]`

> (7)


## Page 8

`[ 114 · paragraph]`

> Chapter 4. Linear Equations and Inverse Matrices

`[ 115 · header]`

> 204

`[ 116 · header]`

> Equations and Pictures in Three Dimensions

`[ 117 · paragraph]`

> In three dimensions, a linear equation like x + y + 2z = 6 produces a plane. The plane
> would go through (0, 0, 0) if the right side were 0. In this case the "6" moves us to a
> parallel plane that misses the center point (0, 0, 0).

`[ 118 · paragraph]`

> A second linear equation will produce another plane. Normally the two planes meet in
> a line. Then a third plane (from a third equation) normally cuts through that line at a point.
> That point will lie on all three planes, so it solves all three equations.

`[ 119 · paragraph]`

> This is the row picture, three planes in three-dimensional space. They meet at the
> solution. One big problem is that this row picture is hard to draw. Three planes are too
> many to see clearly how they meet (maybe Picasso could do it).

`[ 120 · paragraph]`

> The column picture of Av = b is easier. It starts with three column vectors in three-
> dimensional space. We want to combine those columns of A to produce the vector
> v1 (column 1) + v2(column 2) + v3(column 3) = b. Normally there is one way to do
> it. That gives the solution (v1, v2, v3) - which is also the meeting point in the row picture.

`[ 121 · paragraph]`

> I want to give an example of success (one solution) and an example of failure (no
> solution). Both examples are simple, but they really go deeply into linear algebra.

`[ 122 · paragraph]`

> Example 4 Invertible matrix A, one solution v for any right side b.

`[ 123 · paragraph]`

> 1 0 0 V1 1
> Av = b is - 1 1 0 V2 = 3
> 0 - 1 1 V3 5

`[ 124 · equation]` *(base64 10420 chars attached)*

`[ 125 · caption]`

> (8)

`[ 126 · paragraph]`

> This matrix is lower triangular. It has zeros above the main diagonal. Lower triangular
> systems are quickly solved by forward substitution, top to bottom. The top equation gives
> v1, then move down. First V1 = 1. Then -V1 + V2 = 3 gives V2 = 4. Then -02 + V3 = 5
> gives V3 = 9.

`[ 127 · paragraph]`

> Figure 4.7 shows the three columns a1 , a2, a3. When you combine them with 1, 4, 9
> you produce b = (1, 3, 5). In reverse, v = (1, 4, 9) must be the solution to Av = b.

`[ 128 · chart]` *(base64 34116 chars attached)*

> ![image](/image/placeholder)
> - Chart Type: line
> |  | a | a2 | a3 | a4 | C | C2 |
> | --- | --- | --- | --- | --- | --- | --- |
> | item_01 | 0 | 1 | 0 | 1 | 2 | 3 |

`[ 129 · caption]`

> Figure 4.7: Independent columns a1, a2, a3 not in a plane. Dependent columns
> c1, c2, C3 are three vectors all in the same plane.


## Page 9

`[ 130 · header]`

> 4.1. Two Pictures of Linear Equations

`[ 131 · header]`

> 205

`[ 132 · paragraph]`

> Example 5 Singular matrix : no solution to Cv = b or infinitely many solutions
> (depending on b).

`[ 133 · equation]` *(base64 21136 chars attached)*

> 1 0 1
>  w1 - w3 = b1 1 0 -1 W1
>  -w1 + w2 = b2 - 1 1 0 w2 = 3 or 0 or 2 ·
>  -w2 + w3 = b3 0 - 1 1 w3 5 0 -3

`[ 134 · caption]`

> (9)

`[ 135 · paragraph]`

> This matrix C is a "circulant." The diagonals are constants, all 1's or all 0's or all - 1's.
> The diagonals circle around so each diagonal has three equal entries. Circulant matrices
> will be perfect for the Fast Fourier Transform (FFT) in Chapter 8.

`[ 136 · paragraph]`

> To see if C w = b has a solution, add those three equations to get 0 = b1 + b2 + b3.

`[ 137 · heading1]`

> Left side

`[ 138 · equation]` *(base64 5484 chars attached)*

> (w1 - W3 ) + (-w3 + w2 ) + (-w2 + W3 ) = 0.

`[ 139 · caption]`

> (10)

`[ 140 · paragraph]`

> C w = b cannot have a solution unless 0 = b1 +b2 + b3. The components of b = (1,3,5)
> do not add to zero, so C w = (1,3, 5) has no solution.

`[ 141 · paragraph]`

> Figure 4.7 shows the problem. The three columns of C lie in a plane. All combina-
> tions Cw of those columns will lie in that same plane. If the right side vector b is not
> in the plane, then C w = b cannot be solved. The vector b = (1, 3, 5) is off the plane,
> because the equation of the plane requires b1 + b2 + b3 = 0.

`[ 142 · paragraph]`

> Of course C w = (0, 0, 0) always has the zero solution w = (0,0, 0). But when the
> columns of C are in a plane (as here), there are additional nonzero solutions to C w = 0.
> Those three equations are W1 = W3 and W1 = w2 and W2 = W3. The null solutions
> are wn = (c,c,c). When all three components are equal, we have C wn = 0.

`[ 143 · paragraph]`

> The vector b = (1, 2, -3) is also in the plane of the columns, because it does have
> b1 + b2 + b3 = 0. In this good case there must be a particular solution to C w p
> = b.
> There are many particular solutions w p, any solution can be a particular solution.
> since
> I will choose the particular w p (1, 3, 0) that ends in w3 = 0 :
> =

`[ 144 · paragraph]`

> 1 0 -1 1 1
> The complete solution is
> C w = - 1 1 0 3 = 2
> p = w p + any wn
> w complete
> 0 - 1 1 0 -3

`[ 145 · paragraph]`

> Summary These two matrices A and C, with third columns a3 and c3, allow me to
> mention two key words of linear algebra : independence and dependence. This book will
> develop those ideas much further. I am happy if you see them early in the two examples:

`[ 146 · table]` *(base64 33296 chars attached)*

> | a 1 , a2, a3 are independent c 1 , c2, c3 are dependent | A is invertible C is singular | Av = b has one solution v C w = 0 has many solutions wn |
> | --- | --- | --- |

`[ 147 · paragraph]`

> Eventually we will have n column vectors in n-dimensional space. The matrix will be
> n by n. The key question is whether Av = 0 has only the zero solution. Then the columns
> don't lie in any "hyperplane." When columns are independent, the matrix is invertible.


## Page 10

`[ 148 · paragraph]`

> 206

`[ 149 · paragraph]`

> Chapter 4. Linear Equations and Inverse Matrices

`[ 150 · heading1]`

> Problem Set 4.1

`[ 151 · paragraph]`

> Problems 1-8 are about the row and column pictures of Av = b.

`[ 152 · paragraph]`

> 1 With A = I (the identity matrix) draw the planes in the row picture. Three sides of
> a box meet at the solution v = (x,y,z) = (2,3,4):

`[ 153 · equation]` *(base64 14592 chars attached)*

> 1x + 0y + Oz = 2 1 0 0 x 2
>  0x + ly + Oz = 3 or 0 1 0 3
>  ·
>  0x + 0y + 1z = 4 0 0 1 4

`[ 154 · paragraph]`

> Draw the four vectors in the column picture. Two times column 1 plus three times
> column 2 plus four times column 3 equals the right side b.

`[ 155 · paragraph]`

> 2 If the equations in Problem 1 are multiplied by 2,3,4 they become DV = B :

`[ 156 · equation]` *(base64 17928 chars attached)*

> 2x + 0y + Oz = 4 2 0 0 4
>  0x + 3y + Oz = 9 or DV = 0 3 0 9 = B
>  0x + 0y + 4z = 16 0 0 4 16

`[ 157 · paragraph]`

> Why is the row picture the same? Is the solution V the same as v? What is changed
> in the column picture-the columns or the right combination to give B?

`[ 158 · list]`

> 3 If equation 1 is added to equation 2, which of these are changed: the planes in the
> row picture, the vectors in the column picture, the coefficient matrix, the solution?
> The new equations in Problem 1 would be x = 2, x + y = 5, z = 4.

`[ 159 · paragraph]`

> 4 Find a point with z = 2 on the intersection line of the planes x + y + 3z = 6 and
> x - y + z = 4. Find the point with Z = 0. Find a third point halfway between.

`[ 160 · list]`

`[ 161 · list]`

> 5 The first of these equations plus the second equals the third:

`[ 162 · equation]` *(base64 5160 chars attached)*

> x + y + Z = 2
>  x + 2y + Z = 3
>  2x + 3y + 2z = 5.

`[ 163 · paragraph]`

> The first two planes meet along a line. The third plane contains that line, because
> if x,y,z satisfy the first two equations then they also The equations have
> infinitely many solutions (the whole line L). Find three solutions on L.

`[ 164 · list]`

> 6 Move the third plane in Problem 5 to a parallel plane 2x + 3y + 2z = 9. Now the
> three equations have no solution-why not? The first two planes meet along the line
> L, but the third plane doesn't that line.

`[ 165 · list]`

> 7 In Problem 5 the columns are (1, 1, 2) and (1,2,3) and (1,1,2). This is a "singular
> case" because the third column is Find two combinations of the columns that
> give b = (2, 3, 5). This is only possible for b = (4, 6,c) if c =


## Page 11

`[ 166 · heading1]`

> 4.1. Two Pictures of Linear Equations

`[ 167 · header]`

> 207

`[ 168 · list]`

> 8 Normally 4 "planes" in 4-dimensional space meet at a Normally 4
> vectors in 4-dimensional space can combine to produce b. What combination
> of (1, 0, 0, 0), (1, 1, 0, 0), (1, 1, 1, 0), (1, 1, 1, 1) produces b = (3, 3, 3,2)?

`[ 169 · paragraph]`

> Problems 9-14 are about multiplying matrices and vectors.

`[ 170 · paragraph]`

> 9 Compute each Ax by dot products of the rows with the column vector:

`[ 171 · equation]` *(base64 14320 chars attached)*

> 2 1 0 0 1
>  1 2 4 2
>  1 2 1 0 1
>  (a) -2 3 1 2 to
>  0 1 2 1 1
>  -4 1 2 3
>  0 0 1 2 2

`[ 172 · heading1]`

> 10 Compute each Ax in Problem 9 as a combination of the columns:

`[ 173 · paragraph]`

> 1 2 4
> 9(a) becomes Ax = 2 -2 +2 3 + 3 1
> - 4 1 2

`[ 174 · equation]` *(base64 11668 chars attached)*

`[ 175 · paragraph]`

> How many separate multiplications for Ax, when the matrix is "3 by 3"?

`[ 176 · heading1]`

> 11 Find the two components of Ax by rows or by columns:

`[ 177 · equation]` *(base64 11032 chars attached)*

> 3
>  「25 3][4] and [3 12][_2] and | 1~2 0 1
>  2 4
>  1

`[ 178 · heading1]`

> 12 Multiply A times x to find three components of Ax:

`[ 179 · paragraph]`

> 0 0 1 x 2 1 3 1 2 1
> 0 1 0 v and 1 2 3 1 and 1 2
> 1 0 0 z 3 3 6 1 3 3

`[ 180 · equation]` *(base64 12736 chars attached)*

`[ 181 · paragraph]`

> 13

`[ 182 · list]`

> (a) A matrix with m rows and n columns multiplies a vector with compo-
> nents to produce a vector with components.
> (b) The planes from the m equations Ax = b are in -dimensional space.
> The combination of the columns of A is in -dimensional space.

`[ 183 · paragraph]`

> 14 Write 2x+3y+z+5t = 8 as a matrix A (how many rows?) multiplying the column
> vector x = (x,y,z,t) to produce b. The solutions x fill a plane or "hyperplane"
> in 4-dimensional space. The plane is 3-dimensional with no 4D volume.

`[ 184 · heading1]`

> Problems 15-22 ask for matrices that act in special ways on vectors.

`[ 185 · paragraph]`

> 15

`[ 186 · paragraph]`

> (a) What is the 2 by 2 identity matrix? I times [✓] equals [✓]
> (b) What is the 2 by 2 exchange matrix? P times [x] equals [x].

`[ 187 · list]`


## Page 12

`[ 188 · header]`

> 208

`[ 189 · header]`

> Chapter 4. Linear Equations and Inverse Matrices

`[ 190 · list]`

> 16 (a) What 2 by 2 matrix R rotates every vector by 90° ? R times [✓] is [x]
> (b) What 2 by 2 matrix R2 rotates every vector by 180° ?

`[ 191 · list]`

> 17 Find the matrix P that multiplies (x,y,z) to give (y,z,x). Find the matrix Q that
> multiplies (y,z,x) to bring back (x,y,z).

`[ 192 · list]`

> 18 What 2 by 2 matrix E subtracts the first component from the second component ?
> What 3 by 3 matrix does the same ?

`[ 193 · list]`

> 3 3
> 3 ]=[ 32 | and E 5 = 2 ·
> E | 5
> 7 7

`[ 194 · equation]` *(base64 8000 chars attached)*

`[ 195 · list]`

> 19 What 3 by 3 matrix E multiplies (x,y,z) to give (x,y,z+x) ? What matrix E-1
> multiplies (x,y,z) to give (x,y,z - x) ? If you multiply (3,4,5) by E and then
> multiply by E-1 the two results are ( ) and ( ).
> ,

`[ 196 · list]`

> 20 What 2 by 2 matrix P1 projects the vector (x,y) onto the x axis to produce (x, 0) ?
> What matrix P2 projects onto the y axis to produce (0, y) ? If you multiply (5, 7)
> by P1 and then multiply by P2, you get ( ) and ( ).

`[ 197 · list]`

> 21 What 2 by 2 matrix R rotates every vector through 45° ? The vector (1, 0) goes to
> (V2/2,V2/2). The vector (0, 1) goes to (-V2/2, V2/2). Those determine the
> matrix. Draw these particular vectors in the xy plane and find R.

`[ 198 · list]`

> 22 Write the dot product of (1,4,5) and (x,y,z) as a matrix multiplication Av. The
> matrix A has one row. The solutions to Av = 0 lie on a perpendicular to the
> vector · The columns of A are only in -dimensional space.

`[ 199 · list]`

> 23 In MATLAB notation, write the commands that define this matrix A and the column
> vectors v and b. What command would test whether or not Av = b ?

`[ 200 · paragraph]`

> 5 | b = | 17 |
> 1 2 | v =  -2
> A = | 3 4

`[ 201 · list]`

`[ 202 · equation]` *(base64 6640 chars attached)*

`[ 203 · list]`

> 24 If you multiply the 4 by 4 all-ones matrix A = ones(4) and the column V = ones(4,1),
> what is A*v ? (Computer not needed.) If you multiply B = eye(4) + ones(4) times
> W = zeros(4,1) + 2*ones(4,1), what is B*w ?

`[ 204 · paragraph]`

> Questions 25-27 review the row and column pictures in 2, 3, and 4 dimensions.

`[ 205 · list]`

> 25 Draw the row and column pictures for the equations x - 2y = 0, x +y = 6.

`[ 206 · list]`

> 26 For two linear equations in three unknowns x, y, z, the row picture will show (2 or 3)
> (lines or planes) in (2 or 3)-dimensional space. The column picture is in (2 or 3)-
> dimensional space. The solutions normally lie on a ·

`[ 207 · list]`

> 27 For four linear equations in two unknowns x and y, the row picture shows four
> The column picture is in -dimensional space. The equations have no
> solution unless the vector on the right side is a combination of


## Page 13

`[ 208 · paragraph]`

> 4.1. Two Pictures of Linear Equations 209

`[ 209 · heading1]`

> Challenge Problems

`[ 210 · paragraph]`

> 28 Invent a 3 by 3 magic matrix M3 with entries 1, 2, , 9. All rows and columns
> and diagonals add to 15. The first row could be 8, 3, 4. What is M3 times (1, 1, 1) ?
> What is M4 times (1, 1, 1, 1) if a 4 by 4 magic matrix has entries 1, , 16 ?

`[ 211 · list]`

`[ 212 · list]`

> 29 Suppose u and v are the first two columns of a 3 by 3 matrix A. Which third columns
> w would make this matrix singular ? Describe a typical column picture of Av = b
> in that singular case, and a typical row picture (for a random b).

`[ 213 · paragraph]`

> 30 Multiplying by A is a "linear transformation". Those important words mean:

`[ 214 · list]`

`[ 215 · paragraph]`

> If w is a combination of u and v, then Aw is the same combination of Au and Av.

`[ 216 · paragraph]`

> It is this "linearity" Aw = cAu + dAv that gives us the name linear algebra.

`[ 217 · paragraph]`

> 0
> 1 | and v = then Au and Av are the columns of A.
> If u = | 0
> 1

`[ 218 · paragraph]`

> 5 | how is Aw connected to Au and Av ?
> Combine w = cu + dv. If w = | 7

`[ 219 · paragraph]`

> 31 A 9 by 9 Sudoku matrix S has the numbers 1, · , in every row and column, and
> 9
> in every 3 by 3 block. For the all-ones vector v = (1, * 1), what is Sv ?
> · · ,

`[ 220 · paragraph]`

> A better question is: Which row exchanges will produce another Sudoku matrix
> ? Also, which exchanges of block rows give another Sudoku matrix ?

`[ 221 · paragraph]`

> Section 4.5 will look at all possible permutations (reorderings) of the rows. I see
> 6 orders for the first 3 rows, all giving Sudoku matrices. Also 6 permutations of the
> next 3 rows, and of the last 3 rows. And 6 block permutations of the block rows ?

`[ 222 · paragraph]`

> 32 Suppose the second row of A is some number c times the first row :

`[ 223 · paragraph]`

> a b
> A =
> ca cb -

`[ 224 · paragraph]`

> Then if a ≠ 0, the second column of A is what number d times the first column ?
> A square matrix with dependent rows will also have dependent columns. This is
> a crucial fact coming soon.
