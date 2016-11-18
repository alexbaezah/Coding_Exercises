# YOUR CODE, HERE
def DiceGame()
  while true
    num1 = rand(6)+1
    num2 = rand(6)+1

    puts "You rolled a #{num1} and a #{num2}"
    puts "Total: #{num1+num2}"
    puts "Press 'Enter' to roll again, 'S' to stop "
    cont_game = gets.chomp

    if cont_game == 'S'
      break
    end

  end
end

DiceGame()
