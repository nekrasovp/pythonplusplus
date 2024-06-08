import logging
import token
import tokenize
import io


def preprocess_code(source_code):
    result = []
    g = tokenize.generate_tokens(io.StringIO(source_code).readline)

    prev_tokval = None
    for toknum, tokval, _, _, _ in g:
        if prev_tokval is None:
            prev_tokval = tokval
            prev_toknum = toknum
            continue
        if prev_toknum == token.OP and prev_tokval == '+' and toknum == token.OP and tokval == '+':
            result.append((token.OP, '+='))
            result.append((token.NUMBER, '1'))
            prev_tokval = None
        else:
            if prev_tokval is not None:
                result.append((prev_toknum, prev_tokval))
            prev_tokval = tokval
            prev_toknum = toknum

    if prev_tokval is not None:
        result.append((prev_toknum, prev_tokval))

    logging.debug("Tokens:\n%s", result)
    return tokenize.untokenize(result)
