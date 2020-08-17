## Orthonormality
A set of vectors is orthonormal if they are all of unit length and orthogonal to each other. There are various processes in which we can take a set of (linearly independent) vectors and orthonormalise them. If you apply one of these processes to the columns of a matrix, we call this orthogonalising the matrix.

The **QR decomposition** factorises a matrix *M* into two matrices *QR* = *M*, where

- *Q* is the orthogonalised matrix of *M*
- *R* is an upper triangular matrix.

For this investigation, we're only after *Q* for the orthogonalisation of *M*.  
*R* is just a 'by product' of using this method.

# Idea
Given a matrix *A* (*m* x *n*), and two matrices *U* (*m* x *k*) and *V* (*n* x *k*) (consisting of *k* basis vectors), the projection of *A* onto our basis (denoted *A<sub>U,V</sub>*) is defined as

*A<sub>U,V</sub>* = *U(U<sup>T</sup>AV)V<sup>T</sup>*.

First, we'll take *A* to be the matrix representation of an image.  
Starting off with random matrices *U* and *V*, we'll see how accurate the image *A<sub>U,V</sub>* is compared to the original.  
Then, using the following algorithm, we'll see if we can improve our basis to obtain a more accurate projection of *A*.

# The algorithm
We obtain an improved *U* as follows:

- Take *AV* = *U<sup>temp</sup>*  
- We then orthogonalise it using *QR* = *U<sup>temp</sup>*  
- And then letting our new *U* = *Q*

We improve *V* in a similar way, except in the first step we take *A<sup>T</sup>U* = *V<sup>temp</sup>*. (**Note: here, we use the *U* obtained from the orthogonalisation above**)

# Investigation
Each time we apply the algorithm to *U* and *V*, it improves our basis, so now when we take

*A<sub>U,V</sub>* = *U(U<sup>T</sup>AV)V<sup>T</sup>*

we'll (hopefully) get a fairly accurate projection of *A*.
