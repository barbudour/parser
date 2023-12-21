# CardSerializableObject.DeserializeGuidListFromBinary - метод
Выполняет десериализацию заданного объекта SealableList<Guid> из байтового
потока посредством объекта
[BinaryReader](https://learn.microsoft.com/dotnet/api/system.io.binaryreader).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected static void DeserializeGuidListFromBinary(
    	[NotNullAttribute] BinaryReader reader,
    	[CanBeNullAttribute] ref SealableList<Guid> list
    )
VB __Копировать
     Protected Shared Sub DeserializeGuidListFromBinary ( 
    	<NotNullAttribute> reader As BinaryReader,
    	<CanBeNullAttribute> ByRef list As SealableList(Of Guid)
    )
C++ __Копировать
     protected:
    static void DeserializeGuidListFromBinary(
    	[NotNullAttribute] BinaryReader^ reader, 
    	[CanBeNullAttribute] SealableList<Guid>^% list
    )
F# __Копировать
     static member DeserializeGuidListFromBinary : 
            [<NotNullAttribute>] reader : BinaryReader * 
            [<CanBeNullAttribute>] list : SealableList<Guid> byref -> unit 
#### Параметры
reader
[BinaryReader](https://learn.microsoft.com/dotnet/api/system.io.binaryreader)
    Объект, осуществляющий чтение из байтового потока.
list
[SealableList](T_Tessa_Platform_Collections_SealableList_1.htm)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Десериализуемый объект. Может быть равен null.
##  __См. также
#### Ссылки
[CardSerializableObject - ](T_Tessa_Cards_CardSerializableObject.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
