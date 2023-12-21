# CardSerializableObject.SerializeObjectListToBinary<T> \- метод
Выполняет сериализацию коллекции объектов
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm) в байтовый
поток посредством объекта
[BinaryWriter](https://learn.microsoft.com/dotnet/api/system.io.binarywriter).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected static void SerializeObjectListToBinary<T>(
    	[NotNullAttribute] BinaryWriter writer,
    	[CanBeNullAttribute] ICollection<T> items
    )
    where T : CardSerializableObject
VB __Копировать
     Protected Shared Sub SerializeObjectListToBinary(Of T As CardSerializableObject) ( 
    	<NotNullAttribute> writer As BinaryWriter,
    	<CanBeNullAttribute> items As ICollection(Of T)
    )
C++ __Копировать
     protected:
    generic<typename T>
    where T : CardSerializableObject
    static void SerializeObjectListToBinary(
    	[NotNullAttribute] BinaryWriter^ writer, 
    	[CanBeNullAttribute] ICollection<T>^ items
    )
F# __Копировать
     static member SerializeObjectListToBinary : 
            [<NotNullAttribute>] writer : BinaryWriter * 
            [<CanBeNullAttribute>] items : ICollection<'T> -> unit  when 'T : CardSerializableObject
#### Параметры
writer
[BinaryWriter](https://learn.microsoft.com/dotnet/api/system.io.binarywriter)
    Объект, осуществляющий запись в байтовый поток.
items
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<T>
     Коллекция сериализуемых объектов. Если значение равно null, то сериализована будет пустая коллекция. 
#### Параметры типа
T
     Тип объекта, содержащегося в коллекции. Объект должен наследоваться от [CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm). 
## __См. также
#### Ссылки
[CardSerializableObject - ](T_Tessa_Cards_CardSerializableObject.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
