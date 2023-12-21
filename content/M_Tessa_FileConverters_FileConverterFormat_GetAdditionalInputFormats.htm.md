# FileConverterFormat.GetAdditionalInputFormats - метод
Возвращает дополнительные поддерживаемые типы файлов для конвертации, из
которых может быть выполнена конвертация в заданный формат. Не рекомендуется
выполнять конвертацию с использованием этого формата, но конвертация возможна,
если возникла необходимость.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static string[] GetAdditionalInputFormats(
    	FileConverterFormat outputFormat
    )
VB __Копировать
     Public Shared Function GetAdditionalInputFormats ( 
    	outputFormat As FileConverterFormat
    ) As String()
C++ __Копировать
     public:
    static array<String^>^ GetAdditionalInputFormats(
    	FileConverterFormat outputFormat
    )
F# __Копировать
     static member GetAdditionalInputFormats : 
            outputFormat : FileConverterFormat -> string[] 
#### Параметры
outputFormat
[FileConverterFormat](T_Tessa_FileConverters_FileConverterFormat.htm)
    Формат выходного (результирующего) файла.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)[]  
Список дополнительных поддерживаемых форматов, из которых может быть выполнена
конвертация в заданный формат.
##  __См. также
#### Ссылки
[FileConverterFormat - ](T_Tessa_FileConverters_FileConverterFormat.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
