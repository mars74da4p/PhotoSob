from pathlib import Path
import zipfile

IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.bmp', '.webp', '.tiff', '.heic'}

def collect_and_archive_photos(output_zip_path, start_path='C:/'):
    """
    Сканирует файловую систему, начиная с start_path, и упаковывает все фото в ZIP-архив.
    """
    start_dir = Path(start_path)
    archive_path = Path(output_zip_path)
    
    print(f"Начинаем сканирование директории: {start_dir}")
    
    # Открываем архив для записи
    with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        count = 0
        
        for file_path in start_dir.rglob('*'):
            try:
    
                if file_path.is_file() and file_path.suffix.lower() in IMAGE_EXTENSIONS:
                    arcname = f"{file_path.parents.name}_{file_path.name}"
                    zipf.write(file_path, arcname=arcname)
                    count += 1
                    print(f"Добавлено [{count}]: {file_path}")
            except PermissionError:
                continue
            except Exception as e:
                continue
                
    print(f"\nГотово! Архив создан: {archive_path.resolve()}")
    print(f"Всего найдено и упаковано фоток: {count}")

if __name__ == "__main__":
    OUTPUT_ZIP = "all_my_photos.zip"
    START_DIRECTORY = "C:/"  
    
    collect_and_archive_photos(OUTPUT_ZIP, START_DIRECTORY)