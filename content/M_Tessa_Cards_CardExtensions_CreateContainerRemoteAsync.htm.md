# CardExtensions.CreateContainerRemoteAsync - метод
Создаёт контейнер с информацией по заданной карточке и по её файлам. Все файлы
создаются с Remote-содержимым, при загрузке и замене которого не используется
временная папка. Операции с такими файлами будут выполняться быстрее, но при
условии надо быть уверенными, что содержимое файлов, работа с которыми
выполняется, умещается в памяти. Возможные ошибки при загрузке файлов из
карточки игнорируются. В этом случае к созданном контейнере не будет добавлено
файлов, хотя файлы присутствуют в карточке.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<ICardFileContainer> CreateContainerRemoteAsync(
    	this ICardFileManager manager,
    	Card card,
    	IFileRequest request = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function CreateContainerRemoteAsync ( 
    	manager As ICardFileManager,
    	card As Card,
    	Optional request As IFileRequest = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ICardFileContainer)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Task<ICardFileContainer^>^ CreateContainerRemoteAsync(
    	ICardFileManager^ manager, 
    	Card^ card, 
    	IFileRequest^ request = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member CreateContainerRemoteAsync : 
            manager : ICardFileManager * 
            card : Card * 
            ?request : IFileRequest * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _request = defaultArg request null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ICardFileContainer> 
#### Параметры
manager [ICardFileManager](T_Tessa_Cards_ICardFileManager.htm)
    Объект, который управляет объектами контейнеров [ICardFileContainer](T_Tessa_Cards_ICardFileContainer.htm).
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, для которой создаётся контейнер.
request [IFileRequest](T_Tessa_Files_IFileRequest.htm) (Optional)
    Запрос на получение коллекции доступных файлов или null, если используется запрос по умолчанию.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ICardFileContainer](T_Tessa_Cards_ICardFileContainer.htm)>  
Контейнер, содержащий информацию по карточке и её файлам.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [ICardFileManager](T_Tessa_Cards_ICardFileManager.htm). При
вызове метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardExtensions - ](T_Tessa_Cards_CardExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
