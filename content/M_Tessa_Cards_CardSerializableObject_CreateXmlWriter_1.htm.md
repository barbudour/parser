# CardSerializableObject.CreateXmlWriter(StringBuilder, Boolean) - метод
Создаёт объект
[XmlWriter](https://learn.microsoft.com/dotnet/api/system.xml.xmlwriter) для
сериализации объекта
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm) в XML,
который записывается в строковое представление в заданном объекте
stringBuilder.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected static XmlWriter CreateXmlWriter(
    	[NotNullAttribute] StringBuilder stringBuilder,
    	bool omitXmlDeclaration = false
    )
VB __Копировать
     Protected Shared Function CreateXmlWriter ( 
    	<NotNullAttribute> stringBuilder As StringBuilder,
    	Optional omitXmlDeclaration As Boolean = false
    ) As XmlWriter
C++ __Копировать
     protected:
    static XmlWriter^ CreateXmlWriter(
    	[NotNullAttribute] StringBuilder^ stringBuilder, 
    	bool omitXmlDeclaration = false
    )
F# __Копировать
     static member CreateXmlWriter : 
            [<NotNullAttribute>] stringBuilder : StringBuilder * 
            ?omitXmlDeclaration : bool 
    (* Defaults:
            let _omitXmlDeclaration = defaultArg omitXmlDeclaration false
    *)
    -> XmlWriter 
#### Параметры
stringBuilder
[StringBuilder](https://learn.microsoft.com/dotnet/api/system.text.stringbuilder)
     Объект, в который записывается строковое представление сериализованных в XML данных объекта [CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm). 
omitXmlDeclaration
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
     Признак того, что в результирующем документе не должен выводится заголовок XML вида <?xml version="1.0" encoding="utf-8">>. 
#### Возвращаемое значение
[XmlWriter](https://learn.microsoft.com/dotnet/api/system.xml.xmlwriter)  
Созданный объект, предназначенный для сериализации объекта
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm) в XML.
##  __См. также
#### Ссылки
[CardSerializableObject - ](T_Tessa_Cards_CardSerializableObject.htm)
[CreateXmlWriter -
перегрузка](Overload_Tessa_Cards_CardSerializableObject_CreateXmlWriter.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
