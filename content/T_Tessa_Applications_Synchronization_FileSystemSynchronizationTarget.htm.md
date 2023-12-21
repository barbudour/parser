# FileSystemSynchronizationTarget - класс
Целевой объект синхронизации в виде файловой системы
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class FileSystemSynchronizationTarget : IFileSystemSynchronizationTarget, 
    	ISynchronizationTarget, IValidationObject, IValidatable
VB __Копировать
     Public NotInheritable Class FileSystemSynchronizationTarget
    	Implements IFileSystemSynchronizationTarget, ISynchronizationTarget, IValidationObject, IValidatable
C++ __Копировать
     public ref class FileSystemSynchronizationTarget sealed : IFileSystemSynchronizationTarget, 
    	ISynchronizationTarget, IValidationObject, IValidatable
F# __Копировать
     [<SealedAttribute>]
    type FileSystemSynchronizationTarget = 
        class
            interface IFileSystemSynchronizationTarget
            interface ISynchronizationTarget
            interface IValidationObject
            interface IValidatable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FileSystemSynchronizationTarget
Implements
    [IFileSystemSynchronizationTarget](T_Tessa_Applications_Synchronization_IFileSystemSynchronizationTarget.htm), [ISynchronizationTarget](T_Tessa_Applications_Synchronization_ISynchronizationTarget.htm), [IValidatable](T_Tessa_Platform_Validation_IValidatable.htm), [IValidationObject](T_Tessa_Platform_Validation_IValidationObject.htm)
##  __Конструкторы
[FileSystemSynchronizationTarget](M_Tessa_Applications_Synchronization_FileSystemSynchronizationTarget__ctor.htm)|
Initializes a new instance of the FileSystemSynchronizationTarget class.  
---|---  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetSynchronizationStrategy](M_Tessa_Applications_Synchronization_FileSystemSynchronizationTarget_GetSynchronizationStrategy.htm)|
Возвращает стратегию синхронизации файлов  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[IsValid](M_Tessa_Applications_Synchronization_FileSystemSynchronizationTarget_IsValid.htm)|
Выполняет проверку объекта на валидность и возвращает признак того, что объект
является валидным.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OverrideClient64Bit](M_Tessa_Applications_Synchronization_FileSystemSynchronizationTarget_OverrideClient64Bit.htm)|
Переопределяет свойство Client64Bit для пакета приложения, создаваемого из
папки.  
[SetLocalFiles](M_Tessa_Applications_Synchronization_FileSystemSynchronizationTarget_SetLocalFiles.htm)|
Задаёт информацию о локальных файлах.  
[SyncFolder](M_Tessa_Applications_Synchronization_FileSystemSynchronizationTarget_SyncFolder.htm)|
Устанавливает папку синхронизации.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetApplicationPackageAsync](M_Tessa_Applications_Synchronization_FileSystemSynchronizationTarget_TryGetApplicationPackageAsync.htm)|
Возвращает пакет приложения содержащий файлы которые содержатся в целевом
объекте синхронизации. В случае ошибки получения или отсутствия приложения в
целевом объекте возвращает null. Ошибки получения пакета приложения
записываются в validationResultBuilder  
[Validate](M_Tessa_Applications_Synchronization_FileSystemSynchronizationTarget_Validate.htm)|
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
