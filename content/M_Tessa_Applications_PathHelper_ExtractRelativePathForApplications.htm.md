# PathHelper.ExtractRelativePathForApplications - метод
Извлекает путь из filePath относительно rootPath
##  __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static string ExtractRelativePathForApplications(
    	string rootPath,
    	string filePath
    )
VB __Копировать
     Public Shared Function ExtractRelativePathForApplications ( 
    	rootPath As String,
    	filePath As String
    ) As String
C++ __Копировать
     public:
    static String^ ExtractRelativePathForApplications(
    	String^ rootPath, 
    	String^ filePath
    )
F# __Копировать
     static member ExtractRelativePathForApplications : 
            rootPath : string * 
            filePath : string -> string 
#### Параметры
rootPath [String](https://learn.microsoft.com/dotnet/api/system.string)
    Путь к корневому каталогу.
filePath [String](https://learn.microsoft.com/dotnet/api/system.string)
    Полный путь к файлу.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Путь к файлу относительно каталога rootPath.
## __Исключения
[InvalidOperationException](https://learn.microsoft.com/dotnet/api/system.invalidoperationexception)|
Файл filePath не расположен в папке rootPath.  
---|---  
## __См. также
#### Ссылки
[PathHelper - ](T_Tessa_Applications_PathHelper.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
