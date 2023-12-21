# FileHelper.DeleteFileSafe - метод
Удаляет файл по заданному пути. Возвращает признак того, что файл был успешно
удалён или не существовал. Не выбрасывает исключений. Не удаляет папку, в
которой находился файл, даже если в папке других файлов не было.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool DeleteFileSafe(
    	string filePath
    )
VB __Копировать
     Public Shared Function DeleteFileSafe ( 
    	filePath As String
    ) As Boolean
C++ __Копировать
     public:
    static bool DeleteFileSafe(
    	String^ filePath
    )
F# __Копировать
     static member DeleteFileSafe : 
            filePath : string -> bool 
#### Параметры
filePath [String](https://learn.microsoft.com/dotnet/api/system.string)
    Полный путь к файлу, который требуется удалить.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если файл по заданному пути был успешно удалён или не существовал;
false, если при удалении возникла ошибка, например, файл был заблокирован
другим приложением.
## __См. также
#### Ссылки
[FileHelper - ](T_Chronos_Platform_FileHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
