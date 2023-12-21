# CardSerializableObject.SerializeObjectToBinary - метод
Сериализует объект в бинарный поток посредством объекта
[BinaryWriter](https://learn.microsoft.com/dotnet/api/system.io.binarywriter).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected static void SerializeObjectToBinary(
    	[NotNullAttribute] BinaryWriter writer,
    	[CanBeNullAttribute] ISerializableObject obj
    )
VB __Копировать
     Protected Shared Sub SerializeObjectToBinary ( 
    	<NotNullAttribute> writer As BinaryWriter,
    	<CanBeNullAttribute> obj As ISerializableObject
    )
C++ __Копировать
     protected:
    static void SerializeObjectToBinary(
    	[NotNullAttribute] BinaryWriter^ writer, 
    	[CanBeNullAttribute] ISerializableObject^ obj
    )
F# __Копировать
     static member SerializeObjectToBinary : 
            [<NotNullAttribute>] writer : BinaryWriter * 
            [<CanBeNullAttribute>] obj : ISerializableObject -> unit 
#### Параметры
writer
[BinaryWriter](https://learn.microsoft.com/dotnet/api/system.io.binarywriter)
    Объект, осуществляющий запись в бинарный поток.
obj [ISerializableObject](T_Tessa_Platform_Storage_ISerializableObject.htm)
    Объект, сериализация которого выполняется.
##  __См. также
#### Ссылки
[CardSerializableObject - ](T_Tessa_Cards_CardSerializableObject.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
