# TaskSatelliteGetExtension.SetupVirtualSatelliteAsync - метод
В виртуальной карточке-сателлите устанавливает идентификаторы основной
карточки и задания, к которым относится сателлит.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract ValueTask SetupVirtualSatelliteAsync(
    	ICardGetExtensionContext context,
    	Card satellite,
    	Guid mainCardID,
    	Guid taskRowID
    )
VB __Копировать
     Protected MustOverride Function SetupVirtualSatelliteAsync ( 
    	context As ICardGetExtensionContext,
    	satellite As Card,
    	mainCardID As Guid,
    	taskRowID As Guid
    ) As ValueTask
C++ __Копировать
     protected:
    virtual ValueTask SetupVirtualSatelliteAsync(
    	ICardGetExtensionContext^ context, 
    	Card^ satellite, 
    	Guid mainCardID, 
    	Guid taskRowID
    ) abstract
F# __Копировать
     abstract SetupVirtualSatelliteAsync : 
            context : ICardGetExtensionContext * 
            satellite : Card * 
            mainCardID : Guid * 
            taskRowID : Guid -> ValueTask 
#### Параметры
context
[ICardGetExtensionContext](T_Tessa_Cards_Extensions_ICardGetExtensionContext.htm)
    Контекст расширения по загрузке карточки-сателлита.
satellite [Card](T_Tessa_Cards_Card.htm)
    Карточка-сателлит, в которой необходимо сохранить информацию.
mainCardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор основной карточки, с которым связана карточка-сателлит.
taskRowID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор задания, с которым связана карточка-сателлит.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
Асинхронная задача.
##  __См. также
#### Ссылки
[TaskSatelliteGetExtension -
](T_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
