if (typeof chrome !== 'undefined') {
  chrome.runtime.onInstalled.addListener(function (event) {
    init(event);
  });

  chrome.runtime.onStartup.addListener(function (event) {
    init(event)
      .then(function () {
        return artAdder.localGet('disableAutoUpdate')
      })
      .then(function (res) {
        if (!res.disableAutoUpdate) {
          artAdder.chooseMostRecentExhibition()
        }
      })
  });

  chrome.runtime.onMessage.addListener(function (msg) {
    var key = msg.msg.what
    if (artAdder[key] && typeof artAdder[key] === 'function') {
      artAdder[key](msg.msg[key])
    }
  })
}

function init(event) {
  artAdder.fetchSelectorList()
  return syncDefaultList()
    .then(artAdder.getExhibition) // have we chosen a show?
    .then(function (exhibition) {
      // no, this is the first time
      if (!exhibition) {
        artAdder.chooseMostRecentExhibition()
        console.log("I am here bro....")
      }
    })
}

// set default show list from add-art feed
function syncDefaultList() {
  var d = Q.defer()
  // $.ajax({
  //   url: 'https://raw.githubusercontent.com/owise1/add-art-exhibitions/master/exhibitions.json',
  //   dataType: 'json',
  //   success: function (items) {
  //     items = items.sort(artAdder.exhibitionsSort)
  //     if (items.length > 0) {
  //       // artAdder.localSet('defaultShowData', items).then(d.resolve)
  //     }
  //   }
  // })

  var json = [
    {
      "title": "For Freedoms",
      "artist": "Multiple artists",
      "description": "Part of the \"For Freedoms\" 50 State Initiative, these billboards appear from Hartford to Nashville, from Lansing and Los Angeles. The 16 included here are a small selection of dozens of artworks by artists that FF has invited to make use of the high visibility spaces of advertising to invite civic engagement. \"We believe that if artists’ voices replace advertising across the country, public discourse will become more nuanced.\" Artists featured: Paula Crown, Jamila El Sahli, Awol Erizku, Theaster Gates, Eric Gottesman, Emily Hanako Momohara, Alfredo Jaar, Marilyn Minter, Donald Moffett, Lorraine O'Grady, Trevor Paglen, Xaviera Simmons, Christine Sun Kim, Hank Willis Thomas.",
      "link": "https://forfreedoms.org/",
      "thumbnail": "http://addendum.kadist.org/FF/14.jpg",
      "date": 1543438591178,
      "works": [
        {
          "image": "//localhost:8000/get_image?content=Kiru%20work%20ffs&x_size=100&y_size=200",
          "link": "https://forfreedoms.org/"
        },
      ]
    }
  ];
  artAdder.localSet('defaultShowData', json).then(d.resolve)
  return d.promise
}

