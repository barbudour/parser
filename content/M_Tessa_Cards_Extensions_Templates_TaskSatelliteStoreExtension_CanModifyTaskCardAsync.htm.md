# TaskSatelliteStoreExtension.CanModifyTaskCardAsync - метод
Возвращает признак того, что карточку-сателлит разрешено сохранять на
основании данных по заданию.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract ValueTask<bool> CanModifyTaskCardAsync(
    	ICardStoreExtensionContext context,
    	Card mainCard,
    	Guid taskRowID
    )
VB __Копировать
     Protected MustOverride Function CanModifyTaskCardAsync ( 
    	context As ICardStoreExtensionContext,
    	mainCard As Card,
    	taskRowID As Guid
    ) As ValueTask(Of Boolean)
C++ __Копировать
     protected:
    virtual ValueTask<bool> CanModifyTaskCardAsync(
    	ICardStoreExtensionContext^ context, 
    	Card^ mainCard, 
    	Guid taskRowID
    ) abstract
F# __Копировать
     abstract CanModifyTaskCardAsync : 
            context : ICardStoreExtensionContext * 
            mainCard : Card * 
            taskRowID : Guid -> ValueTask<bool> 
#### Параметры
context
[ICardStoreExtensionContext](T_Tessa_Cards_Extensions_ICardStoreExtensionContext.htm)
    Контекст расширения по сохранению карточки-сателлита.
mainCard [Card](T_Tessa_Cards_Card.htm)
     Основная карточка, в которой загружена системная информация и единственное задание, которое соотносится с сохраняемой карточкой-сателлитом. Карточка не содержит секций, поэтому проверка по полям карточки должна выполняться запросом к базе данных. 
taskRowID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор задания, с которым связана карточка-сателлит.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если карточку-сателлит разрешено сохранять на основании данных по
заданию; false в противном случае.
## __См. также
#### Ссылки
[TaskSatelliteStoreExtension -
](T_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
