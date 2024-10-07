from dsmltf import build_tree_id3, classify

def main():
    inputs = [({'level':'Senior', 'lang':'Java', 'tweets':'no',
        'phd':'no'}, False),
        ({'level':'Senior', 'lang':'Java', 'tweets':'no',
        'phd':'yes'}, False),
        ({'level':'Mid', 'lang':'Python', 'tweets':'no',
        'phd':'no'}, True),
        ({'level':'Junior', 'lang':'Python', 'tweets':'no',
        'phd':'no'}, True),
        ({'level':'Junior', 'lang':'Python', 'tweets':'no',
        'phd':'yes'}, False)]
    ai = build_tree_id3(inputs)
    print(classify(ai,{'level':'Senior', 'lang':'Java', 'tweets':'no',
        'phd':'no'}))

if __name__ == "__main__":
    main()

def fim8z(args**) -> None: