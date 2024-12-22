def save_words_to_file(unique_words, total_count):
    try:
        with open('word_count.txt', 'w') as file:
            file.write(f"Total words entered: {total_count}\n")
            file.write(f"Unique words ({len(unique_words)}):\n")
            for word in sorted(unique_words):
                file.write(f"- {word}\n")
        print("Words saved to 'word_count.txt' successfully!")
    except Exception as e:
        print(f"Error saving to file: {e}")

def main():
    # Initialize sets for both case-sensitive and case-insensitive tracking
    unique_words = set()
    case_insensitive_words = set()
    total_words = 0

    print("Enter words one at a time. Program will exit when a duplicate is entered.")
    print("Enter 'save' to save current words to file.")
    
    while True:
        # Get input and remove whitespace
        word = input("\nEnter a word: ").strip()
        
        # Check for save command
        if word.lower() == 'save':
            save_words_to_file(unique_words, total_words)
            continue
            
        # Increment total word count
        total_words += 1
        
        # Check for duplicates (case-insensitive)
        if word.lower() in case_insensitive_words:
            print("\nDuplicate word detected!")
            print(f"Total words entered: {total_words}")
            print(f"Unique words (case-sensitive): {len(unique_words)}")
            print(f"Unique words (case-insensitive): {len(case_insensitive_words)}")
            
            # Display unique words alphabetically
            if unique_words:
                print("\nUnique words (alphabetically):")
                for unique_word in sorted(unique_words):
                    print(f"- {unique_word}")
            
            # Offer to save before exiting
            save = input("\nWould you like to save the words to a file? (yes/no): ").lower()
            if save.startswith('y'):
                save_words_to_file(unique_words, total_words)
            
            break
        
        # Add word to both sets
        unique_words.add(word)
        case_insensitive_words.add(word.lower())

if __name__ == "__main__":
    main()