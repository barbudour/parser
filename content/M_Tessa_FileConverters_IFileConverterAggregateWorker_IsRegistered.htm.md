# IFileConverterAggregateWorker.IsRegistered - метод
Возвращает признак того, что для заданного формата выходного файла был
зарегистрирован объект, выполняющий преобразование в этот формат.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     bool IsRegistered(
    	FileConverterFormat outputFormat
    )
VB __Копировать
     Function IsRegistered ( 
    	outputFormat As FileConverterFormat
    ) As Boolean
C++ __Копировать
     bool IsRegistered(
    	FileConverterFormat outputFormat
    )
F# __Копировать
     abstract IsRegistered : 
            outputFormat : FileConverterFormat -> bool 
#### Параметры
outputFormat
[FileConverterFormat](T_Tessa_FileConverters_FileConverterFormat.htm)
    Формат выходного файла, для которого требуется проверить наличие регистрации.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если для заданного формата выходного файла был зарегистрирован объект,
выполняющий преобразование в этот формат; false в противном случае.
## __См. также
#### Ссылки
[IFileConverterAggregateWorker -
](T_Tessa_FileConverters_IFileConverterAggregateWorker.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
