# FileConverterAggregateWorker.IsRegistered - метод
Возвращает признак того, что для заданного формата выходного файла был
зарегистрирован объект, выполняющий преобразование в этот формат.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool IsRegistered(
    	FileConverterFormat outputFormat
    )
VB __Копировать
     Public Function IsRegistered ( 
    	outputFormat As FileConverterFormat
    ) As Boolean
C++ __Копировать
     public:
    virtual bool IsRegistered(
    	FileConverterFormat outputFormat
    ) sealed
F# __Копировать
     abstract IsRegistered : 
            outputFormat : FileConverterFormat -> bool 
    override IsRegistered : 
            outputFormat : FileConverterFormat -> bool 
#### Параметры
outputFormat
[FileConverterFormat](T_Tessa_FileConverters_FileConverterFormat.htm)
    Формат выходного файла, для которого требуется проверить наличие регистрации.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если для заданного формата выходного файла был зарегистрирован объект,
выполняющий преобразование в этот формат; false в противном случае.
#### Реализации
[IFileConverterAggregateWorker.IsRegistered(FileConverterFormat)](M_Tessa_FileConverters_IFileConverterAggregateWorker_IsRegistered.htm)  
##  __См. также
#### Ссылки
[FileConverterAggregateWorker -
](T_Tessa_FileConverters_FileConverterAggregateWorker.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
