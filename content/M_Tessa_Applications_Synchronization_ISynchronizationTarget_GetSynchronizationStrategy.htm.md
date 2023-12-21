# ISynchronizationTarget.GetSynchronizationStrategy - метод
Возвращает стратегию синхронизации файлов
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    IApplicationSynchronizationStrategy GetSynchronizationStrategy(
    	[NotNullAttribute] ApplicationPackage applicationPackage,
    	[NotNullAttribute] IValidationResultBuilder validationResultBuilder
    )
VB __Копировать
    <NotNullAttribute>
    Function GetSynchronizationStrategy ( 
    	<NotNullAttribute> applicationPackage As ApplicationPackage,
    	<NotNullAttribute> validationResultBuilder As IValidationResultBuilder
    ) As IApplicationSynchronizationStrategy
C++ __Копировать
    [NotNullAttribute]
    IApplicationSynchronizationStrategy^ GetSynchronizationStrategy(
    	[NotNullAttribute] ApplicationPackage^ applicationPackage, 
    	[NotNullAttribute] IValidationResultBuilder^ validationResultBuilder
    )
F# __Копировать
     [<NotNullAttribute>]
    abstract GetSynchronizationStrategy : 
            [<NotNullAttribute>] applicationPackage : ApplicationPackage * 
            [<NotNullAttribute>] validationResultBuilder : IValidationResultBuilder -> IApplicationSynchronizationStrategy 
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
## __См. также
#### Ссылки
[ISynchronizationTarget -
](T_Tessa_Applications_Synchronization_ISynchronizationTarget.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
