# FileSystemSynchronizationTarget.GetSynchronizationStrategy - метод
Возвращает стратегию синхронизации файлов
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IApplicationSynchronizationStrategy GetSynchronizationStrategy(
    	ApplicationPackage applicationPackage,
    	IValidationResultBuilder validationResultBuilder
    )
VB __Копировать
     Public Function GetSynchronizationStrategy ( 
    	applicationPackage As ApplicationPackage,
    	validationResultBuilder As IValidationResultBuilder
    ) As IApplicationSynchronizationStrategy
C++ __Копировать
     public:
    virtual IApplicationSynchronizationStrategy^ GetSynchronizationStrategy(
    	ApplicationPackage^ applicationPackage, 
    	IValidationResultBuilder^ validationResultBuilder
    ) sealed
F# __Копировать
     abstract GetSynchronizationStrategy : 
            applicationPackage : ApplicationPackage * 
            validationResultBuilder : IValidationResultBuilder -> IApplicationSynchronizationStrategy 
    override GetSynchronizationStrategy : 
            applicationPackage : ApplicationPackage * 
            validationResultBuilder : IValidationResultBuilder -> IApplicationSynchronizationStrategy 
#### Параметры
applicationPackage
[ApplicationPackage](T_Tessa_Applications_Package_ApplicationPackage.htm)
     Пакет приложения 
validationResultBuilder
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
     Построитель результатов валидации 
#### Возвращаемое значение
[IApplicationSynchronizationStrategy](T_Tessa_Applications_Synchronization_IApplicationSynchronizationStrategy.htm)  
Стратегия синхронизации файлов
#### Реализации
[ISynchronizationTarget.GetSynchronizationStrategy(ApplicationPackage,
IValidationResultBuilder)](M_Tessa_Applications_Synchronization_ISynchronizationTarget_GetSynchronizationStrategy.htm)  
##  __Исключения
[Exception](https://learn.microsoft.com/dotnet/api/system.exception)| A
delegate callback throws an exception.  
---|---  
##  __См. также
#### Ссылки
[FileSystemSynchronizationTarget -
](T_Tessa_Applications_Synchronization_FileSystemSynchronizationTarget.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
