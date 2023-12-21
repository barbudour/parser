# FileConverterAggregateWorker.Register - метод
Регистрирует объект, ответственный за преобразование файла заданного формата.
##  __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IFileConverterAggregateWorker Register(
    	FileConverterFormat outputFormat,
    	Func<IFileConverterWorker> resolveWorkerFunc
    )
VB __Копировать
     Public Function Register ( 
    	outputFormat As FileConverterFormat,
    	resolveWorkerFunc As Func(Of IFileConverterWorker)
    ) As IFileConverterAggregateWorker
C++ __Копировать
     public:
    virtual IFileConverterAggregateWorker^ Register(
    	FileConverterFormat outputFormat, 
    	Func<IFileConverterWorker^>^ resolveWorkerFunc
    ) sealed
F# __Копировать
     abstract Register : 
            outputFormat : FileConverterFormat * 
            resolveWorkerFunc : Func<IFileConverterWorker> -> IFileConverterAggregateWorker 
    override Register : 
            outputFormat : FileConverterFormat * 
            resolveWorkerFunc : Func<IFileConverterWorker> -> IFileConverterAggregateWorker 
#### Параметры
outputFormat
[FileConverterFormat](T_Tessa_FileConverters_FileConverterFormat.htm)
     Формат выходного файла, для которого выполняется регистрация. Если для этого объекта уже была выполнена регистрация, то она заменяется. 
resolveWorkerFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[IFileConverterWorker](T_Tessa_FileConverters_IFileConverterWorker.htm)>
     Функция, которая получает или создаёт объект. Функция будет использована один раз, в дальнейшем экземпляр объекта будет повторно использоваться. 
#### Возвращаемое значение
[IFileConverterAggregateWorker](T_Tessa_FileConverters_IFileConverterAggregateWorker.htm)  
Текущий объект для цепочки вызовов.
#### Реализации
[IFileConverterAggregateWorker.Register(FileConverterFormat,
Func<IFileConverterWorker>)](M_Tessa_FileConverters_IFileConverterAggregateWorker_Register.htm)  
##  __См. также
#### Ссылки
[FileConverterAggregateWorker -
](T_Tessa_FileConverters_FileConverterAggregateWorker.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
