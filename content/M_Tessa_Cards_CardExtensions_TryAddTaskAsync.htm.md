# CardExtensions.TryAddTaskAsync - метод
Создаёт и добавляет возвращаемое задание с заданными параметрами. После
создания может потребоваться заполнить секции задания и другие параметры
[CardTask](T_Tessa_Cards_CardTask.htm). Возвращённый объект
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm) содержит
ошибки и сообщения, возникшие при создании задания, он всегда не равен null.
Возвращённый объект [CardTask](T_Tessa_Cards_CardTask.htm) может быть равен
null, если при создании были ошибки. В этом случае возвращённый объект
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm) содержит
эти ошибки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<(CardTask task, ValidationResult result)> TryAddTaskAsync(
    	this ICardRepository cardRepository,
    	Card card,
    	Guid taskTypeID,
    	CardRowState state,
    	Guid roleID,
    	string roleName,
    	DateTime? planned = null,
    	string digest = null,
    	Guid? taskRowID = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryAddTaskAsync ( 
    	cardRepository As ICardRepository,
    	card As Card,
    	taskTypeID As Guid,
    	state As CardRowState,
    	roleID As Guid,
    	roleName As String,
    	Optional planned As DateTime? = Nothing,
    	Optional digest As String = Nothing,
    	Optional taskRowID As Guid? = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of (task As CardTask, result As ValidationResult))
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Task<ValueTuple<CardTask^, ValidationResult^>>^ TryAddTaskAsync(
    	ICardRepository^ cardRepository, 
    	Card^ card, 
    	Guid taskTypeID, 
    	CardRowState state, 
    	Guid roleID, 
    	String^ roleName, 
    	Nullable<DateTime> planned = nullptr, 
    	String^ digest = nullptr, 
    	Nullable<Guid> taskRowID = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryAddTaskAsync : 
            cardRepository : ICardRepository * 
            card : Card * 
            taskTypeID : Guid * 
            state : CardRowState * 
            roleID : Guid * 
            roleName : string * 
            ?planned : Nullable<DateTime> * 
            ?digest : string * 
            ?taskRowID : Nullable<Guid> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _planned = defaultArg planned null
            let _digest = defaultArg digest null
            let _taskRowID = defaultArg taskRowID null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<CardTask, ValidationResult>> 
#### Параметры
cardRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
    Репозиторий карточек, используемый для создания заданий.
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, в которую должно быть добавлено задание.
taskTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Тип создаваемого задания.
state [CardRowState](T_Tessa_Cards_CardRowState.htm)
     Состояние созданного задания. Укажите [Inserted](T_Tessa_Cards_CardRowState.htm) для того, чтобы задание можно было создать при сохранении. 
roleID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор роли, на которое назначается задание.
roleName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя роли, на которое назначается задание. Может быть равно null, если создание создаётся для сохранения, но не отображается пользователю. 
planned
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)>
(Optional)
    Дата запланированного завершения задания или null, если используется дата по умолчанию.
digest [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
    Digest созданного задания или null, если у задания отсутствует Digest.
taskRowID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
    Идентификатор созданного задания или null, если идентификатор будет сгенерирован.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-2)<[CardTask](T_Tessa_Cards_CardTask.htm),
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)>>  
Результат создания задания, содержит ошибки и сообщения, возникшие при
создании задания. Всегда не равен null.
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
