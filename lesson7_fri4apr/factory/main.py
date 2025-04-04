import concrete as ct

def main():
    caffe = ct.Product("caffe lavazza", 13, 3)
    print(caffe.calculate_profit())
    factory = ct.Factory(5)
    
    
if __name__ == "__main__":
    main()