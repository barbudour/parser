# DefaultGlobalStorage - класс
Реализация [IGlobalStorage](T_Tessa_Platform_IPC_IGlobalStorage.htm) по
умолчанию с разделяемым хранилищем в памяти, которое реализовано посредством
объекта
[MemoryMappedFile](https://learn.microsoft.com/dotnet/api/system.io.memorymappedfiles.memorymappedfile).
## __Definition
 **Пространство имён:** [Tessa.Platform.IPC](N_Tessa_Platform_IPC.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class DefaultGlobalStorage : GlobalStorageBase
VB __Копировать
     Public Class DefaultGlobalStorage
    	Inherits GlobalStorageBase
C++ __Копировать
     public ref class DefaultGlobalStorage : public GlobalStorageBase
F# __Копировать
     type DefaultGlobalStorage = 
        class
            inherit GlobalStorageBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[GlobalStorageBase](T_Tessa_Platform_IPC_GlobalStorageBase.htm) __ DefaultGlobalStorage
##  __Конструкторы
[DefaultGlobalStorage](M_Tessa_Platform_IPC_DefaultGlobalStorage__ctor.htm)|
Создаёт экземпляр класса с указанием его параметров.  
---|---  
## __Свойства
[IsDisposed](P_Tessa_Platform_IPC_GlobalStorageBase_IsDisposed.htm)| Признак
того, что ресурсы объекта были освобождены.  
(Унаследован от
[GlobalStorageBase](T_Tessa_Platform_IPC_GlobalStorageBase.htm))  
---|---  
[MemoryMappedFile](P_Tessa_Platform_IPC_DefaultGlobalStorage_MemoryMappedFile.htm)|
Разделяемый между процессами файл, который расположен в памяти.  
## __Методы
[CheckDisposed](M_Tessa_Platform_IPC_GlobalStorageBase_CheckDisposed.htm)|
Выбрасывает исключение [ObjectDisposedException], если ресурсы текущего
объекта были освобождены.  
(Унаследован от
[GlobalStorageBase](T_Tessa_Platform_IPC_GlobalStorageBase.htm))  
---|---  
[DisposeAsync()](M_Tessa_Platform_IPC_GlobalStorageBase_DisposeAsync.htm)|
Освобождает ресурсы, занимаемые объектом.  
(Унаследован от
[GlobalStorageBase](T_Tessa_Platform_IPC_GlobalStorageBase.htm))  
[DisposeAsync(Boolean)](M_Tessa_Platform_IPC_DefaultGlobalStorage_DisposeAsync.htm)|
Освобождает ресурсы, занимаемые объектом.  
(Переопределяет
[GlobalStorageBase.DisposeAsync(Boolean)](M_Tessa_Platform_IPC_GlobalStorageBase_DisposeAsync_1.htm))  
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
[OpenAsync](M_Tessa_Platform_IPC_GlobalStorageBase_OpenAsync.htm)|  Открывает
разделяемое хранилище для записи или чтения. При необходимости некоторое время
ожидается снятие блокировки от других процессов.  
(Унаследован от
[GlobalStorageBase](T_Tessa_Platform_IPC_GlobalStorageBase.htm))  
[OpenCoreAsync](M_Tessa_Platform_IPC_DefaultGlobalStorage_OpenCoreAsync.htm)|
Открывает разделяемое хранилище для записи или чтения. При необходимости
некоторое время ожидается снятие блокировки от других процессов.  
(Переопределяет [GlobalStorageBase.OpenCoreAsync(Boolean,
CancellationToken)](M_Tessa_Platform_IPC_GlobalStorageBase_OpenCoreAsync.htm))  
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
[Tessa.Platform.IPC - пространство имён](N_Tessa_Platform_IPC.htm)
