from euler_binder import fetch

PROBLEM = {
    1: """<p>If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.</p>
<p>Find the sum of all the multiples of 3 or 5 below 1000.</p>
""",
    4: "\n<p>A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.</p>\n<p>Find the largest palindrome made from the product of two 3-digit numbers.</p>\n\n",
    11: '<p>In the 20×20 grid below, four numbers along a diagonal line have been marked in red.</p>\n<p class="monospace center">\n08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08<br />\n49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00<br />\n81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65<br />\n52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91<br />\n22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80<br />\n24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50<br />\n32 98 81 28 64 23 67 10 <span class="red"><b>26</b></span> 38 40 67 59 54 70 66 18 38 64 70<br />\n67 26 20 68 02 62 12 20 95 <span class="red"><b>63</b></span> 94 39 63 08 40 91 66 49 94 21<br />\n24 55 58 05 66 73 99 26 97 17 <span class="red"><b>78</b></span> 78 96 83 14 88 34 89 63 72<br />\n21 36 23 09 75 00 76 44 20 45 35 <span class="red"><b>14</b></span> 00 61 33 97 34 31 33 95<br />\n78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92<br />\n16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57<br />\n86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58<br />\n19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40<br />\n04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66<br />\n88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69<br />\n04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36<br />\n20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16<br />\n20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54<br />\n01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48<br /></p>\n<p>The product of these numbers is 26 × 63 × 78 × 14 = 1788696.</p>\n<p>What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?</p>\n\n',
    15: """<p>Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.</p>
<div class="center">
<img src="project/images/p015.png" class="dark_img" alt="" /></div>
<p>How many such routes are there through a 20×20 grid?</p>
""",
    22: """<p>Using <a href="project/resources/p022_names.txt">names.txt</a> (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.</p>
<p>For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.</p>
<p>What is the total of all the name scores in the file?</p>
""",
}


def test_get_raw():
    prob1 = fetch._get_raw(1)
    assert prob1 == PROBLEM[1]


def test_get_unicode():
    prob4 = fetch._get_raw(4)
    assert prob4 == PROBLEM[4]


def test_strip_links():
    assert fetch._strip_links(PROBLEM[1]) == (PROBLEM[1], [])
    assert fetch._strip_links(PROBLEM[15]) == (
        """<p>Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.</p>
<div class="center">
<img src="p015.png" class="dark_img" alt="" /></div>
<p>How many such routes are there through a 20×20 grid?</p>
""",
        [("project/images/p015.png", "p015.png")],
    )
    assert fetch._strip_links(PROBLEM[22]) == (
        """<p>Using <a href="names.txt">names.txt</a> (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.</p>
<p>For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.</p>
<p>What is the total of all the name scores in the file?</p>
""",
        [("project/resources/p022_names.txt", "names.txt")],
    )


def test_inline_format():
    assert (
        fetch._inline_format(PROBLEM[11])
        == '<p>In the 20×20 grid below, four numbers along a diagonal line have been marked in red.</p>\n<p style="text-align: center !important; font-family: monospace">\n08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08<br />\n49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00<br />\n81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65<br />\n52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91<br />\n22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80<br />\n24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50<br />\n32 98 81 28 64 23 67 10 <span style="color: red"><b>26</b></span> 38 40 67 59 54 70 66 18 38 64 70<br />\n67 26 20 68 02 62 12 20 95 <span style="color: red"><b>63</b></span> 94 39 63 08 40 91 66 49 94 21<br />\n24 55 58 05 66 73 99 26 97 17 <span style="color: red"><b>78</b></span> 78 96 83 14 88 34 89 63 72<br />\n21 36 23 09 75 00 76 44 20 45 35 <span style="color: red"><b>14</b></span> 00 61 33 97 34 31 33 95<br />\n78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92<br />\n16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57<br />\n86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58<br />\n19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40<br />\n04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66<br />\n88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69<br />\n04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36<br />\n20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16<br />\n20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54<br />\n01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48<br /></p>\n<p>The product of these numbers is 26 × 63 × 78 × 14 = 1788696.</p>\n<p>What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?</p>\n\n'
    )
