# CardMetadataRecord.SerializeAttributesToXml - метод
Выполняет сериализацию текущего объекта в атрибуты XML.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override void SerializeAttributesToXml(
    	XmlWriter writer
    )
VB __Копировать
     Protected Overrides Sub SerializeAttributesToXml ( 
    	writer As XmlWriter
    )
C++ __Копировать
     protected:
    virtual void SerializeAttributesToXml(
    	XmlWriter^ writer
    ) override
F# __Копировать
     abstract SerializeAttributesToXml : 
            writer : XmlWriter -> unit 
    override SerializeAttributesToXml : 
            writer : XmlWriter -> unit 
#### Параметры
writer
[XmlWriter](https://learn.microsoft.com/dotnet/api/system.xml.xmlwriter)
    Объект, выполняющий запись сериализованных данных в XML.
##  __См. также
#### Ссылки
[CardMetadataRecord - ](T_Tessa_Cards_Metadata_CardMetadataRecord.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
