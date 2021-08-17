use itertools::Itertools;

fn read_words(initial_word: &str) -> Vec<String> {
    let content = std::fs::read_to_string("./wordlist.txt").expect("unable to read word list file");
    content
        .split('\n')
        .skip(1)
        .map(|s| s.split(' '))
        .flatten()
        .filter(|s| !s.is_empty())
        // we can already filter if the word contains a letter that is not in `initial_word`
        .filter(|s| s.chars().all(|c| initial_word.contains(c)))
        .map(|s| s.to_string())
        .collect()
}

#[derive(PartialEq, Eq, Debug)]
struct CountedChars {
    chars: std::collections::BTreeMap<char, usize>,
    nb_chars: usize,
}

impl std::iter::FromIterator<char> for CountedChars {
    fn from_iter<T>(iter: T) -> CountedChars
    where
        T: IntoIterator<Item = char>,
    {
        let mut nb_chars = 0;
        let chars = iter
            .into_iter()
            .fold(std::collections::BTreeMap::default(), |mut chars, c| {
                *chars.entry(c).or_default() += 1;
                nb_chars += 1;
                chars
            });
        CountedChars { chars, nb_chars }
    }
}

fn is_anagram(word: &CountedChars, other_words: &[&String]) -> bool {
    // trying a shortcut
    if other_words.iter().map(|s| s.len()).sum::<usize>() != word.nb_chars {
        return false;
    }
    let sorted_words_char = other_words
        .iter()
        .map(|s| s.chars())
        .flatten()
        .collect::<CountedChars>();
    //println!(
    //    "{:?}  --- compared to {:?}",
    //    other_words, &sorted_words_char
    //);
    sorted_words_char.eq(word)
}

fn generate_anagrams(initial_word: &str, words_list: Vec<String>) -> Vec<String> {
    let initial_word_chars = initial_word.chars().collect();

    words_list
        .iter()
        .combinations(2)
        .filter(|words| is_anagram(&initial_word_chars, &words))
        .map(|words| words.iter().join(" "))
        .collect()
}

fn main() {
    let initial_word = "documenting";
    let words = read_words(initial_word);
    println!("words: {:?}", words);
    println!("words: {}", words.len());
    for _i in 0..10000 {
        let anagrams = generate_anagrams(initial_word, words.clone());

        println!("anagrams: {:?}", anagrams);
    }
}

#[test]
fn small_dataset() {
    let anagrams = generate_anagrams(
        "abc",
        vec![
            "ab".to_string(),
            "bc".to_string(),
            "ac".to_string(),
            "a".to_string(),
            "b".to_string(),
            "c".to_string(),
        ],
    );
    assert_eq!(anagrams, vec!["ab c", "bc a", "ac b"])
}
