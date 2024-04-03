from mouse import move, click
from time import sleep


open_button = (800, 150)
lootbox = (500, 350)


if __name__ == "__main__":
  print('3...')
  sleep(1)
  print('2...')
  sleep(1)
  print('1...')
  sleep(1)
  print('Go!')
  sleep(1)

  try:
    i = 1

    while True:
      move(open_button[0], open_button[1])
      click()
      sleep(2)
      move(lootbox[0], lootbox[1])
      click()
      sleep(6.5)
      move(open_button[0], open_button[1]-75)
      click()

      print("%i lootbox(es) opened!" %i)
      i += 1

  except KeyboardInterrupt: print("Ended.\n")
