# CardExtensions.DeserializeFromJson<T> \- метод
Десериализует объект и его дочерние объекты из заданного текстового JSON с
сохраняемыми типами данных.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static T DeserializeFromJson<T>(
    	this T cardSerializableObject,
    	string json
    )
    where T : CardSerializableObject
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function DeserializeFromJson(Of T As CardSerializableObject) ( 
    	cardSerializableObject As T,
    	json As String
    ) As T
C++ __Копировать
     public:
    [ExtensionAttribute]
    generic<typename T>
    where T : CardSerializableObject
    static T DeserializeFromJson(
    	T cardSerializableObject, 
    	String^ json
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member DeserializeFromJson : 
            cardSerializableObject : 'T * 
            json : string -> 'T  when 'T : CardSerializableObject
#### Параметры
cardSerializableObject T
    Целевой объект.
json [String](https://learn.microsoft.com/dotnet/api/system.string)
    Текстовый JSON, который десериализуется. Не должен быть равен null.
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
