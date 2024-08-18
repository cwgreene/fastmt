import fastmt
import tqdm

def test_solver_choices():
    import random
    mrand = fastmt.MT19937Solver()
    rand = random.Random(int(1))
    initial_state = rand.__getstate__()[1][:-1]
    #b = rand.choices([0,1,2,3], weights=[1,1,1,1])[0]
    b = rand.getrandbits(32)
    mrand.submit(32,[None]*31 + [b>>31])
    for i in tqdm.tqdm(range(624*16)):
        #b = (rand.getrandbits(32) >> 30) & 3
        #b1 = b >> 1
        #b2 = b & 1
        #_ = (rand.getrandbits(32) >> 30) & 3
        b = rand.choices([0,1,2,3], weights=[1,1,1,1])[0]
        #mrand.submit(32, [None]*30+[b2, b1])
        mrand.submit(32, [None]*30 + [b&1,b>>1])
        mrand.submit(32, None)
    result = mrand.solve()
    for i in range(len(initial_state)):
        assert initial_state[i] == result[i]
