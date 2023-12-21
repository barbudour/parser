# CardNewStrategy.FillEntryFieldsAsync - метод
Заполняет поля строковой секции в соответствии с заданной метаинформацией.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task FillEntryFieldsAsync(
    	CardSection cardSection,
    	CardMetadataSection sectionMetadata,
    	CardNewMode mode,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function FillEntryFieldsAsync ( 
    	cardSection As CardSection,
    	sectionMetadata As CardMetadataSection,
    	mode As CardNewMode,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ FillEntryFieldsAsync(
    	CardSection^ cardSection, 
    	CardMetadataSection^ sectionMetadata, 
    	CardNewMode mode, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract FillEntryFieldsAsync : 
            cardSection : CardSection * 
            sectionMetadata : CardMetadataSection * 
            mode : CardNewMode * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override FillEntryFieldsAsync : 
            cardSection : CardSection * 
            sectionMetadata : CardMetadataSection * 
            mode : CardNewMode * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
cardSection [CardSection](T_Tessa_Cards_CardSection.htm)
    Строковая секция карточки.
sectionMetadata
[CardMetadataSection](T_Tessa_Cards_Metadata_CardMetadataSection.htm)
    Метаинформация по секции карточки.
mode [CardNewMode](T_Tessa_Cards_CardNewMode.htm)
    Способ заполнения полей строковой секции.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardNewStrategy.FillEntryFieldsAsync(CardSection, CardMetadataSection,
CardNewMode,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardNewStrategy_FillEntryFieldsAsync.htm)  
##  __См. также
#### Ссылки
[CardNewStrategy - ](T_Tessa_Cards_ComponentModel_CardNewStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
