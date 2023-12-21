# CardMetadata.CreateCopyAsync - метод
Создаёт объект, являющийся неглубокой (shallow) копией указанного объекта
[ICardMetadata](T_Tessa_Cards_ICardMetadata.htm). Все коллекции доступны для
изменения, например, возможно заменить один тип карточки на другой.
При этом сами объекты внутри коллекции (типы карточек, секции и др.) не
клонируются, а ссылаются на те же объекты, что и в cardMetadata.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<CardMetadata> CreateCopyAsync(
    	ICardMetadata cardMetadata,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function CreateCopyAsync ( 
    	cardMetadata As ICardMetadata,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of CardMetadata)
C++ __Копировать
     public:
    static ValueTask<CardMetadata^> CreateCopyAsync(
    	ICardMetadata^ cardMetadata, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member CreateCopyAsync : 
            cardMetadata : ICardMetadata * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<CardMetadata> 
#### Параметры
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Объект метаинформации, копия которого создаётся. Не должен быть равен null.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[CardMetadata](T_Tessa_Cards_Metadata_CardMetadata.htm)>  
Созданная копия.
##  __См. также
#### Ссылки
[CardMetadata - ](T_Tessa_Cards_Metadata_CardMetadata.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
