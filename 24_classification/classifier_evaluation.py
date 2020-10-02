# classifier_evaluation.py


def accuracy(true_positive, false_positive, true_negative, false_negative):
    numerator = true_positive + true_negative
    denominator = true_positive + true_negative + false_positive + false_negative
    return float(numerator) / denominator


def sensitivity(true_positive, false_negative):
    try:
        return float(true_positive) / (true_positive + false_negative)
    except ZeroDivisionError:
        return float('nan')


def specificity(true_negative, false_positive):
    try:
        return float(true_negative) / (true_negative + false_positive)
    except ZeroDivisionError:
        return float('nan')


def positive_predictive_value(true_positive, false_positive):
    try:
        return float(true_positive) / (true_positive + false_positive)
    except ZeroDivisionError:
        return float('nan')


def negative_predictive_value(true_negative, false_negative):
    try:
        return float(true_negative) / (true_negative + false_negative)
    except ZeroDivisionError:
        return float('nan')


def get_stats(true_positive, false_positive, true_negative, false_negative, to_print = True):
    acc = accuracy(true_positive, false_positive, true_negative, false_negative)
    sens = sensitivity(true_positive, false_negative)
    spec = specificity(true_negative, false_positive)
    ppv = positive_predictive_value(true_positive, false_positive)
    if to_print:
        print(' Accuracy: ', round(acc, 3))
        print(' Sensitivity: ', round(sens, 3))
        print(' Specificity: ', round(spec, 3))
        print(' Pos. Pred. Value: ', round(ppv, 3))
    return (acc, sens, spec, ppv)