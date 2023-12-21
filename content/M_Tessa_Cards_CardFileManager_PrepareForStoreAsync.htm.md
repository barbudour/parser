# CardFileManager.PrepareForStoreAsync - метод
Подготавливает карточку из текущего контейнера и контент её файлов к
сохранению. Возвращает объект запрос на сохранение карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<CardStoreRequest> PrepareForStoreAsync(
    	ICardFileContainer container,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function PrepareForStoreAsync ( 
    	container As ICardFileContainer,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardStoreRequest)
C++ __Копировать
     public:
    virtual Task<CardStoreRequest^>^ PrepareForStoreAsync(
    	ICardFileContainer^ container, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract PrepareForStoreAsync : 
            container : ICardFileContainer * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardStoreRequest> 
    override PrepareForStoreAsync : 
            container : ICardFileContainer * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardStoreRequest> 
#### Параметры
container [ICardFileContainer](T_Tessa_Cards_ICardFileContainer.htm)
    Контейнер, содержащий информацию по карточке и её файлам.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm)>  
Запрос на сохранение карточки.
#### Реализации
[ICardFileManager.PrepareForStoreAsync(ICardFileContainer,
CancellationToken)](M_Tessa_Cards_ICardFileManager_PrepareForStoreAsync.htm)  
##  __См. также
#### Ссылки
[CardFileManager - ](T_Tessa_Cards_CardFileManager.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
