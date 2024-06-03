from collections import defaultdict
def solution(word, pages):
    page_index = {}
    page_dict = {}
    total_score_dict = defaultdict(float)
    length = len(word)
    word_lower = word.lower()
    for i, page in enumerate(pages):
        site = page.split('<meta property="og:url" content="https://')[1].split('"')[0]
        page_index[site] = i
        external = []

        for p in page.split('<a href="https://')[1:]:
            external.append(p[:p.index('"')])

        def_score = 0
        for i in range(len(page)):
            if page[i:i+length].lower()==word_lower and not page[i-1].isalpha() and not page[i+length].isalpha():
                def_score += 1.0
        page_dict[site] = (def_score, len(external), external)
        for ex in external:
            total_score_dict[ex] += def_score / len(external)

    max_score = -1
    max_site = ""
    for site in page_dict.keys():
        total_score_dict[site] += page_dict[site][0]
        if total_score_dict[site] > max_score and site in page_index.keys():
            max_score = total_score_dict[site]
            max_site = site

    return page_index[max_site]