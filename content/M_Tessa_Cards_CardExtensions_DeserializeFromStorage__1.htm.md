# CardExtensions.DeserializeFromStorage<T> \- метод
Десериализует объект из заданного хранилища Dictionary<string, object>.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static T DeserializeFromStorage<T>(
    	this T cardSerializableObject,
    	Dictionary<string, Object> storage
    )
    where T : CardSerializableObject
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function DeserializeFromStorage(Of T As CardSerializableObject) ( 
    	cardSerializableObject As T,
    	storage As Dictionary(Of String, Object)
    ) As T
C++ __Копировать
     public:
    [ExtensionAttribute]
    generic<typename T>
    where T : CardSerializableObject
    static T DeserializeFromStorage(
    	T cardSerializableObject, 
    	Dictionary<String^, Object^>^ storage
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member DeserializeFromStorage : 
            cardSerializableObject : 'T * 
            storage : Dictionary<string, Object> -> 'T  when 'T : CardSerializableObject
#### Параметры
cardSerializableObject T
    Целевой объект.
storage
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище, содержащее сериализованные данные.
#### Параметры типа
T
     Тип объекта, содержащегося в хранилище. Объект должен наследоваться от [CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm). 
#### Возвращаемое значение
T  
Десериализованный объект (может подменять значение, при использовании
глобальных ссылок).
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа T. При вызове метода для экземпляра следует опускать первый
параметр. Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardExtensions - ](T_Tessa_Cards_CardExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
