expo2020 = lambda s : str(bin(int(s.replace(" ","").replace("\n",""),base=16))[2:]).zfill(4)
a = expo2020("""
       00000000000003f8000000000000000000000000007fc00000000000000000000000700e0e01c00000000000000000003fc1c0707f80000000000000000007fe18030ffc000000000000000000e0718031c0e000000000000000001c0318031807000000000000000001803180318030000000000000000
018031c0718030000000000000003c1803fe0ff803078000000000000ff1803ff1ff8031fe000000000001f79c0703b81c073df000000000003818f0e01b00e1e30380000000000701dfcc01f0067f701c0000000000600ffec00e006ffe00c0000000000e00f07c00e007c1e00e0000000000e00c03c00e00780600e00000
00000e01c01c00e00700700c0000000000701801e01f00f00301c0000000000781801e01b00f00303c000000001c3fd800f03b81e0037f8700000007f0ffc01fff1fff007fe1fc000000ff9cfc01dfe0ff3007e73fe000001c1f81e0187f1fc300f03f0700000380f00f070e3b8e181e01e0380000300e00fffcc1b067ffe0
0e018                                                                                                                                                                                                                                                    00007
00e00                                                                                                                                                                                                                                                    7ffec
1b06f     ffc00e01c0000700e006386e      3f8ec7            8c00e0      1c0000700e006187f7fdfc30      c00e01c00007006006187fff        ffc30c00c01c00003807          00e187ece6fc30e01c03          800001eff80fdffe0e0f          ff7e03fef000000fff         c3fef
ce0e0     e7eff87ffe0000003c3ff87f       8f1f1e          3fc3ff       878000018300ff87e0fbbbe0      fc3fe01860007f700e187f0d       fbfe1fc30e01dfc00ffe00        6186f9dffe73ec30c00ffe        00e1e0071fe7ff8e3ffcff        1c00f0601c0e0076fc3ff       8e3ff
87edc     00e070                          180600        7ff037        38e39d            81ffc0      0c0303            806007      ff83e1            df70f8      3ffc00            c03838      0700e1            fffe1f      ff0fff            f0e01c     03838
0381e     0ffe7f                           fbffcf      fe0f03         803838            03ffe0      cfe3f3            19f8fe      60fff            803818       0fff71            c6e3f3      f9f8e            c71dff       e0301c            3ffc3f     87e73
fff9c     fc3f87                            ff8700    ff81c1          f07ff3            e0f9ff      c1f070            3fe007                      f00e0f        8f3ff0            01ff9e                      3c0e01        fc0006            006fff     e19e0
00f30     fffec0                             0c0000  6007ff           fe1980            00330f      fffc00            c000e6                     0078ff         77f800            03fddf                     e3c00c         e03fe0            070e3f     ff000
01fff     8e1c00ff87fe007061ee6000            00ce78c1c00f            fc6070070e186600000cc30e      1c01c0            ce0380                   f9c387           e00000            fc3877                   e0380e           c03e7d            fffcfc     00000
7e7df     f7cf806c00ff87fefce00000             e7effc3fe0             06c00ff03fefce00000e7eff      81fe00            6c01ff                  8fffcf            c00000            7e7ffe                  3ff006            e0381d            fc387e     00000
fc387     f70380                               e60700f8e1             866000                        00cc30            e3e01c                0c71e0              07061c            e60000                0ce70c              1c00f1            c3fe00     7063f
e6000     00cff8                              c1c00ff81f60            078cf7                        ff8000            3ffdc6               3c00df               000600            7fff63               980003               38dfff            c00c00     00600
7fffe     19c000                             730fff  fc00c0           003f00                        e67de3            df001f             f8f7cc                 e01f80            0ff01c             1f07ff                 bc07bf            fc1f07     01fe0
1ffc7     c3f87f                            73fff9    dfc3f8          7c7ff0                        181fff            71c6e3            bbfbb8                  ec71df            ff0303            807ffe                  0cec3f            3b9f8e     e60ff
fc038     3803c1                           e0dfe3      fb1bf8         ff60f0                        780383            80300e          1ffff3                    fff9ff            ff0e01          803838                    070079            fc7e1f     ff0fc
7fbc0     1c0381                          806007        fb8361        8e30d8                        3bfc00            c0301c        0e007e7c37f8e3fd87cfc0      0e0700            c1e007        0fe7ff8e3ffcfe1c00f060      0f7e00            61c6fd     dfff7
7ec70     c00fde007f7006187f0dfbf6       1fc30c0         1dfc00       1e300f                        d87e0ffbfe0fc37e018f0000      0383ff87e0f1f1e0fc3ff83        8000000ffff7eefce0e0e7        eefdfffe000001fff81fdf        fe0e0fff7f03fff0000038      0700f
987ec     e6fc33e01c03800003006006      187feef           fc30c0      0c0180                        000700e006183fffff830c00      e01c0000700e006187e3f8f         c30c00e01c0000700e00         6ffec1b06ffec00e01c000         0300e007ffcc1b067ffc       00e01
80000                                                                                                                                                                                                                                                    380f0
0f870e3b8e1c3e00e03800001c1f01e038771dc380f01f07000000e3bc7c018fe0fe3007c7b8e0000007f1ffc01fff1fff007ff1fc0000003e1fd800f87bc3e0037f0f800000000381800e01b00e0030380000000000701801e01f00f00301c0000000000601c01c00e00700700c0000000000e01c03c00e00780700e00000
00000e00e07c00e007c0e00e0000000000600fcfc00e007f7e00c0000000000701dfcc00e0067f701c00000000003818f8e01f00e3e303800000000001e38e0703b81c0e38f000000000000ff1c07ff1ffc071fe0000000000003e1803fe0ff8030f80000000000000018037c07d8030000000000000000018031803180300
        000000000000000180318031803000000000000000001e0718031c0f000000000000000000f8e18030e3e0000000000000000003fe18030ff80000000000000000000f81e0f03e00000000000000000000000ffe000000000000000000000000003f800000000000000000000000000000000000000000
""")

for i,bit in enumerate(a):
    if i%115 == 0:
        print("")
    if bit == '1':
        print("█",end="")
    else:
        print(" ",end="")