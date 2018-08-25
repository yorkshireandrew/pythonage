# Utility class to create javascript styles from pythonage styles
class JavascriptStyle:

    # Create a javascript style from rgb
    @staticmethod
    def rgb_to_style(r, g, b):
        rs = hex(r)[2:]
        if len(rs) == 1:
            rs = '0{0}'.format(rs)
        gs = hex(g)[2:]
        if len(gs) == 1:
            gs = '0{0}'.format(gs)       
        bs = hex(b)[2:]
        if len(bs) == 1:
            bs = '0{0}'.format(bs)  
        return '#{0}{1}{2}'.format(rs,gs,bs);

    # Compute the style if a single character is given otherwise pass through
    @staticmethod
    def compute_style(style):
        if not len(style) == 1:
            return style
        # These should match with colour_data in pixelmap.js
        if style == 'w':
            style = 'white'
        elif style == 'r':
            style = JavascriptStyle.rgb_to_style(200, 50, 50)
        elif style == 'g':
            style = JavascriptStyle.rgb_to_style(50, 200, 50)
        elif style == 'b':
            style = JavascriptStyle.rgb_to_style(50, 50, 200)
        elif style == 'R':
            style = 'red'
        elif style == 'G':
            style = 'green'
        elif style == 'B':
            style = 'blue'
        elif style == 'y':
            style = JavascriptStyle.rgb_to_style(200, 200, 50)
        elif style == 'Y':
            style = 'yellow'
        elif style == 'p':
            style = JavascriptStyle.rgb_to_style(253, 207, 176)
        elif style == '#':
            style = 'black'
        elif style == 'm':
            style = JavascriptStyle.rgb_to_style(185, 122, 87)
        elif style == 'M':
            style = JavascriptStyle.rgb_to_style(119, 70, 49)
        elif style == 'o':
            style = JavascriptStyle.rgb_to_style(255, 176, 89)
        elif style == 'O':
            style = JavascriptStyle.rgb_to_style(255, 127, 39)
        else:
            style = 'black' # default to black if not recognised
