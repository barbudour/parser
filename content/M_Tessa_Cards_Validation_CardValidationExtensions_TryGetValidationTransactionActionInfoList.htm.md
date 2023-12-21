# CardValidationExtensions.TryGetValidationTransactionActionInfoList - метод
Возвращает список выполняемых в транзакции методов для заданного хранилища
storage или null, если искомый список не был найден в хранилище.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static List<Func<ICardStoreExtensionContext, Task>> TryGetValidationTransactionActionInfoList(
    	this IDictionary<string, Object> storage
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetValidationTransactionActionInfoList ( 
    	storage As IDictionary(Of String, Object)
    ) As List(Of Func(Of ICardStoreExtensionContext, Task))
C++ __Копировать
     public:
    [ExtensionAttribute]
    static List<Func<ICardStoreExtensionContext^, Task^>^>^ TryGetValidationTransactionActionInfoList(
    	IDictionary<String^, Object^>^ storage
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetValidationTransactionActionInfoList : 
            storage : IDictionary<string, Object> -> List<Func<ICardStoreExtensionContext, Task>> 
#### Параметры
storage
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище, которое содержит искомый список объектов.
#### Возвращаемое значение
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[ICardStoreExtensionContext](T_Tessa_Cards_Extensions_ICardStoreExtensionContext.htm),
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)>>  
Список выполняемых в транзакции методов, найденный для заданного хранилища
storage, или null, если искомый список не был найден в хранилище.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>. При вызове
метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardValidationExtensions -
](T_Tessa_Cards_Validation_CardValidationExtensions.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
