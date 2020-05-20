import re

from bs4 import BeautifulSoup


ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
               <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>
        In stock
</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>
</body></html>
'''

class ParsedLocator:
  NAME_LOCATOR = 'article.product_pod p.star-rating'
  LINK_LOCATOR = 'article.product_pod p.price_color'
  RATING_LOCATOR= 'article.product_pod h3 a'
  PRICE_LOCATOR = 'article.product_pod h3 a'



class ParsedItem:

  def __init__(self, page):
    self.soup = BeautifulSoup(page, 'html.parser')

  @property
  def name(self):
    locator = ParsedLocator.NAME_LOCATOR
    item_name = self.soup.select_one(locator).attrs['title']
    return item_name

  @property
  def link(self):
    locator = ParsedLocator.LINK_LOCATOR
    item_link = self.soup.select_one(locator).attrs['href']
    return item_link

  @property
  def price(self):
    locator = ParsedLocator.PRICE_LOCATOR
    item_price = self.soup.select_one(locator).string
    pattern = '£([0-9]+\.[0-9]+)'
    matcher = re.search(pattern, item_price)
    print(float(matcher.group(1))*0.2)
    return float(matcher.group(1))*0.2

  @property
  def rating(self):
    locator = ParsedLocator.RATING_LOCATOR
    star_rating = self.soup.select_one(locator)
    classes = star_rating.attrs['class']
    number = list(filter(lambda x: x != 'star-rating', classes))
    return number









item = ParsedItem(ITEM_HTML)
item.price
item.rating
item.rating




