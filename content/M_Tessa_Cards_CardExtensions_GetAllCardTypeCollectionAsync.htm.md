# CardExtensions.GetAllCardTypeCollectionAsync - метод
Возвращает коллекцию, содержащую все типы карточек.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<CardTypeCollection> GetAllCardTypeCollectionAsync(
    	this ICardTypeServerRepository repository,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetAllCardTypeCollectionAsync ( 
    	repository As ICardTypeServerRepository,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardTypeCollection)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Task<CardTypeCollection^>^ GetAllCardTypeCollectionAsync(
    	ICardTypeServerRepository^ repository, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetAllCardTypeCollectionAsync : 
            repository : ICardTypeServerRepository * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardTypeCollection> 
#### Параметры
repository
[ICardTypeServerRepository](T_Tessa_Cards_ICardTypeServerRepository.htm)
    Репозиторий для управления типами карточек.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardTypeCollection](T_Tessa_Cards_CardTypeCollection.htm)>  
Коллекция, содержащая все типы карточек.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[ICardTypeServerRepository](T_Tessa_Cards_ICardTypeServerRepository.htm). При
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
