# CardMetadataColumn.DeserializeElementFromXml - метод
Выполняется для каждого элемента десериализуемого объекта.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override bool DeserializeElementFromXml(
    	string name,
    	XmlReader reader
    )
VB __Копировать
     Protected Overrides Function DeserializeElementFromXml ( 
    	name As String,
    	reader As XmlReader
    ) As Boolean
C++ __Копировать
     protected:
    virtual bool DeserializeElementFromXml(
    	String^ name, 
    	XmlReader^ reader
    ) override
F# __Копировать
     abstract DeserializeElementFromXml : 
            name : string * 
            reader : XmlReader -> bool 
    override DeserializeElementFromXml : 
            name : string * 
            reader : XmlReader -> bool 
#### Параметры
name [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя элемента.
reader
[XmlReader](https://learn.microsoft.com/dotnet/api/system.xml.xmlreader)
    Объект выполняющий чтение сериализованных данных из XML.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если элемент был успешно десериализован; false в противном случае.
## __См. также
#### Ссылки
[CardMetadataColumn - ](T_Tessa_Cards_Metadata_CardMetadataColumn.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
