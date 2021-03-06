fn read_words() -> Vec<String> {
    let content =
        std::fs::read_to_string("../wordlist2.txt").expect("unable to read word list file");
    content.split('\n').map(|s| s.to_string()).collect()
}
//fn read_words() -> Vec<String> {
//    let content = std::fs::read_to_string("./wordlist.txt").expect("unable to read word list file");
//    content
//        .split('\n')
//        .skip(1)
//        .map(|s| s.split(' '))
//        .flatten()
//        .filter(|s| !s.is_empty())
//        .map(|s| s.to_string())
//        .collect()
//}

fn get_char_value(c: char, base_word: &str) -> Option<usize> {
    base_word
        .char_indices()
        .find(|(_i, wc)| c == *wc)
        .map(|(i, _wc)| i)
}

fn get_word_value(word: &str, base_word: &str) -> Option<usize> {
    word.chars()
        .map(|c| get_char_value(c, base_word).map(|v| base_word.len().pow(v as u32)))
        .sum()
}

fn generate_anagrams(initial_word: &str, words_list: &Vec<String>) -> Vec<String> {
    let initial_word_value = get_word_value(initial_word, initial_word)
        .expect("by construction, all letter should be there");

    let words_values = words_list
        .into_iter()
        .filter_map(|w| get_word_value(&w, initial_word).map(|v| ((v, w))))
        .collect::<Vec<_>>();

    let mut anagrams = Vec::new();
    for (i1, (v1, w1)) in words_values.iter().enumerate() {
        for (v2, w2) in &words_values[i1 + 1..] {
            if initial_word_value == v1 + v2 && w1.len() + w2.len() == initial_word.len() {
                anagrams.push(format!("{} {}", w1, w2));
            }
        }
    }
    anagrams
}

fn main() {
    let initial_word = "documenting";
    let words = read_words();
    //println!("words: {:?}", words);
    println!("words: {}", words.len());

    for i in 0..100 {
        let anagrams = generate_anagrams(initial_word, &words);

        if i == 0 {
            println!("anagrams: {:?}", anagrams);
        }
    }
}

#[test]
fn small_dataset() {
    let anagrams = generate_anagrams(
        "abc",
        &vec![
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

#[test]
fn redundant_letter() {
    let anagrams = generate_anagrams(
        "abcb",
        &vec![
            "ab".to_string(),
            "bc".to_string(),
            "ac".to_string(),
            "abc".to_string(),
            "a".to_string(),
            "b".to_string(),
            "c".to_string(),
        ],
    );
    assert_eq!(anagrams, vec!["ab bc", "abc b"])
}

#[test]
fn word_without_letters_in_base_word() {
    let anagrams = generate_anagrams(
        "abc",
        &vec![
            "ab".to_string(),
            "bc".to_string(),
            "ac".to_string(),
            "acd".to_string(),
            "a".to_string(),
            "d".to_string(),
            "b".to_string(),
            "c".to_string(),
        ],
    );
    assert_eq!(anagrams, vec!["ab c", "bc a", "ac b"])
}

#[test]
fn corner_case() {
    let anagrams = generate_anagrams(
        "ab",
        &vec!["aa".to_string(), "a".to_string(), "b".to_string()],
    );
    assert_eq!(anagrams, vec!["a b"]) // aa a should not be a valid anagram
}
