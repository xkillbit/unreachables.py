#! /usr/bin/python3

print("Unreachable hosts:")
unreachables = []
with open('all_given_ips.txt','r') as f:
    full_list = f.readlines()
    print("FULL LIST: {}".format(full_list))
    with open('all_up.txt','r') as upfile:
        up_list = upfile.readlines()
        print("UPHOSTS LIST: {} ".format(up_list))
        for ip in full_list:
            if ip not in up_list:
                unreachables.append(ip)
        print("FULL LIST: {}".format(full_list))
        print("UPHOSTS LIST: {} ".format(up_list))
        print("FULL LIST: {}".format(len(full_list)))
        print("UP HOSTS: {}".format(len(up_list)))
        print("DIFFERENCE: {}".format(len(full_list)-len(up_list)))
        print("UNREACHABLES: {}".format(unreachables))
