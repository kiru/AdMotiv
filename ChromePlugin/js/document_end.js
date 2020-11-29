

var processed_ids = {};

jQuery(function ($) {

  artAdder.getSelectors()
    .then(function (obj) {
      var selectors = obj.selectors
      var host = R.path(['location', 'host'], parent)
      var skips = []
      if (host) {
        host = host.replace('www.', '')
        if (obj.blockedSites.indexOf(host) > -1) return // this site is blocked

        skips = obj.whitelist
          .filter(R.pipe(R.nth(0), R.split(','), R.contains(host)))
          .map(R.nth(1))
      }
      setInterval(function checkIFrames() {

        var banners = $(selectors.join(','))
          .map(function () {
            var origW = this.offsetWidth;
            var origH = this.offsetHeight;

            var goodBye = false;
            var elem = this;
            if (elem.tagName !== 'IFRAME'
              && elem.tagName !== 'IMG'
              && elem.tagName !== 'DIV'
              && elem.tagName !== 'OBJECT'
              && elem.tagName !== 'A'
              && elem.tagName !== 'INS'
            ) goodBye = true
            if ($(elem).data('replaced')) goodBye = true

            return {
              replaced: goodBye,
              ad: this,
              width: origW,
              height: origH,
              id: elem.id
            }
          }).toArray()
          .filter(f => !processed_ids[f.id])
          .filter(f => !f.replaced)
          .filter(f => !(f.width === 0 || f.height === 0))
          .filter(f => !(f.width < 150 && f.height < 150));

        console.log("unprocessed banners:", banners.length);

        if (banners.length > 0) {
          var content = document.body.innerHTML;

          console.log("Do request for banners: ", banners.length);

          $.ajax("https://localhost:8000/get_ad_replacement", {
            method: 'POST',
            contentType: "application/json",
            dataType: 'json',
            data: JSON.stringify({
              "title": document.title,
              "content": content,
              "banners": banners.map(f => {
                return {width: f.width, height: f.height, id: f.id}
              })
            }),
            success: e => {
              let banners_to_replace = e.banners

              // actual ad-replacement
              banners.forEach(function (f) {
                let that = f.ad;
                var $this = $(that)
                var successfulSkips = skips.filter(function (sel) {
                  return $this.is(sel)
                })
                if (successfulSkips.length > 0) {
                  return
                }

                let found_banner = banners_to_replace.find(x => x.id === f.id)
                artAdder.processAdNode(that, found_banner)
                processed_ids[f.id] = true
              });
            }
          });
        }
      }, 2000);
    })
})

jQuery(function ($) {
  setInterval(function () {
    const results = $("div[data-testid=tweet] div div div div span:contains('Promoted')");
    if (results.length > 0) {
      console.log('Removing ad');
      let first = results.slice(0, 1);
      const magix = 10; // Change at your own risk!
      for (let i = 0; i < magix; i++) {
        first = first.parent();
      }
      first.html(
        '<img src="https://localhost:8000/get_image?x_size=600&y_size=100&type_of_content=Todoist&topic=sport" alt="">' // TODO: change that to the actual content
      )
    }
  }, 200);
});
