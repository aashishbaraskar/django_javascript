def UserProfileToJSON(user):
    user_data = {}
    user_data['first_name'] = user.first_name
    user_data['last_name'] = user.last_name
    user_data['email'] = user.email
    user_data['pan_card'] = user.pan_card
    user_data['primary_contact'] = user.primary_contact
    user_data['alternate_contact'] = user.alternate_contact
    user_data['address'] = user.address
    user_data['city'] = user.city
    user_data['town'] = user.town
    user_data['pincode'] = user.pincode
    user_data['landmark'] = user.landmark
    user_data['state'] = user.state
    user_data['beneficiary_name'] = user.beneficiary_name
    user_data['account_no'] = user.account_no
    user_data['ifsc_code'] = user.ifsc_code
    user_data['bank_name'] = user.bank_name

    return user_data
