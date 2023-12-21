# CardSerializableObject.SerializeGuidListToBinary - метод
Выполняет сериализацию заданного объекта SealableList<Guid> в байтовый поток
посредством объекта
[BinaryWriter](https://learn.microsoft.com/dotnet/api/system.io.binarywriter).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected static void SerializeGuidListToBinary(
    	[NotNullAttribute] BinaryWriter writer,
    	[CanBeNullAttribute] SealableList<Guid> list
    )
VB __Копировать
     Protected Shared Sub SerializeGuidListToBinary ( 
    	<NotNullAttribute> writer As BinaryWriter,
    	<CanBeNullAttribute> list As SealableList(Of Guid)
    )
C++ __Копировать
     protected:
    static void SerializeGuidListToBinary(
    	[NotNullAttribute] BinaryWriter^ writer, 
    	[CanBeNullAttribute] SealableList<Guid>^ list
    )
F# __Копировать
     static member SerializeGuidListToBinary : 
            [<NotNullAttribute>] writer : BinaryWriter * 
            [<CanBeNullAttribute>] list : SealableList<Guid> -> unit 
#### Параметры
writer
[BinaryWriter](https://learn.microsoft.com/dotnet/api/system.io.binarywriter)
    Объект, осуществляющий запись в байтовый поток.
list
[SealableList](T_Tessa_Platform_Collections_SealableList_1.htm)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Сериализуемый объект. Может быть равен null.
##  __См. также
#### Ссылки
[CardSerializableObject - ](T_Tessa_Cards_CardSerializableObject.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
