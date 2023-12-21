# KrCardMetadataExtensionBase.ExtendKrTypesAsync - метод
Расширить и настроить указанные типы карточек.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract Task ExtendKrTypesAsync(
    	IList<CardType> krTypes,
    	ICardMetadataExtensionContext context
    )
VB __Копировать
     Protected MustOverride Function ExtendKrTypesAsync ( 
    	krTypes As IList(Of CardType),
    	context As ICardMetadataExtensionContext
    ) As Task
C++ __Копировать
     protected:
    virtual Task^ ExtendKrTypesAsync(
    	IList<CardType^>^ krTypes, 
    	ICardMetadataExtensionContext^ context
    ) abstract
F# __Копировать
     abstract ExtendKrTypesAsync : 
            krTypes : IList<CardType> * 
            context : ICardMetadataExtensionContext -> Task 
#### Параметры
krTypes
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[CardType](T_Tessa_Cards_CardType.htm)>
    Типы карточек для расширения.
context
[ICardMetadataExtensionContext](T_Tessa_Cards_Extensions_ICardMetadataExtensionContext.htm)
    Контекст выполнения операции, предоставляющий доступ к метаданным.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[KrCardMetadataExtensionBase -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrCardMetadataExtensionBase.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
