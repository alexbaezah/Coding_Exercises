# YOUR CODE GOES HERE
def Game()
  game = ["rock", "paper", "scissors"]

  user_score = 0
  computer_score = 0

  while user_score < 5 and computer_score < 5
    computer = game.sample

    puts "\nChoose rock(r), paper(p), or scissors(s): "
    user_input = gets.chomp.downcase

    user_choice = case user_input
    when "r" then "\nPlayer chose rock."
    when "p" then "\nPlayer chose paper."
    when "s" then "\nPlayer chose scissors."
    else
      puts "Invalid entry, try again."
      break
    end

    computer_choice = case computer
    when "rock" then "Computer chose rock."
    when "paper" then "Computer chose paper."
    else "Computer chose scissors."
    end

    puts user_choice
    puts computer_choice

    if (user_input == "r" && computer == "paper") || (user_input == "p" && computer == "scissors") || (user_input == "s" && computer == "rock")
      computer_score += 1
      puts "\nComputer wins!"
      puts "Player Score: #{user_score}, Computer Score: #{computer_score}"
    elsif (user_input == "r" && computer == "scissors") || (user_input == "p" && computer == "rock") || (user_input == "s" && computer == "paper")
      user_score += 1
      puts "\nPlayer wins!"
      puts "Player Score: #{user_score}, Computer Score: #{computer_score}"
    else
      puts "\nTie!"
      puts "Player Score: #{user_score}, Computer Score: #{computer_score}"
    end
  end

end

Game()
