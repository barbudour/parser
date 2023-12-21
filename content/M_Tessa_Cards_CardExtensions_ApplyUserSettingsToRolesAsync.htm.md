# CardExtensions.ApplyUserSettingsToRolesAsync - метод
Асинхронно выполняет копирование настроек одного сотрудника на заданный список
ролей (без учёта заместителей). Запрос доступен только для администраторов.
Возвращает сообщения валидации, в т.ч. возникшие ошибки. Возвращаемое значение
не равно null.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<ValidationResult> ApplyUserSettingsToRolesAsync(
    	this ICardRepository cardRepository,
    	Guid userID,
    	IEnumerable<Guid> roleIdentifiers,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function ApplyUserSettingsToRolesAsync ( 
    	cardRepository As ICardRepository,
    	userID As Guid,
    	roleIdentifiers As IEnumerable(Of Guid),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ValidationResult)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Task<ValidationResult^>^ ApplyUserSettingsToRolesAsync(
    	ICardRepository^ cardRepository, 
    	Guid userID, 
    	IEnumerable<Guid>^ roleIdentifiers, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member ApplyUserSettingsToRolesAsync : 
            cardRepository : ICardRepository * 
            userID : Guid * 
            roleIdentifiers : IEnumerable<Guid> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValidationResult> 
#### Параметры
cardRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
    Репозиторий для управления карточками.
userID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор сотрудника, настройки которого копируются.
roleIdentifiers
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Список идентификаторов ролей, для сотрудников которых копируются настройки.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)>  
Задача, возвращающая сообщения валидации. Возвращаемое значение не равно null.
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
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
