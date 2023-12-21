# CardComponentHelper.TryGetCardTypeAsync(Nullable<Guid>, String,
ICardMetadata, CancellationToken) - метод
Возвращает тип карточки по заданному идентификатору или имени, или null, если
идентификатор и имя равны null или тип карточки не найден по заданным
идентификатору или имени.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<CardType> TryGetCardTypeAsync(
    	Guid? cardTypeID,
    	string cardTypeName,
    	ICardMetadata cardMetadata,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function TryGetCardTypeAsync ( 
    	cardTypeID As Guid?,
    	cardTypeName As String,
    	cardMetadata As ICardMetadata,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of CardType)
C++ __Копировать
     public:
    static ValueTask<CardType^> TryGetCardTypeAsync(
    	Nullable<Guid> cardTypeID, 
    	String^ cardTypeName, 
    	ICardMetadata^ cardMetadata, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member TryGetCardTypeAsync : 
            cardTypeID : Nullable<Guid> * 
            cardTypeName : string * 
            cardMetadata : ICardMetadata * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<CardType> 
#### Параметры
cardTypeID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
     Идентификатор типа карточки или null, если идентификатор неизвестен. 
cardTypeName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя типа карточки или null, если имя неизвестно. 
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[CardType](T_Tessa_Cards_CardType.htm)>  
Тип карточки, полученный по заданному идентификатору, или null, если
идентификатор равен null или тип карточки не найден.
## __См. также
#### Ссылки
[CardComponentHelper - ](T_Tessa_Cards_ComponentModel_CardComponentHelper.htm)
[TryGetCardTypeAsync -
перегрузка](Overload_Tessa_Cards_ComponentModel_CardComponentHelper_TryGetCardTypeAsync.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
