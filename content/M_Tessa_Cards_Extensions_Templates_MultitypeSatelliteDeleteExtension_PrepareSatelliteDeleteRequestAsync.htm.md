# MultitypeSatelliteDeleteExtension.PrepareSatelliteDeleteRequestAsync - метод
Подготавливает запрос на удаление карточки-сателлита, которое выполняется
одновременно с удалением основной карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual ValueTask PrepareSatelliteDeleteRequestAsync(
    	ICardDeleteExtensionContext context,
    	CardDeleteRequest request,
    	Object additionalInfo
    )
VB __Копировать
     Protected Overridable Function PrepareSatelliteDeleteRequestAsync ( 
    	context As ICardDeleteExtensionContext,
    	request As CardDeleteRequest,
    	additionalInfo As Object
    ) As ValueTask
C++ __Копировать
     protected:
    virtual ValueTask PrepareSatelliteDeleteRequestAsync(
    	ICardDeleteExtensionContext^ context, 
    	CardDeleteRequest^ request, 
    	Object^ additionalInfo
    )
F# __Копировать
     abstract PrepareSatelliteDeleteRequestAsync : 
            context : ICardDeleteExtensionContext * 
            request : CardDeleteRequest * 
            additionalInfo : Object -> ValueTask 
    override PrepareSatelliteDeleteRequestAsync : 
            context : ICardDeleteExtensionContext * 
            request : CardDeleteRequest * 
            additionalInfo : Object -> ValueTask 
#### Параметры
context
[ICardDeleteExtensionContext](T_Tessa_Cards_Extensions_ICardDeleteExtensionContext.htm)
    Контекст расширения по удалению основной карточки.
request [CardDeleteRequest](T_Tessa_Cards_CardDeleteRequest.htm)
    Запрос на удаление карточки-сателлита.
additionalInfo [Object](https://learn.microsoft.com/dotnet/api/system.object)
     Дополнительная информация, которая была получена в методе GetAdditionalInfoForDeletion. Например, это токен прав доступа. 
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)
##  __См. также
#### Ссылки
[MultitypeSatelliteDeleteExtension -
](T_Tessa_Cards_Extensions_Templates_MultitypeSatelliteDeleteExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
