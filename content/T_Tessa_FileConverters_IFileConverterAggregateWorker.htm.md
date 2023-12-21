# IFileConverterAggregateWorker - интерфейс
Объект, ответственный за преобразование файла посредством внешних программ, и
обеспечивающий выбор алгоритма преобразования в зависимости от формата
выходного файла.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFileConverterAggregateWorker : IFileConverterWorker
VB __Копировать
     Public Interface IFileConverterAggregateWorker
    	Inherits IFileConverterWorker
C++ __Копировать
     public interface class IFileConverterAggregateWorker : IFileConverterWorker
F# __Копировать
     type IFileConverterAggregateWorker = 
        interface
            interface IFileConverterWorker
        end
Implements
    [IFileConverterWorker](T_Tessa_FileConverters_IFileConverterWorker.htm)
##  __Методы
[ConvertFileAsync](M_Tessa_FileConverters_IFileConverterWorker_ConvertFileAsync.htm)|
Преобразует файл в заданный формат.  
(Унаследован от
[IFileConverterWorker](T_Tessa_FileConverters_IFileConverterWorker.htm))  
---|---  
[IsRegistered](M_Tessa_FileConverters_IFileConverterAggregateWorker_IsRegistered.htm)|
Возвращает признак того, что для заданного формата выходного файла был
зарегистрирован объект, выполняющий преобразование в этот формат.  
[PerformMaintenanceAsync](M_Tessa_FileConverters_IFileConverterWorker_PerformMaintenanceAsync.htm)|
Выполняет обработку в процессе выполнения цикла обслуживания для очереди на
конвертацию файлов. Метод запускается множество раз внутри цикла с
переидичностью, заданной в конфигурационном файле.  
(Унаследован от
[IFileConverterWorker](T_Tessa_FileConverters_IFileConverterWorker.htm))  
[PreprocessAsync](M_Tessa_FileConverters_IFileConverterWorker_PreprocessAsync.htm)|
Выполняет обработку перед запуском цикла обслуживания для очереди на
конвертацию файлов. Метод запускается единственный раз при старте сервиса
конвертации.  
(Унаследован от
[IFileConverterWorker](T_Tessa_FileConverters_IFileConverterWorker.htm))  
[Register](M_Tessa_FileConverters_IFileConverterAggregateWorker_Register.htm)|
Регистрирует объект, ответственный за преобразование файла заданного формата.  
[RemoveRegistrations](M_Tessa_FileConverters_IFileConverterAggregateWorker_RemoveRegistrations.htm)|
Удаляет все регистрации в текущем объекте.  
##  __См. также
#### Ссылки
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
