def heappush(heap, item):
    """Push item onto heap, maintaining the heap invariant."""
    print('before', heap, item)
    tempheap = [heap[i] if i < len(heap) else item for i in range(len(heap) + 1)]
    print(heap)
    heap.append(item)
    heap = tempheap
    print(heap == tempheap)#, newheap)
    _siftdown(heap, 0, len(heap)-1)

def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem

def _siftup(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    childpos = 2*pos + 1    # leftmost child position
    while childpos < endpos:
        # Set childpos to index of smaller child.
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        # Move the smaller child up.
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    _siftdown(heap, startpos, pos)

def heappop(heap):
    """Pop the smallest item off the heap, maintaining the heap invariant."""
    lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup(heap, 0)
        return returnitem
    return lastelt

def dijkstra(edges, source, sink, m):
    g = [[] for edge in range(m)]
    lengths = [0 for edge in range(m)]
    lasts = [0 for edge in range(m)]

    for edge in edges:
        lengths[edge[0]] += 1

    for i, edge in enumerate(g):
        g[i] = [None for x in range(lengths[i])]    
        
    for i, x in enumerate(edges):
        l,r,c = x
        g[l][lasts[l]] = (c, r)
        lasts[l] += 1

    q, seen, mins = [(0,source,())], \
                        [None for a in edges], \
                        [None if a != source else 0 for a in edges]
    while q:
        (cost,v1,path) = heappop(q)
        if seen[v1] is None:
            seen[v1] = True
            path = (v1, path)
            if v1 == sink: return (cost, path)

            for c, v2 in g[v1]:
                if v2 in seen: continue
                prev = mins[v2]
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    return float("inf")

if __name__ == "__main__":
    edges = [
        (0, 1, 7),
        (0, 3, 5),
        (1, 2, 8),
        (1, 3, 9),
        (1, 4, 7),
        (2, 4, 5),
        (3, 4, 15),
        (3, 5, 6),
        (4, 5, 8),
        (4, 6, 9),
        (5, 6, 11)
    ]

    m = 6

    print("=== Dijkstra ===")
    print(edges)
    print("0 -> 4:")
    print(dijkstra(edges, 0, 4, m))
    print("5 -> 6:")
    print(dijkstra(edges, 5, 6, m))