# YOUR CODE HERE
require 'pry'
def NextTrain()
  trains = [2,5,7.5,8.5,9,10,11.5,13.5,14.5,17,18,19,24]
  user_train, user_train_time = [],[]

  while true
    puts "What time are you leaving? "
    user_time = gets.chomp.to_f

    if user_time == 0.0
      puts "\nSorry, I don't understand that time."
    else
      break
    end
  end

  trains.each_with_index do |train,index|
    if train > user_time
      user_train_time << train
      user_train << index+1
    end
  end

  puts "You should catch Train #{user_train.first} leaving at #{user_train_time.first}"

  user_train.each do |train|
    if train == 13
      puts "
      ***DON'T STOP...BELIEVIN' !***

      Just a small town girl
      Living in a lonely world
      She took the midnight train going anywhere
      Just a city boy
      Born and raised in South Detroit
      He took the midnight train going anywhere

      A singer in a smoky room
      A smell of wine and cheap perfume
      For a smile they can share the night
      It goes on and on and on and on

      Strangers waiting, up and down the boulevard
      Their shadows searching in the night
      Streetlights people, living just to find emotion
      Hiding, somewhere in the night."
    end
  end
end

NextTrain()
