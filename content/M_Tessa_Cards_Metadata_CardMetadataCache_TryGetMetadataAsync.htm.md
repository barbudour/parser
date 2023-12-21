# CardMetadataCache.TryGetMetadataAsync - метод
Возвращает доступную только для чтения актуальную метаинформацию по карточкам
или null, если метаинформация недоступна.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<CardMetadata> TryGetMetadataAsync(
    	string builderName = "Default",
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function TryGetMetadataAsync ( 
    	Optional builderName As String = "Default",
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardMetadata)
C++ __Копировать
     public:
    Task<CardMetadata^>^ TryGetMetadataAsync(
    	String^ builderName = L"Default", 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member TryGetMetadataAsync : 
            ?builderName : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _builderName = defaultArg builderName "Default"
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardMetadata> 
#### Параметры
builderName [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
     Имя, по которому будет резолвиться кеш в зависимости от того, каким [ICardMetadataBuilder](T_Tessa_Cards_Metadata_ICardMetadataBuilder.htm) он построен. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardMetadata](T_Tessa_Cards_Metadata_CardMetadata.htm)>  
Метаинформация по карточкам или null, если метаинформация недоступна.
##  __См. также
#### Ссылки
[CardMetadataCache - ](T_Tessa_Cards_Metadata_CardMetadataCache.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
