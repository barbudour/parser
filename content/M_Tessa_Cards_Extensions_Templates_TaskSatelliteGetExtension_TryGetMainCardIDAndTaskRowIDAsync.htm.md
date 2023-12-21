# TaskSatelliteGetExtension.TryGetMainCardIDAndTaskRowIDAsync - метод
Возвращает идентификатор основной карточки и идентификатор задания по
идентификатору карточки-сателлита. Значение false возвращается в том случае,
если сателлит не существует.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract ValueTask<(bool result, Guid? mainCardID, Guid? taskRowID)> TryGetMainCardIDAndTaskRowIDAsync(
    	ICardGetExtensionContext context,
    	Card satellite
    )
VB __Копировать
     Protected MustOverride Function TryGetMainCardIDAndTaskRowIDAsync ( 
    	context As ICardGetExtensionContext,
    	satellite As Card
    ) As ValueTask(Of (result As Boolean, mainCardID As Guid?, taskRowID As Guid?))
C++ __Копировать
     protected:
    virtual ValueTask<ValueTuple<bool, Nullable<Guid>, Nullable<Guid>>> TryGetMainCardIDAndTaskRowIDAsync(
    	ICardGetExtensionContext^ context, 
    	Card^ satellite
    ) abstract
F# __Копировать
     abstract TryGetMainCardIDAndTaskRowIDAsync : 
            context : ICardGetExtensionContext * 
            satellite : Card -> ValueTask<ValueTuple<bool, Nullable<Guid>, Nullable<Guid>>> 
#### Параметры
context
[ICardGetExtensionContext](T_Tessa_Cards_Extensions_ICardGetExtensionContext.htm)
satellite [Card](T_Tessa_Cards_Card.htm)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-3)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean),
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>,
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>>>  
true, если метод вернул значения и карточка-сателлит существует; false в
противном случае.
## __См. также
#### Ссылки
[TaskSatelliteGetExtension -
](T_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
