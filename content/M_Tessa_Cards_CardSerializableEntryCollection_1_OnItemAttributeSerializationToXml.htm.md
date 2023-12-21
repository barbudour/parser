# CardSerializableEntryCollection<T>.OnItemAttributeSerializationToXml - метод
Происходит перед сериализацией элементов коллекции в XML-элемент.
При переопределении метода в него можно добавить логику по дополнению XML-
элемента атрибутами, которые не были добавлены методом сериализации самого
элемента коллекции, но которые обрабатываются при десериализации XML-элемента.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual void OnItemAttributeSerializationToXml(
    	T item,
    	XmlWriter writer
    )
VB __Копировать
     Protected Overridable Sub OnItemAttributeSerializationToXml ( 
    	item As T,
    	writer As XmlWriter
    )
C++ __Копировать
     protected:
    virtual void OnItemAttributeSerializationToXml(
    	T item, 
    	XmlWriter^ writer
    )
F# __Копировать
     abstract OnItemAttributeSerializationToXml : 
            item : 'T * 
            writer : XmlWriter -> unit 
    override OnItemAttributeSerializationToXml : 
            item : 'T * 
            writer : XmlWriter -> unit 
#### Параметры
item [T](T_Tessa_Cards_CardSerializableEntryCollection_1.htm)
    Элемент коллекции, сериализуемый в XML.
writer
[XmlWriter](https://learn.microsoft.com/dotnet/api/system.xml.xmlwriter)
    Объект, осуществляющий запись сериализованных данных в XML.
##  __См. также
#### Ссылки
[CardSerializableEntryCollection<T> \-
](T_Tessa_Cards_CardSerializableEntryCollection_1.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
