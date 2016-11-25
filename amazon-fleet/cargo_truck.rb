#your code, here.
class CargoTruck
  attr_reader :odometer
  attr_accessor :driver

  def initialize(plate_number, branding)
    @plate_number = plate_number
    @branding = branding
  end

  def odometer
    return 0
  end

  def driver=(driver)
    @driver=driver
  end

  def summary
    puts "#{@branding} truck with plate ##{@plate_number} is driven by #{@driver}."
  end
end

truck = CargoTruck.new('AMZ001', "Amazon")
truck.odometer
truck.driver
truck.driver = "Larry"
truck.summary
