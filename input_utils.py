def get_range() -> tuple[int,int]:
    while True:
        try:
            diapason: str = input(
                'Введите через "-" диапазон сканирования (например, 1-1024. Максимальное число - 65535): '
            )

            start_range: int
            end_range: int
            start_range,end_range = map(int,diapason.split('-'))
            
            if not (1 <= start_range <= 65535 and 1 <= end_range <= 65535):
                print("Порты не находятся в диапазоне от 1 до 65535.")
                continue

            if start_range > end_range:
                print("Начальный порт не может быть больше конечного.")
                continue
            return start_range, end_range

            break
            
        except ValueError:
            print(
                "пожалуйста введите корректный диапазон (пример: 1-1024. Максимальное число - 65535)."
            )
