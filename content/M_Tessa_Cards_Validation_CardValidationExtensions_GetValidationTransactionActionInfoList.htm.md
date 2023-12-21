# CardValidationExtensions.GetValidationTransactionActionInfoList - метод
Возвращает список выполняемых в транзакции методов для заданного хранилища
storage или создаёт и возвращает новый список объектов, если искомый список не
был найден в хранилище. Метод не возвращает значение null. Используйте метод,
чтобы добавить действие, записывающее ошибку в результат валидации, когда о
наличии ошибки известно перед началом транзакции, но транзакция должна быть
запущена, чтобы выполнились другие валидаторы.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static List<Func<ICardStoreExtensionContext, Task>> GetValidationTransactionActionInfoList(
    	this IDictionary<string, Object> storage
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetValidationTransactionActionInfoList ( 
    	storage As IDictionary(Of String, Object)
    ) As List(Of Func(Of ICardStoreExtensionContext, Task))
C++ __Копировать
     public:
    [ExtensionAttribute]
    static List<Func<ICardStoreExtensionContext^, Task^>^>^ GetValidationTransactionActionInfoList(
    	IDictionary<String^, Object^>^ storage
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetValidationTransactionActionInfoList : 
            storage : IDictionary<string, Object> -> List<Func<ICardStoreExtensionContext, Task>> 
#### Параметры
storage
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище, которое может содержать искомый список объектов.
#### Возвращаемое значение
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[ICardStoreExtensionContext](T_Tessa_Cards_Extensions_ICardStoreExtensionContext.htm),
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)>>  
Список выполняемых в транзакции методов, найденный или созданный для заданного
хранилища storage.
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
