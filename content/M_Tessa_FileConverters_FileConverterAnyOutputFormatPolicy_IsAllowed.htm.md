# FileConverterAnyOutputFormatPolicy.IsAllowed - метод
Возвращает признак того, что выполнение методов расширения допустимо для
заданного выходного формата по конвертации файлов.
##  __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool IsAllowed(
    	FileConverterFormat outputFormat
    )
VB __Копировать
     Public Function IsAllowed ( 
    	outputFormat As FileConverterFormat
    ) As Boolean
C++ __Копировать
     public:
    virtual bool IsAllowed(
    	FileConverterFormat outputFormat
    ) sealed
F# __Копировать
     abstract IsAllowed : 
            outputFormat : FileConverterFormat -> bool 
    override IsAllowed : 
            outputFormat : FileConverterFormat -> bool 
#### Параметры
outputFormat
[FileConverterFormat](T_Tessa_FileConverters_FileConverterFormat.htm)
    Проверяемый выходной формат.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если выполнение методов расширения допустимо для заданного выходного
формата по конвертации файлов; false в противном случае.
#### Реализации
[IFileConverterOutputFormatPolicy.IsAllowed(FileConverterFormat)](M_Tessa_FileConverters_IFileConverterOutputFormatPolicy_IsAllowed.htm)  
##  __См. также
#### Ссылки
[FileConverterAnyOutputFormatPolicy -
](T_Tessa_FileConverters_FileConverterAnyOutputFormatPolicy.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
