# CardExtensions.RepairAsync - метод
Выполняет исправление структуры заданной карточки на основании данных в
контексте расширений по исправлению карточки. Метод полезен для исправления
карточек-сателлитов, связанных с основной исправляемой карточкой. После
исправления любые сообщения будут записаны в результат валидации текущего
контекста. Возвращает признак того, что исправление выполнено успешно, т.е.
без ошибок, предотвращающих использование карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<bool> RepairAsync(
    	this ICardRepairExtensionContext context,
    	Card card,
    	bool useExtensions = true
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function RepairAsync ( 
    	context As ICardRepairExtensionContext,
    	card As Card,
    	Optional useExtensions As Boolean = true
    ) As Task(Of Boolean)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Task<bool>^ RepairAsync(
    	ICardRepairExtensionContext^ context, 
    	Card^ card, 
    	bool useExtensions = true
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member RepairAsync : 
            context : ICardRepairExtensionContext * 
            card : Card * 
            ?useExtensions : bool 
    (* Defaults:
            let _useExtensions = defaultArg useExtensions true
    *)
    -> Task<bool> 
#### Параметры
context
[ICardRepairExtensionContext](T_Tessa_Cards_Extensions_ICardRepairExtensionContext.htm)
    Текущий контекст исправления карточки. Содержит токен отмены операции в свойстве CancellationToken.
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, которая должна быть исправлена.
useExtensions [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Признак того, что исправление должно выполняться с расширениями.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если исправление выполнено успешно, т.е. без ошибок, предотвращающих
использование карточки; false в противном случае.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[ICardRepairExtensionContext](T_Tessa_Cards_Extensions_ICardRepairExtensionContext.htm).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardExtensions - ](T_Tessa_Cards_CardExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
