# FileConverterFormat.GetRecommendedInputFormats - метод
Возвращает список рекомендуемых поддерживаемых форматов, из которых может быть
выполнена конвертация в заданный формат.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static string[] GetRecommendedInputFormats(
    	FileConverterFormat outputFormat
    )
VB __Копировать
     Public Shared Function GetRecommendedInputFormats ( 
    	outputFormat As FileConverterFormat
    ) As String()
C++ __Копировать
     public:
    static array<String^>^ GetRecommendedInputFormats(
    	FileConverterFormat outputFormat
    )
F# __Копировать
     static member GetRecommendedInputFormats : 
            outputFormat : FileConverterFormat -> string[] 
#### Параметры
outputFormat
[FileConverterFormat](T_Tessa_FileConverters_FileConverterFormat.htm)
    Формат выходного (результирующего) файла.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)[]  
Список рекомендуемых поддерживаемых форматов, из которых может быть выполнена
конвертация в заданный формат.
##  __См. также
#### Ссылки
[FileConverterFormat - ](T_Tessa_FileConverters_FileConverterFormat.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
