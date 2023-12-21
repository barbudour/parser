# CardStoreExecutionStrategy.GetSectionRowRemoverAsync - метод
Возвращает объект, выполняющий удаление строк из заданной коллекционной или
древовидной секции.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<CardSectionRowRemover> GetSectionRowRemoverAsync(
    	CardMetadataSection section,
    	ICardMetadata cardMetadata,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetSectionRowRemoverAsync ( 
    	section As CardMetadataSection,
    	cardMetadata As ICardMetadata,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of CardSectionRowRemover)
C++ __Копировать
     public:
    virtual ValueTask<CardSectionRowRemover^> GetSectionRowRemoverAsync(
    	CardMetadataSection^ section, 
    	ICardMetadata^ cardMetadata, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetSectionRowRemoverAsync : 
            section : CardMetadataSection * 
            cardMetadata : ICardMetadata * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<CardSectionRowRemover> 
    override GetSectionRowRemoverAsync : 
            section : CardMetadataSection * 
            cardMetadata : ICardMetadata * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<CardSectionRowRemover> 
#### Параметры
section [CardMetadataSection](T_Tessa_Cards_Metadata_CardMetadataSection.htm)
    Коллекционная или древовидная секция сохраняемой карточки, из которой требуется удалять строки.
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[CardSectionRowRemover](T_Tessa_Cards_ComponentModel_CardSectionRowRemover.htm)>  
Объект, выполняющий удаление строк из заданной коллекционной или древовидной
секции.
#### Реализации
[ICardStoreExecutionStrategy.GetSectionRowRemoverAsync(CardMetadataSection,
ICardMetadata,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardStoreExecutionStrategy_GetSectionRowRemoverAsync.htm)  
##  __См. также
#### Ссылки
[CardStoreExecutionStrategy -
](T_Tessa_Cards_ComponentModel_CardStoreExecutionStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
