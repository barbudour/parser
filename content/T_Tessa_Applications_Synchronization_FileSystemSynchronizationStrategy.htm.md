# FileSystemSynchronizationStrategy - класс
The file system synchronization strategy.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class FileSystemSynchronizationStrategy : IFileSystemSynchronizationStrategy, 
    	IApplicationSynchronizationStrategy
VB __Копировать
     Public NotInheritable Class FileSystemSynchronizationStrategy
    	Implements IFileSystemSynchronizationStrategy, IApplicationSynchronizationStrategy
C++ __Копировать
     public ref class FileSystemSynchronizationStrategy sealed : IFileSystemSynchronizationStrategy, 
    	IApplicationSynchronizationStrategy
F# __Копировать
     [<SealedAttribute>]
    type FileSystemSynchronizationStrategy = 
        class
            interface IFileSystemSynchronizationStrategy
            interface IApplicationSynchronizationStrategy
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FileSystemSynchronizationStrategy
Implements
    [IApplicationSynchronizationStrategy](T_Tessa_Applications_Synchronization_IApplicationSynchronizationStrategy.htm), [IFileSystemSynchronizationStrategy](T_Tessa_Applications_Synchronization_IFileSystemSynchronizationStrategy.htm)
##  __Конструкторы
[FileSystemSynchronizationStrategy](M_Tessa_Applications_Synchronization_FileSystemSynchronizationStrategy__ctor.htm)|
Initializes a new instance of the FileSystemSynchronizationStrategy class.
Initializes a new instance of the
[Object](https://learn.microsoft.com/dotnet/api/system.object) class.  
---|---  
## __Методы
[CreateFileAsync](M_Tessa_Applications_Synchronization_FileSystemSynchronizationStrategy_CreateFileAsync.htm)|
Создает новый файл с параметрами и содержимым, заданными в content  
---|---  
[DeleteFileAsync](M_Tessa_Applications_Synchronization_FileSystemSynchronizationStrategy_DeleteFileAsync.htm)|
Удаляет файл заданный в file  
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
[OnSynchronizationCompletedAsync](M_Tessa_Applications_Synchronization_FileSystemSynchronizationStrategy_OnSynchronizationCompletedAsync.htm)|
Вызывается при завершении синхронизации элементов  
[ReplaceFileAsync](M_Tessa_Applications_Synchronization_FileSystemSynchronizationStrategy_ReplaceFileAsync.htm)|
Заменяет файл с параметрами и содержимым, заданными в content  
[StartSynchronizationAsync](M_Tessa_Applications_Synchronization_FileSystemSynchronizationStrategy_StartSynchronizationAsync.htm)|
Вызывается при запуске процесса синхронизации  
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
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
