# FileHelper.DeleteOldFiles - метод
Очищает папку с файлами, которые были созданы более суток назад с
использованием методов API и хранятся во временной папке пользователя. Не
выбрасывает исключений, если папку не удалось удалить.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static void DeleteOldFiles(
    	FileSpecialFolder folder
    )
VB __Копировать
     Public Shared Sub DeleteOldFiles ( 
    	folder As FileSpecialFolder
    )
C++ __Копировать
     public:
    static void DeleteOldFiles(
    	FileSpecialFolder folder
    )
F# __Копировать
     static member DeleteOldFiles : 
            folder : FileSpecialFolder -> unit 
#### Параметры
folder [FileSpecialFolder](T_Chronos_Platform_FileSpecialFolder.htm)
    Тип специальной папки, используемой в системе.
##  __Заметки
Рекомендуется вызывать метод в такой момент, когда приложение не использует
никакие временные файлы.
## __См. также
#### Ссылки
[FileHelper - ](T_Chronos_Platform_FileHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
