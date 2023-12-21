# TaskSatelliteGetExtension.PrepareSatelliteWithMainCardInfoAsync - метод
Подготавливает данные карточки-сателлита по данным загруженной основной
карточки.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract ValueTask PrepareSatelliteWithMainCardInfoAsync(
    	ICardGetExtensionContext context,
    	Card satellite,
    	Card mainCard,
    	Object additionalInfo
    )
VB __Копировать
     Protected MustOverride Function PrepareSatelliteWithMainCardInfoAsync ( 
    	context As ICardGetExtensionContext,
    	satellite As Card,
    	mainCard As Card,
    	additionalInfo As Object
    ) As ValueTask
C++ __Копировать
     protected:
    virtual ValueTask PrepareSatelliteWithMainCardInfoAsync(
    	ICardGetExtensionContext^ context, 
    	Card^ satellite, 
    	Card^ mainCard, 
    	Object^ additionalInfo
    ) abstract
F# __Копировать
     abstract PrepareSatelliteWithMainCardInfoAsync : 
            context : ICardGetExtensionContext * 
            satellite : Card * 
            mainCard : Card * 
            additionalInfo : Object -> ValueTask 
#### Параметры
context
[ICardGetExtensionContext](T_Tessa_Cards_Extensions_ICardGetExtensionContext.htm)
    Контекст расширения по загрузке карточки-сателлита.
satellite [Card](T_Tessa_Cards_Card.htm)
    Карточка-сателлит, данные которой подготавливаются.
mainCard [Card](T_Tessa_Cards_Card.htm)
    Основная карточка, данные которой используются.
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
