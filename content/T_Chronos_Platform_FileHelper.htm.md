# FileHelper - класс
Вспомогательные методы для взаимодействия с файлами.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static class FileHelper
VB __Копировать
     Public NotInheritable Class FileHelper
C++ __Копировать
     public ref class FileHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type FileHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FileHelper
##  __Методы
[DeleteFileSafe](M_Chronos_Platform_FileHelper_DeleteFileSafe.htm)|  Удаляет
файл по заданному пути. Возвращает признак того, что файл был успешно удалён
или не существовал. Не выбрасывает исключений. Не удаляет папку, в которой
находился файл, даже если в папке других файлов не было.  
---|---  
[DeleteOldFiles](M_Chronos_Platform_FileHelper_DeleteOldFiles.htm)|  Очищает
папку с файлами, которые были созданы более суток назад с использованием
методов API и хранятся во временной папке пользователя. Не выбрасывает
исключений, если папку не удалось удалить.  
[GetPath](M_Chronos_Platform_FileHelper_GetPath.htm)|  Возвращает полный путь
к заданной специальной папке.  
[ReleaseFilePath](M_Chronos_Platform_FileHelper_ReleaseFilePath.htm)|  Удаляет
временный файл по заданному пути. Возвращает признак того, что файл был
успешно удалён или не существовал. Не выбрасывает исключений.  
[RemoveInvalidFileNameChars](M_Chronos_Platform_FileHelper_RemoveInvalidFileNameChars.htm)|
Возвращает имя файла, в котором удалены все некорректные для имени файла
символы. При этом удаляются начальные и конечные пробелы.  
## __Поля
[DefaultStreamingBufferSize](F_Chronos_Platform_FileHelper_DefaultStreamingBufferSize.htm)|
Размер буфера по умолчанию для операция с потоками
[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream).  
---|---  
[InvalidCharReplacement](F_Chronos_Platform_FileHelper_InvalidCharReplacement.htm)|
Рекомендуемая строка для замены невалидных символов в имени файла. Используйте
эту строку, когда требуется не просто удалить такие символы, а заменить их,
чтобы при использовании имени файлов, состоящего целиком из невалидных
символов, не было ошибок.  
## __См. также
#### Ссылки
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
