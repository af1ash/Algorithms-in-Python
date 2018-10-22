


Hash Tables

The novel concept for a hash table is the use of a hash function to map general keys to corresponding indices in a table.

bucke array

hash function 
a hash code that maps a key k to an integer
a compression function that maps the hash code to an integer within a range of indices, for a buckeet array.
built-in function: hash(x)      # only immutable data types are deemed hashable in Python

Collision-Handling
Separate Chaining is to have each bucket A[j] store its own secondary container, holding items(k, v) such that h(K)=j.
linear probing A[(h(k) + i) mod N]
quadratic probing A[(h(k)+f(i)) mod N] f(i) = i2