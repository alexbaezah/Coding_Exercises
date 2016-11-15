# YOUR CODE GOES HERE
def Game()
  game = ["rock", "paper", "scissors"]
  computer = game.sample

  puts "Choose rock(r), paper(p), or scissors(s): "
  user_input = gets.chomp.downcase

  user_choice = case user_input
  when "r" then "Player chose rock."
  when "p" then "Player chose paper."
  when "s" then "Player chose scissors."
  else "Invalid entry, try again."
  end

  computer_choice = case computer
  when "rock" then "Computer chose rock."
  when "paper" then "Computer chose paper."
  else "Computer chose scissors."
  end

  puts user_choice
  puts computer_choice

  if (user_input == "r" && computer == "paper") || (user_input == "p" && computer == "scissors") || (user_input == "s" && computer == "rock")
    puts "Computer wins!"
  elsif (user_input == "r" && computer == "scissors") || (user_input == "p" && computer == "rock") || (user_input == "s" && computer == "paper")
    puts "Player wins!"
  else
    puts "Tie!"
  end

end

Game()
