# NUTRITION CALCULATOR FOR MEN #


''' INPUTS (assuming imperial inputs) '''

input_weight_imperial = int(input("Please enter your weight in LBS: "))
input_height_imperial = int(input("Please enter your height in INCHES: ")) 
input_age = int(input("Please enter your age in YEARS: "))

input_body_fat_percentage = raw_input("If you know it, please enter your body fat % (if not, press enter): ")
if not input_body_fat_percentage:
   input_body_fat_percentage = None

# input_body_fat_percentage = int(input("Please enter your body fat % : ") or "0" )  # optional


# input physical activity factor (PAF) [Sedentary, Lightly Active, Moderately Active, Very Active, Extremely Active] 
# input body type [ectomorph - thin, mesomorph - athletic, endomorph - heavy] 
# input gender [female, male]

''' CONVERSION (from here on out, everything is calculated using metric values) '''
# if input is imperial, convert to metric -- everything can stay in metric since outputs are in calories and fluid oz 

input_weight_metric = input_weight_imperial / 2.2
input_height_metric = input_height_imperial * 2.54



''' Resting Metabolic Rate RMR '''

# this calculation can be displayed as-is and does not need conversion since final result is in calories rather than a specific metric/imperial unit
output_rmr_metric_default = ( input_weight_metric*13.75 ) + ( input_height_metric*5 ) - ( input_age*6.76 ) + 66
print("Men RMR calculated without user-input body fat is " + str(output_rmr_metric_default) + " calories.")
#rmr calculation based on body fat input as well
if input_body_fat_percentage is not None:
    output_rmr_metric_body_fat =  ( ( (100 - input_body_fat_percentage) * input_weight_metric ) / 100 ) * 21.6 + 370
    print("Men RMR calculated WITH user-input body fat is " + str(output_rmr_metric_body_fat) + " calories.")
    output_tef_metric_body_fat = output_rmr_metric_body_fat * .01
    print ("Men TEF calculated WITH user-input body fat is " + str(output_tef_metric_body_fat) + " calories.")
    output_sedentary_paf_metric_body_fat = ( output_rmr_metric_body_fat * 1.2 ) - output_rmr_metric_body_fat
    print ("Men Sedentary PAF calculated WITH user-input body fat is " + str(output_sedentary_paf_metric_body_fat) + " Physical Activity Calories." )
    output_light_paf_metric_body_fat = ( output_rmr_metric_body_fat * 1.375 ) - output_rmr_metric_body_fat
    print ("Men Light PAF calculated WITH user-input body fat is " + str(output_light_paf_metric_body_fat) + " Physical Activity Calories." )
    output_moderate_paf_metric_body_fat = ( output_rmr_metric_body_fat * 1.55 ) - output_rmr_metric_body_fat
    print ("Men Moderate PAF calculated WITH user-input body fat is " + str(output_moderate_paf_metric_body_fat) + " Physical Activity Calories." )
    output_very_paf_metric_body_fat = ( output_rmr_metric_body_fat * 1.725 ) - output_rmr_metric_body_fat
    print ("Men Very Active PAF calculated WITH user-input body fat is " + str(output_very_paf_metric_body_fat) + " Physical Activity Calories." )
    output_extremely_paf_metric_body_fat = ( output_rmr_metric_body_fat * 1.9 ) - output_rmr_metric_body_fat
    print ("Men Extremely Active PAF calculated WITH user-input body fat is " + str(output_extremely_paf_metric_body_fat) + " Physical Activity Calories." )
    output_tdee_metric_body_fat = output_rmr_metric_body_fat + output_tef_metric_body_fat + output_extremely_paf_metric_body_fat
    output_dgci_build_aggressive_metric_body_fat = output_tdee_metric_body_fat + 500
    output_dgci_build_moderate_metric_body_fat = output_tdee_metric_body_fat + 250
    output_dgci_burn_moderate_metric_body_fat = output_tdee_metric_body_fat - 500
    output_dgci_burn_agressive_metric_body_fat = output_tdee_metric_body_fat - 750
    output_dgci_burn_extreme_metric_body_fat = output_tdee_metric_body_fat - 1000




''' OUTPUT Thermal Effect of Food (calories burned from digestion) TEF '''

output_tef_metric_default = output_rmr_metric_default * .01
print ("Men TEF calculated without user-input body fat is " + str(output_tef_metric_default) + " calories.")


''' OUTPUT physical activity factor PAF ''' 
# this calculation depends on user input of physical activity factor (PAF)

# sedentary -- results are in calories
output_sedentary_paf_metric_default = ( output_rmr_metric_default * 1.2 ) - output_rmr_metric_default
print ("Men Sedentary PAF calculated without user-input body fat is " + str(output_sedentary_paf_metric_default) + " Physical Activity Calories." )

output_light_paf_metric_default = ( output_rmr_metric_default * 1.375 ) - output_rmr_metric_default
print ("Men Light PAF calculated without user-input body fat is " + str(output_light_paf_metric_default) + " Physical Activity Calories." )

# moderately active -- results are in calories 
output_moderate_paf_metric_default = ( output_rmr_metric_default * 1.55 ) - output_rmr_metric_default
print ("Men Moderate PAF calculated without user-input body fat is " + str(output_moderate_paf_metric_default) + " Physical Activity Calories." )

# very active -- results are in calories 
output_very_paf_metric_default = ( output_rmr_metric_default * 1.725 ) - output_rmr_metric_default

print ("Men Very Active PAF calculated without user-input body fat is " + str(output_very_paf_metric_default) + " Physical Activity Calories." )

# extremely active -- results are in calories 
output_extremely_paf_metric_default = ( output_rmr_metric_default * 1.9 ) - output_rmr_metric_default

print ("Men Extremely Active PAF calculated without user-input body fat is " + str(output_extremely_paf_metric_default) + " Physical Activity Calories." )



''' OUTPUT Total Daily Energy Expenditure in calories TDEE '''
''' 
ASSUMPTION: to avoid displaying so many variations based on activity levels,
this test case will be an extremely active individual, using the following two variables: 
output_extremely_paf_metric_default
output_extremely_paf_metric_body_fat
Keep in mind that this variable should be different depending on inputted activity level.
'''
#formula is different depending on (a) if body fat was entered and (b) what activity level is -- results are in calories
output_tdee_metric_default = output_rmr_metric_default + output_tef_metric_default + output_extremely_paf_metric_default



''' OUTPUT Daily Goal Caloric Intake -- calorie intake adjustments based off client goal DGCI '''

# agressive muscle growth (build 1 lb/week | build .45 kg/week) -- results are in calories
output_dgci_build_aggressive_metric_default = output_tdee_metric_default + 500 

# moderate muscle growth (build 0.5 lb/week | build .23 kg/week) -- results are in calories
output_dgci_build_moderate_metric_default = output_tdee_metric_default + 250 

# maintain -- results are in calories
# output_tdee_metric_default
# output_tdee_metric_body_fat

# moderate burn fat (burn 1 lb/ week | .45 kg / week) -- results are in calories
output_dgci_burn_moderate_metric_default = output_tdee_metric_default - 500 

# agressive burn fat (burn 1.5 lb/ week | .68 kg / week) -- results are in calories
output_dgci_burn_agressive_metric_default = output_tdee_metric_default - 750 

# extreme burn fat (burn 2 lb/ week | .91 kg / week) -- results are in calories
output_dgci_burn_extreme_metric_default = output_tdee_metric_default - 1000 



''' OUTPUT Margin Of Error Range of Calories MOE '''
''' 
ASSUMPTION: to avoid displaying so many variations based on activity levels,
this test case will be an extremely active individual, using the following two variables: 
output_extremely_paf_metric_default
output_extremely_paf_metric_body_fat
Keep in mind that this variable should be different depending on inputted activity level.
Our second assumption is that this individual's DGCI (daily goal caloric intake) 
is extreme fat loss, so we'll use the following two variables:
output_dgci_burn_extreme_metric_default
output_dgci_burn_extreme_metric_body_fat
'''
#the following two calculations are not displayed -- they are use to calculate the low and high margin of error (MOE)
moe_metric_default = output_dgci_burn_extreme_metric_default * .15 
moe_metric_body_fat = output_dgci_burn_extreme_metric_body_fat * .15 

#high end calorie intake margin of error (high MOE) -- results are in calories 
output_moe_high_metric_default = output_dgci_burn_extreme_metric_default + moe_metric_default
output_moe_high_metric_body_fat = output_dgci_burn_extreme_metric_body_fat + moe_metric_body_fat

#low end calorie intake margin of error (low MOE) -- results are in calories 
output_moe_low_metric_default = output_dgci_burn_extreme_metric_default - moe_metric_default
output_moe_low_metric_body_fat = output_dgci_burn_extreme_metric_body_fat - moe_metric_body_fat

print("Men high MOE calculated without user-input body fat is " + str(output_moe_high_metric_default) + " calories")
print("Men high MOE calculated WITH user-input body fat is " + str(output_moe_high_metric_body_fat) + " calories")

print("Men low MOE calculated without user-input body fat is " + str(output_moe_low_metric_default) + " calories")
print("Men low MOE calculated WITH user-input body fat is " + str(output_moe_low_metric_body_fat) + " calories")



''' OUTPUT Macronutrient Ratio Recommendations (MRR) '''
''' 
ASSUMPTIONS: 
to avoid displaying so many variations based on activity levels,
this test case will be an extremely active individual (PAF = physical activity factor), using the following two variables: 
output_extremely_paf_metric_default
output_extremely_paf_metric_body_fat
Keep in mind that this variable should be different depending on inputted activity level.
Our second assumption is that this individual's DGCI (daily goal caloric intake) 
is extreme fat loss, so we'll use the following two variables:
output_dgci_burn_extreme_metric_default
output_dgci_burn_extreme_metric_body_fat
'''
#Ectomorph Macros: (Naturally Thinner Body Type/Frame) (ecto) -- results are in grams of [protein, fat, carbs] / day
#protein
output_mmr_ecto_protein_metric_default = ( output_dgci_burn_extreme_metric_default *.25 ) / 4
output_mmr_ecto_protein_metric_body_fat = ( output_dgci_burn_extreme_metric_body_fat *.25 ) / 4
#carb
output_mmr_ecto_carb_metric_default = ( output_dgci_burn_extreme_metric_default *.55 ) / 4
output_mmr_ecto_carb_metric_body_fat = ( output_dgci_burn_extreme_metric_body_fat *.55 ) / 4
#fat
output_mmr_ecto_fat_metric_default = ( output_dgci_burn_extreme_metric_default *.2 ) / 9
output_mmr_ecto_fat_metric_body_fat = ( output_dgci_burn_extreme_metric_body_fat *.2 ) / 9

#Mesomorph Macros: (Naturally Proportional/Athletic Body Type/Frame) (meso) -- results are in grams of [protein, fat, carbs] / day
#protein
output_mmr_meso_protein_metric_default = ( output_dgci_burn_extreme_metric_default *.3 ) / 4
output_mmr_meso_protein_metric_body_fat = ( output_dgci_burn_extreme_metric_body_fat *.3 ) / 4
#carb
output_mmr_meso_carb_metric_default = ( output_dgci_burn_extreme_metric_default *.4 ) / 4
output_mmr_meso_carb_metric_body_fat = ( output_dgci_burn_extreme_metric_body_fat *.4 ) / 4
#fat
output_mmr_meso_fat_metric_default = ( output_dgci_burn_extreme_metric_default *.3 ) / 9
output_mmr_meso_fat_metric_body_fat = ( output_dgci_burn_extreme_metric_body_fat *.3 ) / 9

#Endomorph Macros: (Naturally Heavy Body Type/Frame) (endo) -- results are in grams of [protein, fat, carbs] / day 
#protein
output_mmr_endo_protein_metric_default = ( output_dgci_burn_extreme_metric_default *.35 ) / 4
output_mmr_endo_protein_metric_body_fat = ( output_dgci_burn_extreme_metric_body_fat *.35 ) / 4
#carb
output_mmr_endo_carb_metric_default = ( output_dgci_burn_extreme_metric_default *.25 ) / 4
output_mmr_endo_carb_metric_body_fat = ( output_dgci_burn_extreme_metric_body_fat *.25 ) / 4
#fat
output_mmr_endo_fat_metric_default = ( output_dgci_burn_extreme_metric_default *.4 ) / 9
output_mmr_endo_fat_metric_body_fat = ( output_dgci_burn_extreme_metric_body_fat *.4 ) / 9

print("Men naturally thin MMR calculated without user-input body fat are " + str(output_mmr_ecto_protein_metric_default) + " grams protein " + str(output_mmr_ecto_carb_metric_default) + " grams carbs " + str(output_mmr_ecto_fat_metric_default) + " grams fat.") 
print("Men naturally proportional MMR calculated without user-input body fat are " + str(output_mmr_meso_protein_metric_default) + " grams protein " + str(output_mmr_meso_carb_metric_default) + " grams carbs " + str(output_mmr_meso_fat_metric_default) + " grams fat.") 
print("Men naturally heavy MMR calculated without user-input body fat are " + str(output_mmr_endo_protein_metric_default) + " grams protein " + str(output_mmr_endo_carb_metric_default) + " grams carbs " + str(output_mmr_endo_fat_metric_default) + " grams fat.") 


''' OUTPUT Recommended Water Intake (RWI) ''' 
#two calculations - minimum (min) and maximum (max) water you should drink in fluid oz -- results are in fluid oz 
output_rwi_min = input_weight_metric * .5
output_rwi_max = input_weight_metric * .8 

