# CardSectionRowRemover.CreateAsync - метод
Создаёт экземпляр объекта с указанием секции, из которой должно производиться
удаление строки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<CardSectionRowRemover> CreateAsync(
    	CardMetadataSection section,
    	ICardMetadata cardMetadata,
    	Func<CardMetadataSection, CancellationToken, ValueTask<CardSectionRowRemover>> getRemoverFunc,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function CreateAsync ( 
    	section As CardMetadataSection,
    	cardMetadata As ICardMetadata,
    	getRemoverFunc As Func(Of CardMetadataSection, CancellationToken, ValueTask(Of CardSectionRowRemover)),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of CardSectionRowRemover)
C++ __Копировать
     public:
    static ValueTask<CardSectionRowRemover^> CreateAsync(
    	CardMetadataSection^ section, 
    	ICardMetadata^ cardMetadata, 
    	Func<CardMetadataSection^, CancellationToken, ValueTask<CardSectionRowRemover^>>^ getRemoverFunc, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member CreateAsync : 
            section : CardMetadataSection * 
            cardMetadata : ICardMetadata * 
            getRemoverFunc : Func<CardMetadataSection, CancellationToken, ValueTask<CardSectionRowRemover>> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<CardSectionRowRemover> 
#### Параметры
section [CardMetadataSection](T_Tessa_Cards_Metadata_CardMetadataSection.htm)
    Метаинформация по секции, строка которой должна быть удалена.
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек.
getRemoverFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[CardMetadataSection](T_Tessa_Cards_Metadata_CardMetadataSection.htm),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[CardSectionRowRemover](T_Tessa_Cards_ComponentModel_CardSectionRowRemover.htm)>>
     Функция, возвращающая объект, который описывает удаление строки из секции с заданным идентификатором. Функция может как получать объект из кэша, так и создавать объект самостоятельно. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[CardSectionRowRemover](T_Tessa_Cards_ComponentModel_CardSectionRowRemover.htm)>  
Асинхронная задача.
##  __См. также
#### Ссылки
[CardSectionRowRemover -
](T_Tessa_Cards_ComponentModel_CardSectionRowRemover.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
