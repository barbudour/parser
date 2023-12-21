# CardRepairManager.RepairAsync - метод
Исправляет структуру карточки, например, вследствие изменения её типа
карточки. Возвращает результат исправления, причём, наличие хотя бы одного
сообщения означает, что карточка была как-либо исправлена, а наличие
сообщений-ошибок определяет, что карточка серьёзно повреждена, и её
использование невозможно.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<ValidationResult> RepairAsync(
    	Card card,
    	CardNewMode newMode = CardNewMode.Default,
    	bool notifyFieldsUpdated = false,
    	ICardRepairExtensionContext parentContext = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function RepairAsync ( 
    	card As Card,
    	Optional newMode As CardNewMode = CardNewMode.Default,
    	Optional notifyFieldsUpdated As Boolean = false,
    	Optional parentContext As ICardRepairExtensionContext = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ValidationResult)
C++ __Копировать
     public:
    virtual Task<ValidationResult^>^ RepairAsync(
    	Card^ card, 
    	CardNewMode newMode = CardNewMode::Default, 
    	bool notifyFieldsUpdated = false, 
    	ICardRepairExtensionContext^ parentContext = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract RepairAsync : 
            card : Card * 
            ?newMode : CardNewMode * 
            ?notifyFieldsUpdated : bool * 
            ?parentContext : ICardRepairExtensionContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _newMode = defaultArg newMode CardNewMode.Default
            let _notifyFieldsUpdated = defaultArg notifyFieldsUpdated false
            let _parentContext = defaultArg parentContext null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValidationResult> 
    override RepairAsync : 
            card : Card * 
            ?newMode : CardNewMode * 
            ?notifyFieldsUpdated : bool * 
            ?parentContext : ICardRepairExtensionContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _newMode = defaultArg newMode CardNewMode.Default
            let _notifyFieldsUpdated = defaultArg notifyFieldsUpdated false
            let _parentContext = defaultArg parentContext null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValidationResult> 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Исправляемая карточка.
newMode [CardNewMode](T_Tessa_Cards_CardNewMode.htm) (Optional)
     Способ заполнения добавляемых в карточку полей, который соответствует способу создания карточки. 
notifyFieldsUpdated
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
     Признак того, что в пакете карточки для изменённых полей должны записываться уведомления об изменённых полях. 
parentContext
[ICardRepairExtensionContext](T_Tessa_Cards_Extensions_ICardRepairExtensionContext.htm)
(Optional)
     Контекст по исправлению родительской карточки или null, если текущая исправляемая карточка не связана с родительской карточкой, т.е. не является сателлитом. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)>  
Результат выполнения исправлений. Ошибки в результате сигнализируют о
серьёзном повреждении структуры карточки, а предупреждения и информационные
сообщения - об исправленных повреждениях или о ситуациях, когда исправление не
требуется, но проблема присутствует.
#### Реализации
[ICardRepairManager.RepairAsync(Card, CardNewMode, Boolean,
ICardRepairExtensionContext,
CancellationToken)](M_Tessa_Cards_ICardRepairManager_RepairAsync.htm)  
##  __См. также
#### Ссылки
[CardRepairManager - ](T_Tessa_Cards_CardRepairManager.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
