# CardExtensions.ChangePasswordForCurrentUserAsync - метод
Асинхронно изменяет пароль для текущего сотрудника, если у него тип входа
"Пользователь Tessa". Возвращает сообщения валидации, в т.ч. возникшие ошибки.
Возвращаемое значение не равно null.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<ValidationResult> ChangePasswordForCurrentUserAsync(
    	this ICardRepository cardRepository,
    	string oldPassword,
    	string newPassword,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function ChangePasswordForCurrentUserAsync ( 
    	cardRepository As ICardRepository,
    	oldPassword As String,
    	newPassword As String,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ValidationResult)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Task<ValidationResult^>^ ChangePasswordForCurrentUserAsync(
    	ICardRepository^ cardRepository, 
    	String^ oldPassword, 
    	String^ newPassword, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member ChangePasswordForCurrentUserAsync : 
            cardRepository : ICardRepository * 
            oldPassword : string * 
            newPassword : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValidationResult> 
#### Параметры
cardRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
    Репозиторий для управления карточками.
oldPassword [String](https://learn.microsoft.com/dotnet/api/system.string)
    Старый пароль. Не может быть равен null или пустой строке.
newPassword [String](https://learn.microsoft.com/dotnet/api/system.string)
    Новый пароль. Не может быть равен null или пустой строке.
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
