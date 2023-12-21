# CardRequestExtensions.InvalidateCacheAsync - метод
Выполняет запрос по сбросу кэшей на сервере. Может быть вызван с сервера или
клиента для сессии пользователя с правами администратора. Если в качестве
списка имён cacheNames указывается null, то выполняется сброс всех кэшей; если
указан пустой массив, то сброс не будет выполнен, однако, запрос будет запущен
(т.е. расширения могут определить список кэшей для сброса сами). Возвращает
результат выполнения операции, который не равен null.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<ValidationResult> InvalidateCacheAsync(
    	this ICardRepository cardRepository,
    	string[] cacheNames = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function InvalidateCacheAsync ( 
    	cardRepository As ICardRepository,
    	Optional cacheNames As String() = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ValidationResult)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Task<ValidationResult^>^ InvalidateCacheAsync(
    	ICardRepository^ cardRepository, 
    	array<String^>^ cacheNames = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member InvalidateCacheAsync : 
            cardRepository : ICardRepository * 
            ?cacheNames : string[] * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cacheNames = defaultArg cacheNames null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValidationResult> 
#### Параметры
cardRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
    Репозиторий по управлению карточками.
cacheNames [String](https://learn.microsoft.com/dotnet/api/system.string)[]
(Optional)
     Список кэшей для сброса. Список кэшей, доступных в платформе без расширений, определён в классе [PlatformCacheNames](T_Tessa_Platform_PlatformCacheNames.htm). Список кэшей в типовом решении - в классе Tessa.Extensions.Default.Shared.DefaultCacheNames. Укажите null, чтобы выполнить сброс всех кэшей. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)>  
Результат выполнения операции.
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
[CardRequestExtensions - ](T_Tessa_Cards_CardRequestExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
