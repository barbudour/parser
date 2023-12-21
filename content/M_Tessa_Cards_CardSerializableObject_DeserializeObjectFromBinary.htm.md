# CardSerializableObject.DeserializeObjectFromBinary - метод
Десериализует объект из бинарного потока посредством объекта
[BinaryReader](https://learn.microsoft.com/dotnet/api/system.io.binaryreader).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected static SerializableObject DeserializeObjectFromBinary(
    	[NotNullAttribute] BinaryReader reader
    )
VB __Копировать
     Protected Shared Function DeserializeObjectFromBinary ( 
    	<NotNullAttribute> reader As BinaryReader
    ) As SerializableObject
C++ __Копировать
     protected:
    static SerializableObject^ DeserializeObjectFromBinary(
    	[NotNullAttribute] BinaryReader^ reader
    )
F# __Копировать
     static member DeserializeObjectFromBinary : 
            [<NotNullAttribute>] reader : BinaryReader -> SerializableObject 
#### Параметры
reader
[BinaryReader](https://learn.microsoft.com/dotnet/api/system.io.binaryreader)
    Объект, осуществляющий чтение из бинарного потока.
#### Возвращаемое значение
[SerializableObject](T_Tessa_Platform_Storage_SerializableObject.htm)  
Десериализованный объект.
##  __См. также
#### Ссылки
[CardSerializableObject - ](T_Tessa_Cards_CardSerializableObject.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
