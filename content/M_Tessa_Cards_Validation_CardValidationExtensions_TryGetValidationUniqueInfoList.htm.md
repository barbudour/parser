# CardValidationExtensions.TryGetValidationUniqueInfoList - метод
Возвращает список объектов
[CardValidationUniqueInfo](T_Tessa_Cards_Validation_CardValidationUniqueInfo.htm)
для заданного хранилища storage или null, если искомый список не был найден в
хранилище.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static List<CardValidationUniqueInfo> TryGetValidationUniqueInfoList(
    	this IDictionary<string, Object> storage
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetValidationUniqueInfoList ( 
    	storage As IDictionary(Of String, Object)
    ) As List(Of CardValidationUniqueInfo)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static List<CardValidationUniqueInfo^>^ TryGetValidationUniqueInfoList(
    	IDictionary<String^, Object^>^ storage
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetValidationUniqueInfoList : 
            storage : IDictionary<string, Object> -> List<CardValidationUniqueInfo> 
#### Параметры
storage
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище, которое содержит искомый список объектов.
#### Возвращаемое значение
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[CardValidationUniqueInfo](T_Tessa_Cards_Validation_CardValidationUniqueInfo.htm)>  
Список объектов
[CardValidationUniqueInfo](T_Tessa_Cards_Validation_CardValidationUniqueInfo.htm),
найденный для заданного хранилища storage, или null, если искомый список не
был найден в хранилище.
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
