n = nextIn<> ~parseInt() ~sub(1);
_ = newList<n, 0> ~map(FUNC<i, nextIn ~parseInt()>) ~reduce(0, FUNC<i, j, i ~sub(j)>) ~println();