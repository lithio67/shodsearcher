import shodan
import sys

def main(ip, service):
    API_KEY = "W0YwkW5HVTr06IrgygGVO3pUKg0tvTYt"
    api = shodan.Shodan(API_KEY)

    try:

        query = 'ip:{} {}'.format(ip, service)  
        results = api.search(query)  

        print('Results for IP ', ip, ' and with ', service, ' running:\n')
        for result in results['matches']:
            print("IP: {}".format(result['ip_str']))
            print("Port: {}".format(result['port']))
            print("Service: {}".format(result.get('product', 'Unknown')))
            print("Location: {}".format(result.get('location', {}).get('city', 'Unknown')))
            print("-" * 50)

    except shodan.APIError as e:
        print('Error: {}'.format(e))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python shodsearcher.py [IP] [service]")
        sys.exit(1)

    ip = sys.argv[1]
    service = sys.argv[2]
    main(ip, service)
