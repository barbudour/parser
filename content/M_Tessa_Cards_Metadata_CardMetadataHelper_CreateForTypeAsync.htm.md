# CardMetadataHelper.CreateForTypeAsync - метод
Выполняет построение выборки из метаинформации, относящейся только к заданному
типу карточек.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<CardMetadata> CreateForTypeAsync(
    	Guid cardTypeID,
    	ICardMetadata cardMetadata,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function CreateForTypeAsync ( 
    	cardTypeID As Guid,
    	cardMetadata As ICardMetadata,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of CardMetadata)
C++ __Копировать
     public:
    static ValueTask<CardMetadata^> CreateForTypeAsync(
    	Guid cardTypeID, 
    	ICardMetadata^ cardMetadata, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member CreateForTypeAsync : 
            cardTypeID : Guid * 
            cardMetadata : ICardMetadata * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<CardMetadata> 
#### Параметры
cardTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Тип карточки, для которого требуется получить выборку метаинформации.
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация, необходимая для использования типов карточек совместно с пакетом карточек.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[CardMetadata](T_Tessa_Cards_Metadata_CardMetadata.htm)>  
Выборка из метаинформации, относящаяся к заданному типу карточек.
##  __См. также
#### Ссылки
[CardMetadataHelper - ](T_Tessa_Cards_Metadata_CardMetadataHelper.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
