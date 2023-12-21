# CardSerializableObject.DeserializeObjectListFromBinary<T>(BinaryReader,
SealableObjectList<T>) - метод
Выполняет десериализацию коллекции объектов
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm) из
байтового потока посредством объекта
[BinaryReader](https://learn.microsoft.com/dotnet/api/system.io.binaryreader).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected static void DeserializeObjectListFromBinary<T>(
    	[NotNullAttribute] BinaryReader reader,
    	[CanBeNullAttribute] ref SealableObjectList<T> items
    )
    where T : new(), CardSerializableObject
VB __Копировать
     Protected Shared Sub DeserializeObjectListFromBinary(Of T As {New, CardSerializableObject}) ( 
    	<NotNullAttribute> reader As BinaryReader,
    	<CanBeNullAttribute> ByRef items As SealableObjectList(Of T)
    )
C++ __Копировать
     protected:
    generic<typename T>
    where T : gcnew(), CardSerializableObject
    static void DeserializeObjectListFromBinary(
    	[NotNullAttribute] BinaryReader^ reader, 
    	[CanBeNullAttribute] SealableObjectList<T>^% items
    )
F# __Копировать
     static member DeserializeObjectListFromBinary : 
            [<NotNullAttribute>] reader : BinaryReader * 
            [<CanBeNullAttribute>] items : SealableObjectList<'T> byref -> unit  when 'T : new() and CardSerializableObject
#### Параметры
reader
[BinaryReader](https://learn.microsoft.com/dotnet/api/system.io.binaryreader)
    Объект, осуществляющий чтение из байтового потока.
items
[SealableObjectList](T_Tessa_Platform_Collections_SealableObjectList_1.htm)<T>
     Коллекция, в которую будут записаны десериализованные объекты. Если значение равно null, то будет создана новая коллекция, в противном случае существующая коллекция будет очищена. 
#### Параметры типа
T
     Тип объекта, содержащегося в коллекции. Объект должен наследоваться от [CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm) и определять конструктор по умолчанию. 
## __См. также
#### Ссылки
[CardSerializableObject - ](T_Tessa_Cards_CardSerializableObject.htm)
[DeserializeObjectListFromBinary -
перегрузка](Overload_Tessa_Cards_CardSerializableObject_DeserializeObjectListFromBinary.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
