# TaskSatellitePermissionsGetExtension.CanModifyTaskCardAsync - метод
Возвращает признак того, что карточку-сателлит разрешено сохранять на
основании данных по заданию.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract ValueTask<bool> CanModifyTaskCardAsync(
    	ICardGetExtensionContext context,
    	Card satellite
    )
VB __Копировать
     Protected MustOverride Function CanModifyTaskCardAsync ( 
    	context As ICardGetExtensionContext,
    	satellite As Card
    ) As ValueTask(Of Boolean)
C++ __Копировать
     protected:
    virtual ValueTask<bool> CanModifyTaskCardAsync(
    	ICardGetExtensionContext^ context, 
    	Card^ satellite
    ) abstract
F# __Копировать
     abstract CanModifyTaskCardAsync : 
            context : ICardGetExtensionContext * 
            satellite : Card -> ValueTask<bool> 
#### Параметры
context
[ICardGetExtensionContext](T_Tessa_Cards_Extensions_ICardGetExtensionContext.htm)
    Контекст расширения по загрузке карточки-сателлита.
satellite [Card](T_Tessa_Cards_Card.htm)
     Карточка-сателлит, в которой загружена системная информация, информация по секциям сателлита и единственное задание, которое соотносится с сохраняемой карточкой-сателлитом. Проверка по полям основной карточки карточки должна выполняться запросом к базе данных. 
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если карточку-сателлит разрешено сохранять на основании данных по
заданию; false в противном случае.
## __См. также
#### Ссылки
[TaskSatellitePermissionsGetExtension -
](T_Tessa_Cards_Extensions_Templates_TaskSatellitePermissionsGetExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
