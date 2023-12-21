# IFileConverterWorker - интерфейс
Объект, ответственный за преобразование файла посредством внешних программ,
таких как OpenOffice или LibreOffice. Класс может также реализовывать
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable) для
очистки ресурсов.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFileConverterWorker
VB __Копировать
     Public Interface IFileConverterWorker
C++ __Копировать
     public interface class IFileConverterWorker
F# __Копировать
     type IFileConverterWorker = interface end
##  __Методы
[ConvertFileAsync](M_Tessa_FileConverters_IFileConverterWorker_ConvertFileAsync.htm)|
Преобразует файл в заданный формат.  
---|---  
[PerformMaintenanceAsync](M_Tessa_FileConverters_IFileConverterWorker_PerformMaintenanceAsync.htm)|
Выполняет обработку в процессе выполнения цикла обслуживания для очереди на
конвертацию файлов. Метод запускается множество раз внутри цикла с
переидичностью, заданной в конфигурационном файле.  
[PreprocessAsync](M_Tessa_FileConverters_IFileConverterWorker_PreprocessAsync.htm)|
Выполняет обработку перед запуском цикла обслуживания для очереди на
конвертацию файлов. Метод запускается единственный раз при старте сервиса
конвертации.  
## __См. также
#### Ссылки
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
