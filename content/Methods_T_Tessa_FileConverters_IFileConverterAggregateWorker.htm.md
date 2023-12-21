# IFileConverterAggregateWorker - методы
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
[IFileConverterAggregateWorker -
](T_Tessa_FileConverters_IFileConverterAggregateWorker.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
