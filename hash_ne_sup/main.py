from hash_function.meow import custom_hash

def main():
    message = input("Введите сообщение: ").encode('utf-8')
    hash_result = custom_hash(message)
    print("Хэш (в 16-ричном виде):", hash_result.hex())

if __name__ == "__main__":
    main()
