# TiffToPdfFileConverterWorker - класс
Объект, ответственный за преобразование файла в формат
[Pdf](F_Tessa_FileConverters_FileConverterFormat_Pdf.htm) из формата TIFF.
Обычно не используется как самостоятельный Worker, а применяется в составе
[PdfFileConverterWorker](T_Tessa_Extensions_Default_Chronos_FileConverters_PdfFileConverterWorker.htm).
Регистрация выполняется по константе
[TiffToPdf](F_Tessa_Extensions_Default_Chronos_FileConverters_FileConverterWorkerNames_TiffToPdf.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Chronos.FileConverters](N_Tessa_Extensions_Default_Chronos_FileConverters.htm)  
 **Сборка:** Tessa.Extensions.Default.Chronos (в
Tessa.Extensions.Default.Chronos.dll) Версия: 3.6.0.17
C# __Копировать
     public class TiffToPdfFileConverterWorker : IFileConverterWorker, 
    	IAsyncDisposable
VB __Копировать
     Public Class TiffToPdfFileConverterWorker
    	Implements IFileConverterWorker, IAsyncDisposable
C++ __Копировать
     public ref class TiffToPdfFileConverterWorker : IFileConverterWorker, 
    	IAsyncDisposable
F# __Копировать
     type TiffToPdfFileConverterWorker = 
        class
            interface IFileConverterWorker
            interface IAsyncDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ TiffToPdfFileConverterWorker
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IFileConverterWorker](T_Tessa_FileConverters_IFileConverterWorker.htm)
##  __Заметки
Наследники класса могут переопределять методы интерфейса, например, добавив к
ним обработку файлов других форматов. Класс может также реализовывать
[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable)
для очистки ресурсов, для этого в наследнике переопределяется метод
[!:Dispose] и вызывается сначала его базовая реализация.
## __Конструкторы
[TiffToPdfFileConverterWorker](M_Tessa_Extensions_Default_Chronos_FileConverters_TiffToPdfFileConverterWorker__ctor.htm)|
Инициализирует новый экземпляр класса TiffToPdfFileConverterWorker  
---|---  
##  __Методы
[ConvertFileAsync](M_Tessa_Extensions_Default_Chronos_FileConverters_TiffToPdfFileConverterWorker_ConvertFileAsync.htm)|
Преобразует файл в заданный формат.  
---|---  
[DisposeAsync](M_Tessa_Extensions_Default_Chronos_FileConverters_TiffToPdfFileConverterWorker_DisposeAsync.htm)|
Освобождение занятых ресурсов.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[PerformMaintenanceAsync](M_Tessa_Extensions_Default_Chronos_FileConverters_TiffToPdfFileConverterWorker_PerformMaintenanceAsync.htm)|
Выполняет обработку в процессе выполнения цикла обслуживания для очереди на
конвертацию файлов. Метод запускается множество раз внутри цикла с
переидичностью, заданной в конфигурационном файле.  
[PreprocessAsync](M_Tessa_Extensions_Default_Chronos_FileConverters_TiffToPdfFileConverterWorker_PreprocessAsync.htm)|
Выполняет обработку перед запуском цикла обслуживания для очереди на
конвертацию файлов. Метод запускается единственный раз при старте сервиса
конвертации.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Extensions.Default.Chronos.FileConverters - пространство
имён](N_Tessa_Extensions_Default_Chronos_FileConverters.htm)
