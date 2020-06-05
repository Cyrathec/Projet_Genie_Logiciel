import logging
import sys
from model.database import DatabaseEngine
from controller.restaurant_controller import RestaurantController
from controller.product_controller import ProductController

from vue.root_frame import RootFrame

def main():

	# configure logging
	root = logging.getLogger()
	root.setLevel(logging.DEBUG)

	handler = logging.StreamHandler(sys.stdout)
	handler.setLevel(logging.DEBUG)
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	handler.setFormatter(formatter)
	root.addHandler(handler)

	logging.info("Start 2eat App")

	# Init db
	logging.info("Init database")
	database_engine = DatabaseEngine(url='sqlite:///database.db')
	database_engine.create_database()

	# controller
	restaurant_controller = RestaurantController(database_engine)
	product_controller = ProductController(database_engine)

	# init vue
	root = RootFrame(restaurant_controller, product_controller)
	root.master.title("2eat subscription app")
	root.show_menu()

	# start
	root.mainloop()


if __name__ == "__main__":
	main()
