import bs4
from bs4 import BeautifulSoup
from gtts import gTTS

def extract_stories_from_NPR_text(text):
    soup = BeautifulSoup(text, 'html.parser')
    stories = []
    
    story_elements = soup.find_all('div', class_='story-wrap')
    
    for story in story_elements:
        title = story.find('h3', class_='title').get_text().strip()
        
        teaser_element = story.find('p', class_='teaser')
        if teaser_element:
            teaser = teaser_element.get_text().strip()
        else:
            teaser = ''
        stories.append((title, teaser))
    return stories

def read_nth_story(stories, n, filename):
    if n < 0 or n >= len(stories):
        raise ValueError(f"Invalid index {n}. It should be between 0 and {len(stories)-1}.")
    
    title, teaser = stories[n]
    
    text_to_synthesize = f"{title}. {teaser}"
    
    tts = gTTS(text=text_to_synthesize, lang='en')
    
    tts.save(filename)
