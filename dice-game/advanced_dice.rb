# YOUR ADVANCED CODE, HERE
def DiceGame()
  puts "How many sides does your dice have? "
  sides = gets.chomp

  puts "How many times would you like to roll your pair of dice?"
  num = gets.chomp
  puts ""

  while true
    counter = 0

    while counter < num.to_i
      num1 = rand(sides.to_i) + 1
      num2 = rand(sides.to_i) + 1

      puts "You rolled a #{num1} and a #{num2}. Total: #{num1+num2}"
      counter += 1
    end

    puts "\nRoll Again? (Y/N)> "
    cont_game = gets.chomp
    if cont_game == "N"
      break
    end
    
  end
end

DiceGame()
