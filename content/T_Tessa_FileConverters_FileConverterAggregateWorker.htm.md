# FileConverterAggregateWorker - класс
Объект, ответственный за преобразование файла посредством внешних программ, и
обеспечивающий выбор алгоритма преобразования в зависимости от формата
выходного файла.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class FileConverterAggregateWorker : IFileConverterAggregateWorker, 
    	IFileConverterWorker, IAsyncDisposable
VB __Копировать
     Public NotInheritable Class FileConverterAggregateWorker
    	Implements IFileConverterAggregateWorker, IFileConverterWorker, IAsyncDisposable
C++ __Копировать
     public ref class FileConverterAggregateWorker sealed : IFileConverterAggregateWorker, 
    	IFileConverterWorker, IAsyncDisposable
F# __Копировать
     [<SealedAttribute>]
    type FileConverterAggregateWorker = 
        class
            interface IFileConverterAggregateWorker
            interface IFileConverterWorker
            interface IAsyncDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FileConverterAggregateWorker
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IFileConverterAggregateWorker](T_Tessa_FileConverters_IFileConverterAggregateWorker.htm), [IFileConverterWorker](T_Tessa_FileConverters_IFileConverterWorker.htm)
##  __Конструкторы
[FileConverterAggregateWorker](M_Tessa_FileConverters_FileConverterAggregateWorker__ctor.htm)|
Инициализирует новый экземпляр класса FileConverterAggregateWorker  
---|---  
##  __Методы
[ConvertFileAsync](M_Tessa_FileConverters_FileConverterAggregateWorker_ConvertFileAsync.htm)|
Преобразует файл в заданный формат.  
---|---  
[DisposeAsync](M_Tessa_FileConverters_FileConverterAggregateWorker_DisposeAsync.htm)|
Освобождает ресурсы, занимаемые объектом.  
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
[IsRegistered](M_Tessa_FileConverters_FileConverterAggregateWorker_IsRegistered.htm)|
Возвращает признак того, что для заданного формата выходного файла был
зарегистрирован объект, выполняющий преобразование в этот формат.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[PerformMaintenanceAsync](M_Tessa_FileConverters_FileConverterAggregateWorker_PerformMaintenanceAsync.htm)|
Выполняет обработку в процессе выполнения цикла обслуживания для очереди на
конвертацию файлов. Метод запускается множество раз внутри цикла с
переидичностью, заданной в конфигурационном файле.  
[PreprocessAsync](M_Tessa_FileConverters_FileConverterAggregateWorker_PreprocessAsync.htm)|
Выполняет обработку перед запуском цикла обслуживания для очереди на
конвертацию файлов. Метод запускается единственный раз при старте сервиса
конвертации.  
[Register](M_Tessa_FileConverters_FileConverterAggregateWorker_Register.htm)|
Регистрирует объект, ответственный за преобразование файла заданного формата.  
[RemoveRegistrations](M_Tessa_FileConverters_FileConverterAggregateWorker_RemoveRegistrations.htm)|
Удаляет все регистрации в текущем объекте.  
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
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
