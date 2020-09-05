# get_ratios.py

def get_ratios(vect1, vect2):
    '''
    Assumes vect1 and vect2 are equal length lists of numbers
    Returns a list containing the meaningful values of
        vect1[i] / vect2[i]
    '''
    ratios = []
    for index in range(0, len(vect1)):
        try:
            ratios.append(vect1[index] / vect2[index])
        except ZeroDivisionError:
            ratios.append(float('nan'))
        except:
            raise ValueError('get_ratios called with bad arguments')
    return ratios


def test_get_ratios():
    vect1 = [1, 2, 3, 0, 5]
    vect2 = [9, 7, 6, 7, 0]
    vect_ratios = get_ratios(vect1, vect2)
    print(vect_ratios)

    vect1 = [1, 2, 3, 0, 5]
    vect2 = [9, 7, 7, 0, 'a']
    vect_ratios = get_ratios(vect1, vect2)
    print(vect_ratios)


if __name__ == '__main__':
    test_get_ratios()