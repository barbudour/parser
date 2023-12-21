# TaskSatelliteGetExtension.PrepareRequestToLoadMainCardAsync - метод
Подготавливает запрос на загрузку основной карточки, данные которой
используются, а также информация по правам доступа к которой используются при
загрузке карточки-сателлита.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract ValueTask PrepareRequestToLoadMainCardAsync(
    	ICardGetExtensionContext context,
    	CardGetRequest request,
    	Guid mainCardID,
    	Guid taskRowID,
    	Object additionalInfo
    )
VB __Копировать
     Protected MustOverride Function PrepareRequestToLoadMainCardAsync ( 
    	context As ICardGetExtensionContext,
    	request As CardGetRequest,
    	mainCardID As Guid,
    	taskRowID As Guid,
    	additionalInfo As Object
    ) As ValueTask
C++ __Копировать
     protected:
    virtual ValueTask PrepareRequestToLoadMainCardAsync(
    	ICardGetExtensionContext^ context, 
    	CardGetRequest^ request, 
    	Guid mainCardID, 
    	Guid taskRowID, 
    	Object^ additionalInfo
    ) abstract
F# __Копировать
     abstract PrepareRequestToLoadMainCardAsync : 
            context : ICardGetExtensionContext * 
            request : CardGetRequest * 
            mainCardID : Guid * 
            taskRowID : Guid * 
            additionalInfo : Object -> ValueTask 
#### Параметры
context
[ICardGetExtensionContext](T_Tessa_Cards_Extensions_ICardGetExtensionContext.htm)
    Контекст расширения по загрузке карточки-сателлита.
request [CardGetRequest](T_Tessa_Cards_CardGetRequest.htm)
    Запрос на загрузку основной карточки.
mainCardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор основной карточки.
taskRowID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор задания, к которому относится карточка-сателлит.
additionalInfo [Object](https://learn.microsoft.com/dotnet/api/system.object)
     Дополнительная информация, которая была получена в методе PrepareSatelliteAfterLoadingAndGetAdditionalInfo. Например, это токен прав доступа. 
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
Асинхронная задача.
##  __См. также
#### Ссылки
[TaskSatelliteGetExtension -
](T_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
