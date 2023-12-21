# ICardFileManager.CreateContainerAsync - метод
Создаёт контейнер с информацией по заданной карточке и по её файлам.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<ICardFileContainer> CreateContainerAsync(
    	Card card,
    	IFileRequest request = null,
    	IList<IFileTag> additionalTags = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function CreateContainerAsync ( 
    	card As Card,
    	Optional request As IFileRequest = Nothing,
    	Optional additionalTags As IList(Of IFileTag) = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ICardFileContainer)
C++ __Копировать
    Task<ICardFileContainer^>^ CreateContainerAsync(
    	Card^ card, 
    	IFileRequest^ request = nullptr, 
    	IList<IFileTag^>^ additionalTags = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract CreateContainerAsync : 
            card : Card * 
            ?request : IFileRequest * 
            ?additionalTags : IList<IFileTag> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _request = defaultArg request null
            let _additionalTags = defaultArg additionalTags null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ICardFileContainer> 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, для которой создаётся контейнер.
request [IFileRequest](T_Tessa_Files_IFileRequest.htm) (Optional)
    Запрос на получение коллекции доступных файлов или null, если используется запрос по умолчанию.
additionalTags
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[IFileTag](T_Tessa_Files_IFileTag.htm)>
(Optional)
     Дополнительные теги для создаваемых файлов. Например, укажите [FileTag.Large], чтобы все файлы считались большими и не сохранялись локально. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ICardFileContainer](T_Tessa_Cards_ICardFileContainer.htm)>  
Созданный контейнер.
##  __См. также
#### Ссылки
[ICardFileManager - ](T_Tessa_Cards_ICardFileManager.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
