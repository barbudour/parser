# IFileSystemSynchronizationSource - интерфейс
Описание интерфейса источника синхронизации файловой системы
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFileSystemSynchronizationSource : ISynchronizationSource, 
    	IValidationObject, IValidatable
VB __Копировать
     Public Interface IFileSystemSynchronizationSource
    	Inherits ISynchronizationSource, IValidationObject, IValidatable
C++ __Копировать
     public interface class IFileSystemSynchronizationSource : ISynchronizationSource, 
    	IValidationObject, IValidatable
F# __Копировать
     type IFileSystemSynchronizationSource = 
        interface
            interface ISynchronizationSource
            interface IValidationObject
            interface IValidatable
        end
Implements
    [ISynchronizationSource](T_Tessa_Applications_Synchronization_ISynchronizationSource.htm), [IValidatable](T_Tessa_Platform_Validation_IValidatable.htm), [IValidationObject](T_Tessa_Platform_Validation_IValidationObject.htm)
##  __Методы
[IsValid](M_Tessa_Platform_Validation_IValidatable_IsValid.htm)| Выполняет
проверку объекта на валидность и возвращает признак того, что объект является
валидным.  
(Унаследован от [IValidatable](T_Tessa_Platform_Validation_IValidatable.htm))  
---|---  
[TryCreateSynchronizationEnumerableAsync](M_Tessa_Applications_Synchronization_ISynchronizationSource_TryCreateSynchronizationEnumerableAsync.htm)|
Осуществляет попытку создания перечислителя файлов необходимых для
синхронизации элементов между файлами находящимися в источнике и текущем
состоянии пакета приложения находящегося в состоянии currentState. В случае
если не при создании произошли ошибки, то ошибки помещаются в
validationResultBuilder, и возвращается null  
(Унаследован от
[ISynchronizationSource](T_Tessa_Applications_Synchronization_ISynchronizationSource.htm))  
[Validate](M_Tessa_Platform_Validation_IValidationObject_Validate.htm)|
Выполняет валидацию текущего объекта и всех его дочерних объектов.  
(Унаследован от
[IValidationObject](T_Tessa_Platform_Validation_IValidationObject.htm))  
##  __Методы расширения
[Validate](M_Tessa_Platform_Validation_ValidationExtensions_Validate.htm)|
Выполняет валидацию объекта и всех его дочерних объектов.  
(Определяется
[ValidationExtensions](T_Tessa_Platform_Validation_ValidationExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
