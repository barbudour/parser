# FileConverterFormat.IsSupportedConversion - метод
Возвращает признак того, что конвертация допустима для заданных форматов.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool IsSupportedConversion(
    	FileConverterFormat outputFormat,
    	string inputFormat
    )
VB __Копировать
     Public Shared Function IsSupportedConversion ( 
    	outputFormat As FileConverterFormat,
    	inputFormat As String
    ) As Boolean
C++ __Копировать
     public:
    static bool IsSupportedConversion(
    	FileConverterFormat outputFormat, 
    	String^ inputFormat
    )
F# __Копировать
     static member IsSupportedConversion : 
            outputFormat : FileConverterFormat * 
            inputFormat : string -> bool 
#### Параметры
outputFormat
[FileConverterFormat](T_Tessa_FileConverters_FileConverterFormat.htm)
    Формат выходного (результирующего) файла.
inputFormat [String](https://learn.microsoft.com/dotnet/api/system.string)
    Формат входного файла, для которого требуется выполнить конвертацию.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если конвертация допустима для заданных форматов; false в противном
случае.
## __См. также
#### Ссылки
[FileConverterFormat - ](T_Tessa_FileConverters_FileConverterFormat.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
