


countries = ['Argentina', 'Somalia', 'Tuvalu', 'Malta', 'Armenia', 'Christmas Island', 'Uganda',
             'Central African Republic', 'Gambia', 'Morocco', 'Sint Maarten (Dutch part)', 'Tunisia', 'Aland Islands',
             'Angola', 'Yemen', 'Niue', 'Brunei Darussalam', 'Sudan', 'Holy See (Vatican City State)', 'Malaysia',
             'New Zealand', 'Palestinian Territory, Occupied', 'Iran, Islamic Republic of', 'Macedonia, Republic of',
             'Montenegro', 'Macao', 'Belarus', 'Netherlands', 'Greenland', 'Thailand', 'French Southern Territories',
             'Cyprus', "Korea, Democratic People's Republic of", 'Rwanda', 'Ethiopia', 'Saint Barthélemy', 'Botswana',
             'Puerto Rico', 'Cape Verde', 'Nicaragua', 'Croatia', 'Guadeloupe', 'Réunion', 'Belize',
             'Northern Mariana Islands', 'Indonesia', 'Serbia', 'British Indian Ocean Territory', 'Wallis and Futuna',
             'Saint Martin (French part)', 'Nigeria', 'Spain', 'Guernsey', 'Guyana', 'Namibia',
             'Venezuela, Bolivarian Republic of', 'Pitcairn', 'Suriname', 'Switzerland', 'Portugal', 'Saudi Arabia',
             'Tanzania, United Republic of', 'Norfolk Island', 'Iceland', 'Ukraine', 'Estonia', 'Nauru', 'Comoros',
             'Andorra', 'Turks and Caicos Islands', 'Guatemala', 'Cameroon', 'Chile', 'Bulgaria', 'Afghanistan',
             'Sri Lanka', 'Romania', 'Tokelau', 'Montserrat', 'Congo', 'Congo, The Democratic Republic of the',
             'Luxembourg', 'Bolivia, Plurinational State of', 'South Georgia and the South Sandwich Islands',
             'Djibouti', 'Brazil', 'Burkina Faso', 'Curaçao', 'Heard Island and McDonald Islands', 'Cook Islands',
             'Cocos (Keeling) Islands', 'China', 'Haiti', 'Swaziland', 'Mali', 'Burundi', 'Taiwan, Province of China',
             'Ireland', 'Maldives', 'France', 'Martinique', 'Nepal', 'Saint Lucia', 'Uruguay', 'Seychelles', 'Algeria',
             'Panama', 'Anguilla', 'Cuba', 'San Marino', 'Dominica', 'Germany', 'Iraq', 'Chad', 'Tonga', 'Qatar',
             'Lesotho', 'Liberia', 'Bosnia and Herzegovina', 'Canada', 'Turkey', 'French Guiana', 'Jersey', 'Niger',
             'Paraguay', 'Bangladesh', 'Barbados', 'Mauritius', 'United Kingdom', 'Bhutan', 'Isle of Man',
             'Svalbard and Jan Mayen', 'Falkland Islands (Malvinas)', "Lao People's Democratic Republic",
             'Saint Vincent and the Grenadines', 'Korea, Republic of', 'Dominican Republic', 'Philippines',
             'Austria', 'Samoa', 'South Africa', 'Australia', 'Bahamas', 'Fiji', 'Mayotte', 'Albania',
             'Sierra Leone', 'Gibraltar', 'Kazakhstan', 'French Polynesia', 'Jordan', 'Ecuador', 'Liechtenstein',
             'Solomon Islands', 'Belgium', 'Gabon', 'Bermuda', 'Georgia', 'Saint Pierre and Miquelon', 'Ghana',
             'Guinea', 'Singapore', 'Vanuatu', 'New Caledonia', 'Sao Tome and Principe', 'Mexico', 'Equatorial Guinea',
             'Pakistan', 'Marshall Islands', 'Jamaica', 'Antigua and Barbuda', 'South Sudan', 'Japan', 'Slovenia',
             'Moldova, Republic of', 'Virgin Islands, British', 'Latvia', 'Kenya', 'Trinidad and Tobago', 'Norway',
             'Timor-Leste', 'Faroe Islands', 'Zimbabwe', 'Kuwait', 'Mozambique', 'Mauritania', 'Benin', 'Togo',
             'Sweden', 'Cayman Islands', 'Mongolia', 'United States', 'United States Minor Outlying Islands',
             'Papua New Guinea', 'Hong Kong', 'Myanmar', 'Viet Nam', 'Malawi', 'Micronesia, Federated States of',
             'Aruba', 'Virgin Islands, U.S.', 'Saint Helena, Ascension and Tristan da Cunha', 'Oman',
             'Bonaire, Sint Eustatius and Saba', 'Senegal', 'Monaco', 'Russian Federation', 'Antarctica',
             'American Samoa', 'Slovakia', 'Guinea-Bissau', 'Egypt', 'Madagascar', 'Guam', 'United Arab Emirates',
             'Kiribati', 'Israel', 'Eritrea', 'Saint Kitts and Nevis', 'El Salvador', 'Lebanon', 'Poland',
             'Syrian Arab Republic', 'Cambodia', 'Czech Republic', 'Tajikistan', 'India', 'Denmark', "Côte d'Ivoire",
             'Kyrgyzstan', 'Peru', 'Italy', 'Bouvet Island', 'Palau', 'Lithuania', 'Colombia', 'Turkmenistan', 'Zambia',
             'Libya', 'Greece', 'Honduras', 'Azerbaijan', 'Costa Rica', 'Uzbekistan', 'Hungary',
             'Grenada', 'Bahrain', 'Finland']

sorted_countries = sorted(countries)
print(sorted_countries)
oneword_country = list()
twoword_country = list()
threeword_country = list()
fourword_country = list()
aboveword_country = list()
for x in sorted_countries:
    if len(x) <= 1:
        oneword_country.append(x)
    elif len(x) <= 2:
        twoword_country.append(x)
    elif len(x) <= 3:
        threeword_country.append(x)
    elif len(x) <= 4:
        fourword_country.append(x)
    else:
        aboveword_country.append(x)
print("#"*20 + "result"+20*"#")
print(fourword_country)

length = [len(c) for c in countries]
print(length)
maxlength = max(length)
minlength = min(length)

# find the largerst country

largests_country = [c for c in countries if len(c)==maxlength]
print(f'largest country is {largests_country}')

# find the smallerst country
smallerst_country = [c for c in countries if len(c)==minlength]
print(f'smallest country is{smallerst_country}')
        
    
