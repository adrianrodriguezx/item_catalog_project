from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Category, Item

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
User1 = User(name="Albert Einstein", email="aeinstein@edu.com",
             picture='https://en.wikipedia.org/wiki/Albert_Einstein#/media/File:Albert_Einstein_(Nobel).png')
session.add(User1)
session.commit()

# Create Categories Soccer 
category1 = Category(name="Soccer")
session.add(category1)
session.commit()

# Create an Item Soccer
Item1 = Item(name="Shinguards",
	description="Part of our Ghost guard collection, this is a great fitting guard for the beginner and advanced athlete Shin guard is made up of 3 different shields fitted together for highest flexibility and perfect fit Snug fitting compression sleeve holds guard securely in place without bulk Soft and durable EVA backing on shield for durable, lightweight cushioning and extra comfort",
	item_category=category1, item_creator=User1)

session.add(Item1)
session.commit()

# Create an Item Soccer
Item2 = Item(name="Soccer Cleats",
	description="Cleats or studs are protrusions on the sole of a shoe, or on an external attachment to a shoe, that provide additional traction on a soft or slippery surface. In American English the term cleats is used synecdochically to refer to shoes featuring such protrusions.",
	item_category=category1, item_creator=User1)

session.add(Item2)
session.commit()

# Create an Item Soccer
Item3 = Item(name="Soccer Ball",
	description="A football, soccer ball, or association football ball is the ball used in the sport of association football.",
	item_category=category1, item_creator=User1)

session.add(Item3)
session.commit()

###
# Create dummy user
User2 = User(name="Isaac Newton", email="inewton@edu.com",
             picture='https://en.wikipedia.org/wiki/Isaac_Newton#/media/File:GodfreyKneller-IsaacNewton-1689.jpg')
session.add(User2)
session.commit()

# Create Categories Baseball
category2 = Category(name="Baseball")
session.add(category2)
session.commit()

# Create an Item Baseball
Item1 = Item(name="Bat",
	description="A baseball bat is a smooth wooden or metal club used in the sport of baseball to hit the ball after it is thrown by the pitcher.",
	item_category=category2, item_creator=User2)

session.add(Item1)
session.commit()

###
# Create Categories Hockey 
category3 = Category(name="Hockey")
session.add(category3)
session.commit()

# Create an Item Hockey
Item2 = Item(name="Stick",
	description="A hockey stick is a piece of equipment used in field hockey, ice hockey, roller hockey or underwater hockey to move the ball or puck.",
	item_category=category3, item_creator=User2)

session.add(Item2)
session.commit()


# Create Categories 
category4 = Category(name="Skating")
session.add(category4)
session.commit()

category5 = Category(name="Foosball")
session.add(category5)
session.commit()

category6 = Category(name="Rock Climbing")
session.add(category6)
session.commit()

category7 = Category(name="Snowboarding")
session.add(category7)
session.commit()

category8 = Category(name="Frisbee")
session.add(category8)
session.commit()

category9 = Category(name="Basketball")
session.add(category9)
session.commit()