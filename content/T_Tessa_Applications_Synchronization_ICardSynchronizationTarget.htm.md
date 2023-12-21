# ICardSynchronizationTarget - интерфейс
Описание интерфейса целевого объекта синхронизации приложения в виде карточки
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardSynchronizationTarget : ISynchronizationTarget, 
    	IValidationObject, IValidatable
VB __Копировать
     Public Interface ICardSynchronizationTarget
    	Inherits ISynchronizationTarget, IValidationObject, IValidatable
C++ __Копировать
     public interface class ICardSynchronizationTarget : ISynchronizationTarget, 
    	IValidationObject, IValidatable
F# __Копировать
     type ICardSynchronizationTarget = 
        interface
            interface ISynchronizationTarget
            interface IValidationObject
            interface IValidatable
        end
Implements
    [ISynchronizationTarget](T_Tessa_Applications_Synchronization_ISynchronizationTarget.htm), [IValidatable](T_Tessa_Platform_Validation_IValidatable.htm), [IValidationObject](T_Tessa_Platform_Validation_IValidationObject.htm)
##  __Методы
[GetSynchronizationStrategy](M_Tessa_Applications_Synchronization_ISynchronizationTarget_GetSynchronizationStrategy.htm)|
Возвращает стратегию синхронизации файлов  
(Унаследован от
[ISynchronizationTarget](T_Tessa_Applications_Synchronization_ISynchronizationTarget.htm))  
---|---  
[IsValid](M_Tessa_Platform_Validation_IValidatable_IsValid.htm)| Выполняет
проверку объекта на валидность и возвращает признак того, что объект является
валидным.  
(Унаследован от [IValidatable](T_Tessa_Platform_Validation_IValidatable.htm))  
[TryGetApplicationPackageAsync](M_Tessa_Applications_Synchronization_ISynchronizationTarget_TryGetApplicationPackageAsync.htm)|
Возвращает пакет приложения содержащий файлы которые содержатся в целевом
объекте синхронизации. В случае ошибки получения или отсутствия приложения в
целевом объекте возвращает null. Ошибки получения пакета приложения
записываются в validationResultBuilder  
(Унаследован от
[ISynchronizationTarget](T_Tessa_Applications_Synchronization_ISynchronizationTarget.htm))  
[Validate](M_Tessa_Platform_Validation_IValidationObject_Validate.htm)|
Выполняет валидацию текущего объекта и всех его дочерних объектов.  
(Унаследован от
[IValidationObject](T_Tessa_Platform_Validation_IValidationObject.htm))  
[WithApplicationAlias](M_Tessa_Applications_Synchronization_ICardSynchronizationTarget_WithApplicationAlias.htm)|
Устанавливает псевдоним пакета приложения  
[WithClient64Bit](M_Tessa_Applications_Synchronization_ICardSynchronizationTarget_WithClient64Bit.htm)|
Устанавливает, что приложение использует 64-битную архитектуру.  
[WithSavingUpdateProgress](M_Tessa_Applications_Synchronization_ICardSynchronizationTarget_WithSavingUpdateProgress.htm)|
Устанавливает функцию обновления прогресса сохранения данных в карточку  
## __Методы расширения
[Validate](M_Tessa_Platform_Validation_ValidationExtensions_Validate.htm)|
Выполняет валидацию объекта и всех его дочерних объектов.  
(Определяется
[ValidationExtensions](T_Tessa_Platform_Validation_ValidationExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
