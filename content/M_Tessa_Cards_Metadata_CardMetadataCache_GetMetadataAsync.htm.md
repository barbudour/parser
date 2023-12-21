# CardMetadataCache.GetMetadataAsync - метод
Возвращает доступную только для чтения актуальную метаинформацию по карточкам,
доступную в кэше.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<CardMetadata> GetMetadataAsync(
    	Func<string, CancellationToken, Task<CardMetadata>> getMetadataAsync,
    	string builderName = "Default",
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetMetadataAsync ( 
    	getMetadataAsync As Func(Of String, CancellationToken, Task(Of CardMetadata)),
    	Optional builderName As String = "Default",
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardMetadata)
C++ __Копировать
     public:
    Task<CardMetadata^>^ GetMetadataAsync(
    	Func<String^, CancellationToken, Task<CardMetadata^>^>^ getMetadataAsync, 
    	String^ builderName = L"Default", 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member GetMetadataAsync : 
            getMetadataAsync : Func<string, CancellationToken, Task<CardMetadata>> * 
            ?builderName : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _builderName = defaultArg builderName "Default"
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardMetadata> 
#### Параметры
getMetadataAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardMetadata](T_Tessa_Cards_Metadata_CardMetadata.htm)>>
     Функция, возвращающая метаинформацию, которая заместит доступную через кэш метаинформацию, если в кэше отсутствует актуальное значение. 
builderName [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
     Имя, по которому будет резолвиться кеш в зависимости от того каким [ICardMetadataBuilder](T_Tessa_Cards_Metadata_ICardMetadataBuilder.htm) он построен. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardMetadata](T_Tessa_Cards_Metadata_CardMetadata.htm)>  
Актуальная метаинформация по карточкам.
## __См. также
#### Ссылки
[CardMetadataCache - ](T_Tessa_Cards_Metadata_CardMetadataCache.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
