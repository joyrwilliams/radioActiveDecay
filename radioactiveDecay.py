import math
import sys

disposalConstant = 37.00
decayConstant = 0.693

def days_to_safe_decay_level(initial, percent, half_life):

    days = -(half_life / decayConstant) *\
                             math.log(disposalConstant/(initial/percent))
    return days

def safe_activity_level(initial, days, half_life):
    safeLevel = initial * math.exp((-decayConstant*days)/half_life)

    return safeLevel

def new_isotope_activity(initial, half_life):

    initial = initial * math.exp(-(decayConstant/half_life))

    return initial

       
def main():
    try:
        isotope = input('Enter Phosphourus or Chromium: ')
        initial = float(input('Enter the initial activity of the radio isotope: '))
        isotopeMass = float(input('Enter the mass of the radioisotope: '))
        percentMass = float(input('Enter the percentage of mass that is radioactive: '))
        print()
        isotope = isotope[0].upper()
        
        if isotope == 'P':
            half_life = 14.262

            percentMass = (percentMass*isotopeMass)/100 
            days = days_to_safe_decay_level(initial, percentMass, half_life)

            safeLevel = safe_activity_level(initial, days, half_life)
        
            print('Isotope: Phosphorus')
            
            print('The number of days to safe level:',format(days,'.3f'), 'days')

            print('The safe activity level: ', format(safeLevel, '.3f'), 'kBq')
            print()
            print('Isotope activity at the end of each day: ')

            count = 0
            while initial >= safeLevel:
                initial = new_isotope_activity(initial, half_life)
                count += 1
                print('Day', count,': ', format(initial, '.4f'))


        elif isotope == 'C': 
            half_life = 27.7025
                                  
            percentMass = (percentMass*isotopeMass)/100 
            days = days_to_safe_decay_level(initial, percentMass, half_life)

            safeLevel = safe_activity_level(initial, days, half_life)

            
            print('Isotope: Chromium')

            print('The number of days to safe level:',format(days,'.3f'), 'days')

            print('The safe activity level: ', format(safeLevel, '.3f'), 'kBq')
            print()
            print('Isotope activity at the end of each day: ')



            count = 0
            while initial >= safeLevel:
                initial = new_isotope_activity(initial, half_life)
                count+= 1
                print('Day', count,': ', format(initial, '.4f'))

        elif isotope == 'Q':
            print('The program will now quit')
            sys.exit()
            
        else:
            print('Error, the isotope you entered does not exist')
            sys.exit()
            
    except IOError:
        print('Error: There was an input error, please run and try again!')

    except ValueError:
        print('Error: Non-numeric data was entered, please run and try again!')

    except:
        print('Error: An error has occured')
    
main()
