import wikipediaapi

# Wikipedia requires a custom User-Agent identifying your application
wiki = wikipediaapi.Wikipedia(
    user_agent="MyDataExtractorBot/1.0 (contact@example.com)",
    language="en"
)

# Fetch the page
page = wiki.page("Python_(programming_language)")

if page.exists():
    print(f"Title: {page.title}")
    print("\nSummary:")
    print(page.summary[:500])  # Print first 500 characters
    
    # Access a specific section
    history_section = page.section_by_title("History")
    if history_section:
        print(f"\n{history_section.title} Section:")
        print(history_section.text[:300])
else:
    print("Page not found.")
