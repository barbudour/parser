# CardHelper.ExecuteTypeExtensionsAsync - метод
Выполняет расширения на типы карточек для заданного типа расширений type.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<ValidationResult> ExecuteTypeExtensionsAsync(
    	CardTypeExtensionType type,
    	Card card,
    	ICardMetadata cardMetadata,
    	Func<ITypeExtensionContext, Task> executeActionAsync,
    	Object externalContext = null,
    	Dictionary<string, Object> info = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function ExecuteTypeExtensionsAsync ( 
    	type As CardTypeExtensionType,
    	card As Card,
    	cardMetadata As ICardMetadata,
    	executeActionAsync As Func(Of ITypeExtensionContext, Task),
    	Optional externalContext As Object = Nothing,
    	Optional info As Dictionary(Of String, Object) = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ValidationResult)
C++ __Копировать
     public:
    static Task<ValidationResult^>^ ExecuteTypeExtensionsAsync(
    	CardTypeExtensionType^ type, 
    	Card^ card, 
    	ICardMetadata^ cardMetadata, 
    	Func<ITypeExtensionContext^, Task^>^ executeActionAsync, 
    	Object^ externalContext = nullptr, 
    	Dictionary<String^, Object^>^ info = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member ExecuteTypeExtensionsAsync : 
            type : CardTypeExtensionType * 
            card : Card * 
            cardMetadata : ICardMetadata * 
            executeActionAsync : Func<ITypeExtensionContext, Task> * 
            ?externalContext : Object * 
            ?info : Dictionary<string, Object> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _externalContext = defaultArg externalContext null
            let _info = defaultArg info null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValidationResult> 
#### Параметры
type [CardTypeExtensionType](T_Tessa_Cards_CardTypeExtensionType.htm)
    Тип расширений, выполнение которых производится.
card [Card](T_Tessa_Cards_Card.htm)
    Основная проверяемая карточка (т.е. не файл и не задание).
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек, файлов и заданий.
executeActionAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[ITypeExtensionContext](T_Tessa_Cards_ITypeExtensionContext.htm),
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)>
    Действие, выполняющее расширение.
externalContext [Object](https://learn.microsoft.com/dotnet/api/system.object)
(Optional)
     Внешний контекст расширения, в рамках которого выполняется расширение на тип карточки, или null, если такой контекст неизвестен. 
info
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)> (Optional)
     Дополнительная информация, связанная с контекстом, или null, если дополнительная информация не задана. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)>  
Результат выполнения расширений.
##  __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
