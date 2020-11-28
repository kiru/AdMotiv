import random

quotes = [
  {
    "text": "Genius is one percent inspiration and ninety-nine percent perspiration.",
    "author": "Thomas Edison"
  },
  {
    "text": "You can observe a lot just by watching.",
    "author": "Yogi Berra"
  },
  {
    "text": "A house divided against itself cannot stand.",
    "author": "Abraham Lincoln"
  },
  {
    "text": "Difficulties increase the nearer we get to the goal.",
    "author": "Johann Wolfgang von Goethe"
  },
  {
    "text": "Fate is in your hands and no one elses",
    "author": "Byron Pulsifer"
  },
  {
    "text": "Be the chief but never the lord.",
    "author": "Lao Tzu"
  },
  {
    "text": "Nothing happens unless first we dream.",
    "author": "Carl Sandburg"
  },
  {
    "text": "Well begun is half done.",
    "author": "Aristotle"
  },
  {
    "text": "Life is a learning experience, only if you learn.",
    "author": "Yogi Berra"
  },
  {
    "text": "Self-complacency is fatal to progress.",
    "author": "Margaret Sangster"
  },
  {
    "text": "Peace comes from within. Do not seek it without.",
    "author": "Buddha"
  },
  {
    "text": "What you give is what you get.",
    "author": "Byron Pulsifer"
  },
  {
    "text": "We can only learn to love by loving.",
    "author": "Iris Murdoch"
  },
  {
    "text": "Life is change. Growth is optional. Choose wisely.",
    "author": "Karen Clark"
  },
  {
    "text": "You'll see it when you believe it.",
    "author": "Wayne Dyer"
  },
  {
    "text": "Today is the tomorrow we worried about yesterday.",
    "author": "unknown"
  },
  {
    "text": "It's easier to see the mistakes on someone else's paper.",
    "author": "unknown"
  },
  {
    "text": "Every man dies. Not every man really lives.",
    "author": "unknown"
  }]

formatted_quotes_calendar = [
  "Don't forget to attend {} from {} til {} on {}",
  "Remember to turn up for {} from {} til {} on {}",
  "{} is taking place from {} til {} on {}, don't miss it!",
  "Watching youtube instead of following {} from {} til {} on {}?!",
  "You can take a break until {} begins at {} until {} on {}"
]

formatted_quotes_todoist = [
  "Don't forget to {}!",
  "Remember to {}!",
  "Did you {}?",
  "Are you sure you finished with {}?",
  "You've got some free time to {}"
]

formatted_quotes_todoist_due = [
  "Don't forget to {} by {}!",
  "Remember to {} by {}!",
  "Did you already finish {}? The deadline is on {}",
  "Are you sure you will finish with {}, before {}?",
  "You've got some free time to {}, the deadline's on {}"
]

formatted_quotes_todoist_keyword = [
  "Reading about {} is cool but don't forget to {}!",
  "Reading about {} is cool but remember to {}!",
  "I see you're reading about {}, did you already finish {}?",
  "If you keep on reading about {}, are you sure you will finish with {}?",
  "You're reading about {} so you've got some free time to {}"
]

formatted_quotes_todoist_keyword_due = [
  "Reading about {} is cool but don't forget to {} by {}!",
  "Reading about {} is cool but remember to {} by {}!",
  "I see you're reading about {}, did you already finish {}? The deadline is on {}",
  "If you keep on reading about {}, are you sure you will finish with {}, before {}?",
  "You're reading about {} so you've got some free time to {}, the deadline's on {}"
]

def get_motivational_quote():
    return random.choice(quotes)

if __name__ == '__main__':
    get_motivational_quote()



