# FileSystemApplicationPackageFileEnumerable - класс
The file system application package file enumerable.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class FileSystemApplicationPackageFileEnumerable : IApplicationPackageFileEnumerable, 
    	IAsyncEnumerable<ApplicationPackageFileContent>, IAsyncDisposable
VB __Копировать
     Public NotInheritable Class FileSystemApplicationPackageFileEnumerable
    	Implements IApplicationPackageFileEnumerable, IAsyncEnumerable(Of ApplicationPackageFileContent), 
    	IAsyncDisposable
C++ __Копировать
     public ref class FileSystemApplicationPackageFileEnumerable sealed : IApplicationPackageFileEnumerable, 
    	IAsyncEnumerable<ApplicationPackageFileContent^>, IAsyncDisposable
F# __Копировать
     [<SealedAttribute>]
    type FileSystemApplicationPackageFileEnumerable = 
        class
            interface IApplicationPackageFileEnumerable
            interface IAsyncEnumerable<ApplicationPackageFileContent>
            interface IAsyncDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FileSystemApplicationPackageFileEnumerable
Implements
    [IAsyncEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.iasyncenumerable-1)<[ApplicationPackageFileContent](T_Tessa_Applications_Package_ApplicationPackageFileContent.htm)>, [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IApplicationPackageFileEnumerable](T_Tessa_Applications_Synchronization_IApplicationPackageFileEnumerable.htm)
##  __Конструкторы
[FileSystemApplicationPackageFileEnumerable](M_Tessa_Applications_Synchronization_FileSystemApplicationPackageFileEnumerable__ctor.htm)|
Initializes a new instance of the FileSystemApplicationPackageFileEnumerable
class. Initializes a new instance of the
[Object](https://learn.microsoft.com/dotnet/api/system.object) class.  
---|---  
## __Методы
[DisposeAsync](M_Tessa_Applications_Synchronization_FileSystemApplicationPackageFileEnumerable_DisposeAsync.htm)|  
---|---  
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
[GetAsyncEnumerator](M_Tessa_Applications_Synchronization_FileSystemApplicationPackageFileEnumerable_GetAsyncEnumerator.htm)|  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetPackageAsync](M_Tessa_Applications_Synchronization_FileSystemApplicationPackageFileEnumerable_GetPackageAsync.htm)|
Gets Пакет приложения  
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
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetFaultedResultAsync](M_Tessa_Applications_Synchronization_FileSystemApplicationPackageFileEnumerable_TryGetFaultedResultAsync.htm)|
Возвращает ошибки при загрузке приложения. Метод может выполнить запрос к
серверу. Результат не равен null, но может быть пустым
[Empty](P_Tessa_Platform_Validation_ValidationResult_Empty.htm).  
## __Методы расширения
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
