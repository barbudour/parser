# FileSystemSynchronizationSource - класс
Источник синхронизации файлов в виде файловой системы
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class FileSystemSynchronizationSource : IFileSystemSynchronizationSource, 
    	ISynchronizationSource, IValidationObject, IValidatable
VB __Копировать
     Public Class FileSystemSynchronizationSource
    	Implements IFileSystemSynchronizationSource, ISynchronizationSource, IValidationObject, IValidatable
C++ __Копировать
     public ref class FileSystemSynchronizationSource : IFileSystemSynchronizationSource, 
    	ISynchronizationSource, IValidationObject, IValidatable
F# __Копировать
     type FileSystemSynchronizationSource = 
        class
            interface IFileSystemSynchronizationSource
            interface ISynchronizationSource
            interface IValidationObject
            interface IValidatable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FileSystemSynchronizationSource
Implements
    [IFileSystemSynchronizationSource](T_Tessa_Applications_Synchronization_IFileSystemSynchronizationSource.htm), [ISynchronizationSource](T_Tessa_Applications_Synchronization_ISynchronizationSource.htm), [IValidatable](T_Tessa_Platform_Validation_IValidatable.htm), [IValidationObject](T_Tessa_Platform_Validation_IValidationObject.htm)
##  __Конструкторы
[FileSystemSynchronizationSource](M_Tessa_Applications_Synchronization_FileSystemSynchronizationSource__ctor.htm)|
Initializes a new instance of the FileSystemSynchronizationSource class.
Initializes a new instance of the
[Object](https://learn.microsoft.com/dotnet/api/system.object) class.  
---|---  
## __Методы
[CreateSynchronizationEnumerable](M_Tessa_Applications_Synchronization_FileSystemSynchronizationSource_CreateSynchronizationEnumerable.htm)|
Возвращает перечислитель файлов для пакета приложения  
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
[IsValid](M_Tessa_Applications_Synchronization_FileSystemSynchronizationSource_IsValid.htm)|
Выполняет проверку объекта на валидность и возвращает признак того, что объект
является валидным.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[SyncFolder](M_Tessa_Applications_Synchronization_FileSystemSynchronizationSource_SyncFolder.htm)|
Устанавливает папку синхронизации  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryCreateSynchronizationEnumerableAsync](M_Tessa_Applications_Synchronization_FileSystemSynchronizationSource_TryCreateSynchronizationEnumerableAsync.htm)|
Осуществляет попытку создания перечислителя файлов необходимых для
синхронизации элементов между файлами находящимися в источнике и текущем
состоянии пакета приложения находящегося в состоянии currentState. В случае
если не при создании произошли ошибки, то ошибки помещаются в
validationResultBuilder, и возвращается null  
[TryGetApplicationPackage](M_Tessa_Applications_Synchronization_FileSystemSynchronizationSource_TryGetApplicationPackage.htm)|
Осуществляет попытку получения пакета приложения. В случае если пакет
приложения не может быть получен возвращает null. Ошибки построения пакета
приложения записываются в validationResultBuilder  
[Validate](M_Tessa_Applications_Synchronization_FileSystemSynchronizationSource_Validate.htm)|
Выполняет валидацию текущего объекта и всех его дочерних объектов.  
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
[Validate](M_Tessa_Platform_Validation_ValidationExtensions_Validate.htm)|
Выполняет валидацию объекта и всех его дочерних объектов.  
(Определяется
[ValidationExtensions](T_Tessa_Platform_Validation_ValidationExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
