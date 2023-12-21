# FileHelper.RemoveInvalidFileNameChars - метод
Возвращает имя файла, в котором удалены все некорректные для имени файла
символы. При этом удаляются начальные и конечные пробелы.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static string RemoveInvalidFileNameChars(
    	string fileName,
    	string replacement = null
    )
VB __Копировать
     Public Shared Function RemoveInvalidFileNameChars ( 
    	fileName As String,
    	Optional replacement As String = Nothing
    ) As String
C++ __Копировать
     public:
    static String^ RemoveInvalidFileNameChars(
    	String^ fileName, 
    	String^ replacement = nullptr
    )
F# __Копировать
     static member RemoveInvalidFileNameChars : 
            fileName : string * 
            ?replacement : string 
    (* Defaults:
            let _replacement = defaultArg replacement null
    *)
    -> string 
#### Параметры
fileName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя файла, в котором могут содержаться некорректные символы.
replacement [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
     Строка, на которую заменяется каждый из некорректных символов. По умолчанию пустая строка. Используйте [InvalidCharReplacement](F_Chronos_Platform_FileHelper_InvalidCharReplacement.htm), чтобы подставить рекомендуемый символ-заменитель. 
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Имя файла, в котором удалены все некорректные для имени файла символы.
##  __См. также
#### Ссылки
[FileHelper - ](T_Chronos_Platform_FileHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
