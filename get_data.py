import pandas as pd

# show all the columns
pd.set_option('display.max_columns', None)

URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQnxMS3my42BtJpFyxl1A0y9fYN7HiBB7tnjEOzPQ528okNH88F_Ad6KHXPdPbboV613m1A-z7DbpbO/pub?output=csv"


# URL = "https://docs.google.com/spreadsheets/d/1UoKzzRzOCt-FXLLqDKLbryEKEgllGAQUEJ5qtmmQwpU/edit#gid=0"
# csv_url = URL.replace('/edit#gid=', '/export?format=csv&gid=')

def get_data():
    return pd.read_csv(URL, encoding='utf-8')


df = get_data()

# save the data to a csv file
df.to_csv('data.csv', index=False)

# count = 0
# # show columns with for
# for col in get_data().columns:
#     print(col)
#     count += 1
#
# print(count)

a = ["Name (Optional)",
     "District",
     "Town/City",
     "Age",
     "Sex",
     "Highest level of education",
     "Monthly Income",
     "Do you have access to pipe water supply from NWSDB?",
     "Do you know which water treatment plant serves your pipe water supply?",
     "If yes, mention the name of water treatment plant.",
     "What do you primarily use for drinking in your household on a daily basis?",
     "Does this consumption is personal choice or the common practice in your residence?",
     "Why do you use bottled water over pipe water, what influences your choice? (Tick all that apply)",
     "What is your monthly bottled water consumption, Approximately how many liters(L) ?",
     "What size of bottled water do you usually purchase?",
     "Do you have a specific choice of bottled water brand you purchase?",
     "If yes, mention the brand/s",
     "What qualities do you check when choosing the type of bottled water?",
     "Rate your bottled water experience from 1(bad) - 5 (good) [Taste]",
     "Rate your bottled water experience from 1(bad) - 5 (good) [Ordure/smell]",
     "Rate your bottled water experience from 1(bad) - 5 (good) [Color]",
     "Have you ever tested or refer any test reports on the quality of the bottled water you consume?",
     "If yes, were you satisfied with the quality of the bottled water?",
     "Have you used piped water for drinking/cooking before?",
     "If yes, what is the incident/ occurrence/ moment that made you change from pipe water to bottled water?",
     "Rate your piped water experience from 1(bad) - 5 (good) [Taste]",
     "Rate your piped water experience from 1(bad) - 5 (good) [Ordure/smell]",
     "Rate your piped water experience from 1(bad) - 5 (good) [Color]",
     "Does your pipe water have special smell/taste?",
     "Does your pipe water have special colour?",
     "Have you ever tested or refer any test reports on the quality of pipe water you consume?",
     "If yes, were you satisfied with the quality of the pipe water?",
     "How often do you clean the water storage at your residency?",
     "If you have options below as drinking water, choose them according to your priority. [1st Choice]",
     "If you have options below as drinking water, choose them according to your priority. [2nd Choice]",
     "If you have options below as drinking water, choose them according to your priority. [3rd Choice]",
     "If you have options below as drinking water, choose them according to your priority. [4th Choice]",
     "If you have options below as drinking water, choose them according to your priority. [5th Choice]",
     "Are you aware of the environmental impact of plastic bottled water?",
     "If you are aware, does this knowledge influence your choices in using bottled water?",
     "Countries like Germany provide daily updates about water quality to their consumers. Do you think there should be more initiatives/promotions like that in Sri Lanka to encourage the use of pipe water over bottled water?",
     "If yes, what are your suggestions",
     "Why do you use pipe water over bottled water, what influences your choice? (Tick all that apply)",
     "How often do you clean the water storage at your residency?.1",
     "Do you treat your pipe water before consumption?",
     "Rate your pipe water experience from 1(bad) - 5 (good) [Taste]",
     "Rate your pipe water experience from 1(bad) - 5 (good) [Ordure/smell]",
     "Rate your pipe water experience from 1(bad) - 5 (good) [Color]",
     "Do you have any unpleasant experience with pipe water?",
     "If yes, explain",
     "Have you ever tested or refer any test reports on the quality of pipe water you consume?.1",
     "If yes, were you satisfied with the quality of the pipe water?.1",
     "Do you have any unpleasant experience with bottled water",
     "If yes, explain.1",
     "Have you ever tested or refer any test reports on the quality of bottled water you consume?",
     "If yes, were you satisfied with the quality of the bottled water?.1",
     "Rate your pipe water experience from 1(bad) - 5 (good) [Taste].1",
     "Rate your pipe water experience from 1(bad) - 5 (good) [Ordure/smell].1",
     "Rate your pipe water experience from 1(bad) - 5 (good) [Color].1",
     "If you have options below as drinking water, choose them according to your priority. [1st Choice].1",
     "If you have options below as drinking water, choose them according to your priority. [2nd Choice].1",
     "If you have options below as drinking water, choose them according to your priority. [3rd Choice].1",
     "If you have options below as drinking water, choose them according to your priority. [4th Choice].1",
     "If you have options below as drinking water, choose them according to your priority. [5th Choice].1",
     "Are you aware of the environmental impact of plastic bottled water?.1",
     "If you are aware, does this knowledge influence your choice in using bottled water?",
     "Countries like Germany provide daily updates about water quality to their consumers. Do you think there should be more initiatives/promotions like that in Sri Lanka to encourage the use of pipe water over bottled water?.1",
     "If yes, what are your suggestions.1",
     "Would you be willing to provide a water sample from your residence if requested for research purposes?",
     "If yes, please mention your contact details (Phone no. or Address)"]

b = [
    "නම",
    "දිස්ත්‍රි‌ක්‌කය",
    "නගරය/ගම",
    "වයස",
    "ස්ත්‍රී/පුරුෂ භාවය",
    "ඉහළම අධ්‍යාපන මට්ටම",
    "මාසික ආදායම",
    "ඔබ ජලය භාවිතා කරන්නේ ජාතික ජල සම්පාදන මණ්ඩලය (NSWDB/Water Board) මගින් සපයන නල ජල සැපයුමකින්ද?",
    "ඔබට නල ජලය ලබාදෙන ජල පවිත්‍රාගාරය පිළිබඳ තොරතුරු ඔබ දන්නවාද?",
    "ඔව් නම් ජල පවිත්‍රාගාරයේ නම පහත සදහන් කරන්න.",
    "ඔබේ නිවසේ බීම සඳහා දෛනිකව භාවිතා කරන්නේ කුමක්ද?",
    "මෙම පරිභෝජනය පුද්ගලික තේරීමක් ද නැතහොත් ඔබේ නිවසේ පොදු පුරුද්දක් ද?",
    "ඔබ නල ජලයට වෙනුවට බෝතල් කළ ජලය භාවිතයට පෙළබීමට මුලික වූ හේතු මොනවාද?  (අදාළ සියල්ල සලකුණු කරන්න)",
    "ඔබේ මාසික බෝතල් කළ ජල පරිභෝජනය ආසන්න වශයෙන් ලීටර් කීයක් (L) ?",
    "ඔබ සාමාන්‍යයෙන් මිලදී ගන්නේ කුමන ප්‍රමාණයේ බෝතල් කළ ජලයද?",
    "ඔබ බෝතල් කළ ජල මිලදී ගන්නා විශේෂිත වූ වෙළෙද නාම/නාමයක් (brand) තිබේද?",
    "ඔව් නම්, එම වෙළඳ නාම/නාමය සඳහන් කරන්න",
    "බෝතල් කළ වතුර වෙළෙද නාමය තෝරාගැනීමේදී ඔබ පරීක්ෂා කරන්නේ කුමන ගුණාංගද?",
    "ඔබේ බෝතල් කළ ජලයේ ගුණාංග සදහා ලකුණක් ලබාදෙන්න. 1 (අප්‍රසන්න) - 5 (ප්‍රසන්න)  [රස]",
    "ඔබේ බෝතල් කළ ජලයේ ගුණාංග සදහා ලකුණක් ලබාදෙන්න. 1 (අප්‍රසන්න) - 5 (ප්‍රසන්න)  [සුවඳ]",
    "ඔබේ බෝතල් කළ ජලයේ ගුණාංග සදහා ලකුණක් ලබාදෙන්න. 1 (අප්‍රසන්න) - 5 (ප්‍රසන්න)  [වර්ණය]",
    "ඔබ පරිභෝජනය කරන බෝතල් කළ ජලයේ ගුණාත්මකභාවය පිළිබඳව ඔබ කවදා හෝ පරීක්‍ෂා කර හෝ පරීක්‍ෂණ වාර්තා අධ්‍යයනය කර තිබේද?",
    "ඔව් නම් බෝතල් කළ ජලයෙහි ගුණාත්මක බව ගැන ඔබ සෑහීමකට පත් වූයේද?",
    "ඔබ මීට පෙර බීමට/ඉවුම් පිහුම් සඳහා නළ ජලය භාවිතා කර තිබේද?",
    "ඔව් නම්, ඔබ නල ජල පානය අතහර බෝතල් කළ ජලය භාවිතය ඇරඹීමට හේතු වූ සිදුවීම/මොහොත කුමක්ද?",
    "ඔබේ නල ජලයේ ගුණාංග සදහා ලකුණක් ලබාදෙන්න. 1 (අප්‍රසන්න) - 5 (ප්‍රසන්න)  [රස]",
    "ඔබේ නල ජලයේ ගුණාංග සදහා ලකුණක් ලබාදෙන්න. 1 (අප්‍රසන්න) - 5 (ප්‍රසන්න)  [සුවඳ]",
    "ඔබේ නල ජලයේ ගුණාංග සදහා ලකුණක් ලබාදෙන්න. 1 (අප්‍රසන්න) - 5 (ප්‍රසන්න)  [වර්ණය]",
    "ඔබේ නල ජලයේ විශේෂ සුවඳක්/රසයක් තිබේද?",
    "ඔබේ නල ජලයට විශේෂ වර්ණයක් තිබේද?",
    "ඔබ පරිභෝජනය කරන නල ජලයේ ගුණාත්මකභාවය පිළිබඳව ඔබ කවදා හෝ පරීක්‍ෂා කර හෝ පරීක්‍ෂණ වාර්තා අධ්‍යයනය කර තිබේද?",
    "ඔව් නම් නල ජලයේ ගුණාත්මක බව ගැන ඔබ සෑහීමකට පත් වූයේද?",
    "ඔබ ඔබේ පදිංචි ස්ථානයේ ජල ටැංකිය කොපමණ වාරයක් පිරිසිදු කරනවාද?",
    "ඔබට පානීය ජලය ලෙස පහත විකල්ප තිබේ නම්, ඔබේ ප්‍රමුඛතාවය අනුව ඒවා තෝරන්න. [පලමු තේරීම]",
    "ඔබට පානීය ජලය ලෙස පහත විකල්ප තිබේ නම්, ඔබේ ප්‍රමුඛතාවය අනුව ඒවා තෝරන්න. [දෙවන තේරීම]",
    "ඔබට පානීය ජලය ලෙස පහත විකල්ප තිබේ නම්, ඔබේ ප්‍රමුඛතාවය අනුව ඒවා තෝරන්න. [තෙවන තේරීම]",
    "ඔබට පානීය ජලය ලෙස පහත විකල්ප තිබේ නම්, ඔබේ ප්‍රමුඛතාවය අනුව ඒවා තෝරන්න. [සිව්වන තේරීම]",
    "ඔබට පානීය ජලය ලෙස පහත විකල්ප තිබේ නම්, ඔබේ ප්‍රමුඛතාවය අනුව ඒවා තෝරන්න. [පස්වන තේරීම]",
    "ප්ලාස්ටික් බෝතල් භාවිතය නිසා ඇති වන පාරිසරික බලපෑම ගැන ඔබ දැනුවත්ද?",
    "දැනුවත් නම්, ඔබ බෝතල් කළ ජලය තේරීමට මෙම දැනුම බලපානවාද?",
    "ජර්මනිය වැනි රටවල් තම පාරිභෝගිකයින්ට සපයන නල ජලයේ ගුණාත්මකභාවය පිළිබඳ දිනපතා තොරතුරු(updates) සපයයි.  බෝතල් කළ ජලයට වඩා නළ ජලය භාවිතය දිරිමත් කිරීම සඳහා ශ්‍රී ලංකාව තුළ තවත් එවැනි මුල පිරීම් / ප්‍රවර්ධන තිබිය යුතු යැයි ඔබ සිතනවාද?",
    "ඔව් නම්, ඔබේ යෝජනා මොනවාද",
    "ඔබ බෝතල් කළ ජලය වෙනුවට නල ජලය භාවිතයට පෙළබීමට මුලික වූ හේතු මොනවාද?  (අදාළ සියල්ල සලකුණු කරන්න)",
    "ඔබ ඔබේ පදිංචි ස්ථානයේ ජල ටැංකිය කොපමණ වාරයක් පිරිසිදු කරනවාද?.1",
    "ඔබ ඔබේ නල ජලය පරිභෝජනයට පෙර පිරියම් කරනවාද?",
    "ඔබේ නල ජලයේ ගුණාංග සදහා ලකුණක් ලබාදෙන්න. 1 (අප්‍රසන්න) - 5 (ප්‍රසන්න)  [රස].1",
    "ඔබේ නල ජලයේ ගුණාංග සදහා ලකුණක් ලබාදෙන්න. 1 (අප්‍රසන්න) - 5 (ප්‍රසන්න)  [සුවඳ].1",
    "ඔබේ නල ජලයේ ගුණාංග සදහා ලකුණක් ලබාදෙන්න. 1 (අප්‍රසන්න) - 5 (ප්‍රසන්න)  [වර්ණය].1",
    "නල ජලය භාවිතයේදී ඔබ මුහුණ දුන් අමිහිරි අත්දැකීමක් තිබේද?",
    "තිබේ නම්, එය පහත සඳහන් කරන්න",
    "ඔබ පරිභෝජනය කරන නල ජලයේ ගුණාත්මකභාවය පිළිබඳව ඔබ කවදා හෝ පරීක්‍ෂා කර හෝ පරීක්‍ෂණ වාර්තා අධ්‍යයනය කර තිබේද?.1",
    "ඔව් නම් නල ජලයේ ගුණාත්මක බව ගැන ඔබ සෑහීමකට පත් වූයේද?.1",
    "බෝතල් කළ ජලය භාවිතයේදී ඔබ මුහුණ දුන් අමිහිරි අත්දැකීමක් තිබේද?",
    "තිබේ නම්, එය පහත සඳහන් කරන්න.1",
    "බෝතල් කළ ජලයේ ගුණාත්මකභාවය පිළිබඳව ඔබ කවදා හෝ පරීක්‍ෂා කර හෝ පරීක්‍ෂණ වාර්තා අධ්‍යයනය කර තිබේද?",
    "ඔව් නම් බෝතල් කළ ජලයෙහි ගුණාත්මක බව ගැන ඔබ සෑහීමකට පත් වූයේද?.1",
    "ඔබ භාවිතා කල බෝතල් කළ ජලයේ ගුණාංග සදහා ලකුණක් ලබාදෙන්න. 1 (අප්‍රසන්න) - 5 (ප්‍රසන්න)  [රස]",
    "ඔබ භාවිතා කල බෝතල් කළ ජලයේ ගුණාංග සදහා ලකුණක් ලබාදෙන්න. 1 (අප්‍රසන්න) - 5 (ප්‍රසන්න)  [සුවඳ]",
    "ඔබ භාවිතා කල බෝතල් කළ ජලයේ ගුණාංග සදහා ලකුණක් ලබාදෙන්න. 1 (අප්‍රසන්න) - 5 (ප්‍රසන්න)  [වර්ණය]",
    "ඔබට පානීය ජලය ලෙස පහත විකල්ප තිබේ නම්, ඔබේ ප්‍රමුඛතාවය අනුව ඒවා තෝරන්න. [පලමු තේරීම].1",
    "ඔබට පානීය ජලය ලෙස පහත විකල්ප තිබේ නම්, ඔබේ ප්‍රමුඛතාවය අනුව ඒවා තෝරන්න. [දෙවන තේරීම].1",
    "ඔබට පානීය ජලය ලෙස පහත විකල්ප තිබේ නම්, ඔබේ ප්‍රමුඛතාවය අනුව ඒවා තෝරන්න. [තෙවන තේරීම].1",
    "ඔබට පානීය ජලය ලෙස පහත විකල්ප තිබේ නම්, ඔබේ ප්‍රමුඛතාවය අනුව ඒවා තෝරන්න. [සිව්වන තේරීම].1",
    "ඔබට පානීය ජලය ලෙස පහත විකල්ප තිබේ නම්, ඔබේ ප්‍රමුඛතාවය අනුව ඒවා තෝරන්න. [පස්වන තේරීම].1",
    "ප්ලාස්ටික් බෝතල් භාවිතය නිසා ඇති වන පාරිසරික බලපෑම ගැන ඔබ දැනුවත්ද?.1",
    "දැනුවත් නම්, ඔබ නල ජලය තේරීමට මෙම දැනුම බලපානවාද?",
    "ජර්මනිය වැනි රටවල් තම පාරිභෝගිකයින්ට සපයන නල ජලයේ ගුණාත්මකභාවය පිළිබඳ දිනපතා තොරතුරු(updates) සපයයි.  බෝතල් කළ ජලයට වඩා නළ ජලය භාවිතය දිරිමත් කිරීම සඳහා ශ්‍රී ලංකාව තුළ තවත් එවැනි මුල පිරීම් / ප්‍රවර්ධන තිබිය යුතු යැයි ඔබ සිතනවාද?.1",
    "ඔව් නම්, ඔබේ යෝජනා මොනවාද.1",
    "පර්යේෂණ කටයුතු සඳහා ඉල්ලුම් කළහොත් ඔබේ නිවසින් ජල සාම්පලයක් ලබා දීමට ඔබ කැමතිද?",
    "ඔව් නම්, කරුණාකර ඔබගේ සම්බන්ධතා තොරතුරු සඳහන් කරන්න (දුරකථන අංකය හෝ ලිපිනය)"]

print(len(a))
print(len(b))
column_mapping = dict(zip(a, b))

# keep only the columns that are in the a and b in the dataframe
all_columns = a + b
filtered_df = df[[col for col in df.columns if col in all_columns]]

# Now, we'll rename the Sinhala columns to their English counterparts using our mapping
# Only do this for columns that actually exist in the DataFrame
filtered_df.rename(columns={col: column_mapping[col] for col in filtered_df.columns if col in column_mapping}, inplace=True)

# Saving the cleaned DataFrame to a new CSV
filtered_df.to_csv('cleaned_data.csv', index=False)

# Verifying the changes
print(filtered_df.head())

exit()
# create mappping with using a and b
column_mapping = dict(zip(a, b))
print(column_mapping)

# check if columns in the a and b are in the dataframe
for i in a:
    if i not in df.columns:
        print(i, "is not in the dataframe")

new_df = pd.DataFrame()

new_df['Timestamp'] = df['Timestamp']
new_df['Choose your language'] = df['Choose your language']

# Apply column mapping and copy direct columns
for english_column, non_english_column in column_mapping.items():
    if english_column in df.columns:
        new_df[english_column] = df[english_column]
    elif non_english_column in df.columns:
        new_df[english_column] = df[non_english_column]

# For columns that don't need mapping and are direct copy
# Example: new_df['Timestamp'] = your_original_df['Timestamp']

# Handle duplicates and missing data if necessary
new_df.drop_duplicates(inplace=True)
# new_df.fillna('Some value or method', inplace=True)

# Verify the final DataFrame
print(new_df.head())
print(new_df.dtypes)

# save the new dataframe
new_df.to_csv('new_df.csv', index=False)
