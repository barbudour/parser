# CardExtensions.DeleteAsync(ICardTypeServerRepository,
ICardSerializableEntry, CancellationToken) - метод
Удаляет заданный тип карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task DeleteAsync(
    	this ICardTypeServerRepository repository,
    	ICardSerializableEntry cardType,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function DeleteAsync ( 
    	repository As ICardTypeServerRepository,
    	cardType As ICardSerializableEntry,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Task^ DeleteAsync(
    	ICardTypeServerRepository^ repository, 
    	ICardSerializableEntry^ cardType, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member DeleteAsync : 
            repository : ICardTypeServerRepository * 
            cardType : ICardSerializableEntry * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
repository
[ICardTypeServerRepository](T_Tessa_Cards_ICardTypeServerRepository.htm)
    Репозиторий для управления типами карточек.
cardType [ICardSerializableEntry](T_Tessa_Cards_ICardSerializableEntry.htm)
    Объект, описывающий тип карточки.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
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
[DeleteAsync -
перегрузка](Overload_Tessa_Cards_CardExtensions_DeleteAsync.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
