# CardExtensions.GetFileSourceAsync(ICardRepository, Card, CardFile,
CancellationToken) - метод
Асинхронно возвращает местоположение контента файла для заданного файла file
указанной карточки card. Местоположение определяется выполнением запроса
[GetFileSource](F_Tessa_Cards_CardRequestTypes_GetFileSource.htm). Метод
возвращает null, если определить местоположение не удалось, обычно в этом
случае будет использоваться местоположение по умолчанию.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<CardFileSourceType?> GetFileSourceAsync(
    	this ICardRepository cardRepository,
    	Card card,
    	CardFile file,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetFileSourceAsync ( 
    	cardRepository As ICardRepository,
    	card As Card,
    	file As CardFile,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardFileSourceType?)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Task<Nullable<CardFileSourceType>>^ GetFileSourceAsync(
    	ICardRepository^ cardRepository, 
    	Card^ card, 
    	CardFile^ file, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetFileSourceAsync : 
            cardRepository : ICardRepository * 
            card : Card * 
            file : CardFile * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<Nullable<CardFileSourceType>> 
#### Параметры
cardRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
    Репозиторий для управления карточками.
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, для файла которой требуется получить местоположение контента.
file [CardFile](T_Tessa_Cards_CardFile.htm)
    Файл карточки, для которого требуется получить местоположение контента.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[CardFileSourceType](T_Tessa_Cards_CardFileSourceType.htm)>>  
Задача, возвращающая местоположение контента для заданного файла указанной
карточки или null, если Digest неизвестен или не требуется.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [ICardRepository](T_Tessa_Cards_ICardRepository.htm). При вызове
метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardExtensions - ](T_Tessa_Cards_CardExtensions.htm)
[GetFileSourceAsync -
перегрузка](Overload_Tessa_Cards_CardExtensions_GetFileSourceAsync.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
