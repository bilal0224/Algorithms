Longest Common Subsequence
------------------------

  A *subsequence* is a *sequence* that appears in the same relative order, but not necessarily contiguous. For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”. Given two sentences, We need to find the *longest subsequence that both sentences has in common.* 
  If we try to solve this problem using **Brute Force** method, the time taken would in order of *O(n x 2^n)*. The time can be drastically improved using **Dynamic Programing** Approach.
  The problem is solved using the bottom up dynamic approach. The time taken in this method is *O(n^2)* which is a lot better than the brute force.
