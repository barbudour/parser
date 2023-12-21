# FileHelper.ReleaseFilePath - метод
Удаляет временный файл по заданному пути. Возвращает признак того, что файл
был успешно удалён или не существовал. Не выбрасывает исключений.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool ReleaseFilePath(
    	string filePath,
    	bool keepFolder,
    	out Exception exception
    )
VB __Копировать
     Public Shared Function ReleaseFilePath ( 
    	filePath As String,
    	keepFolder As Boolean,
    	<OutAttribute> ByRef exception As Exception
    ) As Boolean
C++ __Копировать
     public:
    static bool ReleaseFilePath(
    	String^ filePath, 
    	bool keepFolder, 
    	[OutAttribute] Exception^% exception
    )
F# __Копировать
     static member ReleaseFilePath : 
            filePath : string * 
            keepFolder : bool * 
            exception : Exception byref -> bool 
#### Параметры
filePath [String](https://learn.microsoft.com/dotnet/api/system.string)
     Полный путь к файлу, который требуется удалить. Путь должен содержать только корректные символы для файловой системы. 
keepFolder [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Признак того, что не требуется удалять папку, в которой был расположен временный файл.
exception [Exception](https://learn.microsoft.com/dotnet/api/system.exception)
     Исключение, возникшее при удалении файла, или null, если удаление успешно выполнено. 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если файл по заданному пути был успешно удалён или не существовал;
false, если при удалении возникла ошибка, например, файл был заблокирован
другим приложением.
## __См. также
#### Ссылки
[FileHelper - ](T_Chronos_Platform_FileHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
