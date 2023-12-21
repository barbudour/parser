# CardTypeMetadataExtension.TryGetCardTypeAsync - метод
Возвращает метаинформацию по заданному типу карточки или null, если тип
карточки не найден.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected ValueTask<CardType> TryGetCardTypeAsync(
    	ICardMetadataExtensionContext context,
    	Guid cardTypeID,
    	bool useServerMetadataOnClient = true
    )
VB __Копировать
     Protected Function TryGetCardTypeAsync ( 
    	context As ICardMetadataExtensionContext,
    	cardTypeID As Guid,
    	Optional useServerMetadataOnClient As Boolean = true
    ) As ValueTask(Of CardType)
C++ __Копировать
     protected:
    ValueTask<CardType^> TryGetCardTypeAsync(
    	ICardMetadataExtensionContext^ context, 
    	Guid cardTypeID, 
    	bool useServerMetadataOnClient = true
    )
F# __Копировать
     member TryGetCardTypeAsync : 
            context : ICardMetadataExtensionContext * 
            cardTypeID : Guid * 
            ?useServerMetadataOnClient : bool 
    (* Defaults:
            let _useServerMetadataOnClient = defaultArg useServerMetadataOnClient true
    *)
    -> ValueTask<CardType> 
#### Параметры
context
[ICardMetadataExtensionContext](T_Tessa_Cards_Extensions_ICardMetadataExtensionContext.htm)
cardTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор запрашиваемого типа карточки.
useServerMetadataOnClient
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
     Признак того, что при использовании на клиенте должна быть задействована серверная метаинформация, которая содержит все типы карточек, а не только тип, предпросмотр которого выполняется. При использовании на сервере параметр игнорируется. 
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[CardType](T_Tessa_Cards_CardType.htm)>  
Метаинформация по заданному типу карточки или null, если тип карточки не
найден.
## __См. также
#### Ссылки
[CardTypeMetadataExtension -
](T_Tessa_Cards_Extensions_CardTypeMetadataExtension.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
