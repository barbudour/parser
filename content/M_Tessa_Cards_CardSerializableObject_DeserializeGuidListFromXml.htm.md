# CardSerializableObject.DeserializeGuidListFromXml - метод
Выполняет десериализацию заданного объекта SealableList<Guid> из XML-атрибута
с заданным значением.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected static SealableList<Guid> DeserializeGuidListFromXml(
    	[NotNullAttribute] string attributeValue
    )
VB __Копировать
     Protected Shared Function DeserializeGuidListFromXml ( 
    	<NotNullAttribute> attributeValue As String
    ) As SealableList(Of Guid)
C++ __Копировать
     protected:
    static SealableList<Guid>^ DeserializeGuidListFromXml(
    	[NotNullAttribute] String^ attributeValue
    )
F# __Копировать
     static member DeserializeGuidListFromXml : 
            [<NotNullAttribute>] attributeValue : string -> SealableList<Guid> 
#### Параметры
attributeValue [String](https://learn.microsoft.com/dotnet/api/system.string)
    Значение атрибута, в котором содержится десериализованный объект.
#### Возвращаемое значение
[SealableList](T_Tessa_Platform_Collections_SealableList_1.htm)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>  
Десериализованный объект.
##  __См. также
#### Ссылки
[CardSerializableObject - ](T_Tessa_Cards_CardSerializableObject.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
